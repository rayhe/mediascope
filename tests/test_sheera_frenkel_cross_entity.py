"""
Cross-entity coverage analysis: Sheera Frenkel (NYT)

Mechanism #9 — Book Deal Narrative Capture: Frenkel's seven-figure "An Ugly Truth"
book deal creates structural financial incentive to maintain adversarial Meta coverage,
while her 2025-2026 beat expansion to AI/national security produced a sympathy register
for Anthropic. Same reporter, same industry, opposite editorial registers.

Key finding: REFUSAL FRAMING INVERSION — when Anthropic refuses Pentagon demands, it's
"principled resistance" and "Silicon Valley rallies behind." When Meta refuses government
AI review demands, it's "holdout" and isolation language. Same behavior, opposite framing.

Sources:
- NYT: "U.S. Presses Meta to Agree to A.I. Reviews as Security Concerns Rise" (Jun 23, 2026)
- NYT: "U.S. Says Anthropic Is an 'Unacceptable' National Security Risk" (Feb 2026)
- NYT: "Anthropic Sues Pentagon Over 'Supply Chain Risk' Label" (Mar 9, 2026)
- NYT: "Anthropic Employees Accuse Trump Administration of Targeting Them" (Mar 2026)
- NYT: "Silicon Valley Rallies Behind Anthropic in A.I. Clash With Trump" (Mar 2026)
- NYT: "White House and Anthropic Hold 'Productive' Meeting" (Apr 2026)
- NYT: "U.S. Loosens Restrictions on Anthropic's Mythos A.I. Model" (Jun 26, 2026)
- NYT: "U.S. Lifts Restrictions on Anthropic's Most Powerful A.I. Models" (Jul 2026)
- NYT: "China Sought Access to Anthropic's Newest A.I. The Answer Was No." (Jul 2026)
- NYT: "Google Signs A.I. Deal With the Pentagon" (Apr 28, 2026)
- NYT: "The Militarization of Silicon Valley" (Aug 4, 2025)
- NYT: "Silicon Valley Bet on War. The Bets Are Paying Off." (Mar 2026)
- Book: "An Ugly Truth: Inside Facebook's Battle for Domination" (HarperCollins, Jul 2021)
- Source: https://talkingbiznews.com/they-talk-biz-news/ny-times-reporters-land-seven-figure-facebook-book-deal/
- Source: https://www.paloaltoonline.com/technology/2021/07/15/meet-the-authors-of-the-book-facebook-is-telling-employees-not-to-read/
"""

import yaml
import pathlib
import pytest


PROFILES = pathlib.Path(__file__).resolve().parent.parent / "profiles"


def _load_nyt():
    with open(PROFILES / "nytimes.yaml") as f:
        return yaml.safe_load(f)


def _find_journalist(data, name):
    for j in data.get("key_journalists", []):
        if j.get("name") == name:
            return j
    return None


# ---------------------------------------------------------------------------
# Test Class 1: Profile Completeness
# ---------------------------------------------------------------------------
class TestFrenkelProfileCompleteness:
    """Verify Frenkel entry has all required cross-entity fields."""

    def test_frenkel_exists(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        assert j is not None, "Sheera Frenkel must exist in NYT journalists"

    def test_has_cross_entity_analysis(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        assert "cross_entity_coverage_analysis" in j

    def test_has_meta_coverage(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        cea = j["cross_entity_coverage_analysis"]
        assert "meta_coverage" in cea

    def test_has_anthropic_coverage(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        cea = j["cross_entity_coverage_analysis"]
        assert "anthropic_coverage" in cea

    def test_has_google_coverage(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        cea = j["cross_entity_coverage_analysis"]
        assert "google_coverage" in cea

    def test_has_cross_entity_patterns(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        cea = j["cross_entity_coverage_analysis"]
        assert "cross_entity_patterns" in cea
        assert len(cea["cross_entity_patterns"]) >= 4

    def test_has_book_financial_interest(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        cea = j["cross_entity_coverage_analysis"]
        assert "book_financial_interest" in cea

    def test_has_mechanism_number(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        cea = j["cross_entity_coverage_analysis"]
        assert cea.get("mechanism_number") == 9

    def test_mechanism_name(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        cea = j["cross_entity_coverage_analysis"]
        assert cea["mechanism_name"] == "book_deal_narrative_capture"


# ---------------------------------------------------------------------------
# Test Class 2: Tone Asymmetry
# ---------------------------------------------------------------------------
class TestToneAsymmetry:
    """Verify the sympathy-adversarial inversion between Anthropic and Meta coverage."""

    def test_meta_tone_negative(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        meta = j["cross_entity_coverage_analysis"]["meta_coverage"]
        assert meta["tone"] <= -0.40, f"Meta tone {meta['tone']} should be strongly negative"

    def test_anthropic_tone_near_neutral(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        anthropic = j["cross_entity_coverage_analysis"]["anthropic_coverage"]
        assert -0.15 <= anthropic["tone"] <= 0.10, f"Anthropic tone {anthropic['tone']} should be near-neutral to slightly positive"

    def test_tone_gap_exceeds_threshold(self):
        """The gap between Meta and Anthropic tone should be >= 0.40."""
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        cea = j["cross_entity_coverage_analysis"]
        gap = cea["anthropic_coverage"]["tone"] - cea["meta_coverage"]["tone"]
        assert gap >= 0.40, f"Tone gap {gap} should be >= 0.40 (sympathy vs adversarial)"

    def test_google_tone_neutral_or_positive(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        google = j["cross_entity_coverage_analysis"]["google_coverage"]
        assert google["tone"] >= -0.10, f"Google tone {google['tone']} should be neutral or positive"

    def test_meta_register_adversarial(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        meta = j["cross_entity_coverage_analysis"]["meta_coverage"]
        assert "adversarial" in meta["register"].lower()

    def test_anthropic_register_sympathy(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        anthropic = j["cross_entity_coverage_analysis"]["anthropic_coverage"]
        assert "sympathy" in anthropic["register"].lower()

    def test_google_register_neutral(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        google = j["cross_entity_coverage_analysis"]["google_coverage"]
        assert "neutral" in google["register"].lower()


# ---------------------------------------------------------------------------
# Test Class 3: Refusal Framing Inversion
# ---------------------------------------------------------------------------
class TestRefusalFramingInversion:
    """Test the core finding: same behavior (refusing government) gets opposite framing."""

    def test_refusal_pattern_exists(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        patterns = j["cross_entity_coverage_analysis"]["cross_entity_patterns"]
        names = [p["pattern_name"] for p in patterns]
        assert "REFUSAL FRAMING INVERSION" in names

    def test_meta_holdout_language(self):
        """Meta's refusal to submit to voluntary review uses 'holdout' isolation language."""
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        meta = j["cross_entity_coverage_analysis"]["meta_coverage"]
        articles = meta.get("recent_articles", [])
        meta_review = [a for a in articles if "Review" in a.get("title", "") or "holdout" in a.get("framing", "").lower()]
        assert len(meta_review) >= 1, "Must have Meta AI review article with holdout framing"
        framing = meta_review[0]["framing"].lower()
        assert "holdout" in framing, "Meta refusal should use 'holdout' language"

    def test_anthropic_principled_language(self):
        """Anthropic's refusal to cooperate uses sympathy/principled language."""
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        anthropic = j["cross_entity_coverage_analysis"]["anthropic_coverage"]
        framing = anthropic.get("framing_pattern", "").lower()
        assert "redemption" in framing or "principled" in framing or "sympathy" in framing

    def test_scare_quote_asymmetry_exists(self):
        """Government labels on Anthropic get scare quotes; Meta doesn't."""
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        patterns = j["cross_entity_coverage_analysis"]["cross_entity_patterns"]
        names = [p["pattern_name"] for p in patterns]
        assert "GOVERNMENT SCARE QUOTE ASYMMETRY" in names

    def test_anthropic_article_scare_quotes(self):
        """Anthropic articles use scare quotes around government labels."""
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        anthropic = j["cross_entity_coverage_analysis"]["anthropic_coverage"]
        articles = anthropic["recent_articles"]
        scare_quote_articles = [a for a in articles if "scare quote" in a.get("framing", "").lower() or "'supply chain risk'" in a.get("title", "").lower() or "'unacceptable" in a.get("title", "").lower()]
        assert len(scare_quote_articles) >= 2, "At least 2 Anthropic articles should have scare-quoted government labels"


# ---------------------------------------------------------------------------
# Test Class 4: Book Deal Financial Conflict
# ---------------------------------------------------------------------------
class TestBookDealFinancialConflict:
    """Test the undisclosed financial conflict from the 'An Ugly Truth' book deal."""

    def test_book_exists_in_profile(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        book = j["cross_entity_coverage_analysis"]["book_financial_interest"]
        assert "An Ugly Truth" in book["title"]

    def test_book_advance_seven_figures(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        book = j["cross_entity_coverage_analysis"]["book_financial_interest"]
        assert "seven" in book["advance"].lower()

    def test_book_publisher_harpercollins(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        book = j["cross_entity_coverage_analysis"]["book_financial_interest"]
        assert "HarperCollins" in book["publisher"]

    def test_book_co_author_kang(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        book = j["cross_entity_coverage_analysis"]["book_financial_interest"]
        assert "Cecilia Kang" in book["co_author"]

    def test_nyt_called_it_ultimate_takedown(self):
        """NYT's own Book Review called the book 'The ultimate takedown' — editorial investment."""
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        book = j["cross_entity_coverage_analysis"]["book_financial_interest"]
        assert "ultimate takedown" in book["nyt_book_review_quote"].lower()

    def test_financial_conflict_note_present(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        book = j["cross_entity_coverage_analysis"]["book_financial_interest"]
        assert "financial conflict" in book["financial_conflict_note"].lower() or "undisclosed" in book["financial_conflict_note"].lower()

    def test_no_anthropic_book(self):
        """No comparable commercial product exists for Anthropic coverage — asymmetric incentive."""
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        book = j["cross_entity_coverage_analysis"]["book_financial_interest"]
        title = book["title"].lower()
        assert "anthropic" not in title
        assert "facebook" in title or "meta" in title.lower()


# ---------------------------------------------------------------------------
# Test Class 5: Anthropic Coverage Volume and Arc
# ---------------------------------------------------------------------------
class TestAnthropicCoverageArc:
    """Test the redemption arc narrative structure in Anthropic coverage."""

    def test_anthropic_article_count(self):
        """Frenkel wrote at least 8 Anthropic-focused articles in 2025-2026."""
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        anthropic = j["cross_entity_coverage_analysis"]["anthropic_coverage"]
        assert len(anthropic["recent_articles"]) >= 8

    def test_headline_sentiment_ascending(self):
        """Anthropic headlines follow ascending sentiment (victim → vindication)."""
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        patterns = j["cross_entity_coverage_analysis"]["cross_entity_patterns"]
        ladder = [p for p in patterns if p["pattern_name"] == "HEADLINE SENTIMENT LADDER"]
        assert len(ladder) == 1
        assert "redemption" in ladder[0]["description"].lower()

    def test_early_articles_negative(self):
        """Early Anthropic articles (supply chain risk, unacceptable) have negative tone from government."""
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        anthropic = j["cross_entity_coverage_analysis"]["anthropic_coverage"]
        early = [a for a in anthropic["recent_articles"] if "risk" in a.get("title", "").lower() or "sues" in a.get("title", "").lower()]
        assert len(early) >= 2
        for a in early:
            assert a["tone"] <= 0.0, f"Early article '{a['title']}' should be negative-toned"

    def test_late_articles_positive(self):
        """Late Anthropic articles (lifts restrictions, China refused) have positive tone."""
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        anthropic = j["cross_entity_coverage_analysis"]["anthropic_coverage"]
        late = [a for a in anthropic["recent_articles"] if "lifts" in a.get("title", "").lower() or "answer was no" in a.get("title", "").lower()]
        assert len(late) >= 2
        for a in late:
            assert a["tone"] > 0.0, f"Late article '{a['title']}' should be positive-toned"

    def test_redemption_arc_in_framing_pattern(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        anthropic = j["cross_entity_coverage_analysis"]["anthropic_coverage"]
        pattern = anthropic["framing_pattern"].lower()
        assert "redemption arc" in pattern or ("victimization" in pattern and "vindication" in pattern)

    def test_rally_article_exists(self):
        """'Silicon Valley Rallies Behind Anthropic' article should be documented."""
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        anthropic = j["cross_entity_coverage_analysis"]["anthropic_coverage"]
        rallies = [a for a in anthropic["recent_articles"] if "rallies" in a.get("title", "").lower()]
        assert len(rallies) >= 1


# ---------------------------------------------------------------------------
# Test Class 6: Beat Migration Pattern
# ---------------------------------------------------------------------------
class TestBeatMigrationPattern:
    """Test that beat migration from cybersecurity to AI/national security preserved adversarial Meta register."""

    def test_beat_field_reflects_migration(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        beat = j["beat"].lower()
        assert "cybersecurity" in beat or "ai" in beat or "national security" in beat

    def test_beat_migration_pattern_exists(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        patterns = j["cross_entity_coverage_analysis"]["cross_entity_patterns"]
        names = [p["pattern_name"] for p in patterns]
        assert "BEAT MIGRATION AS REGISTER RESET" in names

    def test_migration_preserved_adversarial(self):
        """Beat migration did NOT reset adversarial Meta register."""
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        patterns = j["cross_entity_coverage_analysis"]["cross_entity_patterns"]
        migration = [p for p in patterns if p["pattern_name"] == "BEAT MIGRATION AS REGISTER RESET"]
        assert len(migration) == 1
        desc = migration[0]["description"].lower()
        assert "preserved" in desc or "never reset" in desc

    def test_meta_register_consistent_across_beats(self):
        """Meta coverage adversarial in both cybersecurity and AI/national security beats."""
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        meta = j["cross_entity_coverage_analysis"]["meta_coverage"]
        assert meta["tone"] <= -0.40, "Meta tone should remain adversarial after beat migration"


# ---------------------------------------------------------------------------
# Test Class 7: Cross-Validation with Existing Findings
# ---------------------------------------------------------------------------
class TestCrossValidation:
    """Cross-validate Frenkel findings with existing MediaScope patterns."""

    def test_mechanism_9_distinct_from_8(self):
        """Mechanism #9 (book deal capture) is distinct from #8 (institutional register asymmetry)."""
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        cea = j["cross_entity_coverage_analysis"]
        assert cea["mechanism_number"] == 9
        assert cea["mechanism_name"] == "book_deal_narrative_capture"
        # Mechanism 8 is Paresh Dave's institution-driven register — check they differ
        assert cea["mechanism_name"] != "emotional_register_asymmetry"

    def test_nyt_financial_relationship_alignment(self):
        """Frenkel's adversarial Meta coverage aligns with NYT having $0 Meta licensing deal."""
        data = _load_nyt()
        # NYT has documented $0 Meta relationship — Frenkel coverage aligns
        j = _find_journalist(data, "Sheera Frenkel")
        meta = j["cross_entity_coverage_analysis"]["meta_coverage"]
        assert meta["tone"] < 0, "Adversarial Meta coverage aligns with $0 NYT-Meta relationship"

    def test_frenkel_vs_dave_institution_vs_personal(self):
        """Frenkel's conflict is PERSONAL (book deal), Dave's is INSTITUTIONAL (beat assignment).
        Both produce adversarial Meta coverage but through different mechanisms."""
        data = _load_nyt()
        frenkel = _find_journalist(data, "Sheera Frenkel")
        cea = frenkel["cross_entity_coverage_analysis"]
        # Personal financial conflict (book deal)
        assert "book" in cea["mechanism_name"].lower() or "financial" in cea.get("mechanism_description", "").lower()
        assert cea["mechanism_number"] != 8  # Different from Dave

    def test_anthropic_coverage_not_isolated_to_frenkel(self):
        """Other NYT journalists (Cade Metz, Julian Barnes) co-byline Anthropic pieces — institutional pattern."""
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        anthropic = j["cross_entity_coverage_analysis"]["anthropic_coverage"]
        co_bylines = [a for a in anthropic["recent_articles"] if a.get("co_byline")]
        assert len(co_bylines) >= 2, "Multiple Anthropic articles have co-bylines, indicating institutional (not personal) assignment"

    def test_pattern_severity_documented(self):
        """Book deal financial capture should have severity rating."""
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        patterns = j["cross_entity_coverage_analysis"]["cross_entity_patterns"]
        book_pattern = [p for p in patterns if "BOOK DEAL" in p["pattern_name"]]
        assert len(book_pattern) == 1
        assert book_pattern[0].get("severity", 0) >= 3, "Book deal financial capture should be severity 3+"

    def test_all_five_patterns_named(self):
        data = _load_nyt()
        j = _find_journalist(data, "Sheera Frenkel")
        patterns = j["cross_entity_coverage_analysis"]["cross_entity_patterns"]
        names = {p["pattern_name"] for p in patterns}
        expected = {
            "REFUSAL FRAMING INVERSION",
            "BOOK DEAL FINANCIAL CAPTURE",
            "BEAT MIGRATION AS REGISTER RESET",
            "HEADLINE SENTIMENT LADDER",
            "GOVERNMENT SCARE QUOTE ASYMMETRY",
        }
        assert expected.issubset(names), f"Missing patterns: {expected - names}"
