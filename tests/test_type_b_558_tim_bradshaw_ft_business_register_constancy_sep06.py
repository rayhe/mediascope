"""Type B #558 (2026-09-06 06:00 PDT): Tim Bradshaw (FT) business-register
constancy test - FT global technology correspondent covering AI deals, M&A,
and Big Tech strategy across entities.

Career arc: FT Los Angeles tech/media beat (Poynter profile, 2017) -> SF bureau
chief -> global technology correspondent (talkingbiznews FT expansion
announcement). Paired with MIT Technology Review's Will Douglas Heaven for the
"State of AI" editorial partnership (Oct 29, 2025). Career sources:
https://www.poynter.org/business-work/2017/are-tech-and-media-becoming-the-same-beat-financial-times-has-a-reporter-in-l-a-to-cover-the-convergence/
https://talkingbiznews.com/they-talk-biz-news/the-ft-is-expanding-its-tech-coverage/amp/
https://www.morningstar.com/news/pr-newswire/20251029dc10721/mit-technology-review-and-the-financial-times-form-strategic-editorial-partnership-to-explore-the-global-impact-of-artificial-intelligence
https://muckrack.com/tim-bradshaw

Meta pieces (3):
1. Meta partners with Singapore-based startup K-ID to add its AgeKey
   age-verification tech to Meta apps, plans rollout across multiple countries
   in 2026 (Dec 17, 2025), http://www.techmeme.com/251217/p2, byline
   "Tim Bradshaw/Financial Times" verbatim in Techmeme page title (verified by
   browser.open this run). Neutral partnership/compliance framing, +0.10.
2. Instagram's Threads launch take (Jul 6, 2023),
   https://www.techmeme.com/230706/p17, byline "Tim Bradshaw/Financial Times"
   verbatim in Techmeme page title (verified by browser.open this run).
   "Throwback to the giddy early days of Twitter"; Meta infrastructure framed
   as advantage over bug-plagued smaller rivals. Constructive, +0.20.
3. "Sheryl Sandberg and Nick Clegg join Nvidia-backed AI start-up Nscale"
   board (Mar 9, 2026), FT mirror at
   http://mypresstoday.com/gb/en/post/2534/341444399/sheryl-sandberg-and-nick-clegg-join-nvidia-backed-ai-start-up-nscale.html
   (verbatim from this run's search output). Byline secondary-attested via
   BuzzSumo author-page listing (no verbatim byline seen this run; disclosed).
   Meta-personnel item (ex-COO, ex-global-affairs president), neutral deal
   framing, +0.05. Disclosed as personnel-adjacent, not Meta-company.

Non-Meta pieces (3):
1. OpenAI/Jony Ive secretive AI device: "critical problems" could delay the
   screenless audio/visual device,
   https://spyglass.org/openai-digital-assistant-device-jony-ive/ (verbatim
   from this run's search output). Attribution verbatim: "The Financial Times
   Tim Bradshaw, Cristina Criddle, Michael Acton, & Ryan McMorrow". Co-byline
   x4 (individual voice diluted; disclosed). Sympathetic "building hardware is
   hard" framing of negative facts, -0.10. Exact publication date NOT verified
   this run; recorded as not_verified, never guessed.
2. Apple acquires Israeli start-up Q.AI for nearly $2B (Jan 29, 2026),
   https://www.tipranks.com/news/the-fly/apple-acquires-israeli-start-up-q-ai-for-nearly-2b-ft-reports-thefly
   (verbatim from this run's search output). Attribution verbatim: "The
   Financial Times' Tim Bradshaw and Michael Acton report". "Race to build AI
   devices", Apple closing the gap "with rivals such as Meta, Google, and
   OpenAI in next-generation devices". Aspirational racer framing, +0.20.
   Wearables-adjacent: silent-speech facial-expression analysis for AI-enabled
   wearables.
3. OpenAI scales back, reworks $500B Stargate project (Apr 9, 2026),
   https://www.tipranks.com/news/the-fly/ai-daily-openai-scales-back-reworks-500b-stargate-project-thefly-news
   (verbatim from this run's search output). Byline and date
   secondary-attested via GitHub news-archive mirror ("FT (Tim Bradshaw, Apr
   9)"). Negative facts (scale-back) in business register, -0.15.

Scorer (MANUAL ILLUSTRATIVE, standing rule Aug 28 2026; arithmetic only):
Meta [+0.10, +0.20, +0.05] avg 0.1167 vs non-Meta [-0.10, +0.20, -0.15]
avg -0.0167. Delta (Meta minus non-Meta) +0.1333. p_value NOT_CALCULATED,
cohens_d NOT_CALCULATED, ci_95 NOT_CALCULATED, is_significant False,
artifact_grade False.

Interpretation (falsification family; extends #548 and #553, which tested
WIRED surveillance-desk reporters, to the FT's non-Meta-beat tech
correspondent): Bradshaw applies a constant business-press register across
Meta and competitors. Meta marginally SOFTER (+0.1333), which runs against
the journalist-level anti-Meta bias hypothesis. Control against simplistic
financial determinism: FT's OpenAI licensing deal (Apr 29, 2024, in-corpus)
does not buy uniformly soft OpenAI coverage from Bradshaw; his two OpenAI
items score -0.10 and -0.15.

Strongest counterargument: beat-assignment artifact. Bradshaw is not FT's
Meta-beat reporter (that is Hannah Murphy, whose Meta register is
adversarial per in-corpus #206-era analysis). His Meta touches are
personnel/partnership/product-launch, never investigations, so the softness
could reflect topic assignment rather than personal evenhandedness. Genre
confound: all six items are deals/partnerships/product news, inherently
neutral-positive. Time mismatch: Threads item is Jul 2023 vs rest 2025-26.
Co-bylines (x4 on the Ive device, x2 on Q.AI) dilute individual voice. n=3
per side. MANUAL ILLUSTRATIVE, correlation-only.

Evidence hygiene: URLs carried verbatim from this run's tool output; no
ft.com URLs constructed (the one verbatim ft.com URL seen this run was not
needed and not used). Byline and date gaps disclosed per item, never filled
by guessing. No em dashes in any new prose.

Novelty (per durable rule): zero tim_bradshaw keys in financial-times.yaml
before this run (grep verified); no #558 in git log (grep verified); no
test_type_b_558 files on disk before this run (glob verified); #556 was Type
E, #557 was Type A, so rotation A->B->C->D->E requires Type B here.
"""

import os
import re

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, "profiles", "financial-times.yaml")
LOG = os.path.join(REPO, "iteration-log.md")

META_URLS = [
    "http://www.techmeme.com/251217/p2",
    "https://www.techmeme.com/230706/p17",
    "http://mypresstoday.com/gb/en/post/2534/341444399/sheryl-sandberg-and-nick-clegg-join-nvidia-backed-ai-start-up-nscale.html",
]
NON_META_URLS = [
    "https://spyglass.org/openai-digital-assistant-device-jony-ive/",
    "https://www.tipranks.com/news/the-fly/apple-acquires-israeli-start-up-q-ai-for-nearly-2b-ft-reports-thefly",
    "https://www.tipranks.com/news/the-fly/ai-daily-openai-scales-back-reworks-500b-stargate-project-thefly-news",
]


def _load_profile():
    with open(PROFILE) as f:
        return yaml.safe_load(f)


def _bradshaw():
    profile = _load_profile()
    matches = [j for j in profile["key_journalists"] if j["name"] == "Tim Bradshaw"]
    assert len(matches) == 1, "expected exactly one Tim Bradshaw entry"
    return matches[0]


def _mechanism():
    return _bradshaw()["cross_entity_coverage_analysis"]


def _mechanism_block_text():
    with open(PROFILE) as f:
        text = f.read()
    start = text.index("- name: Tim Bradshaw")
    end = text.index("known_conflicts:", start)
    return text[start:end]


class TestMechanismExistsAndShape:
    def test_bradshaw_entry_present(self):
        profile = _load_profile()
        names = [j["name"] for j in profile["key_journalists"]]
        assert "Tim Bradshaw" in names

    def test_identity_fields(self):
        m = _mechanism()
        assert m["mechanism_id"] == 558
        assert m["iteration"] == 558
        assert m["type"].startswith("Type B")
        assert m["journalist"] == "Tim Bradshaw"
        assert m["date_analyzed"] == "2026-09-06"

    def test_finding_type_falsification(self):
        m = _mechanism()
        assert "falsification" in m["finding"].lower()

    def test_beat_and_location(self):
        b = _bradshaw()
        assert "technology correspondent" in b["beat"].lower()
        assert "San Francisco" in b["location"]


class TestSourceAttribution:
    def test_meta_urls_verbatim(self):
        block = _mechanism_block_text()
        for url in META_URLS:
            assert url in block, f"missing verbatim Meta URL: {url}"

    def test_non_meta_urls_verbatim(self):
        block = _mechanism_block_text()
        for url in NON_META_URLS:
            assert url in block, f"missing verbatim non-Meta URL: {url}"

    def test_no_constructed_ft_urls(self):
        block = _mechanism_block_text()
        assert "ft.com/content" not in block, "no constructed ft.com URLs allowed"

    def test_byline_gaps_disclosed(self):
        m = _mechanism()
        meta_items = m["meta_coverage"]["examples"]
        nscale = [e for e in meta_items if "Nscale" in e["title"]][0]
        assert "secondary" in nscale["byline_attribution"]
        ive = [e for e in m["non_meta_coverage"]["examples"] if "Jony Ive" in e["title"]][0]
        assert ive["date_verified"] is False

    def test_no_invented_publication_dates(self):
        m = _mechanism()
        for section in ("meta_coverage", "non_meta_coverage"):
            for e in m[section]["examples"]:
                assert "date_verified" in e, f"missing date_verified disclosure: {e['title'][:40]}"
                if e["date_verified"] is False:
                    disclosure = (str(e.get("date")) + " " + str(e.get("byline_evidence", ""))).lower()
                    assert "secondary" in disclosure or "not_verified" in disclosure, \
                        f"undisclosed date gap: {e['title'][:40]}"


class TestScorerArithmetic:
    def test_meta_scores_array(self):
        s = _mechanism()["scorer"]
        assert s["meta_scores"] == [0.10, 0.20, 0.05]

    def test_non_meta_scores_array(self):
        s = _mechanism()["scorer"]
        assert s["non_meta_scores"] == [-0.10, 0.20, -0.15]

    def test_meta_avg(self):
        s = _mechanism()["scorer"]
        expected = sum(s["meta_scores"]) / len(s["meta_scores"])
        assert abs(s["meta_avg"] - expected) < 1e-3
        assert abs(s["meta_avg"] - 0.1167) < 1e-3

    def test_non_meta_avg(self):
        s = _mechanism()["scorer"]
        expected = sum(s["non_meta_scores"]) / len(s["non_meta_scores"])
        assert abs(s["non_meta_avg"] - expected) < 1e-3
        assert abs(s["non_meta_avg"] - (-0.0167)) < 1e-3

    def test_delta(self):
        s = _mechanism()["scorer"]
        expected = s["meta_avg"] - s["non_meta_avg"]
        assert abs(s["delta_meta_minus_non_meta"] - expected) < 1e-3
        assert abs(s["delta_meta_minus_non_meta"] - 0.1333) < 1e-3

    def test_statistical_discipline(self):
        s = _mechanism()["scorer"]
        assert s["method"] == "manual_illustrative"
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"
        assert s["is_significant"] is False
        assert s["artifact_grade"] is False


class TestInterpretationAndDiscipline:
    def test_financial_determinism_control(self):
        m = _mechanism()
        text = (m["finding"] + " " + m["interpretation"]).lower()
        assert "openai" in text and "deal" in text

    def test_strongest_counterargument_beat_assignment(self):
        m = _mechanism()
        ca = m["strongest_counterargument"].lower()
        assert "beat" in ca and "murphy" in ca

    def test_confounders_listed(self):
        m = _mechanism()
        conf = " ".join(m["confounders"]).lower()
        for term in ("genre", "co-byline", "n=3", "time"):
            assert term in conf, f"confounder missing: {term}"

    def test_wearables_hook_present(self):
        m = _mechanism()
        text = (m["finding"] + " " + m["interpretation"]).lower()
        assert "wearable" in text

    def test_no_em_dashes_in_block(self):
        block = _mechanism_block_text()
        assert "\u2014" not in block, "em dash found in new YAML prose"
        assert "\u2013" not in block, "en dash found in new YAML prose"

    def test_manual_illustrative_labeled(self):
        block = _mechanism_block_text().lower()
        assert "manual illustrative" in block


class TestRotationAndIterationLog:
    def test_iteration_log_has_558_type_b(self):
        with open(LOG) as f:
            text = f.read()
        assert "#558 Type B" in text

    def test_rotation_chain_recorded(self):
        with open(LOG) as f:
            text = f.read()
        assert "557 A -> 558 B" in text

    def test_novelty_single_558_test_file(self):
        tests_dir = os.path.join(REPO, "tests")
        matches = [f for f in os.listdir(tests_dir) if "558" in f]
        assert len(matches) == 1
        assert matches[0].startswith("test_type_b_558_tim_bradshaw")
