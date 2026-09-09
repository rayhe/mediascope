"""Type C #634: Associated Press triple-AI-payer wire architecture (Sep 2026 status).

FIRST dedicated AP mechanism in the corpus (mechanism_id 615, next free
pre-commit; max numeric mechanism_id was 614). The Associated Press carries
three AI-payer legs - OpenAI (Jul 13 2023 prototype 2-year deal, the FIRST
OpenAI publisher licensing deal; stated term elapsed circa Jul 2025;
renewal status UNRESOLVED in bounded Sep 2026 searches), Google (Jan 15 2025
Gemini real-time feed, the first Google publisher deal for Gemini;
re-confirmed in the Dec 11 2025 Google AI pilot), and Microsoft (Feb 5 2026
Publisher Content Marketplace first-wave pilot partner; usage-based
payments). The AP is the corpus FIRST triple-AI-payer wire service and the
wire feeding every tracked publication: upstream incentive geometry, not a
publication-level tone claim.

Framework stress point: the number-599 ACTIVE convention (no termination
reporting equals still active) is applied here at its WEAKEST point - the
only first-gen OpenAI publisher deal whose stated term has fully elapsed
(about 14 months past expiry). A quiet lapse is as consistent with the
bounded evidence as a quiet renewal; UNRESOLVED cuts both ways. This run
documents the convention as an assumption, not a fact, and BOUNDS the
falsification family rather than joining it.

Qualitative Type C mapping. tone_scores NOT_SCORED; p_value, cohens_d,
ci_95 NOT_CALCULATED (standing rule Aug 28 2026). Correlational language
only; no causal claim; no coverage-tone claim.

Rotation: Type C follows Type B (#633) per A,B,C,D,E. Rotation guard
deselected pre-commit per the #565 followup convention; anchor patched in
the followup commit once the main commit SHA is known.
"""

import os
import re
import subprocess

import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENTITIES_PATH = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = "associated_press_triple_ai_payer_wire_architecture_615"


def _mechanism():
    with open(ENTITIES_PATH, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    assert MECH_KEY in data, f"{MECH_KEY} missing from competitor-entities.yaml"
    return data[MECH_KEY]


class TestIterationMetadata634:
    def test_mechanism_id_615(self):
        assert _mechanism()["mechanism_id"] == 615

    def test_iteration_634(self):
        assert _mechanism()["iteration"] == 634

    def test_type_c(self):
        m = _mechanism()
        assert m["iteration_type"] == "C"
        assert m["rotation"] == "Type C"
        assert m["type"] == "financial_incentive_mapping"
        assert m["type_label"] == "Financial Incentive Mapping"

    def test_date_time_pdt(self):
        m = _mechanism()
        assert m["date_analyzed"] == "2026-09-09"
        assert m["time_pdt"] == "14:00"

    def test_job_and_goal(self):
        m = _mechanism()
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_mechanism_name_carries_finding(self):
        name = _mechanism()["mechanism_name"]
        assert "Associated Press" in name
        assert "triple-AI-payer" in name
        assert "FIRST AP entity" in name


class TestYamlStructure615:
    def test_top_level_key_present(self):
        with open(ENTITIES_PATH, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        assert MECH_KEY in data

    def test_legs_keys(self):
        legs = _mechanism()["legs"]
        assert set(legs.keys()) == {"openai_leg", "google_leg", "microsoft_leg"}

    def test_sources_count_10(self):
        assert len(_mechanism()["sources"]) == 10

    def test_sources_all_https_or_http_verbatim(self):
        for url in _mechanism()["sources"]:
            assert url.startswith("http"), f"non-URL source: {url!r}"

    def test_cohort_geometry_keys(self):
        cg = _mechanism()["cohort_geometry"]
        assert "first_gen_cohort" in cg
        assert "meta_zero" in cg
        assert "falsification_family" in cg
        assert "monitoring_item" in cg

    def test_monitoring_item_present(self):
        assert "quarterly" in _mechanism()["cohort_geometry"]["monitoring_item"]

    def test_research_method_mentions_bounded(self):
        rm = _mechanism()["research_method"]
        assert "iteration-492" in rm
        assert "no canonical URLs constructed" in rm

    def test_ascii_only_block(self):
        with open(ENTITIES_PATH, encoding="utf-8") as fh:
            raw = fh.read()
        start = raw.index(MECH_KEY)
        block = raw[start : start + 13000]
        bad = [c for c in block if ord(c) >= 128]
        assert not bad, f"non-ASCII in mechanism block: {bad[:5]}"


class TestOpenAiLeg615:
    def _leg(self):
        return _mechanism()["legs"]["openai_leg"]

    def test_announced_2023_07_13(self):
        assert self._leg()["announced"] == "2023-07-13"

    def test_two_year_term(self):
        assert "2-year" in self._leg()["term"]

    def test_two_year_sourcing(self):
        term = self._leg()["term"]
        assert "Axios" in term or "Dexerto" in term
        assert "Engadget" in term

    def test_value_undisclosed(self):
        assert "undisclosed" in self._leg()["value"]

    def test_archive_back_to_1985(self):
        assert "1985" in self._leg()["scope"]

    def test_expiry_circa_2025_07(self):
        assert self._leg()["expiry"] == "circa 2025-07"

    def test_renewal_status_unresolved(self):
        assert "UNRESOLVED" in self._leg()["renewal_status"]

    def test_active_convention_weakest_application(self):
        conv = self._leg()["convention_applied"]
        assert "WEAKEST" in conv
        assert "14 months" in conv

    def test_prototype_significance(self):
        assert "FIRST OpenAI publisher licensing deal" in self._leg()[
            "prototype_significance"
        ]

    def test_primary_source_urls_verbatim(self):
        urls = self._leg()["primary_sources"]
        assert len(urls) == 4
        assert urls[0] == (
            "https://www.ap.org/media-center/press-releases/2023/"
            "ap-open-ai-agree-to-share-select-news-content-and-technology-in-new-collaboration/"
        )
        assert urls[2] == (
            "https://www.dexerto.com/tech/the-associated-press-signs-deal-"
            "with-openai-to-help-train-chatgpt-2210858/"
        )


class TestGoogleLeg615:
    def _leg(self):
        return _mechanism()["legs"]["google_leg"]

    def test_announced_2025_01_15(self):
        assert self._leg()["announced"] == "2025-01-15"

    def test_first_gemini_publisher_deal(self):
        assert "first Google publisher deal for Gemini" in self._leg()["form"]

    def test_realtime_feed_scope(self):
        assert "real-time" in self._leg()["scope"]

    def test_google_declined_credit_or_link(self):
        assert "declined to say whether AP journalism would be credited or linked" in (
            self._leg()["scope"]
        )

    def test_terms_undisclosed(self):
        assert "undisclosed" in self._leg()["value"]

    def test_dec_2025_pilot_reconfirmation(self):
        recon = self._leg()["reconfirmation"]
        assert "2025-12-11" in recon
        assert "Estadao" in recon
        assert "Gemini app" in recon

    def test_google_source_urls(self):
        urls = self._leg()["sources"]
        assert len(urls) == 3
        assert urls[0] == (
            "https://www.ap.org/media-center/ap-in-the-news/2025/"
            "google-signs-deal-with-ap-to-deliver-up-to-date-news-through-"
            "its-gemini-ai-chatbot/"
        )
        assert urls[2] == (
            "https://pressgazette.co.uk/platforms/"
            "news-publisher-ai-deals-lawsuits-openai-google/"
        )


class TestMicrosoftLeg615:
    def _leg(self):
        return _mechanism()["legs"]["microsoft_leg"]

    def test_announced_2026_02_05(self):
        assert self._leg()["announced"] == "2026-02-05"

    def test_pcm_form(self):
        assert "Publisher Content Marketplace" in self._leg()["form"]
        assert "first-wave pilot partner" in self._leg()["form"]

    def test_usage_based_value(self):
        assert "usage-based" in self._leg()["value"]

    def test_co_pilots_include_tracked_owners(self):
        co = self._leg()["co_pilots"]
        for name in ("Vox Media", "Conde Nast", "Business Insider Inc", "Hearst"):
            assert name in co, f"{name} missing from PCM co-pilot list"

    def test_yahoo_demand_partner(self):
        assert "Yahoo" in self._leg()["co_pilots"]

    def test_copilot_grounding_scope(self):
        assert "Copilot" in self._leg()["scope"]

    def test_microsoft_source_urls(self):
        urls = self._leg()["sources"]
        assert len(urls) == 3
        assert urls[0] == (
            "https://www.technologyrecord.com/article/"
            "new-microsoft-platform-lets-publishers-set-terms-for-ai-content-use"
        )
        assert urls[2] == (
            "https://digiday.com/media/qa-nikhil-kolar-vp-microsoft-ai-"
            "scales-its-click-to-sign-ai-content-marketplace/"
        )


class TestConfounders615:
    def _confs(self):
        return _mechanism()["confounders_ranked"]

    def test_strength_tiers_present(self):
        assert set(self._confs().keys()) == {"strong", "moderate", "weak"}

    def test_two_strong_confounders(self):
        assert len(self._confs()["strong"]) == 2

    def test_undisclosed_terms_strong(self):
        assert any("undisclosed-terms" in c for c in self._confs()["strong"])

    def test_active_convention_weakness_strong(self):
        assert any("UNRESOLVED cuts both ways" in c for c in self._confs()["strong"])

    def test_moderate_confounds(self):
        mods = self._confs()["moderate"]
        assert len(mods) == 2
        assert any("search space" in c for c in mods)
        assert any("usage" in c for c in mods)

    def test_weak_confounds(self):
        assert len(self._confs()["weak"]) == 1

    def test_cooperative_structure_confounder(self):
        coop = _mechanism()["ap_cooperative_structure"]
        assert "nonprofit" in coop
        assert "1846" in coop
        assert "STRUCTURAL confounder" in coop

    def test_counterevidence_three(self):
        ce = _mechanism()["counterevidence"]
        assert len(ce) == 3
        assert any("quietly lapsed" in c for c in ce)
        assert any("NOT licensing deals" in c for c in ce)


class TestStatisticalDiscipline615:
    def test_tone_scores_not_scored(self):
        assert _mechanism()["tone_scores"] == "NOT_SCORED"

    def test_not_calculated(self):
        sd = _mechanism()["statistical_discipline"]
        for token in ("p_value", "cohens_d", "ci_95"):
            assert token in sd and "NOT_CALCULATED" in sd

    def test_no_coverage_tone_claim(self):
        sd = _mechanism()["statistical_discipline"]
        assert "no coverage-tone claim" in sd

    def test_correlational_language_only(self):
        sd = _mechanism()["statistical_discipline"]
        assert "Correlational language only" in sd
        assert "no causal claim" in sd

    def test_upstream_not_publication_claim(self):
        assert "UPSTREAM" in _mechanism()["upstream_significance"]

    def test_meta_zero_wire_level(self):
        assert "0 dollars" in _mechanism()["cohort_geometry"]["meta_zero"]


class TestNovelty615:
    def test_mechanism_615_key_unique_in_profiles(self):
        count = 0
        for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for fn in files:
                if fn.endswith((".yaml", ".yml")):
                    with open(os.path.join(root, fn), encoding="utf-8") as fh:
                        count += fh.read().count("associated_press_triple_ai_payer_wire_architecture_615")
        assert count == 1, f"mechanism key appears {count} times in profiles/"

    def test_mechanism_id_615_unique(self):
        hits = []
        for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for fn in files:
                if fn.endswith((".yaml", ".yml")):
                    path = os.path.join(root, fn)
                    with open(path, encoding="utf-8") as fh:
                        for i, line in enumerate(fh, 1):
                            if re.match(r"\s*mechanism_id:\s*615\s*$", line):
                                hits.append(f"{path}:{i}")
        assert len(hits) == 1, f"mechanism_id 615 not unique: {hits}"

    def test_first_ap_entity_claim(self):
        assert "FIRST AP entity anywhere in profiles" in _mechanism()["novelty"]

    def test_triple_ai_payer_first_claim(self):
        assert "FIRST triple-AI-payer wire architecture" in _mechanism()["novelty"]

    def test_post_expiry_first_claim(self):
        assert "FIRST post-expiry mapping" in _mechanism()["novelty"]

    def test_weakest_convention_first_claim(self):
        assert "weakest application point" in _mechanism()["novelty"]

    def test_distinct_from_prior_mechanisms(self):
        nov = _mechanism()["novelty"]
        for ref in ("number 609", "number 604", "number 569"):
            assert ref in nov, f"{ref} distinction missing from novelty"

    def test_verification_block(self):
        v = _mechanism()["verification"]
        assert v["iteration"] == 634
        assert v["type"] == "C"
        assert v["date"] == "2026-09-09 14:00 PDT"
        assert v["yaml_parse_clean"] is True
        assert v["ascii_only"] is True


class TestRotationCycleGuard634:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the main-commit SHA is known.
    ANCHORED_SHA = "a53a4c82ecd3963b0882dc011e8e4ab13d433b35"  # #634 main commit (patched in followup per #565 convention)

    @staticmethod
    def _mains():
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        return [s for s in out if re.match(r"^Type [A-E] #\d+:", s)]

    def test_window_630_634_closes_b_to_c(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("C", "634"),
            ("B", "633"),
            ("A", "632"),
            ("E", "631"),
            ("D", "630"),
        ], f"rotation window 630-634 wrong: {observed}"

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["C", "B", "A", "E", "D"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                f"rotation broken: {a} -> {b} is not a valid cycle edge"
            )

    def test_anchor_is_main_patch_in_followup(self):
        # Post-commit anchor: the #634 main commit. Patched in the followup
        # per the #565 convention once the main commit SHA is known.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [
            l for l in out if re.match(r"^[0-9a-f]{40} Type [A-E] #\d+:", l)
        ]
        sha, subject = mains[0].split(" ", 1)
        assert sha == self.ANCHORED_SHA, f"anchor not yet patched: {sha}"
        assert subject.startswith("Type C #634:"), (
            f"anchor points at wrong main commit: {subject!r}"
        )
