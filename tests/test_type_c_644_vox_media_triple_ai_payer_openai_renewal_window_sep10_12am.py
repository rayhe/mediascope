"""Type C #644: Vox Media triple-AI-payer architecture (Sep 2026 status) - OpenAI
May 29 2024 deal renewal window UNRESOLVED plus Microsoft Publisher Content
Marketplace pay-per-use leg plus ProRata 50-percent revenue-share leg, Meta $0,
PMX-split counterparty-continuity confound.

Extends mechanism 494 (Vox Media x OpenAI deal structure, iteration 494) and
the iteration-544 Vox Media x Microsoft PCM dual-payer mapping into the first
dedicated Vox Media triple-payer aggregation: the pre-split owner of tracked
publication The Verge collects AI revenue from three distinct channels while
Meta pays $0.

The OpenAI leg (announced May 29 2024 via the same Axios scoop as the Atlantic
deal, terms undisclosed) is the FIFTH member of the #609 first-gen OpenAI
publisher renewal cohort and the only one never given its own bounded renewal
query set: #609 mapped Conde Nast, Atlantic, and FT (three bounded query
sets) and named Vox in cohort geometry only. Bounded Sep 2026 searches this
run surface NO renewal, extension, renegotiation, or termination reporting for
the Vox leg: status UNRESOLVED, treated ACTIVE per the #599 Vox convention.

The ProRata leg (Jun 2025 publisher wave, Digiday) is the FIRST dedicated
ProRata mechanism in the corpus - previously only passing mentions. ProRata
is disclosed as an intermediary marketplace, not a Meta competitor.

Structural complication: the Jun-Jul 2026 ownership split (Lupa Systems /
Murdoch took NY Mag plus Vox.com plus podcast network for circa $300M,
closed Jul 8; PMC took The Verge plus Eater plus SB Nation into the new PMX
subsidiary, completed Jun 18, per the-verge.yaml) means the May 2024 OpenAI
counterparty was the pre-split Vox Media - deal assignment to successor
entities is unreported, a bounded continuity confound.

Qualitative Type C mapping. tone_scores NOT_SCORED; p_value, cohens_d,
ci_95 NOT_CALCULATED (standing rule Aug 28 2026). Correlational language
only; no causal claim; no coverage-tone claim. BOUNDS the falsification
family rather than joining it.

Rotation: Type C follows Type B (#643) per A,B,C,D,E. Rotation guard
deselected pre-commit per the #565 followup convention; anchor patched in
the followup commit once the main commit SHA is known.
"""

import ast
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENTITIES_PATH = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = "vox_media_triple_ai_payer_openai_renewal_window_621"
FILENAME = "test_type_c_644_vox_media_triple_ai_payer_openai_renewal_window_sep10_12am.py"


def _mechanism():
    with open(ENTITIES_PATH, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    assert MECH_KEY in data, f"{MECH_KEY} missing from competitor-entities.yaml"
    return data[MECH_KEY]


def _count_def_tests():
    path = os.path.join(TESTS_DIR, FILENAME)
    tree = ast.parse(open(path).read())
    return sum(
        isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
        and n.name.startswith("test_")
        for n in ast.walk(tree)
    )


def _read(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read()


class TestIterationMetadata644:
    def test_mechanism_id_621(self):
        assert _mechanism()["mechanism_id"] == 621

    def test_iteration_644(self):
        assert _mechanism()["iteration"] == 644

    def test_type_c(self):
        m = _mechanism()
        assert m["iteration_type"] == "C"
        assert m["rotation"] == "Type C"
        assert m["type"] == "financial_incentive_mapping"
        assert m["type_label"] == "Financial Incentive Mapping"

    def test_date_time_pdt(self):
        m = _mechanism()
        assert m["date_analyzed"] == "2026-09-10"
        assert m["time_pdt"] == "00:00"

    def test_job_and_goal(self):
        m = _mechanism()
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_mechanism_name_mentions_renewal_window(self):
        assert "renewal window UNRESOLVED" in _mechanism()["mechanism_name"]


class TestYamlStructure621:
    def test_top_level_key(self):
        with open(ENTITIES_PATH, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        assert MECH_KEY in data

    def test_ascii_only(self):
        assert _mechanism()["verification"]["ascii_only"] is True

    def test_no_em_dash_in_block(self):
        text = _read(ENTITIES_PATH)
        start = text.index(MECH_KEY)
        block = text[start:]
        assert "\u2014" not in block

    def test_legs_keys(self):
        legs = _mechanism()["legs"]
        assert set(legs.keys()) == {
            "openai_leg",
            "renewal_window",
            "microsoft_pcm_leg",
            "prorata_leg",
            "meta_side",
            "ownership_split_continuity",
        }

    def test_confounders_ranked_structure(self):
        confs = _mechanism()["confounders_ranked"]
        assert len(confs) == 5
        strengths = [c["strength"] for c in confs]
        assert strengths.count("STRONG") == 2
        assert strengths.count("MODERATE") == 2
        assert strengths.count("WEAK") == 1

    def test_counterevidence_count(self):
        assert len(_mechanism()["counterevidence"]) == 4


class TestOpenAILeg621:
    def test_announced_may_29_2024(self):
        assert _mechanism()["legs"]["openai_leg"]["announced"] == "2024-05-29"

    def test_mechanism_494_reference(self):
        assert _mechanism()["legs"]["openai_leg"]["mechanism"] == 494

    def test_terms_undisclosed(self):
        leg = _mechanism()["legs"]["openai_leg"]
        assert leg["financial_terms"] == "undisclosed"
        assert "undisclosed" in leg["term"]

    def test_vox_term_undisclosed_vs_atlantic(self):
        assert "Atlantic two-year" in _mechanism()["legs"]["openai_leg"]["term"]

    def test_principals_include_lightcap(self):
        assert "Brad Lightcap" in _mechanism()["legs"]["openai_leg"]["principals"]

    def test_same_scoop_as_atlantic(self):
        assert "Sara Fischer" in _mechanism()["legs"]["openai_leg"]["scoop"]

    def test_primary_sources_verbatim(self):
        sources = _mechanism()["legs"]["openai_leg"]["primary_sources"]
        assert len(sources) == 5
        assert any("voxmedia.com/2024/5/29" in s for s in sources)
        assert any("thewrap.com/vox-the-atlantic-chatgpt-openai-deal" in s for s in sources)
        assert any("venturebeat.com" in s for s in sources)

    def test_union_opposition_source(self):
        sources = _mechanism()["legs"]["openai_leg"]["primary_sources"]
        assert any("vox-media-union-openai-deal-demands-transparency" in s for s in sources)


class TestRenewalWindow621:
    def test_status_unresolved(self):
        assert _mechanism()["legs"]["renewal_window"]["status"] == "UNRESOLVED"

    def test_bounded_searches_two(self):
        searches = _mechanism()["legs"]["renewal_window"]["bounded_searches"]
        assert len(searches) == 2
        assert any("renewal extension 2025 2026" in s for s in searches)

    def test_circular_repo_commit_rejected(self):
        searches = _mechanism()["legs"]["renewal_window"]["bounded_searches"]
        assert any("rejected circular" in s for s in searches)

    def test_active_convention_599(self):
        assert "#599" in _mechanism()["legs"]["renewal_window"]["convention"]

    def test_fifth_cohort_member(self):
        cohort = _mechanism()["legs"]["renewal_window"]["cohort"]
        assert "Fifth member" in cohort
        assert "Atlantic (May 29 2024, same scoop day)" in cohort
        assert "Time (Jun 27 2024, mapped #639)" in cohort

    def test_609_named_vox_only_in_geometry(self):
        cohort = _mechanism()["legs"]["renewal_window"]["cohort"]
        assert "never received its own bounded renewal query set" in cohort

    def test_positive_control_jul_2026(self):
        pc = _mechanism()["legs"]["renewal_window"]["positive_control"]
        assert "Jul 2026" in pc
        assert "$5M" in pc


class TestMicrosoftPcmLeg621:
    def test_announced_feb_2026(self):
        assert _mechanism()["legs"]["microsoft_pcm_leg"]["announced"] == "2026-02"

    def test_544_reference(self):
        assert "#544" in _mechanism()["legs"]["microsoft_pcm_leg"]["mechanism"]

    def test_co_design_partner(self):
        assert "co-design partner" in _mechanism()["legs"]["microsoft_pcm_leg"]["structure"]

    def test_pay_per_use(self):
        assert "pay-per-use" in _mechanism()["legs"]["microsoft_pcm_leg"]["structure"]

    def test_pricing_model_a_la_carte(self):
        assert "a la carte" in _mechanism()["legs"]["microsoft_pcm_leg"]["pricing_model"]

    def test_payer_nexus_caveat(self):
        caveat = _mechanism()["legs"]["microsoft_pcm_leg"]["payer_nexus_caveat"]
        assert "$13.75B" in caveat
        assert "mechanism 82" in caveat

    def test_sources_verbatim(self):
        sources = _mechanism()["legs"]["microsoft_pcm_leg"]["sources"]
        assert len(sources) == 3
        assert any("searchengineland.com" in s for s in sources)
        assert any("digiday.com/media/qa-nikhil-kolar" in s for s in sources)


class TestProRataLeg621:
    def test_announced_jun_2025(self):
        assert "Jun 2025" in _mechanism()["legs"]["prorata_leg"]["announced"]

    def test_fifty_percent_payout(self):
        assert "50 percent" in _mechanism()["legs"]["prorata_leg"]["structure"]

    def test_gist_ai(self):
        assert "Gist.ai" in _mechanism()["legs"]["prorata_leg"]["structure"]

    def test_perplexity_comparison(self):
        assert "25 percent" in _mechanism()["legs"]["prorata_leg"]["comparison"]

    def test_first_dedicated_mechanism(self):
        assert "FIRST dedicated ProRata mechanism" in _mechanism()["legs"]["prorata_leg"]["corpus_status"]

    def test_intermediary_disclosure(self):
        disclosure = _mechanism()["legs"]["prorata_leg"]["intermediary_disclosure"]
        assert "not a Meta competitor" in disclosure

    def test_digiday_source(self):
        assert "digiday.com/media/boston-globe-future-vox-media-join-proratas" in _mechanism()["legs"]["prorata_leg"]["source"]


class TestMetaSide621:
    def test_meta_zero(self):
        assert "$0" in _mechanism()["legs"]["meta_side"]["status"]

    def test_llm_pulse_map(self):
        evidence = _mechanism()["legs"]["meta_side"]["evidence"]
        assert "LLM Pulse" in evidence
        assert "News Corp" in evidence

    def test_no_vox_in_meta_partners(self):
        evidence = _mechanism()["legs"]["meta_side"]["evidence"]
        assert "no Vox Media, PMX, or Lupa entity present" in evidence

    def test_corpus_13_partners(self):
        assert "13 confirmed Meta AI content partners" in _mechanism()["legs"]["meta_side"]["corpus"]

    def test_source_url(self):
        assert "llmpulse.ai/blog/ai-content-licensing-deals" in _mechanism()["legs"]["meta_side"]["source"]


class TestOwnershipSplit621:
    def test_lupa_deal(self):
        event = _mechanism()["legs"]["ownership_split_continuity"]["event"]
        assert "Lupa Systems" in event
        assert "$300M" in event
        assert "Jul 8 2026" in event

    def test_pmc_pmx_deal(self):
        event = _mechanism()["legs"]["ownership_split_continuity"]["event"]
        assert "PMX" in event
        assert "Jun 18 2026" in event

    def test_bankoff_went_with_lupa(self):
        assert "Bankoff" in _mechanism()["legs"]["ownership_split_continuity"]["personnel"]

    def test_continuity_confounder_not_lapse(self):
        q = _mechanism()["legs"]["ownership_split_continuity"]["continuity_question"]
        assert "continuity confound" in q
        assert "NOT as deal lapse" in q

    def test_verge_under_pmx(self):
        assert "PMC/PMX" in _mechanism()["legs"]["ownership_split_continuity"]["relevance"]


class TestConfounders621:
    def test_strong_undisclosed_terms(self):
        strong = [c["text"] for c in _mechanism()["confounders_ranked"] if c["strength"] == "STRONG"]
        assert any("undisclosed" in t for t in strong)

    def test_strong_ownership_splinter(self):
        strong = [c["text"] for c in _mechanism()["confounders_ranked"] if c["strength"] == "STRONG"]
        assert any("Ownership-splinter" in t for t in strong)

    def test_moderate_nexus(self):
        moderate = [c["text"] for c in _mechanism()["confounders_ranked"] if c["strength"] == "MODERATE"]
        assert any("nexus" in t for t in moderate)

    def test_moderate_prorata_intermediary(self):
        moderate = [c["text"] for c in _mechanism()["confounders_ranked"] if c["strength"] == "MODERATE"]
        assert any("intermediary" in t for t in moderate)

    def test_weak_paywall(self):
        weak = [c["text"] for c in _mechanism()["confounders_ranked"] if c["strength"] == "WEAK"]
        assert any("paywalls" in t for t in weak)

    def test_counterevidence_pmc_google_lawsuits(self):
        ce = _mechanism()["counterevidence"]
        assert any("TWO active lawsuits" in c for c in ce)

    def test_counterevidence_jarvis(self):
        ce = _mechanism()["counterevidence"]
        assert any("Jeff Jarvis" in c for c in ce)

    def test_counterevidence_union(self):
        ce = _mechanism()["counterevidence"]
        assert any("Vox Media Union" in c for c in ce)


class TestStatisticalDiscipline621:
    def test_not_scored(self):
        assert _mechanism()["tone_scores"] == "NOT_SCORED"

    def test_not_calculated(self):
        sd = _mechanism()["statistical_discipline"]
        assert "NOT_CALCULATED" in sd

    def test_no_causal_claim(self):
        sd = _mechanism()["statistical_discipline"]
        assert "no causal claim" in sd
        assert "no coverage-tone claim" in sd

    def test_iteration_492_rule(self):
        assert "iteration-492" in _mechanism()["statistical_discipline"]

    def test_standing_rule_aug_28(self):
        assert "Aug 28 2026" in _mechanism()["statistical_discipline"]


class TestNovelty621:
    def test_first_vox_renewal_window(self):
        assert "FIRST dedicated Vox Media OpenAI renewal-window mapping" in _mechanism()["novelty"]

    def test_first_prorata_mechanism(self):
        assert "FIRST dedicated ProRata mechanism" in _mechanism()["novelty"]

    def test_first_triple_payer(self):
        assert "FIRST triple-payer aggregation for Vox" in _mechanism()["novelty"]

    def test_first_ownership_splinter_confound(self):
        assert "ownership-splinter as a deal-continuity confound" in _mechanism()["novelty"]

    def test_distinct_from_544_and_494(self):
        novelty = _mechanism()["novelty"]
        assert "#544" in novelty
        assert "mechanism 494" in novelty
        assert "mechanism 112" in novelty

    def test_research_method_queries(self):
        rm = _mechanism()["research_method"]
        assert "4 browser.search query sets" in rm
        assert "iteration-492" in rm
        assert "no canonical URLs constructed" in rm

    def test_research_method_precommit_greps(self):
        rm = _mechanism()["research_method"]
        assert "test_type_c_644" in rm
        assert "mechanism_621" in rm
        assert "No em dashes" in rm


class TestRotationCycleGuard644:
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

    def test_window_640_644_closes_b_to_c(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("C", "644"),
            ("B", "643"),
            ("A", "642"),
            ("E", "641"),
            ("D", "640"),
        ], f"rotation window 640-644 wrong: {observed}"

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
        # Post-commit anchor: the #644 main commit. Patched in the followup
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
        assert sha.startswith("9252fe7d7eb0d723a5135e2138b9e4185a07a158"), f"anchor not yet patched: {sha}"
        assert subject.startswith("Type C #644:"), (
            f"post-commit anchor broken: newest main is not #644: {subject!r}"
        )

    def test_rotation_guard_regex_actually_matches(self):
        subjects = self._mains()
        assert len(subjects) >= 5, "fewer than 5 main commits in history"
        assert all(re.match(r"^Type [A-E] #\d+:", s) for s in subjects[:5])


class TestDocSyncRatchet644:
    def _readme(self):
        return _read(README_PATH)

    def _arch(self):
        return _read(ARCH_PATH)

    def test_readme_has_644_row(self):
        assert re.search(r"#644", self._readme()), "README.md missing the #644 test-table row"

    def test_arch_has_644_row(self):
        assert re.search(r"#644", self._arch()), "docs/ARCHITECTURE.md missing the #644 tree row"

    def test_prior_rows_intact(self):
        readme, arch = self._readme(), self._arch()
        for n in ("639", "640", "641", "642", "643"):
            assert re.search(rf"#{n}", readme), f"README.md lost the #{n} row"
            assert re.search(rf"#{n}", arch), f"docs/ARCHITECTURE.md lost the #{n} row"

    def test_readme_row_test_count_matches(self):
        m = re.search(rf"`{re.escape(FILENAME)}`\s*\|\s*(\d+)\s*\|", self._readme())
        assert m, "README #644 row missing or malformed"
        assert int(m.group(1)) == _count_def_tests(), (
            f"README row says {m.group(1)} but file carries {_count_def_tests()}"
        )

    def test_readme_row_says_644(self):
        line = next(
            (ln for ln in self._readme().splitlines() if FILENAME in ln),
            None,
        )
        assert line is not None, "README missing the #644 row entirely"
        assert "#644" in line, "README #644 row does not reference #644"

    def test_log_starts_with_644(self):
        assert _read(LOG_PATH).lstrip().startswith("#644 Type C:")
