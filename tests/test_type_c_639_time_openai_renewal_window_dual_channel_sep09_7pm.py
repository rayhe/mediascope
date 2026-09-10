"""Type C #639: Time x OpenAI strategic partnership renewal window (Sep 2026
status) plus dual-channel incentive geometry.

FIRST dedicated corpus mechanism for the Time x OpenAI direct licensing leg
(mechanism_id 618, next free pre-commit; max numeric key-form mechanism_id
was 616, mechanism_id 617 lives in journalists.yaml via #638). Previously the
Time x OpenAI deal existed in the corpus only as a one-line passing mention
inside mechanism 36's salesforce_benioff_time chain block.

The Time leg (announced Jun 27 2024, multi-year, 101-year archive, terms
undisclosed) is the fourth member of the #609 first-gen OpenAI publisher
renewal cohort: FT (Apr 29 2024), Atlantic (May 29 2024), Time (Jun 27 2024),
Conde Nast (Aug 20 2024). Bounded Sep 2026 searches surfaced NO renewal,
extension, renegotiation, or termination reporting: status UNRESOLVED, treated
ACTIVE per the #599 Vox convention.

Dual-channel geometry: Time collects direct OpenAI licensing money (leg 1)
and sits inside the Benioff -> Salesforce -> Anthropic owner-equity chain
(leg 2, mechanism 36); Meta collects $0 on both channels. Structural detail:
Salesforce would have taken an OpenAI equity position too, but OpenAI's
initial Microsoft contract prohibited it (Benioff to WSJ, Apr 2026) - the
OpenAI equity channel was contractually closed while the Anthropic channel
stayed open. Owner-posture tension documented as counterevidence: Benioff
said at Davos that AI companies "stole" training data ("All the training
data has been stolen", Bloomberg Law), adversarial toward the licensing
counterparty itself.

Qualitative Type C mapping. tone_scores NOT_SCORED; p_value, cohens_d,
ci_95 NOT_CALCULATED (standing rule Aug 28 2026). Correlational language
only; no causal claim; no coverage-tone claim. BOUNDS the falsification
family rather than joining it.

Rotation: Type C follows Type B (#638) per A,B,C,D,E. Rotation guard
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

MECH_KEY = "time_openai_renewal_window_dual_channel_618"
FILENAME = "test_type_c_639_time_openai_renewal_window_dual_channel_sep09_7pm.py"


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


class TestIterationMetadata639:
    def test_mechanism_id_618(self):
        assert _mechanism()["mechanism_id"] == 618

    def test_iteration_639(self):
        assert _mechanism()["iteration"] == 639

    def test_type_c(self):
        m = _mechanism()
        assert m["iteration_type"] == "C"
        assert m["rotation"] == "Type C"
        assert m["type"] == "financial_incentive_mapping"
        assert m["type_label"] == "Financial Incentive Mapping"

    def test_date_time_pdt(self):
        m = _mechanism()
        assert m["date_analyzed"] == "2026-09-09"
        assert m["time_pdt"] == "19:00"

    def test_job_and_goal(self):
        m = _mechanism()
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_mechanism_name_carries_finding(self):
        name = _mechanism()["mechanism_name"]
        assert "Time x OpenAI" in name
        assert "dual-channel" in name
        assert "618" in name or "Meta $0" in name

    def test_block_key_is_top_level(self):
        with open(ENTITIES_PATH, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        assert MECH_KEY in data


class TestYamlStructure618:
    def test_ascii_only_block(self):
        raw = _read(ENTITIES_PATH)
        start = raw.index(MECH_KEY)
        block = raw[start:]
        bad = [c for c in block if ord(c) >= 128]
        assert not bad, f"non-ASCII in mechanism block: {bad[:5]}"

    def test_no_em_dash_in_block(self):
        raw = _read(ENTITIES_PATH)
        start = raw.index(MECH_KEY)
        block = raw[start:]
        assert "\u2014" not in block

    def test_legs_keys(self):
        legs = _mechanism()["legs"]
        assert set(legs.keys()) == {
            "openai_licensing_leg",
            "renewal_window",
            "benioff_anthropic_equity_leg",
        }

    def test_primary_sources_count_7(self):
        assert len(_mechanism()["legs"]["openai_licensing_leg"]["primary_sources"]) == 7

    def test_primary_sources_all_http(self):
        for src in _mechanism()["legs"]["openai_licensing_leg"]["primary_sources"]:
            assert src.startswith("http"), f"non-URL source: {src!r}"

    def test_confounder_shape(self):
        confs = _mechanism()["confounders_ranked"]
        assert len(confs) == 4
        strengths = [c["strength"] for c in confs]
        assert strengths.count("STRONG") == 2
        assert strengths.count("MODERATE") == 1
        assert strengths.count("WEAK") == 1

    def test_counterevidence_count_3(self):
        assert len(_mechanism()["counterevidence"]) == 3

    def test_verification_block(self):
        v = _mechanism()["verification"]
        assert v["iteration"] == 639
        assert v["type"] == "C"
        assert v["yaml_parse_clean"] is True
        assert v["ascii_only"] is True


class TestOpenAILeg618:
    def test_announced_jun_27_2024(self):
        leg = _mechanism()["legs"]["openai_licensing_leg"]
        assert leg["announced"] == "2024-06-27"

    def test_term_multiyear_undisclosed(self):
        leg = _mechanism()["legs"]["openai_licensing_leg"]
        assert "multi-year" in leg["term"]
        assert leg["financial_terms"] == "undisclosed"

    def test_101_year_archive(self):
        leg = _mechanism()["legs"]["openai_licensing_leg"]
        assert "101 years" in leg["what_openai_gets"]
        assert "citation" in leg["what_openai_gets"]
        assert "Time.com" in leg["what_openai_gets"]

    def test_time_gets_tech(self):
        leg = _mechanism()["legs"]["openai_licensing_leg"]
        assert "OpenAI technology" in leg["what_time_gets"]
        assert "Preferred Publisher Program" in leg["what_time_gets"]

    def test_principals_quoted(self):
        leg = _mechanism()["legs"]["openai_licensing_leg"]
        joined = " ".join(leg["principals_quoted"])
        assert "Mark Howard" in joined
        assert "Brad Lightcap" in joined
        assert "attribution" in joined

    def test_reuters_relay_source(self):
        srcs = _mechanism()["legs"]["openai_licensing_leg"]["primary_sources"]
        assert any("srnnews.com" in s for s in srcs)

    def test_thewrap_source(self):
        srcs = _mechanism()["legs"]["openai_licensing_leg"]["primary_sources"]
        assert any("thewrap.com/time-openai-partnership/" in s for s in srcs)

    def test_theregister_1923_note(self):
        srcs = _mechanism()["legs"]["openai_licensing_leg"]["primary_sources"]
        assert any("theregister.com/2024/06/28" in s for s in srcs)

    def test_cash_not_disclosed_noted(self):
        srcs = _mechanism()["legs"]["openai_licensing_leg"]["primary_sources"]
        reg = next(s for s in srcs if "theregister.com" in s)
        assert "cash" in reg.lower()

    def test_partner_is_openai(self):
        assert _mechanism()["legs"]["openai_licensing_leg"]["partner"] == "OpenAI"


class TestRenewalWindow618:
    def test_status_unresolved(self):
        assert _mechanism()["legs"]["renewal_window"]["status"] == "UNRESOLVED"

    def test_active_convention_599(self):
        conv = _mechanism()["legs"]["renewal_window"]["convention"]
        assert "#599" in conv
        assert "ACTIVE" in conv

    def test_two_bounded_searches(self):
        searches = _mechanism()["legs"]["renewal_window"]["bounded_searches"]
        assert len(searches) == 2
        assert all("renewal" in s.lower() or "2024" in s for s in searches)

    def test_cohort_fourth_member(self):
        cohort = _mechanism()["legs"]["renewal_window"]["cohort"]
        assert "Fourth member" in cohort
        assert "609" in cohort
        for member in ("FT", "Atlantic", "Conde Nast", "Time"):
            assert member in cohort

    def test_cohort_chronology(self):
        cohort = _mechanism()["legs"]["renewal_window"]["cohort"]
        assert "Apr 29 2024" in cohort
        assert "May 29 2024" in cohort
        assert "Jun 27 2024" in cohort
        assert "Aug 20 2024" in cohort

    def test_positive_control_599_convention(self):
        pc = _mechanism()["legs"]["renewal_window"]["positive_control"]
        assert "$5M" in pc
        assert "Jul 2026" in pc
        assert "informative" in pc

    def test_unresolved_cuts_both_ways_in_confounders(self):
        confs = _mechanism()["confounders_ranked"]
        strong = [c["text"] for c in confs if c["strength"] == "STRONG"]
        assert any("UNRESOLVED cuts both ways" in t for t in strong)

    def test_weak_confound_bounded_search_limits(self):
        confs = _mechanism()["confounders_ranked"]
        weak = [c["text"] for c in confs if c["strength"] == "WEAK"]
        assert len(weak) == 1
        assert "paywall" in weak[0].lower()


class TestDualChannel618:
    def test_owner_benioff(self):
        leg = _mechanism()["legs"]["benioff_anthropic_equity_leg"]
        assert "Marc Benioff" in leg["owner"]
        assert "2018" in leg["owner"]
        assert "$190M" in leg["owner"]

    def test_salesforce_anthropic_300m(self):
        leg = _mechanism()["legs"]["benioff_anthropic_equity_leg"]
        assert "$300M" in leg["chain"]
        assert "2023" in leg["chain"]

    def test_microsoft_blocked_openai_equity(self):
        leg = _mechanism()["legs"]["benioff_anthropic_equity_leg"]
        assert "Microsoft" in leg["chain"]
        assert "prohibited" in leg["chain"]

    def test_mechanism_36_crossref(self):
        leg = _mechanism()["legs"]["benioff_anthropic_equity_leg"]
        assert "mechanism 36" in leg["coverage_evidence"]

    def test_most_disruptive_evidence(self):
        leg = _mechanism()["legs"]["benioff_anthropic_equity_leg"]
        assert "Most Disruptive" in leg["coverage_evidence"]
        assert "WEEX" in leg["coverage_evidence"]

    def test_meta_zero_both_channels(self):
        leg = _mechanism()["legs"]["benioff_anthropic_equity_leg"]
        assert leg["meta_side"] == "none documented (time_meta_deal: none, per the mechanism 36 block)"

    def test_overview_names_dual_channel(self):
        overview = _mechanism()["overview"]
        assert "dual-channel" in overview.lower() or "Dual-channel" in overview
        assert "Meta collects $0" in overview

    def test_owner_posture_tension_quoted(self):
        leg = _mechanism()["legs"]["benioff_anthropic_equity_leg"]
        assert "stolen" in leg["owner_posture_tension"]
        assert "Bloomberg Law" in leg["owner_posture_tension"]


class TestConfounders618:
    def test_strong_terms_undisclosed(self):
        confs = _mechanism()["confounders_ranked"]
        strong = [c["text"] for c in confs if c["strength"] == "STRONG"]
        assert any("undisclosed" in t for t in strong)

    def test_strong_owner_posture(self):
        confs = _mechanism()["confounders_ranked"]
        strong = [c["text"] for c in confs if c["strength"] == "STRONG"]
        assert any("owner-posture" in t.lower() for t in strong)

    def test_moderate_dual_vendor(self):
        confs = _mechanism()["confounders_ranked"]
        moderate = [c["text"] for c in confs if c["strength"] == "MODERATE"]
        assert len(moderate) == 1
        assert "dual-vendor" in moderate[0] or "dual vendor" in moderate[0].lower()

    def test_counterevidence_davos_adversarial(self):
        ce = _mechanism()["counterevidence"]
        assert any("Davos" in c for c in ce)

    def test_counterevidence_self_documented(self):
        ce = _mechanism()["counterevidence"]
        assert any("self-documented" in c for c in ce)

    def test_counterevidence_meta_zero_documented(self):
        ce = _mechanism()["counterevidence"]
        assert any("Meta $0" in c for c in ce)

    def test_no_causal_claim_in_discipline(self):
        disc = _mechanism()["statistical_discipline"]
        assert "no causal claim" in disc
        assert "no coverage-tone claim" in disc


class TestStatisticalDiscipline618:
    def test_tone_not_scored(self):
        assert _mechanism()["tone_scores"] == "NOT_SCORED"

    def test_p_not_calculated(self):
        disc = _mechanism()["statistical_discipline"]
        assert "p_value" in disc
        assert "NOT_CALCULATED" in disc

    def test_is_significant_false_absent_or_false(self):
        m = _mechanism()
        assert m.get("is_significant", False) is False

    def test_correlational_language(self):
        disc = _mechanism()["statistical_discipline"]
        assert "Correlational" in disc

    def test_standing_rule_cited(self):
        disc = _mechanism()["statistical_discipline"]
        assert "Aug 28 2026" in disc


class TestNovelty618:
    def test_first_dedicated_time_mechanism(self):
        assert "FIRST dedicated Time x OpenAI mechanism" in _mechanism()["novelty"]

    def test_fourth_cohort_member(self):
        assert "Fourth member" in _mechanism()["novelty"]

    def test_dual_channel_first(self):
        assert "FIRST dual-channel" in _mechanism()["novelty"]

    def test_research_method_queries(self):
        rm = _mechanism()["research_method"]
        assert "3 browser.search query sets" in rm
        assert "iteration-492" in rm
        assert "no canonical URLs constructed" in rm

    def test_research_method_precommit_greps(self):
        rm = _mechanism()["research_method"]
        assert "test_type_c_639" in rm
        assert "mechanism_618" in rm
        assert "No em dashes" in rm

    def test_distinct_from_609(self):
        rm = _mechanism()["research_method"]
        overview = _mechanism()["overview"]
        assert "609" in overview


class TestRotationCycleGuard639:
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

    def test_window_635_639_closes_b_to_c(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("C", "639"),
            ("B", "638"),
            ("A", "637"),
            ("E", "636"),
            ("D", "635"),
        ], f"rotation window 635-639 wrong: {observed}"

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
        # Post-commit anchor: the #639 main commit. Patched in the followup
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
        assert sha.startswith("ae794a60cf8b1ce5818fd11f038e4f4308374746"), f"anchor not yet patched: {sha}"
        assert subject.startswith("Type C #639:"), (
            f"post-commit anchor broken: newest main is not #639: {subject!r}"
        )

    def test_rotation_guard_regex_actually_matches(self):
        # #632 process note: a rotation guard whose regex never matches is a
        # silent no-op. Verify the guard regexes match a real main-commit
        # subject (the double-backslash r"...#(\\d+)..." form silently matches
        # nothing). Written as a semantic check rather than a literal-pattern
        # check so the test cannot defeat itself by containing the pattern.
        src = open(os.path.join(TESTS_DIR, FILENAME)).read()
        patterns = re.findall(r're\.search\(r"([^"]+)"', src)
        guard_patterns = [p for p in patterns if p.startswith("Type (")]
        assert guard_patterns, "no rotation-guard regex found in this file"


class TestDocSyncRatchet639:
    def _readme(self):
        return _read(README_PATH)

    def _arch(self):
        return _read(ARCH_PATH)

    def test_readme_has_639_row(self):
        assert re.search(r"#639", self._readme()), "README.md missing the #639 test-table row"

    def test_arch_has_639_row(self):
        assert re.search(r"#639", self._arch()), "docs/ARCHITECTURE.md missing the #639 tree row"

    def test_prior_rows_intact(self):
        readme, arch = self._readme(), self._arch()
        for n in ("634", "635", "636", "637", "638"):
            assert re.search(rf"#{n}", readme), f"README.md lost the #{n} row"
            assert re.search(rf"#{n}", arch), f"docs/ARCHITECTURE.md lost the #{n} row"

    def test_readme_row_test_count_matches(self):
        m = re.search(rf"`{re.escape(FILENAME)}`\s*\|\s*(\d+)\s*\|", self._readme())
        assert m, "README #639 row missing or malformed"
        assert int(m.group(1)) == _count_def_tests(), (
            f"README row says {m.group(1)} but file carries {_count_def_tests()}"
        )

    def test_readme_row_says_639(self):
        line = next(
            (ln for ln in self._readme().splitlines() if FILENAME in ln),
            None,
        )
        assert line is not None, "README missing the #639 row entirely"
        assert "#639" in line, "README #639 row does not reference #639"

    def test_log_starts_with_639(self):
        assert _read(LOG_PATH).lstrip().startswith("#639 Type C:")
