"""
Test Type B #533: Keach Hagey (WSJ) matched-story-type symmetry - Sep 05 2026

Mechanism #533 Type B - Journalist Cross-Entity Tracking
Journalist: Keach Hagey (Wall Street Journal senior reporter, AI companies beat)
Focus: Reporter-level matched-story-type register comparison. On
legal/regulatory enforcement stories Hagey's Meta register (Wynn-Williams
lawsuit, Jun 25 2026, co-byline Meghan Bobrowsky) and OpenAI register (state
AG investigation, Jun 13 2026, co-byline Georgia Wells) are essentially
symmetric: Meta MANUAL ILLUSTRATIVE -0.35 vs OpenAI -0.30, delta -0.05,
p_value NOT_CALCULATED, is_significant False, NOT artifact-grade. The larger
apparent gap (Meta lawsuit -0.35 vs OpenAI Astra safety eval -0.15, delta
-0.20) is a story-type mismatch artifact. Extends mechanism #32 (Wells
dual-beat control: register difference explained by story type, not financial
relationship) and #532 (WSJ publication-level dual-deal near-symmetry, delta
-0.075) from publication level to reporter level.

Validates:
- Keach Hagey exists in news-corp.yaml journalist_profiles with WSJ role
- Mechanism 533 exists with correct iteration_type B, iteration 533, date 2026-09-05
- Meta side: Wynn-Williams lawsuit article with verbatim title, date, co-author, URL
- OpenAI side: AG investigation (Wells co-byline) + Astra critical-cyber (Schechner co-byline),
  verbatim titles and URLs
- Matched comparison: legal_regulatory_enforcement story type, delta -0.05,
  p_value NOT_CALCULATED, is_significant False
- Statistical discipline: correlation_not_causation true, artifact_readiness
  declines analysis.json update, confounders ranked STRONG/MODERATE/WEAK,
  counter_evidence present
- Hygiene: ASCII-only, no em/en dashes, HTTPS-only URLs, cross-references to
  #32 and #532, novelty statement

No em dashes allowed per project rule.

Source URLs:
  - Meta Wynn-Williams: https://www.wsj.com/us-news/law/meta-tried-to-silence-her-now-shes-suing-b228997c
  - OpenAI AG investigation: https://www.wsj.com/tech/openai-investigated-by-coalition-of-state-attorneys-general-088a3928
  - OpenAI Astra critical cyber: https://www.wsj.com/tech/ai/openai-to-restrict-astra-model-after-rating-it-critical-cyber-risk-499b5a46
"""

import pathlib

import yaml

PROFILES_DIR = pathlib.Path(__file__).resolve().parent.parent / "profiles"

META_URL = "https://www.wsj.com/us-news/law/meta-tried-to-silence-her-now-shes-suing-b228997c"
AG_URL = "https://www.wsj.com/tech/openai-investigated-by-coalition-of-state-attorneys-general-088a3928"
ASTRA_URL = "https://www.wsj.com/tech/ai/openai-to-restrict-astra-model-after-rating-it-critical-cyber-risk-499b5a46"


def load_news_corp_profile():
    with open(PROFILES_DIR / "news-corp.yaml") as f:
        return yaml.safe_load(f)


def get_hagey_profile(data):
    """Extract Keach Hagey's journalist profile from news-corp.yaml."""
    for jp in data.get("journalist_profiles", []):
        if jp.get("name") == "Keach Hagey":
            return jp
    return None


def get_mech(profile):
    mech = profile.get("cross_entity_coverage_analysis", {})
    assert mech.get("mechanism_id") == 533, "mechanism 533 missing for Hagey"
    return mech


def walk_strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from walk_strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk_strings(v)


# ---------------------------------------------------------------------------
# Class 1: Profile structure and existence
# ---------------------------------------------------------------------------
class TestHageyProfileStructure:
    """Verify Keach Hagey's journalist profile exists and is properly structured."""

    def test_profile_exists(self):
        data = load_news_corp_profile()
        profile = get_hagey_profile(data)
        assert profile is not None, "Keach Hagey profile missing from news-corp.yaml"

    def test_current_role(self):
        data = load_news_corp_profile()
        profile = get_hagey_profile(data)
        assert profile.get("current_role") == "senior_reporter"

    def test_publication_is_wsj(self):
        data = load_news_corp_profile()
        profile = get_hagey_profile(data)
        assert profile.get("publication") == "The Wall Street Journal"

    def test_beat_covers_openai(self):
        data = load_news_corp_profile()
        profile = get_hagey_profile(data)
        beat = str(profile.get("beat", ""))
        assert "OpenAI" in beat

    def test_background_mentions_optimist_book(self):
        data = load_news_corp_profile()
        profile = get_hagey_profile(data)
        background = str(profile.get("background", ""))
        assert "Optimist" in background
        assert "Altman" in background


# ---------------------------------------------------------------------------
# Class 2: Mechanism identity
# ---------------------------------------------------------------------------
class TestMechanismIdentity:
    """Verify mechanism 533 identity fields."""

    def test_mechanism_id_533(self):
        data = load_news_corp_profile()
        mech = get_mech(get_hagey_profile(data))
        assert mech["mechanism_id"] == 533

    def test_iteration_type_b(self):
        data = load_news_corp_profile()
        mech = get_mech(get_hagey_profile(data))
        assert mech.get("iteration_type") == "B"
        assert mech.get("iteration") == 533

    def test_date_2026_09_05(self):
        data = load_news_corp_profile()
        mech = get_mech(get_hagey_profile(data))
        assert mech.get("date") == "2026-09-05"

    def test_author_kit_with_ray(self):
        data = load_news_corp_profile()
        mech = get_mech(get_hagey_profile(data))
        assert mech.get("author") == "Kit (with Ray)"


# ---------------------------------------------------------------------------
# Class 3: Meta coverage
# ---------------------------------------------------------------------------
class TestMetaCoverage:
    """Verify the Meta Wynn-Williams lawsuit article entry."""

    def _article(self):
        data = load_news_corp_profile()
        mech = get_mech(get_hagey_profile(data))
        articles = mech["meta_coverage"]["articles"]
        assert len(articles) == 1
        return articles[0]

    def test_title_verbatim(self):
        a = self._article()
        assert a["title"] == "Meta Tried to Silence Her. Now She's Suing."

    def test_date_2026_06_25(self):
        a = self._article()
        assert a["date"] == "2026-06-25"

    def test_co_author_bobrowsky(self):
        a = self._article()
        assert a["co_author"] == "Meghan Bobrowsky"

    def test_url_verbatim_https(self):
        a = self._article()
        assert a["source_url"] == META_URL
        assert a["source_url"].startswith("https://")

    def test_tone_manual_illustrative(self):
        a = self._article()
        assert a["tone_MANUAL_ILLUSTRATIVE"] == -0.35

    def test_research_method_bounded(self):
        a = self._article()
        assert a["research_method"] == "search_result_excerpt_bounded_sep05"


# ---------------------------------------------------------------------------
# Class 4: OpenAI coverage
# ---------------------------------------------------------------------------
class TestOpenAICoverage:
    """Verify the two OpenAI article entries."""

    def _articles(self):
        data = load_news_corp_profile()
        mech = get_mech(get_hagey_profile(data))
        return mech["openai_coverage"]["articles"]

    def test_two_openai_articles(self):
        assert len(self._articles()) == 2

    def test_ag_investigation_wells_cobyline(self):
        arts = self._articles()
        ag = next(a for a in arts if "Attorneys General" in a["title"])
        assert ag["date"] == "2026-06-13"
        assert ag["co_author"] == "Georgia Wells"
        assert ag["source_url"] == AG_URL
        assert ag["tone_MANUAL_ILLUSTRATIVE"] == -0.30
        assert ag["topic"] == "ag_investigation"

    def test_astra_schechner_cobyline(self):
        arts = self._articles()
        astra = next(a for a in arts if "Astra" in a["title"])
        assert astra["date"] == "2026-09-02"
        assert astra["co_author"] == "Sam Schechner"
        assert astra["source_url"] == ASTRA_URL
        assert astra["tone_MANUAL_ILLUSTRATIVE"] == -0.15
        assert astra["topic"] == "ai_safety_eval"
        assert astra["research_method"] == "search_result_excerpt_bounded_sep05"


# ---------------------------------------------------------------------------
# Class 5: Matched comparison
# ---------------------------------------------------------------------------
class TestMatchedComparison:
    """Verify the matched-story-type symmetry scorer."""

    def _mc(self):
        data = load_news_corp_profile()
        mech = get_mech(get_hagey_profile(data))
        return mech["matched_comparison"]

    def test_story_type_legal_enforcement(self):
        assert self._mc()["story_type"] == "legal_regulatory_enforcement"

    def test_delta_minus_0_05(self):
        mc = self._mc()
        assert mc["meta_tone_MANUAL_ILLUSTRATIVE"] == -0.35
        assert mc["openai_tone_MANUAL_ILLUSTRATIVE"] == -0.30
        assert mc["delta"] == -0.05

    def test_delta_note_discipline(self):
        note = str(self._mc()["delta_note"])
        assert "NOT_CALCULATED" in note
        assert "is_significant false" in note
        assert "NOT artifact-grade" in note

    def test_mismatched_comparison_noted(self):
        note = str(self._mc()["mismatched_comparison_note"])
        assert "-0.20" in note
        assert "story types" in note or "story type" in note


# ---------------------------------------------------------------------------
# Class 6: Statistical discipline
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline:
    """Verify no-significance discipline, confounders, counter-evidence."""

    def test_correlation_not_causation(self):
        data = load_news_corp_profile()
        mech = get_mech(get_hagey_profile(data))
        assert mech.get("correlation_not_causation") is True

    def test_artifact_readiness_declines_update(self):
        data = load_news_corp_profile()
        mech = get_mech(get_hagey_profile(data))
        readiness = str(mech.get("artifact_readiness", ""))
        assert "No analysis.json update" in readiness

    def test_confounders_ranked_three_tiers(self):
        data = load_news_corp_profile()
        mech = get_mech(get_hagey_profile(data))
        conf = mech.get("confounders_ranked", {})
        for tier in ("strong", "moderate", "weak"):
            assert len(conf.get(tier, [])) >= 1, f"confounder tier {tier} empty"

    def test_confounders_name_co_byline(self):
        data = load_news_corp_profile()
        mech = get_mech(get_hagey_profile(data))
        strong = " ".join(mech["confounders_ranked"]["strong"])
        assert "Co-byline dilution" in strong

    def test_counter_evidence_nonempty(self):
        data = load_news_corp_profile()
        mech = get_mech(get_hagey_profile(data))
        ce = mech.get("counter_evidence", [])
        assert len(ce) >= 3

    def test_cross_references_32_and_532(self):
        data = load_news_corp_profile()
        mech = get_mech(get_hagey_profile(data))
        refs = " ".join(mech.get("cross_references", []))
        assert "mechanism_32" in refs
        assert "iteration_532" in refs


# ---------------------------------------------------------------------------
# Class 7: Hygiene
# ---------------------------------------------------------------------------
class TestHygiene:
    """Verify file hygiene: ASCII, no em/en dashes, HTTPS URLs, novelty."""

    def test_subtree_ascii_only(self):
        data = load_news_corp_profile()
        profile = get_hagey_profile(data)
        text = yaml.dump(profile, allow_unicode=True)
        text.encode("ascii")

    def test_no_em_or_en_dashes(self):
        data = load_news_corp_profile()
        profile = get_hagey_profile(data)
        text = yaml.dump(profile, allow_unicode=True)
        assert "\u2014" not in text
        assert "\u2013" not in text

    def test_all_urls_https(self):
        data = load_news_corp_profile()
        profile = get_hagey_profile(data)
        urls = [s for s in walk_strings(profile) if s.startswith("http")]
        assert len(urls) >= 3
        assert all(u.startswith("https://") for u in urls), urls

    def test_distinct_from_prior_novelty(self):
        data = load_news_corp_profile()
        mech = get_mech(get_hagey_profile(data))
        distinct = str(mech.get("distinct_from_prior", ""))
        assert "First Type B entry" in distinct
        assert "zero test_type_b_533" in distinct

    def test_test_file_self_reference(self):
        data = load_news_corp_profile()
        mech = get_mech(get_hagey_profile(data))
        assert mech.get("test_file") == (
            "tests/test_type_b_533_keach_hagey_matched_story_type_symmetry_sep05_5am.py"
        )
