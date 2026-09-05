"""
Test Type B #538: Cade Metz (NYT) litigation-adversary register symmetry + Science-desk discovery reframing - Sep 05 2026

Mechanism #538 Type B - Journalist Cross-Entity Tracking
Journalist: Cade Metz (New York Times; Tech desk 2017-2026, Science desk from ~Aug 13 2026)
Focus: Reporter-level extension of mechanism 471 (NYT publication-level
litigation-posture boundary), the way 533 extended 532. Metz covers OpenAI -
the company his employer has sued since Dec 2023 for copyright infringement -
in a neutral launch/scoop register (GPT-5.6 Sol, $500B Ohio datacenter,
Broadcom Jalapeno chip, Z.ai open-weight piece), while his Meta register is
equally researcher-access neutral (Moltbook acquisition, Superintelligence Lab
talent analysis, Periodic Labs brain-drain). MANUAL ILLUSTRATIVE Meta avg -0.15
vs OpenAI avg -0.0625, delta -0.0875, near-symmetric; p_value NOT_CALCULATED,
is_significant False, NOT artifact-grade. The naive lawsuit-hardening
prediction fails at this reporter. The Aug 2026 Science-desk move (Wasik memo:
cover AI "through the same kind of lens that we use to cover other forms of
discovery") formalizes the discovery register. Driver class:
beat/institutional (researcher-access + Science-desk framing), NOT financial.
Joins the falsification family (457, 471, 472, 493, 498, 502, 503).

Validates:
- Cade Metz exists in profiles/careers/journalists.yaml with NYT career entries
- Science-desk career entry (~Aug 2026) present with Wasik-memo source URL
- Mechanism 538 exists with iteration_type B, iteration 538, date 2026-09-05
- OpenAI scored corpus: 4 solo bylines, verbatim titles, tones, Muck Rack provenance
- Meta scored corpus: 2 solo bylines, verbatim titles, tones, mirror provenance
- Scorer recomputation: meta avg -0.15, openai avg -0.0625, delta -0.0875
- Statistical discipline: NOT_CALCULATED p/cohens_d/ci, is_significant False,
  correlation_not_causation, confounders ranked STRONG/MODERATE/WEAK,
  counter_evidence, artifact_readiness declines analysis.json update
- Hygiene: ASCII-only, no em/en dashes, HTTPS-only URLs, single-key invariant,
  novelty statement, cross-references to 471/32/533

No em dashes allowed per project rule.

Source URLs (verbatim from search full-URL listings; nytimes.com policy-blocked):
  - Muck Rack profile: https://muckrack.com/cademetz/articles
  - Science desk memo: https://www.editorandpublisher.com/stories/reporter-to-start-new-ai-beat-on-the-new-york-times-science-desk,263009
  - Corroboration: https://talkingbiznews.com/media-news/ny-times-tech-reporter-metz-moving-to-science-desk-to-cover-ai/
  - Corroboration: https://www.citybiz.co/article/889210/new-york-times-moves-cade-metz-to-science-desk-to-cover-ai/
  - Moltbook mirror: https://mediaairbase.com/2026/03/11/meta-acquires-moltbook-the-social-network-just-for-a-i-bots/
  - Chinese-talent mirror: https://www.mutualfundobserver.com/discuss/discussion/65003/in-the-a-i-race-chinese-talent-still-drives-american-research
  - Periodic Labs mirror: https://www.thetermspot.com/sources/download/2a78bb1f17599c41d984f28b395a12345a9a85f1b1eee832c884b7e288041e76-12535a42-3106-4a8f-a09e-feb1c20e1427
"""

import pathlib

import yaml

PROFILES_DIR = pathlib.Path(__file__).resolve().parent.parent / "profiles"
JOURNALISTS_YAML = PROFILES_DIR / "careers" / "journalists.yaml"

MECH_KEY = "type_b_538_cade_metz_litigation_adversary_register_symmetry_science_desk"

MUCKRACK_URL = "https://muckrack.com/cademetz/articles"
EP_MEMO_URL = "https://www.editorandpublisher.com/stories/reporter-to-start-new-ai-beat-on-the-new-york-times-science-desk,263009"

OPENAI_TITLES = [
    "OpenAI Releases New, More Powerful A.I. Model",
    "OpenAI Close to Landing $500 Billion Data Center With Backing From Nvidia",
    "OpenAI and Broadcom Unveil Custom A.I. Chip Design",
    "A Chinese A.I. Lab May Test the World's Cybersecurity With a Model",
]
META_TITLES = [
    "Meta Acquires Moltbook, the Social Network Just for A.I. Bots",
    "Top A.I. Researchers Leave OpenAI, Google and Meta for New Start-Up",
]


def load_journalists():
    with open(JOURNALISTS_YAML) as f:
        return yaml.safe_load(f)


def get_metz_profile(data):
    """Extract Cade Metz's journalist profile from journalists.yaml."""
    for j in data.get("journalists", []):
        if j.get("name") == "Cade Metz":
            return j
    return None


def get_mech(profile):
    cc = profile.get("competitor_coverage", {})
    assert list(cc.keys()) == [MECH_KEY], "single-key invariant violated for Metz competitor_coverage"
    mech = cc[MECH_KEY]
    assert mech.get("mechanism_id") == 538, "mechanism 538 missing for Metz"
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
# Class 1: Profile structure and Science-desk career entry
# ---------------------------------------------------------------------------
class TestMetzProfileStructure:
    """Verify Cade Metz's profile exists with NYT career and the new Science-desk entry."""

    def test_profile_exists(self):
        data = load_journalists()
        profile = get_metz_profile(data)
        assert profile is not None, "Cade Metz profile missing from journalists.yaml"

    def test_multi_publication(self):
        data = load_journalists()
        profile = get_metz_profile(data)
        assert profile.get("multi_publication") is True

    def test_nyt_career_present(self):
        data = load_journalists()
        profile = get_metz_profile(data)
        pubs = [c.get("publication") for c in profile.get("career", [])]
        assert "nytimes" in pubs

    def test_genius_makers_in_notes(self):
        data = load_journalists()
        profile = get_metz_profile(data)
        notes = str(profile.get("notes", ""))
        assert "Genius Makers" in notes

    def test_science_desk_career_entry(self):
        data = load_journalists()
        profile = get_metz_profile(data)
        sci = [c for c in profile.get("career", []) if "science of artificial intelligence" in str(c.get("beat", ""))]
        assert len(sci) == 1, "Science-desk career entry missing or duplicated"
        entry = sci[0]
        assert entry.get("publication") == "nytimes"
        assert entry.get("event_type") == "moved"
        assert entry.get("start") == "2026-08"

    def test_science_desk_entry_sources_wasik_memo(self):
        data = load_journalists()
        profile = get_metz_profile(data)
        sci = [c for c in profile.get("career", []) if "science of artificial intelligence" in str(c.get("beat", ""))][0]
        assert sci.get("source_url") == EP_MEMO_URL
        assert "discovery" in str(sci.get("notes", ""))

    def test_no_prior_competitor_coverage_key(self):
        data = load_journalists()
        profile = get_metz_profile(data)
        cc = profile.get("competitor_coverage", {})
        assert len(cc) == 1
        assert MECH_KEY in cc


# ---------------------------------------------------------------------------
# Class 2: Mechanism identity
# ---------------------------------------------------------------------------
class TestMechanismIdentity:
    """Verify mechanism 538 identity fields."""

    def test_mechanism_id_538(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        assert mech["mechanism_id"] == 538

    def test_iteration_538(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        assert mech["iteration"] == 538

    def test_iteration_type_b(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        assert mech["iteration_type"] == "B"

    def test_date(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        assert mech["date"] == "2026-09-05"

    def test_journalist_and_publication(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        assert mech["journalist"] == "Cade Metz"
        assert mech["publication"] == "nytimes"

    def test_mechanism_id_unique_in_file(self):
        text = JOURNALISTS_YAML.read_text()
        assert text.count("mechanism_id: 538") == 1


# ---------------------------------------------------------------------------
# Class 3: OpenAI corpus (litigation adversary, solo bylines)
# ---------------------------------------------------------------------------
class TestOpenAICorpus:
    """Verify the four scored OpenAI-side solo bylines."""

    def _articles(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        return mech["openai_corpus_scored"]

    def test_four_scored_items(self):
        assert len(self._articles()) == 4

    def test_titles_verbatim(self):
        titles = [a["title"] for a in self._articles()]
        for t in OPENAI_TITLES:
            assert t in titles, f"missing OpenAI title: {t}"

    def test_all_solo_byline(self):
        for a in self._articles():
            assert a["byline"] == "solo", a["title"]

    def test_tones(self):
        tones = {a["title"]: a["tone"] for a in self._articles()}
        assert tones["OpenAI Releases New, More Powerful A.I. Model"] == -0.05
        assert tones["OpenAI Close to Landing $500 Billion Data Center With Backing From Nvidia"] == -0.05
        assert tones["OpenAI and Broadcom Unveil Custom A.I. Chip Design"] == 0.0
        assert tones["A Chinese A.I. Lab May Test the World's Cybersecurity With a Model"] == -0.15

    def test_muckrack_provenance(self):
        for a in self._articles():
            assert a["url"] == MUCKRACK_URL, a["title"]
            assert "Muck Rack" in a["url_note"]

    def test_sol_dek_no_lawsuit_vocabulary(self):
        sol = next(a for a in self._articles() if "More Powerful A.I. Model" in a["title"])
        summary = str(sol["summary"])
        assert "cybersecurity concerns" in summary
        assert "lawsuit" not in summary.lower() or "zero NYT-lawsuit" in summary

    def test_zai_piece_targets_zai_not_openai(self):
        zai = next(a for a in self._articles() if "Cybersecurity With a Model" in a["title"])
        summary = str(zai["summary"])
        assert "Z.ai" in summary
        assert "not OpenAI" in summary or "not scandal" in summary

    def test_unscored_cobyline_noted(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        unscored = mech["openai_corpus_unscored"]
        assert len(unscored) == 1
        assert "Mike Isaac" in unscored[0]["byline"]
        assert "Altman" in unscored[0]["title"]


# ---------------------------------------------------------------------------
# Class 4: Meta corpus (solo bylines)
# ---------------------------------------------------------------------------
class TestMetaCorpus:
    """Verify the two scored Meta-side solo bylines."""

    def _articles(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        return mech["meta_corpus_scored"]

    def test_two_scored_items(self):
        assert len(self._articles()) == 2

    def test_titles_verbatim(self):
        titles = [a["title"] for a in self._articles()]
        for t in META_TITLES:
            assert t in titles, f"missing Meta title: {t}"

    def test_all_solo_byline(self):
        for a in self._articles():
            assert a["byline"] == "solo", a["title"]

    def test_tones(self):
        tones = {a["title"]: a["tone"] for a in self._articles()}
        assert tones["Meta Acquires Moltbook, the Social Network Just for A.I. Bots"] == -0.05
        assert tones["Top A.I. Researchers Leave OpenAI, Google and Meta for New Start-Up"] == -0.25

    def test_moltbook_byline_verified(self):
        molt = next(a for a in self._articles() if "Moltbook" in a["title"])
        assert molt["date"] == "2026-03-10"
        assert "By Cade Metz" in molt["url_note"]
        assert molt["url"].startswith("https://")

    def test_periodic_labs_agarwal_anecdote(self):
        per = next(a for a in self._articles() if "New Start-Up" in a["title"])
        assert "Agarwal" in str(per["summary"])
        assert "turned down" in str(per["summary"])

    def test_unscored_eli_tan_cobyline_noted(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        unscored = mech["meta_corpus_unscored"]
        assert len(unscored) == 1
        assert "Eli Tan" in unscored[0]["byline"]
        assert "Superintelligence Lab" in str(unscored[0]["summary"])

    def test_symmetric_capacity_2024_investigation(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        cap = mech["symmetric_accountability_capacity"]
        assert len(cap) == 1
        summary = str(cap[0]["summary"])
        assert "OpenAI" in summary and "Google" in summary and "Meta" in summary
        assert cap[0]["date"] == "2024"


# ---------------------------------------------------------------------------
# Class 5: Scorer consistency
# ---------------------------------------------------------------------------
class TestScorerConsistency:
    """Recompute the MANUAL ILLUSTRATIVE tones from the logged arrays."""

    def _tones(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        return mech["manual_illustrative_tones"]

    def test_arrays_match_corpora(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        mt = self._tones()
        assert mt["meta"] == [a["tone"] for a in mech["meta_corpus_scored"]]
        assert mt["openai"] == [a["tone"] for a in mech["openai_corpus_scored"]]

    def test_meta_avg(self):
        mt = self._tones()
        assert abs(sum(mt["meta"]) / len(mt["meta"]) - mt["meta_avg"]) < 1e-9
        assert mt["meta_avg"] == -0.15

    def test_openai_avg(self):
        mt = self._tones()
        assert abs(sum(mt["openai"]) / len(mt["openai"]) - mt["openai_avg"]) < 1e-9
        assert mt["openai_avg"] == -0.0625

    def test_delta(self):
        mt = self._tones()
        assert abs((mt["meta_avg"] - mt["openai_avg"]) - mt["delta"]) < 1e-9
        assert mt["delta"] == -0.0875

    def test_near_symmetric_magnitude(self):
        mt = self._tones()
        assert abs(mt["delta"]) < 0.10

    def test_note_discipline(self):
        note = str(self._tones()["note"])
        assert "MANUAL ILLUSTRATIVE" in note
        assert "No significance claimed" in note


# ---------------------------------------------------------------------------
# Class 6: Statistical discipline
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline:
    """Verify no-significance discipline, confounders, counter-evidence."""

    def test_p_value_not_calculated(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        sd = mech["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci"] == "NOT_CALCULATED"

    def test_not_significant(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        assert mech["statistical_discipline"]["is_significant"] is False

    def test_correlation_not_causation(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        assert mech["statistical_discipline"]["correlation_not_causation"] is True

    def test_artifact_readiness_declines_update(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        assert "No analysis.json update" in str(mech.get("artifact_readiness", ""))

    def test_confounders_ranked_three_tiers(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        conf = mech.get("confounders", {})
        for tier in ("strong", "moderate", "weak"):
            assert len(conf.get(tier, [])) >= 1, f"confounder tier {tier} empty"

    def test_strong_confounders_name_key_limits(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        strong = " ".join(mech["confounders"]["strong"])
        assert "policy-blocked" in strong
        assert "Volume asymmetry" in strong

    def test_counter_evidence_nonempty(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        assert len(mech.get("counter_evidence", [])) >= 3

    def test_counter_evidence_names_agarwal_gap(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        ce = " ".join(mech["counter_evidence"])
        assert "Agarwal" in ce

    def test_cross_references(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        refs = " ".join(mech.get("cross_references", []))
        assert "mechanism 471" in refs
        assert "mechanism 32" in refs
        assert "533" in refs

    def test_institutional_context_lawsuit(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        ctx = mech["institutional_context"]
        assert "Dec 2023" in ctx["nyt_v_openai_lawsuit"]
        assert "widespread theft" in ctx["nyt_v_openai_lawsuit"]

    def test_institutional_context_wasik_memo(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        ctx = mech["institutional_context"]
        assert "discovery" in ctx["science_desk_move"]
        assert "editorandpublisher.com" in ctx["science_desk_move"]

    def test_driver_class_not_financial(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        assert "NOT financial" in str(mech["finding"])
        assert "beat/institutional" in str(mech["finding"])


# ---------------------------------------------------------------------------
# Class 7: Hygiene and novelty
# ---------------------------------------------------------------------------
class TestHygiene:
    """Verify file hygiene: ASCII, no em/en dashes, HTTPS URLs, novelty."""

    def test_subtree_ascii_only(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        # Scoped to the new mechanism subtree: the Metz profile carries
        # pre-existing non-ASCII (Conde/Nast migration arrows in older career
        # notes), so the whole-profile ASCII check used for Hagey in #533 does
        # not apply here. New data must be ASCII-only.
        text = yaml.dump(mech, allow_unicode=True)
        text.encode("ascii")

    def test_no_em_or_en_dashes(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        text = yaml.dump(mech, allow_unicode=True)
        assert "\u2014" not in text
        assert "\u2013" not in text

    def test_all_urls_https(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        urls = [s for s in walk_strings(mech) if s.startswith("http")]
        assert len(urls) >= 8
        assert all(u.startswith("https://") for u in urls), [u for u in urls if not u.startswith("https://")]

    def test_novelty_statement(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        novelty = str(mech.get("novelty", ""))
        assert "First dedicated Type B on Cade Metz" in novelty
        assert "zero test_type_b_538" in novelty.lower()

    def test_research_method_names_sources(self):
        data = load_journalists()
        mech = get_mech(get_metz_profile(data))
        method = str(mech.get("research_method", ""))
        assert "muckrack" in method.lower()
        assert "nytimes.com policy-blocked" in method
