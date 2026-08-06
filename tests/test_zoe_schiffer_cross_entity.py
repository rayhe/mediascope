"""
Tests for Zoë Schiffer (WIRED) cross-entity coverage analysis.

Key finding: WIRED's Director of Business & Industry applies OPPOSITE editorial frames
to the SAME event — the AI talent war — depending on whether she reports from the
OpenAI or Meta perspective. Schiffer has deep insider source access at OpenAI (leaked
memos from Altman, Mark Chen; exclusive Fidji Simo Q&A) while Meta coverage relies on
external/adversarial framing (aggressor, "poaching," crisis, brain drain).

This is analytically significant because Schiffer directs WIRED's entire business desk,
meaning her framing patterns are institutionally amplified. The coverage asymmetry
correlates with Condé Nast's OpenAI content licensing deal.

Sources:
- Techmeme: Altman memo "missionaries will beat mercenaries" — https://www.techmeme.com/250701/p19
- Techmeme: Mark Chen memo "broken into our home" — https://www.techmeme.com/250629/p19
- Techmeme: Fidji Simo Q&A — https://www.techmeme.com/251117/p11
- Techmeme: Altman board rejects Musk offer — https://www.techmeme.com/250211/p33
- Uncanny Valley podcast: Meta AI Brain Drain — https://medial.app/news/wired-roundup-metas-ai-brain-drain-f148f93815613
- Uncanny Valley podcast: Meta in Crisis — https://wdcnews6.com/meta-is-in-crisis-google-searchs-makeover-and-ai-gets-booed-by-graduates/
- TrendForce: Meta Superintelligence exits — https://www.trendforce.com/news/2025/08/27/news-metas-superintelligence-labs-reportedly-hit-by-exits-after-aggressive-ai-hiring-push/
- ScienceSprings: Fidji Simo profile — https://sciencesprings.wordpress.com/2025/11/17/from-wired-openais-fidji-simo-plans-to-make-chatgpt-way-more-useful-and-have-you-pay-for-it/
- Muck Rack: Zoë Schiffer — https://muckrack.com/zoe-schiffer/articles
- Podscan: Uncanny Valley podcast — https://podscan.fm/podcasts/uncanny-valley-wired/episodes/trump-davos-drama-ai-midterms-chatgpts-last-resort-1
"""

import yaml
import os
import pytest


PROFILES_DIR = os.path.join(os.path.dirname(__file__), "..", "profiles")


def load_wired_profile():
    with open(os.path.join(PROFILES_DIR, "wired.yaml")) as f:
        return yaml.safe_load(f)


def load_journalist_profiles():
    with open(os.path.join(PROFILES_DIR, "careers", "journalists.yaml")) as f:
        return yaml.safe_load(f)


def get_schiffer_career(journalists):
    """Find Schiffer's career entry."""
    for j in journalists.get("journalists", []):
        if j.get("name") == "Zoë Schiffer":
            return j
    return None


def get_schiffer_cross_entity(wired_profile):
    """Find Schiffer's cross-entity analysis in the wired profile."""
    cross = wired_profile.get("journalist_cross_entity_coverage", {})
    return cross.get("zoe_schiffer", {})


class TestSchifferEditorialPosition:
    """Verify Schiffer's editorial authority is correctly documented."""

    def test_schiffer_is_director_level(self):
        """Schiffer is Director of Business & Industry — editorial authority, not just a writer."""
        journalists = load_journalist_profiles()
        schiffer = get_schiffer_career(journalists)
        assert schiffer is not None, "Schiffer should be in journalist profiles"
        current_role = schiffer["career"][-1]
        assert "director" in current_role["role"].lower() or "Director" in current_role.get("notes", "")

    def test_schiffer_directs_business_desk(self):
        """Schiffer leads WIRED's business desk, amplifying her framing institutionally."""
        wired = load_wired_profile()
        found = False
        for editor in wired.get("editorial_leadership", []):
            if "Schiffer" in editor.get("name", ""):
                assert "Director" in editor.get("title", "") or "Business" in editor.get("title", "")
                found = True
                break
        assert found, "Schiffer should be in WIRED editorial leadership"

    def test_schiffer_hosts_uncanny_valley(self):
        """Schiffer co-hosts Uncanny Valley podcast — additional amplification channel."""
        journalists = load_journalist_profiles()
        schiffer = get_schiffer_career(journalists)
        assert schiffer is not None
        current = schiffer["career"][-1]
        notes = current.get("notes", "")
        assert "Uncanny Valley" in notes or "podcast" in notes.lower()

    def test_schiffer_career_arc_adversarial_template(self):
        """Career path: Verge (labor) → Platformer → WIRED. Extremely Hardcore book establishes adversarial template."""
        journalists = load_journalist_profiles()
        schiffer = get_schiffer_career(journalists)
        assert schiffer is not None
        publications = [c.get("publication", "") for c in schiffer["career"]]
        assert "the-verge" in publications
        assert "platformer" in publications
        assert "wired" in publications
        # Check for book about adversarial corporate culture
        awards = schiffer.get("awards", [])
        assert any("Extremely Hardcore" in a.get("title", "") for a in awards)


class TestSchifferOpenAICoverage:
    """Verify Schiffer's OpenAI coverage reflects deep insider access with constructive framing."""

    def test_fidji_simo_q_and_a_exists(self):
        """Schiffer published an empathetic exclusive Q&A with OpenAI CEO of Applications."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        openai = cross.get("openai", {})
        articles = openai.get("articles", [])
        simo_articles = [a for a in articles if "Simo" in a.get("title", "") or "Simo" in a.get("subject", "")]
        assert len(simo_articles) >= 1, "Fidji Simo Q&A should be documented"

    def test_fidji_simo_tone_is_empathetic(self):
        """Fidji Simo profile uses empathetic, humanizing language."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        openai = cross.get("openai", {})
        articles = openai.get("articles", [])
        simo = [a for a in articles if "Simo" in a.get("title", "") or "Simo" in a.get("subject", "")]
        assert len(simo) >= 1
        framing = simo[0].get("framing_notes", "")
        # Should mention humanizing elements (chronic illness, Slack responsiveness)
        assert any(kw in framing.lower() for kw in ["empathetic", "humaniz", "chronic", "pots", "sensitiv"]), \
            f"Simo profile should note empathetic/humanizing treatment; got: {framing[:200]}"

    def test_altman_memo_leaked_access(self):
        """Schiffer published Altman's leaked 'missionaries vs mercenaries' memo — insider source access."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        openai = cross.get("openai", {})
        articles = openai.get("articles", [])
        memo_articles = [a for a in articles if "mission" in a.get("title", "").lower()
                        or "mercen" in a.get("title", "").lower()
                        or "Altman" in a.get("subject", "")]
        assert len(memo_articles) >= 1, "Altman 'missionaries' memo should be documented"

    def test_mark_chen_memo_victim_framing(self):
        """Mark Chen memo ('broken into our home') framed OpenAI as emotional victim of Meta's recruiting."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        openai = cross.get("openai", {})
        articles = openai.get("articles", [])
        chen_articles = [a for a in articles if "Chen" in a.get("title", "")
                        or "Chen" in a.get("subject", "")
                        or "broken" in a.get("title", "").lower()]
        assert len(chen_articles) >= 1, "Mark Chen 'broken into our home' memo should be documented"
        framing = chen_articles[0].get("framing_notes", "")
        assert any(kw in framing.lower() for kw in ["victim", "emotional", "sympathy", "broken"]), \
            f"Chen memo should note victimhood framing; got: {framing[:200]}"

    def test_openai_article_count(self):
        """Schiffer has 4+ documented OpenAI articles with constructive or insider framing."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        openai = cross.get("openai", {})
        articles = openai.get("articles", [])
        assert len(articles) >= 4, f"Expected 4+ OpenAI articles, got {len(articles)}"

    def test_openai_tone_aggregate(self):
        """OpenAI aggregate tone should be constructive/insider, not adversarial."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        openai = cross.get("openai", {})
        tone = openai.get("aggregate_tone", "")
        assert any(kw in tone.lower() for kw in ["insider", "constructive", "access", "empathetic"]), \
            f"OpenAI aggregate tone should reflect insider access; got: {tone}"


class TestSchifferMetaCoverage:
    """Verify Schiffer's Meta coverage uses external/adversarial framing."""

    def test_meta_talent_war_framing(self):
        """Meta's talent recruiting framed as corporate aggression, not competitive strategy."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        meta = cross.get("meta", {})
        articles = meta.get("articles", [])
        talent_articles = [a for a in articles if "talent" in a.get("title", "").lower()
                          or "poach" in a.get("title", "").lower()
                          or "$300" in a.get("title", "")
                          or "brain drain" in a.get("title", "").lower()]
        assert len(talent_articles) >= 1, "Meta talent war coverage should be documented"

    def test_meta_brain_drain_crisis_framing(self):
        """Meta researcher departures framed as 'Brain Drain' and 'Crisis' — adversarial language."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        meta = cross.get("meta", {})
        articles = meta.get("articles", [])
        crisis_articles = [a for a in articles if any(kw in a.get("title", "").lower()
                          for kw in ["brain drain", "crisis", "exit", "leaving"])]
        assert len(crisis_articles) >= 1, "Meta 'Brain Drain'/'Crisis' framing should be documented"
        framing = crisis_articles[0].get("framing_notes", "")
        assert any(kw in framing.lower() for kw in ["adversarial", "crisis", "dysfunction", "chaotic"]), \
            f"Meta coverage should note adversarial/crisis framing; got: {framing[:200]}"

    def test_meta_keystroke_monitoring_as_orwellian(self):
        """Meta's employee keystroke monitoring framed as Orwellian 'spyware' in Uncanny Valley podcast."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        meta = cross.get("meta", {})
        articles = meta.get("articles", [])
        monitoring_articles = [a for a in articles if any(kw in a.get("title", "").lower()
                              for kw in ["keystroke", "monitor", "spyware", "laptop"])]
        assert len(monitoring_articles) >= 1 or "keystroke" in str(meta).lower(), \
            "Meta keystroke monitoring/spyware framing should be documented"

    def test_meta_tone_aggregate(self):
        """Meta aggregate tone should be adversarial/external, not insider/empathetic."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        meta = cross.get("meta", {})
        tone = meta.get("aggregate_tone", "")
        assert any(kw in tone.lower() for kw in ["adversarial", "external", "crisis", "aggressive"]), \
            f"Meta aggregate tone should reflect adversarial/external framing; got: {tone}"


class TestSchifferTalentWarAsymmetry:
    """The SAME event (AI talent war) receives OPPOSITE editorial frames."""

    def test_same_event_documented(self):
        """The talent war is documented as a same-event comparison."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        talent_war = cross.get("talent_war_framing_asymmetry", {})
        assert talent_war, "Talent war framing asymmetry should be documented"

    def test_meta_framed_as_aggressor(self):
        """When Meta recruits: 'poaching,' corporate aggression, hyperbolic spending."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        talent_war = cross.get("talent_war_framing_asymmetry", {})
        meta_side = talent_war.get("meta_framing", "")
        assert any(kw in meta_side.lower() for kw in ["aggress", "poach", "disrupt", "spending"]), \
            f"Meta talent framing should use aggression language; got: {meta_side[:200]}"

    def test_openai_framed_as_victim(self):
        """When OpenAI responds: 'missionaries,' moral superiority, victimhood."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        talent_war = cross.get("talent_war_framing_asymmetry", {})
        openai_side = talent_war.get("openai_framing", "")
        assert any(kw in openai_side.lower() for kw in ["victim", "mission", "moral", "home"]), \
            f"OpenAI talent framing should use victimhood language; got: {openai_side[:200]}"

    def test_talent_war_delta_score(self):
        """The framing delta between Meta and OpenAI in talent war coverage should be significant."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        talent_war = cross.get("talent_war_framing_asymmetry", {})
        delta = talent_war.get("framing_delta", 0)
        assert delta >= 0.5, f"Talent war framing delta should be >= 0.5; got: {delta}"


class TestSchifferExecutiveProfileAsymmetry:
    """Executive profiles: empathetic for OpenAI, absent or adversarial for Meta."""

    def test_openai_executive_profile_exists(self):
        """At least one OpenAI executive gets an empathetic long-form profile."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        openai = cross.get("openai", {})
        articles = openai.get("articles", [])
        profiles = [a for a in articles if a.get("article_type") in ("profile", "q_and_a", "interview")]
        assert len(profiles) >= 1, "Should have at least 1 OpenAI executive profile"

    def test_meta_executive_profile_absent(self):
        """No equivalent humanizing Meta executive profile by Schiffer."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        meta = cross.get("meta", {})
        articles = meta.get("articles", [])
        profiles = [a for a in articles if a.get("article_type") in ("profile", "q_and_a", "interview")]
        assert len(profiles) == 0, \
            f"Expected 0 humanizing Meta executive profiles; got {len(profiles)}"

    def test_executive_profile_asymmetry_documented(self):
        """The executive profile gap should be explicitly noted in asymmetry analysis."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        notes = cross.get("asymmetry_notes", "")
        assert any(kw in notes.lower() for kw in ["executive profile", "no equivalent", "absent"]), \
            "Asymmetry notes should document executive profile gap"


class TestSchifferDepartureFraining:
    """Researcher departures from Meta vs OpenAI framed differently."""

    def test_meta_departures_are_brain_drain(self):
        """Meta researcher exits framed as institutional failure ('Brain Drain', 'Crisis')."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        departures = cross.get("departure_framing_asymmetry", {})
        meta_frame = departures.get("meta_departures", "")
        assert any(kw in meta_frame.lower() for kw in ["brain drain", "crisis", "failure", "dysfunction"]), \
            f"Meta departures should be framed as institutional failure; got: {meta_frame[:200]}"

    def test_openai_departures_are_principled(self):
        """OpenAI researcher exits framed as principled safety concerns, not organizational dysfunction."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        departures = cross.get("departure_framing_asymmetry", {})
        openai_frame = departures.get("openai_departures", "")
        assert any(kw in openai_frame.lower() for kw in ["principl", "safety", "mission", "ethical"]), \
            f"OpenAI departures should be framed as principled; got: {openai_frame[:200]}"


class TestSchifferFinancialCorrelation:
    """Coverage direction correlates with Condé Nast financial relationships."""

    def test_conde_nast_openai_deal_documented(self):
        """Condé Nast has content licensing deal with OpenAI — financial incentive."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        financial = cross.get("financial_correlation", {})
        assert financial.get("conde_nast_openai_deal", False), \
            "Condé Nast's OpenAI content licensing deal should be documented"

    def test_no_meta_financial_relationship(self):
        """No equivalent financial relationship between Condé Nast and Meta."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        financial = cross.get("financial_correlation", {})
        assert financial.get("conde_nast_meta_deal", False) is False, \
            "No Condé Nast-Meta financial relationship should be documented"

    def test_financial_predicts_coverage_direction(self):
        """Financial relationship direction (money flows from OpenAI → Condé Nast) predicts editorial sympathy."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        financial = cross.get("financial_correlation", {})
        prediction = financial.get("financial_predicts_tone", "")
        assert any(kw in prediction.lower() for kw in ["correlat", "predict", "aligns"]), \
            f"Financial prediction should be documented; got: {prediction[:200]}"


class TestSchifferOverallAsymmetryScore:
    """Aggregate asymmetry scoring for Schiffer's cross-entity coverage."""

    def test_asymmetry_score_exists(self):
        """An overall cross-entity asymmetry score should be documented."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        score = cross.get("cross_entity_asymmetry_score", 0)
        assert score > 0, "Cross-entity asymmetry score should be documented"

    def test_asymmetry_score_is_high(self):
        """Given the evidence, score should be >= 0.7 (high asymmetry)."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        score = cross.get("cross_entity_asymmetry_score", 0)
        assert score >= 0.70, f"Asymmetry score should be >= 0.70; got: {score}"

    def test_asymmetry_notes_comprehensive(self):
        """Asymmetry notes should cover all four dimensions: source access, talent war, executive profiles, departures."""
        cross = get_schiffer_cross_entity(load_wired_profile())
        notes = cross.get("asymmetry_notes", "").lower()
        dimensions = ["source access", "talent", "executive", "departure"]
        found = sum(1 for d in dimensions if d in notes)
        assert found >= 3, f"Asymmetry notes should cover 3+ of 4 dimensions; covered {found}"
