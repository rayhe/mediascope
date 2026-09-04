"""Type A #517 (2026-09-04 11:00 PDT): The Guardian x Anthropic book-piracy
editorial register vs OpenAI deal-partner register.

The Guardian's Feb 14 2025 strategic partnership with OpenAI (mechanism_514)
predicts softer OpenAI coverage. Observed: a GRADIENT, not a binary. The
Guardian publishes entity-targeted piracy framing in the opinion-editorial
register against Anthropic (Kathryn James, Aug 5 2026, "Why is Anthropic
destroying books?", cross-linking the Guardian-view "authors should be
protected over big tech" editorial line; plus Sep 2025 $1.5bn settlement
news) while OpenAI's documented book piracy (Books1/Books2, Tremblay
shadow-library allegations, O'Reilly DE-COP study) draws no equivalent
Guardian editorial - a bounded site:theguardian.com absence. The Guardian
DOES cover OpenAI copyright fights adversarially in news register (NYT-led
sanctions motion, Milmo rogue-agent pieces), so the asymmetry is register
depth and editorial companionship, not coverage existence.

Statistical discipline: MANUAL ILLUSTRATIVE tones at article level, n=2 vs
n=3. Live scorer reproduced this run: delta -0.31, p_value 0.315, cohens_d
-1.98, is_significant False. Directionally consistent with deal-partner
softening; no significance claimed or claimable. correlation_not_causation.

Evidence hygiene: the James piece was viewed full-text via the
drwebdomain.blog mirror (Guardian original confirmed via mirror outlinks);
the sanctions piece via the dailyguardian.eu mirror; the settlement URL and
News Sniffer archive record are Guardian-canonical. All URLs carried
verbatim from search-result full-URL listings or tool-verified opens - no
canonical URLs constructed. No zero-coverage claims without the bounded
method (iteration-492 rule).

Durable conventions (from #495): line-anchored (^, re.MULTILINE) heading
search in iteration-log.md; relative newest-first ordering between
neighbors, never absolute-top or fixed head slices.
"""

import os
import re
from datetime import datetime

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GUARDIAN_PROFILE = os.path.join(REPO, "profiles", "guardian.yaml")
LOG = os.path.join(REPO, "iteration-log.md")
MECH_KEY = "mechanism_517_guardian_anthropic_piracy_editorial_vs_openai_deal_partner"

JAMES_MIRROR = "https://drwebdomain.blog/2026/08/06/why-is-anthropic-destroying-books-kathryn-james-the-guardian/"
SETTLEMENT_URL = "https://www.theguardian.com/technology/2025/sep/05/anthropic-settlement-ai-book-lawsuit"
NEWSNIFFER_URL = "https://www.newssniffer.co.uk/versions/16485671"
FINAL_APPROVAL_URL = "https://firstamendment.mtsu.edu/post/judge-approves-1-5b-anthropic-settlement-over-pirated-books-used-to-train-chatbot/"
SANCTIONS_MIRROR = "https://dailyguardian.eu/news-outlets-seek-sanctions-against-openai-in-copyright-battle/"
REGISTER_BOOKS_URL = "https://www.theregister.com/2023/09/21/authors_guild_openai_lawsuit/"
BLOOMBERGLAW_TREMBLAY_URL = "https://news.bloomberglaw.com/tech-and-telecom-law/openai-facing-another-copyright-suit-over-ai-training-on-novels"
REGISTER_OREILLY_URL = "https://www.theregister.com/software/2025/04/03/study-suggests-openai-isnt-waiting-for-copyright-exemption/1097658?td=keepreading"


def _mechanism():
    with open(GUARDIAN_PROFILE) as f:
        doc = yaml.safe_load(f)
    return doc["competitor_relationships"]["anthropic"][MECH_KEY]


def _mechanism_text():
    return yaml.dump(_mechanism(), default_flow_style=False, sort_keys=False, allow_unicode=False)


def _segment(log_text, num):
    """Return the text of iteration #num's log entry (heading to next heading)."""
    headings = [(m.start(), m.group(1)) for m in re.finditer(r"^#(\d+) Type [A-E]:", log_text, re.M)]
    starts = [pos for pos, n in headings if n == str(num)]
    assert starts, f"#{num} heading not found"
    start = starts[0]
    later = [pos for pos, _ in headings if pos > start]
    end = min(later) if later else len(log_text)
    return log_text[start:end]


class TestMechanism517Structure:
    def test_yaml_parses(self):
        with open(GUARDIAN_PROFILE) as f:
            yaml.safe_load(f)

    def test_mechanism_key_exists_under_anthropic(self):
        with open(GUARDIAN_PROFILE) as f:
            doc = yaml.safe_load(f)
        assert MECH_KEY in doc["competitor_relationships"]["anthropic"]

    def test_identity_fields(self):
        m = _mechanism()
        assert m["mechanism_id"] == 517
        assert m["iteration"] == 517
        assert m["iteration_type"] == "A"
        assert m["iteration_time"] == "2026-09-04 11:00 PDT"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_publication_and_pair(self):
        m = _mechanism()
        assert m["publication_focus"] == "The Guardian"
        assert "Anthropic" in m["entity_pair"]
        assert "OpenAI" in m["entity_pair"]

    def test_gradient_not_binary_framing(self):
        m = _mechanism()
        assert "GRADIENT" in m["discovery_summary"]
        assert "not a binary" in m["discovery_summary"]

    def test_anthropic_description_points_to_mechanism(self):
        with open(GUARDIAN_PROFILE) as f:
            doc = yaml.safe_load(f)
        desc = doc["competitor_relationships"]["anthropic"]["description"]
        assert "mechanism_517" in desc

    def test_mechanism_is_nested_dict(self):
        assert isinstance(_mechanism(), dict)


class TestAnthropicArticlesEvidence:
    def test_two_anthropic_articles(self):
        arts = _mechanism()["anthropic_articles"]
        assert len(arts) == 2

    def test_james_piece_identity(self):
        j = _mechanism()["anthropic_articles"][0]
        assert j["title"] == "Why is Anthropic destroying books?"
        assert j["author"] == "Kathryn James"
        assert j["date"] == "2026-08-05"
        assert j["register"] == "comment/opinion"
        assert j["publication"] == "The Guardian"

    def test_james_piece_first_hand_via_mirror(self):
        j = _mechanism()["anthropic_articles"][0]
        assert j["mirror_url"] == JAMES_MIRROR
        assert j["dateline_verified"] == "Wed 5 Aug 2026 07.00 EDT"

    def test_james_key_phrases_adversarial(self):
        phrases = _mechanism()["anthropic_articles"][0]["key_phrases"]
        assert any("pirated sources instead" in p for p in phrases)
        assert any("destructively scan" in p for p in phrases)

    def test_james_editorial_cross_link(self):
        j = _mechanism()["anthropic_articles"][0]
        assert "authors should be protected over big tech" in j["editorial_cross_link"]

    def test_james_tone_adversarial(self):
        assert _mechanism()["anthropic_articles"][0]["manual_illustrative_tone"] == pytest.approx(-0.65)

    def test_settlement_piece_identity(self):
        s = _mechanism()["anthropic_articles"][1]
        assert s["url"] == SETTLEMENT_URL
        assert s["archive_record"] == NEWSNIFFER_URL
        assert s["register"] == "news"

    def test_settlement_figures(self):
        facts = _mechanism()["anthropic_articles"][1]["key_facts"]
        joined = " ".join(facts)
        assert "$1.5bn" in joined
        assert "500,000 books" in joined
        assert "LibGen" in joined
        assert "Martinez-Olguin" in joined

    def test_settlement_tone_moderate_negative(self):
        assert _mechanism()["anthropic_articles"][1]["manual_illustrative_tone"] == pytest.approx(-0.3)


class TestOpenAIDealPartnerEvidence:
    def test_partnership_note_present(self):
        p = _mechanism()["openai_articles_deal_partner"]["partnership"]
        assert "Feb 14 2025" in p
        assert "mechanism_514" in p

    def test_three_openai_articles(self):
        arts = _mechanism()["openai_articles_deal_partner"]["articles"]
        assert len(arts) == 3

    def test_sanctions_piece_first_hand_via_mirror(self):
        s = _mechanism()["openai_articles_deal_partner"]["articles"][0]
        assert s["title"] == "News outlets seek sanctions against OpenAI in copyright battle"
        assert s["mirror_url"] == SANCTIONS_MIRROR
        assert s["register"] == "news"

    def test_sanctions_key_phrases(self):
        phrases = _mechanism()["openai_articles_deal_partner"]["articles"][0]["key_phrases"]
        assert any("obstruction" in p for p in phrases)

    def test_sanctions_tone_capacity_for_negative(self):
        # counter to the softening thesis: proves negative OpenAI framing capacity
        assert _mechanism()["openai_articles_deal_partner"]["articles"][0]["manual_illustrative_tone"] == pytest.approx(-0.25)

    def test_milmo_rogue_pieces_present(self):
        titles = [a["title"] for a in _mechanism()["openai_articles_deal_partner"]["articles"]]
        assert any("rogue" in t for t in titles)
        assert any("radical transparency" in t for t in titles)

    def test_openai_tones(self):
        tones = [a["manual_illustrative_tone"] for a in _mechanism()["openai_articles_deal_partner"]["articles"]]
        assert tones == pytest.approx([-0.25, -0.1, -0.15])


class TestOpenAIPiracyEditorialAbsence:
    def test_absence_block_present(self):
        a = _mechanism()["openai_piracy_editorial_absence"]
        assert "bounded absence" in a["status"]

    def test_absence_method_named(self):
        a = _mechanism()["openai_piracy_editorial_absence"]
        assert "site:theguardian.com" in a["method"]

    def test_three_documented_openai_piracy_facts(self):
        facts = _mechanism()["openai_piracy_editorial_absence"]["openai_documented_piracy_that_lacks_guardian_editorial"]
        assert len(facts) == 3
        joined = " ".join(facts)
        assert "Books1/Books2" in joined
        assert "Tremblay" in joined
        assert "O'Reilly" in joined

    def test_absence_source_urls_verbatim(self):
        urls = _mechanism()["openai_piracy_editorial_absence"]["source_urls"]
        assert REGISTER_BOOKS_URL in urls
        assert BLOOMBERGLAW_TREMBLAY_URL in urls
        assert REGISTER_OREILLY_URL in urls


class TestScorerReproduction:
    def _run(self):
        from mediascope.score.asymmetry import calculate_asymmetry
        return calculate_asymmetry(
            target_scores=[-0.65, -0.3],
            peer_scores=[-0.25, -0.1, -0.15],
            target_entity="anthropic",
            peer_entities=["openai"],
            publication_slug="guardian",
            period_start=datetime(2025, 9, 1),
            period_end=datetime(2026, 9, 4),
        )

    def test_delta_matches_profile(self):
        r = self._run()
        assert r.asymmetry_score == pytest.approx(_mechanism()["scorer_manual_illustrative"]["asymmetry_delta"], abs=0.01)

    def test_target_peer_means(self):
        r = self._run()
        res = _mechanism()["scorer_manual_illustrative"]
        assert r.target_avg_tone == pytest.approx(res["target_avg"], abs=0.01)
        assert r.peer_avg_tone == pytest.approx(res["peer_avg"], abs=0.01)

    def test_not_significant(self):
        r = self._run()
        assert r.is_significant is False
        assert _mechanism()["scorer_manual_illustrative"]["is_significant"] is False

    def test_p_value_matches(self):
        r = self._run()
        assert r.p_value == pytest.approx(_mechanism()["scorer_manual_illustrative"]["p_value"], abs=0.01)

    def test_cohens_d_matches(self):
        r = self._run()
        assert r.cohens_d == pytest.approx(_mechanism()["scorer_manual_illustrative"]["cohens_d"], abs=0.01)

    def test_manual_illustrative_note_present(self):
        note = _mechanism()["scorer_manual_illustrative"]["note"]
        assert "MANUAL ILLUSTRATIVE" in note
        assert "NOT statistically significant" in note

    def test_ci_recorded_ordered(self):
        res = _mechanism()["scorer_manual_illustrative"]
        assert res["ci_lower"] <= res["ci_upper"]

    def test_live_scorer_flag(self):
        assert _mechanism()["scorer_manual_illustrative"]["reproduced_by_live_scorer"] is True


class TestSourceHygiene:
    def test_all_urls_https(self):
        m = _mechanism()
        urls = [JAMES_MIRROR, SETTLEMENT_URL, NEWSNIFFER_URL, FINAL_APPROVAL_URL,
                SANCTIONS_MIRROR, REGISTER_BOOKS_URL, BLOOMBERGLAW_TREMBLAY_URL,
                REGISTER_OREILLY_URL]
        for u in urls:
            assert u.startswith("https://"), u
        text = _mechanism_text()
        for u in urls:
            assert u in text, u

    def test_no_em_dashes_in_new_mechanism_text(self):
        assert "\u2014" not in _mechanism_text()
        assert "\u2013" not in _mechanism_text()

    def test_ascii_only_in_new_mechanism_text(self):
        text = _mechanism_text()
        assert all(ord(c) < 128 for c in text)


class TestConfoundersAndDiscipline:
    def test_confounders_ranked_three_tiers(self):
        confs = _mechanism()["confounders_ranked"]
        assert set(confs.keys()) == {"strong", "moderate", "weak"}
        assert len(confs["strong"]) == 2
        assert len(confs["moderate"]) == 2

    def test_register_mismatch_confounder_present(self):
        strong = " ".join(_mechanism()["confounders_ranked"]["strong"])
        assert "Register mismatch" in strong
        assert "opinion" in strong

    def test_news_value_gap_confounder_present(self):
        strong = " ".join(_mechanism()["confounders_ranked"]["strong"])
        assert "News-value gap" in strong

    def test_counter_evidence_nonempty(self):
        ce = _mechanism()["counter_evidence"]
        assert len(ce) == 4

    def test_counter_evidence_sanctions_coverage(self):
        ce = " ".join(_mechanism()["counter_evidence"])
        assert "hiding and destroying evidence" in ce

    def test_correlation_not_causation(self):
        assert _mechanism()["correlation_not_causation"] is True
        assert "does not imply editorial control" in _mechanism()["cautious_language"]

    def test_cross_references_include_514(self):
        assert 514 in _mechanism()["cross_references"]

    def test_financial_context_correlate_only(self):
        assert "correlate only" in _mechanism()["financial_context"]["status"]


class TestSiblingBlockIntegrity:
    # Regression guard: the #517 edit once orphaned the amazon block's
    # subkeys (dropped its heading, then restored it without financial_tie).
    # These tests assert the neighboring competitor_relationships blocks are
    # structurally intact after the mechanism insertion.
    def test_amazon_block_intact(self):
        with open(GUARDIAN_PROFILE) as f:
            doc = yaml.safe_load(f)
        amazon = doc["competitor_relationships"]["amazon"]
        assert amazon["financial_tie"] == "none"
        assert amazon["estimated_value"] == "$0"
        assert amazon["description"] == "No known direct financial relationship."
        assert amazon["coverage_prediction"] == "neutral"

    def test_anthropic_base_fields_intact(self):
        with open(GUARDIAN_PROFILE) as f:
            doc = yaml.safe_load(f)
        anth = doc["competitor_relationships"]["anthropic"]
        assert anth["financial_tie"] == "none"
        assert anth["estimated_value"] == "$0"
        assert anth["coverage_prediction"] == "neutral"

    def test_openai_licensing_block_untouched(self):
        with open(GUARDIAN_PROFILE) as f:
            doc = yaml.safe_load(f)
        openai = doc["competitor_relationships"]["openai"]
        assert openai["financial_tie"] == "licensing"


class TestNoveltyVsPrior:
    def test_no_prior_guardian_anthropic_type_a(self):
        with open(GUARDIAN_PROFILE) as f:
            doc = yaml.safe_load(f)
        anth = doc["competitor_relationships"]["anthropic"]
        mech_keys = [k for k in anth if k.startswith("mechanism_")]
        assert mech_keys == [MECH_KEY]

    def test_openai_partner_block_is_data_not_mechanism(self):
        # guardian.yaml openai competitor_relationships block carries the deal as
        # data rows; the Type A mechanism lives under anthropic. No duplicate key.
        with open(GUARDIAN_PROFILE) as f:
            doc = yaml.safe_load(f)
        openai = doc["competitor_relationships"]["openai"]
        assert not any("517" in k for k in openai)


class TestIterationLog:
    def test_517_entry_present(self):
        with open(LOG) as f:
            log_text = f.read()
        seg = _segment(log_text, 517)
        assert "Type A" in seg

    def test_517_entry_guardian_anthropic(self):
        with open(LOG) as f:
            log_text = f.read()
        seg = _segment(log_text, 517)
        assert "Guardian" in seg
        assert "Anthropic" in seg

    def test_517_scorer_numbers_in_log(self):
        with open(LOG) as f:
            log_text = f.read()
        seg = _segment(log_text, 517)
        assert "-0.31" in seg
        assert "0.315" in seg

    def test_rotation_transparency_516_to_517(self):
        with open(LOG) as f:
            log_text = f.read()
        seg = _segment(log_text, 517)
        assert "516 E -> 517 A" in seg

    def test_517_newer_than_516(self):
        with open(LOG) as f:
            log_text = f.read()
        headings = [(m.start(), m.group(1)) for m in re.finditer(r"^#(\d+) Type [A-E]:", log_text, re.M)]
        pos517 = next(p for p, n in headings if n == "517")
        pos516 = next(p for p, n in headings if n == "516")
        assert pos517 < pos516, "newest-first ordering violated"
