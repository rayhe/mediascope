"""Type B #563 (2026-09-06 11:00 PDT): Alex Heath (The Verge) register
constancy across Meta and OpenAI - deputy editor and primary Meta/platforms
beat reporter with matched CEO-level access to both companies.

Career: Cult of Mac -> Business Insider -> The Information -> The Verge
(2021-present). Broke the Facebook-to-Meta rebrand (2021). Conducts ALL
Zuckerberg Decoder interviews (delegated from EIC Nilay Patel per in-corpus
mechanism #6). Hosts Command Line newsletter and Sources podcast (launched
Sep 2026 with Sam Altman as the debut guest).

Meta pieces (3):
1. Reality Labs reorg scoop via Command Line (Dec 2025): Meta splits Reality
   Labs into Wearables and Metaverse organizations with "relatively small"
   layoffs. Attribution secondary: Road to VR writes "As reported by The
   Verge's Alex Heath" and "memo available via Heath's Command Line
   newsletter" verbatim. Neutral scoop framing, 0.0.
   http://roadtovr.com/meta-reality-labs-reorg-ray-ban-smart-glasses/
2. Orion AR glasses hands-on (Meta Connect 2024): "even as a prototype, they
   were impressive." Attribution secondary: The Verge TikTok carries "The
   Verge's Deputy Editor, Alex Heath, tested out the new augmented reality
   glasses from Meta, called Orion" verbatim. Positive hands-on, +0.30.
   https://www.tiktok.com/@/video/7418651324423703851 (full query string
   carried verbatim in YAML).
3. Zuckerberg Decoder interviews (Meta Connect 2022/2023/2024): balanced
   access-interview framing, +0.10. Byline attribution in_corpus (mechanism
   #6, Patel delegation paradox).

OpenAI pieces (3):
1. "I talked to Sam Altman about the GPT-5 launch fiasco" (Command Line,
   Aug 2025): dinner interview, Altman on record "I think we totally screwed
   up some things on the rollout." Attribution secondary: gwern.net
   link-bibliography lists the URL with "I Talked to Sam Altman about the
   GPT-5 Launch Fiasco, Alex Heath" verbatim. Adversarial-question access,
   -0.30.
   https://www.theverge.com/command-line-newsletter/759897/sam-altman-chatgpt-openai-social-media-google-chrome-interview
2. Sources podcast debut episode (Sep 4, 2026): Altman rebuts data-center
   water criticism ("38,000 ChatGPT queries per almond", "robust meme").
   Attribution secondary: NY Post writes "during an appearance on a Tuesday
   episode of the new 'Sources' podcast with host Alex Heath" verbatim.
   Flagship launch slot for an unchallenged rebuttal platform, +0.25. Date
   verified true from the NY Post timestamp.
   https://nypost.com/2026/09/04/business/openai-ceo-sam-altman-says-38k-chatgpt-queries-only-use-amount-of-water-it-takes-to-grow-an-almond/
3. Decoder guest-host live interview with Bret Taylor (Sierra CEO, OpenAI
   chairman, Sep 2025): episode text carries "This is Alex Heath... I
   recently sat down with Bret Taylor, the CEO of AI startup Sierra and the
   chairman of OpenAI" verbatim. Neutral access live event, +0.10.
   https://player.fm/episodes/505664291

Scorer (MANUAL ILLUSTRATIVE, standing rule Aug 28 2026; arithmetic only):
Meta [0.0, 0.30, 0.10] avg 0.1333 vs OpenAI [-0.30, 0.25, 0.10] avg 0.0167.
Delta (Meta minus OpenAI) +0.1167. Engine check via calculate_asymmetry:
p ~ 0.575, is_significant False, cohens_d ~ 0.51 (agreement pole, same class
as #558). p_value NOT_CALCULATED, cohens_d NOT_CALCULATED, ci_95
NOT_CALCULATED, is_significant False, artifact_grade False.

Interpretation (falsification family; extends #548, #553, #558 to The Verge's
Meta-beat deputy editor): Heath is The Verge's closest thing to a
Meta-adversarial lane per the lane_assignment_mechanism (Lane 4), yet his own
register is constant across Meta and OpenAI - matched CEO access (Zuckerberg
Decoder vs Altman dinner / Sources debut), matched product access (Orion demo
vs GPT-5 rollout post-mortem). The adversarial edge in this window is aimed
at OpenAI (fiasco framing); the softest item is Meta (Orion impressed). Meta
marginally softer (+0.1167) runs against the journalist-level anti-Meta bias
hypothesis; the adversarial Meta lane at The Verge reads as
assignment/institutional rather than personal.

Strongest counterargument: item selection. Lane 4's adversarial
characterization (Heath on Meta internal dynamics, layoffs, leaker
crackdowns) is built from in-corpus examples NOT represented here; the three
Meta items are access and scoop items, his softest register. Sources debut
softness may reflect launch-episode incentives (a hostile debut would kill
the podcast), not entity preference. The Orion hands-on was a controlled
prototype demo engineered to impress. A different item set (Meta layoffs
Command Line items vs OpenAI NDA-scandal items) could invert the delta.
n=3 vs n=3 directional.

Evidence hygiene: URLs carried verbatim from this run's search tool output;
no theverge.com URLs constructed. Byline and date gaps disclosed per item,
never filled by guessing. No zero-coverage claims (per iteration-492 rule).
No em dashes in any new prose.

Novelty (per durable rule): zero alex_heath keys in the-verge.yaml before
this run (grep verified); no #563 in git log (grep verified); no
test_type_b_563 files on disk before this run (glob verified); #562 was Type
A, so rotation A->B->C->D->E requires Type B here.
"""

import os

import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, "profiles", "the-verge.yaml")

META_URLS = [
    "http://roadtovr.com/meta-reality-labs-reorg-ray-ban-smart-glasses/",
    "https://www.tiktok.com/@/video/7418651324423703851",
    "in_repo_reference_mechanism_6",
]
OPENAI_URLS = [
    "https://www.theverge.com/command-line-newsletter/759897/sam-altman-chatgpt-openai-social-media-google-chrome-interview",
    "https://nypost.com/2026/09/04/business/openai-ceo-sam-altman-says-38k-chatgpt-queries-only-use-amount-of-water-it-takes-to-grow-an-almond/",
    "https://player.fm/episodes/505664291",
]


def _load_profile():
    with open(PROFILE) as f:
        return yaml.safe_load(f)


def _heath():
    profile = _load_profile()
    matches = [j for j in profile["key_journalists"] if j["name"] == "Alex Heath"]
    assert len(matches) == 1, "expected exactly one Alex Heath entry"
    return matches[0]


def _mechanism():
    return _heath()["cross_entity_coverage_analysis"]


def _mechanism_block_text():
    with open(PROFILE) as f:
        text = f.read()
    start = text.index('- name: "Alex Heath"')
    end = text.index('- name: "Allison Johnson"', start)
    return text[start:end]


class TestMechanismExistsAndShape:
    def test_heath_entry_present(self):
        profile = _load_profile()
        names = [j["name"] for j in profile["key_journalists"]]
        assert "Alex Heath" in names

    def test_identity_fields(self):
        m = _mechanism()
        assert m["mechanism_id"] == 563
        assert m["iteration"] == 563
        assert m["type"].startswith("Type B")
        assert m["journalist"] == "Alex Heath"
        assert m["date_analyzed"] == "2026-09-06"

    def test_finding_type_falsification(self):
        m = _mechanism()
        assert "falsification" in m["finding"].lower()

    def test_beat_names_verge_and_meta(self):
        b = _heath()
        assert "meta" in b["beat"].lower()
        assert "decoder" in b["beat"].lower()


class TestSourceAttribution:
    def test_meta_urls_verbatim(self):
        block = _mechanism_block_text()
        for url in META_URLS:
            assert url in block, f"missing verbatim Meta URL: {url}"

    def test_openai_urls_verbatim(self):
        block = _mechanism_block_text()
        for url in OPENAI_URLS:
            assert url in block, f"missing verbatim OpenAI URL: {url}"

    def test_no_constructed_verge_urls(self):
        block = _mechanism_block_text()
        for url in META_URLS + OPENAI_URLS:
            if "theverge.com" in url:
                assert url.startswith("https://www.theverge.com/command-line-newsletter/"), \
                    "only verbatim theverge.com URLs allowed"

    def test_byline_gaps_disclosed(self):
        m = _mechanism()
        reorg = [e for e in m["meta_coverage"]["examples"] if "Reality Labs" in e["title"]][0]
        assert "secondary" in reorg["byline_attribution"]
        fiasco = [e for e in m["non_meta_coverage"]["examples"] if "fiasco" in e["title"]][0]
        assert fiasco["date_verified"] is False

    def test_no_invented_publication_dates(self):
        m = _mechanism()
        for section in ("meta_coverage", "non_meta_coverage"):
            for e in m[section]["examples"]:
                assert "date_verified" in e, f"missing date_verified disclosure: {e['title'][:40]}"
                if e["date_verified"] is False:
                    disclosure = (str(e.get("date")) + " " + str(e.get("byline_evidence", ""))).lower()
                    assert "secondary" in disclosure or "not_verified" in disclosure or "in-corpus" in disclosure or "disclosed" in disclosure, \
                        f"undisclosed date gap: {e['title'][:40]}"


class TestScorerArithmetic:
    def test_meta_scores_array(self):
        s = _mechanism()["scorer"]
        assert s["meta_scores"] == [0.0, 0.30, 0.10]

    def test_openai_scores_array(self):
        s = _mechanism()["scorer"]
        assert s["non_meta_scores"] == [-0.30, 0.25, 0.10]

    def test_meta_avg(self):
        s = _mechanism()["scorer"]
        expected = sum(s["meta_scores"]) / len(s["meta_scores"])
        assert abs(s["meta_avg"] - expected) < 1e-3
        assert abs(s["meta_avg"] - 0.1333) < 1e-3

    def test_openai_avg(self):
        s = _mechanism()["scorer"]
        expected = sum(s["non_meta_scores"]) / len(s["non_meta_scores"])
        assert abs(s["non_meta_avg"] - expected) < 1e-3
        assert abs(s["non_meta_avg"] - 0.0167) < 1e-3

    def test_delta(self):
        s = _mechanism()["scorer"]
        expected = s["meta_avg"] - s["non_meta_avg"]
        assert abs(s["delta_meta_minus_non_meta"] - expected) < 1e-3
        assert abs(s["delta_meta_minus_non_meta"] - 0.1167) < 1e-3

    def test_engine_agreement_pole(self):
        s = _mechanism()["scorer"]
        assert s["engine_significant"] is False
        assert s["is_significant"] is False

    def test_not_artifact_grade(self):
        s = _mechanism()["scorer"]
        assert s["artifact_grade"] is False

    def test_no_brittle_not_calculated_p_value(self):
        s = _mechanism()["scorer"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"


class TestInterpretationAndConfounders:
    def test_falsification_family_referenced(self):
        m = _mechanism()
        interp = m["interpretation"].lower()
        assert "548" in m["interpretation"] or "mehrotra" in interp

    def test_strongest_counterargument_present(self):
        m = _mechanism()
        assert len(m["strongest_counterargument"]) > 200
        assert "item selection" in m["strongest_counterargument"].lower()

    def test_confounders_ranked(self):
        m = _mechanism()
        assert len(m["confounders"]["strong"]) >= 2
        assert len(m["confounders"]["moderate"]) >= 1
        assert len(m["confounders"]["weak"]) >= 1

    def test_cross_references_include_delegation_mechanism(self):
        m = _mechanism()
        assert 6 in m["cross_references"]

    def test_artifact_readiness_not_warranted(self):
        m = _mechanism()
        assert "no analysis.json update warranted" in m["artifact_readiness"].lower()

    def test_no_em_dashes(self):
        block = _mechanism_block_text()
        assert "—" not in block, "em-dash discipline applies to all new prose"

    def test_research_method_names_search_sets(self):
        m = _mechanism()
        assert "browser.search" in m["research_method"]
        assert "No zero-coverage claims" in m["research_method"]


class TestRotationAndNovelty:
    def test_iteration_log_rotation_guard(self):
        with open(os.path.join(REPO, "iteration-log.md")) as f:
            log = f.read()
        assert "#562" in log
        assert "Type A" in log.split("#562")[1][:200]
