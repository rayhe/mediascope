"""
Test Type B #543: Kevin Roose (NYT) Hard Fork late-window matched-episode framing - Sep 05 2026

Mechanism #543 Type B - Journalist Cross-Entity Tracking
Journalist: Kevin Roose (New York Times tech columnist 2017-Aug 2026; Hard Fork co-host)
Focus: First NUMBERED Type B on Roose (prior Aug 8 work was unnumbered, commit
1149ad2, triple professional identity capture). Four consecutive Hard Fork
episodes (Aug 14-Sep 4 2026) spanning his NYT departure transition form a
matched-window test: Zuckerberg's pro-AI essay gets "Anti-Doom Fantasy" with a
dek questioning credibility (MANUAL ILLUSTRATIVE -0.50); OpenAI's two-week
training halt gets neutral "Two-Week Pause" with safety-leadership dek
(+0.10); Meta's $17.1B settlement gets "Shifts the Blame" / "capitulated"
(-0.35). CONTROL: Hugging Face (open-source lab) gets sympathetic victim
framing ("Mob That Attacked", +0.25), falsifying blanket anti-open-source
hostility - the dismissiveness tracks Meta/Zuckerberg specifically.
MANUAL ILLUSTRATIVE Meta avg -0.425 vs OpenAI +0.10, delta -0.525,
p_value NOT_CALCULATED, is_significant False, NOT artifact-grade.
Gradient persists through the departure-transition window, consistent with
professional-identity capture rather than NYT institutional capture
(all four episodes still NYT-branded, so the separation is not clean).
Joins the falsification family; #538 (Metz) is the same-window symmetric
counterexample showing the gradient is reporter-specific, not newsroom-wide.

Validates:
- Kevin Roose exists in profiles/careers/journalists.yaml with NYT career
  entries and the Aug 2026 departure context
- Mechanism 543 exists with iteration_type B, iteration 543, date 2026-09-05
- Episode corpus: 4 scored episodes, verbatim titles/deks/tones, mirror provenance
- Scorer recomputation: meta avg -0.425, openai avg 0.10, delta -0.525
- Statistical discipline: NOT_CALCULATED p/cohens_d/ci, is_significant False,
  correlation_not_causation, confounders ranked STRONG/MODERATE/WEAK,
  counter_evidence, artifact_readiness declines analysis.json update
- Hygiene: ASCII-only subtree, no em/en dashes, HTTPS-only URLs,
  novelty statement, cross-references to 1149ad2/24/538

No em dashes allowed per project rule.

Source URLs (verbatim from search full-URL listings; NYT canonical pages not fetched):
  - Podbean listing: https://www.podbean.com/podcast-detail/bv3xk-e2b35/Hard-Fork-Podcast
  - Zeno.FM listing: https://zeno.fm/podcast/hard-fork/
  - Deezer listing: https://www.deezer.com/us/show/2507892
  - Princeton CITP: https://citp.princeton.edu/news/2026/arvind-narayanan-featured-hard-fork-podcast-meta-shifts-blame-do-data-center-bans-work
  - BuzzSumo profile: https://buzzsumo.com/journalist/kevin-roose-732442/
  - UTA signing: https://talkingbiznews.com/media-news/roose-newton-sign-with-talent-agency/
  - Departure: https://talkingbiznews.com/media-news/tech-columnist-roose-departing-ny-times/
"""

import pathlib

import yaml

PROFILES_DIR = pathlib.Path(__file__).resolve().parent.parent / "profiles"
JOURNALISTS_YAML = PROFILES_DIR / "careers" / "journalists.yaml"

MECH_KEY = "type_b_543_kevin_roose_hard_fork_late_window_matched_framing"

PODBEAN_URL = "https://www.podbean.com/podcast-detail/bv3xk-e2b35/Hard-Fork-Podcast"
ZENO_URL = "https://zeno.fm/podcast/hard-fork/"

EP_ZUCK_TITLE = "Zuckerberg's Anti-Doom Fantasy + Finally an A.I. Detector That Works + A.I. Math"
EP_META_TITLE = "Meta Shifts the Blame + Do Data Center Bans Work? + The Final HatGPT"
EP_OPENAI_TITLE = "OpenAI's Two-Week Pause + Jill Lepore on the Threat of the 'Artificial State' + Train of Thought"
EP_HF_TITLE = "The A.I. Mob That Attacked Hugging Face + METR's Ajeya Cotra"

EP_ZUCK_DEK = "But do we think it's credible?"
EP_OPENAI_DEK = "Will this encourage other labs to hit the brakes too?"
EP_META_DEK = "why it capitulated"


def load_journalists():
    with open(JOURNALISTS_YAML) as f:
        return yaml.safe_load(f)


def get_roose_profile(data):
    """Extract Kevin Roose's journalist profile from journalists.yaml."""
    for j in data.get("journalists", []):
        if j.get("name") == "Kevin Roose":
            return j
    return None


def get_mech(profile):
    cc = profile.get("competitor_coverage", {})
    assert list(cc.keys()) == [MECH_KEY], "single-key invariant violated for Roose competitor_coverage"
    mech = cc[MECH_KEY]
    assert mech.get("mechanism_id") == 543, "mechanism 543 missing for Roose"
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
# Class 1: Profile structure and departure context
# ---------------------------------------------------------------------------
class TestRooseProfileStructure:
    """Verify Kevin Roose's profile exists with NYT career and departure context."""

    def test_profile_exists(self):
        data = load_journalists()
        profile = get_roose_profile(data)
        assert profile is not None, "Kevin Roose profile missing from journalists.yaml"

    def test_nyt_career_present(self):
        data = load_journalists()
        profile = get_roose_profile(data)
        pubs = [c.get("publication") for c in profile.get("career", [])]
        assert "nytimes" in pubs

    def test_departure_noted_in_career(self):
        data = load_journalists()
        profile = get_roose_profile(data)
        notes = " ".join(str(c.get("notes", "")) for c in profile.get("career", []))
        assert "Leaving NYT" in notes or "leaving NYT" in notes.lower()

    def test_competitor_coverage_single_key(self):
        data = load_journalists()
        profile = get_roose_profile(data)
        cc = profile.get("competitor_coverage", {})
        assert len(cc) == 1
        assert MECH_KEY in cc


# ---------------------------------------------------------------------------
# Class 2: Mechanism identity
# ---------------------------------------------------------------------------
class TestMechanismIdentity:
    """Verify mechanism 543 identity fields."""

    def test_mechanism_id_543(self):
        data = load_journalists()
        mech = get_mech(get_roose_profile(data))
        assert mech["mechanism_id"] == 543

    def test_iteration_543(self):
        data = load_journalists()
        mech = get_mech(get_roose_profile(data))
        assert mech["iteration"] == 543

    def test_iteration_type_b(self):
        data = load_journalists()
        mech = get_mech(get_roose_profile(data))
        assert mech["iteration_type"] == "B"

    def test_date(self):
        data = load_journalists()
        mech = get_mech(get_roose_profile(data))
        assert mech["date"] == "2026-09-05"

    def test_journalist_and_publication(self):
        data = load_journalists()
        mech = get_mech(get_roose_profile(data))
        assert mech["journalist"] == "Kevin Roose"
        assert mech["publication"] == "nytimes"

    def test_mechanism_id_unique_in_file(self):
        text = JOURNALISTS_YAML.read_text()
        assert text.count("mechanism_id: 543") == 1

    def test_author_attribution(self):
        data = load_journalists()
        mech = get_mech(get_roose_profile(data))
        assert mech["author"] == "Kit (with Ray)"

    def test_temporal_bound(self):
        data = load_journalists()
        mech = get_mech(get_roose_profile(data))
        assert "2026-08-14" in mech["temporal_bound"]
        assert "2026-09-04" in mech["temporal_bound"]


# ---------------------------------------------------------------------------
# Class 3: Episode corpus (verbatim titles, deks, tones)
# ---------------------------------------------------------------------------
class TestEpisodeCorpus:
    """Verify the four scored Hard Fork episodes."""

    def _mechs(self):
        data = load_journalists()
        return get_mech(get_roose_profile(data))

    def _all_episodes(self):
        mech = self._mechs()
        return (
            mech["meta_corpus_scored"]
            + mech["openai_corpus_scored"]
            + mech["control_corpus_scored"]
        )

    def test_four_episodes_total(self):
        assert len(self._all_episodes()) == 4

    def test_zuckerberg_essay_episode(self):
        eps = self._all_episodes()
        ep = next(e for e in eps if e["date"] == "2026-08-14")
        assert ep["title"] == EP_ZUCK_TITLE
        assert ep["tone"] == -0.5
        assert EP_ZUCK_DEK in ep["dek"]
        assert "Future Is for Everyone" in ep["summary"]

    def test_meta_settlement_episode(self):
        eps = self._all_episodes()
        ep = next(e for e in eps if e["date"] == "2026-08-28")
        assert ep["title"] == EP_META_TITLE
        assert ep["tone"] == -0.35
        assert EP_META_DEK in ep["dek"]
        assert "17.1" in ep["dek"]

    def test_openai_pause_episode(self):
        eps = self._all_episodes()
        ep = next(e for e in eps if e["date"] == "2026-08-21")
        assert ep["title"] == EP_OPENAI_TITLE
        assert ep["tone"] == 0.1
        assert EP_OPENAI_DEK in ep["dek"]

    def test_huggingface_control_episode(self):
        mech = self._mechs()
        eps = mech["control_corpus_scored"]
        assert len(eps) == 1
        ep = eps[0]
        assert ep["title"] == EP_HF_TITLE
        assert ep["tone"] == 0.25
        assert "Nvidia Buys Hugging Face in $12.9 Billion Deal" in ep["summary"]

    def test_episode_urls_verbatim(self):
        eps = self._all_episodes()
        urls = [e["url"] for e in eps]
        assert PODBEAN_URL in urls
        assert ZENO_URL in urls

    def test_departure_sources(self):
        mech = self._mechs()
        srcs = mech["departure_sources"]
        assert "https://talkingbiznews.com/media-news/roose-newton-sign-with-talent-agency/" in srcs
        assert "https://talkingbiznews.com/media-news/tech-columnist-roose-departing-ny-times/" in srcs


# ---------------------------------------------------------------------------
# Class 4: Scorer consistency
# ---------------------------------------------------------------------------
class TestScorerConsistency:
    """Recompute the MANUAL ILLUSTRATIVE scorer from corpus tones."""

    def _tones(self):
        data = load_journalists()
        mech = get_mech(get_roose_profile(data))
        t = mech["manual_illustrative_tones"]
        meta = [e["tone"] for e in mech["meta_corpus_scored"]]
        openai = [e["tone"] for e in mech["openai_corpus_scored"]]
        control = [e["tone"] for e in mech["control_corpus_scored"]]
        return t, meta, openai, control

    def test_meta_tones(self):
        t, meta, openai, control = self._tones()
        assert meta == [-0.5, -0.35]
        assert t["meta"] == [-0.5, -0.35]

    def test_openai_tone(self):
        t, meta, openai, control = self._tones()
        assert openai == [0.1]
        assert t["openai"] == [0.1]

    def test_control_tone(self):
        t, meta, openai, control = self._tones()
        assert control == [0.25]
        assert t["huggingface_control"] == [0.25]

    def test_meta_avg(self):
        t, meta, openai, control = self._tones()
        assert abs(sum(meta) / len(meta) - t["meta_avg"]) < 1e-9
        assert t["meta_avg"] == -0.425

    def test_openai_avg(self):
        t, meta, openai, control = self._tones()
        assert abs(sum(openai) / len(openai) - t["openai_avg"]) < 1e-9
        assert t["openai_avg"] == 0.1

    def test_delta(self):
        t, meta, openai, control = self._tones()
        expected = (sum(meta) / len(meta)) - (sum(openai) / len(openai))
        assert abs(expected - t["delta"]) < 1e-9
        assert t["delta"] == -0.525

    def test_manual_illustrative_note(self):
        t, meta, openai, control = self._tones()
        assert "MANUAL ILLUSTRATIVE" in t["note"]
        assert "No significance claimed" in t["note"]


# ---------------------------------------------------------------------------
# Class 5: Statistical discipline
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline:
    """Verify standing statistical-discipline fields."""

    def _mech(self):
        data = load_journalists()
        return get_mech(get_roose_profile(data))

    def test_p_value_not_calculated(self):
        assert self._mech()["statistical_discipline"]["p_value"] == "NOT_CALCULATED"

    def test_cohens_d_not_calculated(self):
        assert self._mech()["statistical_discipline"]["cohens_d"] == "NOT_CALCULATED"

    def test_ci_not_calculated(self):
        assert self._mech()["statistical_discipline"]["ci"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        assert self._mech()["statistical_discipline"]["is_significant"] is False

    def test_correlation_not_causation(self):
        assert self._mech()["statistical_discipline"]["correlation_not_causation"] is True

    def test_confounders_ranked(self):
        conf = self._mech()["confounders"]
        assert set(conf.keys()) == {"strong", "moderate", "weak"}
        assert len(conf["strong"]) == 3
        assert len(conf["moderate"]) == 3
        assert len(conf["weak"]) == 2
        strong_text = " ".join(conf["strong"])
        assert "producer-written" in strong_text
        assert "Genre mismatch" in strong_text

    def test_counter_evidence_present(self):
        ce = self._mech()["counter_evidence"]
        assert len(ce) == 4
        ce_text = " ".join(ce)
        assert "genre-default" in ce_text
        assert "Altman/Amodei vision essay" in ce_text

    def test_artifact_readiness_declines(self):
        ar = str(self._mech()["artifact_readiness"])
        assert "No analysis.json update warranted" in ar

    def test_cross_references(self):
        cr = " ".join(self._mech()["cross_references"])
        assert "1149ad2" in cr
        assert "538" in cr

    def test_finding_states_not_artifact_grade(self):
        assert "NOT artifact-grade" in str(self._mech()["finding"])


# ---------------------------------------------------------------------------
# Class 6: Hygiene and novelty
# ---------------------------------------------------------------------------
class TestHygiene:
    """Verify file hygiene: ASCII, no em/en dashes, HTTPS URLs, novelty."""

    def test_subtree_ascii_only(self):
        data = load_journalists()
        mech = get_mech(get_roose_profile(data))
        text = yaml.dump(mech, allow_unicode=True)
        text.encode("ascii")

    def test_no_em_or_en_dashes(self):
        data = load_journalists()
        mech = get_mech(get_roose_profile(data))
        text = yaml.dump(mech, allow_unicode=True)
        assert "\u2014" not in text
        assert "\u2013" not in text

    def test_all_urls_https(self):
        data = load_journalists()
        mech = get_mech(get_roose_profile(data))
        urls = [s for s in walk_strings(mech) if s.startswith("http")]
        assert len(urls) >= 6
        assert all(u.startswith("https://") for u in urls), [u for u in urls if not u.startswith("https://")]

    def test_novelty_statement(self):
        data = load_journalists()
        mech = get_mech(get_roose_profile(data))
        novelty = str(mech.get("novelty", ""))
        assert "First numbered Type B mechanism on Kevin Roose" in novelty
        assert "zero test_type_b_543" in novelty.lower()

    def test_research_method_names_sources(self):
        data = load_journalists()
        mech = get_mech(get_roose_profile(data))
        method = str(mech.get("research_method", ""))
        assert "podbean" in method.lower()
        assert "zeno.fm" in method.lower()
        assert "iteration-492" in method
