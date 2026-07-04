"""Tests for MIT Technology Review article: "The Meta hack shows there's
more to AI security than Mythos" (June 2026).

Type A article deep dive — AI security/agentic vulnerability coverage.
Validates entity cluster corrections (Bo Li, Nature false positive),
education topic metaphor suppression, and source extraction accuracy.
"""

import pytest

from mediascope.analyze.entities import detect_entities
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sentiment import analyze_composite, analyze_vader
from mediascope.analyze.sources import extract_sources, analyze_source_stance
from mediascope.analyze.topics import classify_topic


ARTICLE = (
    "On June 5, 404 Media reported that attackers had been using Meta's "
    "AI customer support agent to steal Instagram accounts. Their approach "
    "was simple: They asked the agent to link the accounts to email addresses "
    "that they controlled, and the agent complied. One attacker broke into "
    "the dormant Obama White House account and made pro-Iran posts; others "
    "took over accounts with valuable, single-word handles, possibly in "
    "order to sell them. "
    "AI cybersecurity concerns are nothing new. Since Anthropic announced "
    "in April that its Mythos model was too good at hacking to be released "
    "to the general public, commentators, researchers, and federal officials "
    "alike have fixated on the idea that superpowered AI systems could lay "
    "waste to our computer infrastructure. That is not quite what this "
    "Instagram hack was: There, AI was the target rather than the attacker, "
    "and the method was far simpler than anything Mythos would cook up. But "
    "as companies offload more work to AI, these comparatively unsophisticated "
    "attacks could wreak their own havoc. "
    "As AI becomes more and more widely used especially when AI is more and "
    "more widely used to automate our work flows, like account recovery I "
    "think attackers are going to be more and more motivated to attack AI "
    "itself, says Neil Gong, a professor of electrical and computer "
    "engineering at Duke University. "
    "Gong and other scholars have been issuing warnings about the security "
    "vulnerabilities of AI agents for a while. They publish papers and blog "
    "posts detailing exploits such as indirect prompt injection, which "
    "involves hijacking agents using commands hidden in websites, emails, "
    "or other seemingly anodyne data sources. Compared with these techniques, "
    "the Meta hack was practically mindless. The only complication that "
    "hackers had to overcome was using a VPN that matched the true account "
    "owner's location; then they directly asked the support agent to change "
    "the account's email address, and it complied. "
    "Meta has not commented publicly on how this vulnerability slipped "
    "through the cracks. But given the simplicity of the exploit, Gong says, "
    "it should have been uncovered easily, before the agent was deployed. "
    "It is really surprising, he says. I do not understand why they did not "
    "find this simple problem. "
    "Jessica Ji, a senior research analyst at Georgetown Center for Security "
    "and Emerging Technology, agrees. It raises questions like: Were there "
    "even guardrails in place? she says. Did anyone think to test for this "
    "kind of scenario? She notes that the oversight is particularly striking "
    "coming from a company like Meta, which has extensive expertise in both "
    "AI and cybersecurity. Meta did not respond to a request for comment for "
    "this article, but on Monday a Meta spokesperson said on X that the "
    "vulnerability had been resolved. "
    "As embarrassing a moment as this might be for Meta in particular, it "
    "also highlights some core vulnerabilities shared by all AI agents. "
    "Unlike traditional software, agents can respond in flexible and "
    "unexpected ways to new circumstances, which is why they might be able "
    "to substitute for human customer support agents. But AI agents can also "
    "be tricked in ways that humans would not be, and because they can take "
    "real-world actions, those mistakes have consequences. A human would say, "
    "Okay, why do you want to change the email address? and maybe respond "
    "with a security question, says Somesh Jha, a professor of computer "
    "science at the University of Wisconsin Madison. What is going on with "
    "these agents is they are very eager to finish the task. It is almost "
    "like some elementary school student who just wants to please the teacher. "
    "There are ways to mitigate the risks. Companies can use traditional "
    "software to build guardrails that make sure agents follow strict rules, "
    "such as always asking for answers to security questions before sending "
    "sensitive account information to a new email address. And the experts "
    "consulted for this article all agree that agents should undergo rigorous "
    "red-teaming, a process in which developers try their best to attack a "
    "system in order to discover its vulnerabilities before it is deployed. "
    "But there are also countervailing forces. Companies want to deploy "
    "capable agents, and the more power an agent has and the fewer guardrails "
    "it is subject to the more work it can potentially take on. Security "
    "and utility always have a trade-off, says Bo Li, a professor of "
    "computer science at the University of Illinois Urbana-Champaign. And "
    "adequate red-teaming can be expensive. Defenders have to expend more "
    "resources than attackers do, because attackers only need to discover a "
    "single exploit, while defenders try to discover and patch as many as "
    "they can. When attackers are working toward something as valuable as a "
    "single-word Instagram handle, they will pour resources into finding "
    "exploits, so defenders have to spend even more money to protect that "
    "prize. "
    "As AI models continue to improve, hardening their defenses might "
    "actually get easier. Though the probabilistic nature of large language "
    "models means that LLM agents will always be vulnerable to some forms "
    "of attack, a more sophisticated model might have identified an attempt "
    "to change the email associated with the Obama White House account as "
    "suspicious. And AI systems can be used for agent red-teaming, much as "
    "participants in Anthropic Project Glasswing use Mythos to identify "
    "vulnerabilities in their software. "
    "Still, experts expect that the problem of securing AI agents will only "
    "become more pressing in the future. As agents grow more capable, "
    "companies that adopt them may want to give them more power, both to "
    "provide more services with fewer humans and to avoid being left behind "
    "by their competitors. In the fast-moving world of AI, the time needed "
    "to carefully secure risky agentic systems might seem like an "
    "unconscionable delay. "
    "Everybody wants to be the first to do something and just push things "
    "out without careful scrutiny and red-teaming, Jha says. I think it is "
    "a very dangerous thing."
)


# --------------------------------------------------------------------------- #
# Entity detection fixes validated by this article
# --------------------------------------------------------------------------- #


class TestEntityFixes:
    """Validates entity cluster corrections discovered during this deep dive."""

    def test_bo_li_is_academic_not_meta(self):
        """Bo Li (UIUC professor) should be in Academic/Research, not Meta.

        Bo Li was previously in the Meta cluster because of the Virtue AI
        acqui-hire, but when quoted as a UIUC professor she is an
        independent academic.
        """
        entities = detect_entities(ARTICLE)
        bo_li = [e for e in entities if e.entity == "Bo Li"]
        assert bo_li, "Bo Li not detected"
        assert bo_li[0].cluster == "Academic/Research"

    def test_nature_not_detected_as_journal(self):
        """Lowercase 'nature' in 'probabilistic nature' should not match
        the Nature journal entity.

        The Academic/Research cluster regex must use (?-i:Nature) to
        require capitalization when matching bare 'Nature'.
        """
        entities = detect_entities(ARTICLE)
        nature_hits = [e for e in entities if e.canonical_name == "Nature"]
        assert not nature_hits, (
            f"False positive: 'nature' matched as Nature journal: "
            f"{nature_hits}"
        )

    def test_meta_entities_detected(self):
        entities = detect_entities(ARTICLE)
        meta_entities = [e for e in entities if e.cluster == "Meta"]
        names = {e.entity for e in meta_entities}
        assert "Meta" in names
        assert "Instagram" in names

    def test_anthropic_entities_detected(self):
        entities = detect_entities(ARTICLE)
        anthropic = [e for e in entities if e.cluster == "Anthropic"]
        names = {e.entity for e in anthropic}
        assert "Anthropic" in names
        assert "Mythos" in names
        assert "Project Glasswing" in names

    def test_duke_university_detected(self):
        """Duke University should be detected as Academic/Research."""
        entities = detect_entities(ARTICLE)
        duke = [e for e in entities if "Duke" in e.entity]
        assert duke, "Duke University not detected"
        assert duke[0].cluster == "Academic/Research"

    def test_university_of_illinois_detected(self):
        entities = detect_entities(ARTICLE)
        uiuc = [
            e for e in entities
            if "Illinois" in e.entity and e.cluster == "Academic/Research"
        ]
        assert uiuc, "University of Illinois not detected in Academic/Research"

    def test_university_of_wisconsin_detected(self):
        entities = detect_entities(ARTICLE)
        uw = [
            e for e in entities
            if "Wisconsin" in e.entity and e.cluster == "Academic/Research"
        ]
        assert uw, "University of Wisconsin not detected in Academic/Research"


# --------------------------------------------------------------------------- #
# Topic classification: education metaphor suppression
# --------------------------------------------------------------------------- #


class TestTopicMetaphorSuppression:
    """Education topic should not fire on metaphorical school language."""

    def test_education_not_in_top_topics(self):
        """Metaphorical 'elementary school student' should not trigger
        the education topic when the article is about AI security."""
        topics = classify_topic(ARTICLE)
        topic_names = [t.topic for t in topics]
        assert "education" not in topic_names, (
            f"Education topic should be suppressed for metaphorical usage; "
            f"got: {topics}"
        )

    def test_cybersecurity_is_top_topic(self):
        topics = classify_topic(ARTICLE)
        assert topics, "No topics detected"
        assert topics[0].topic == "cybersecurity"

    def test_ai_development_in_topics(self):
        topics = classify_topic(ARTICLE)
        topic_names = [t.topic for t in topics]
        assert "ai_development" in topic_names


# --------------------------------------------------------------------------- #
# Framing device detection
# --------------------------------------------------------------------------- #


class TestFramingDetection:
    """Key framing devices in the MIT Tech Review AI security article."""

    def test_loaded_language_detected(self):
        devices = detect_framing_devices(ARTICLE)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        evidence = {d.evidence_text for d in loaded}
        assert any("mindless" in e for e in evidence), \
            "'practically mindless' not in loaded_language"
        assert any("embarrass" in e for e in evidence), \
            "'embarrassing' not in loaded_language"

    def test_rhetorical_questions_detected(self):
        devices = detect_framing_devices(ARTICLE)
        rhetorical = [
            d for d in devices if d.device_type == "rhetorical_question"
        ]
        assert len(rhetorical) >= 2, (
            f"Expected >=2 rhetorical questions (guardrails? test?), "
            f"got {len(rhetorical)}"
        )

    def test_refusal_amplification_detected(self):
        devices = detect_framing_devices(ARTICLE)
        refusals = [
            d for d in devices if d.device_type == "refusal_amplification"
        ]
        assert refusals, "'did not respond' should trigger refusal_amplification"

    def test_analogy_metaphor_detected(self):
        """The 'elementary school student' analogy should be caught."""
        devices = detect_framing_devices(ARTICLE)
        analogies = [
            d for d in devices if d.device_type == "analogy_metaphor"
        ]
        assert analogies, "elementary school student analogy not detected"

    def test_kicker_framing_detected(self):
        """'very dangerous thing' at the end is a kicker."""
        devices = detect_framing_devices(ARTICLE)
        kickers = [d for d in devices if d.device_type == "kicker_framing"]
        assert kickers, "'very dangerous thing' kicker not detected"


# --------------------------------------------------------------------------- #
# Source extraction
# --------------------------------------------------------------------------- #


class TestSourceExtraction:
    """Source attribution for the 4 named experts + Meta no-comment."""

    def test_four_named_expert_sources(self):
        sources = extract_sources(ARTICLE)
        experts = [s for s in sources if s.is_expert]
        assert len(experts) >= 4, (
            f"Expected >=4 expert sources (Gong, Ji, Jha, Li), "
            f"got {len(experts)}: {[s.name for s in experts]}"
        )

    def test_meta_no_comment_detected(self):
        sources = extract_sources(ARTICLE)
        no_comment = [s for s in sources if s.source_type == "no_comment"]
        assert no_comment, "Meta's 'did not respond' should be no_comment"

    def test_neil_gong_affiliation(self):
        sources = extract_sources(ARTICLE)
        gong = [s for s in sources if "Gong" in s.name]
        assert gong, "Neil Gong not extracted as source"
        assert "Duke" in gong[0].affiliation


# --------------------------------------------------------------------------- #
# Sentiment
# --------------------------------------------------------------------------- #


class TestSentiment:
    """VADER vs composite tone for a critical-but-measured article."""

    def test_vader_positive_bias(self):
        """VADER scores this critical article highly positive (~0.96),
        demonstrating the known academic-tone gap.  The composite
        correction should bring it negative."""
        vader = analyze_vader(ARTICLE)
        # VADER is unreliable on this genre
        assert vader["compound"] > 0.5, (
            f"VADER unexpectedly negative ({vader['compound']}); "
            f"this article is a known VADER false-positive case"
        )

    def test_composite_corrects_to_negative(self):
        comp = analyze_composite(ARTICLE)
        assert comp.overall_tone < 0.0, (
            f"Composite should correct to negative for this article, "
            f"got {comp.overall_tone}"
        )
