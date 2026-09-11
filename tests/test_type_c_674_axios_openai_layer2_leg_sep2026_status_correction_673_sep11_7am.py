"""Type C #674: OpenAI x Axios Layer-2 salary-funding leg Sep 2026 status
verification and formal correction to #673 / mechanism 638 gradient-absent
premise.

FIRST Sep 2026 status verification of the OpenAI x Axios Layer-2
newsroom-funding leg with a first-hand primary-source read (openai.com
announcement, 123 lines rendered this run): OpenAI states it is funding
Axios local-news expansion by building newsrooms in four cities
(Pittsburgh, Kansas City, Boulder, Huntsville); three-year term to Jan
2028; Jan 2026 expansion to nine more communities (43 total); 35 cities
active as of Apr 2026. Deal ACTIVE Sep 2026; no renewal or termination
reporting in bounded query sets.

CORRECTION: Type B #673 / mechanism 638 asserted "(corpus holds no
verified AI-lab licensing/payment leg for Axios)" and rendered a
gradient-absent verdict. That premise is FALSE: mechanism 53 (Layer 2)
and mechanism 478 document the OpenAI x Axios leg, and the primary source
confirms it first-hand. Revised verdict: gradient PRESENT at Axios
(OpenAI to Axios, Layer 2), pair-misaligned for the Meta-vs-Apple
comparison; the 673 OpenAI-coronation counterevidence is invalidated
(funder-consistent, not entity-neutral); Axios is removed from the
clean-control set. The 638 block is left untouched per the Type D
read-only convention; this mechanism carries the dated correction.

Also documents the bounded multi-lab Sep 2026 new-deal sweep: no new
paid publisher licensing signings surfaced for Meta, OpenAI (beyond the
India attribution blitz), Google, Anthropic, xAI, or Perplexity in the
searched windows (bounded absences per the iteration-492 rule).

Research method: 6 browser.search query sets + 2 first-hand browser.open
reads (LLM Pulse master deal map updated Sep 7 2026; OpenAI Axios
announcement). No canonical URLs constructed; no zero-coverage claims.

Rotation: Type C follows Type B (#673) per A,B,C,D,E. Rotation guard and
doc-sync classes deselected pre-commit per the #565 followup convention;
anchor patched in the followup commit once the main commit SHA is known.
The novelty-anchor test (exactly one "Type C #674:" main commit
post-followup) is likewise deselected pre-commit.
"""

import ast
import glob
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

MECH_KEY = "mechanism_639_axios_openai_layer2_leg_sep2026_status_correction_673"
FILENAME = "test_type_c_674_axios_openai_layer2_leg_sep2026_status_correction_673_sep11_7am.py"

OPENAI_AXIOS_URL = "http://openai.com/index/partnering-with-axios-expands-openai-work-with-the-news-industry/"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. The rotation-guard class is deselected pre-commit.
ANCHORED_SHA = "6296a23"


def _entities():
    with open(ENTITIES_PATH) as f:
        return yaml.safe_load(f)


def _openai():
    return _entities()["entities"]["openai"]


def _mechanism():
    oa = _openai()
    assert MECH_KEY in oa, f"{MECH_KEY} missing from entities.openai"
    return oa[MECH_KEY]


def _mechanism_text():
    return yaml.safe_dump(_mechanism(), allow_unicode=True)


def _count_def_tests():
    path = os.path.join(TESTS_DIR, FILENAME)
    tree = ast.parse(open(path).read())
    return sum(
        isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
        and n.name.startswith("test_")
        for n in ast.walk(tree)
    )


def read_readme():
    with open(README_PATH) as f:
        return f.read()


def read_arch():
    with open(ARCH_PATH) as f:
        return f.read()


def read_log_start():
    with open(LOG_PATH) as f:
        return f.read()


class TestIterationMetadata674:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 674

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 639

    def test_mechanism_id_unique_repo_wide(self):
        seen = {}
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                if int(m.group(1)) == 639:
                    seen.setdefault(639, []).append(path)
        assert len(seen.get(639, [])) == 1, f"mechanism_id 639 not unique: {seen.get(639)}"

    def test_type_c_rotation_and_mapping_type(self):
        m = _mechanism()
        assert m["rotation"] == "Type C"
        assert m["type"] == "financial_incentive_mapping"

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_date_and_time(self):
        m = _mechanism()
        assert m["date_analyzed"] == "2026-09-11"
        assert m["time_pdt"] == "07:00"

    def test_no_duplicate_674_file(self):
        others = [p for p in glob.glob(os.path.join(TESTS_DIR, "test_type_c_674_*.py"))
                  if os.path.basename(p) != FILENAME]
        assert not others, f"duplicate #674 test files: {others}"


class TestStatusVerification674:
    def test_deal_active(self):
        assert _mechanism()["sep2026_status_verification"]["deal_active"] is True

    def test_primary_source_quote_verbatim(self):
        q = _mechanism()["sep2026_status_verification"]["primary_source_quote"]
        assert "new content partnership with Axios" in q
        assert "funding to help expand its local news coverage" in q

    def test_four_cities(self):
        c = _mechanism()["sep2026_status_verification"]["four_cities"]
        assert "Pittsburgh" in c
        assert "Kansas City" in c
        assert "Boulder" in c
        assert "Huntsville" in c

    def test_vandehei_investment_quote(self):
        q = _mechanism()["sep2026_status_verification"]["vandehei_quote"]
        assert "investment allows us to continue our expansion" in q

    def test_three_year_term(self):
        t = _mechanism()["sep2026_status_verification"]["term"]
        assert "three-year" in t
        assert "Jan 2028" in t

    def test_jan2026_expansion(self):
        e = _mechanism()["sep2026_status_verification"]["expansion_jan2026"]
        assert "nine additional" in e
        assert "43 communities" in e

    def test_apr2026_scale(self):
        s = _mechanism()["sep2026_status_verification"]["expansion_scale_apr2026"]
        assert "35 cities" in s

    def test_adweek_mechanics(self):
        a = _mechanism()["sep2026_status_verification"]["adweek_2026_mechanics"]
        assert "training" in a
        assert "retrieval" in a
        assert "supersystems" in a

    def test_no_renewal_reporting_bounded(self):
        r = _mechanism()["sep2026_status_verification"]["renewal_or_termination_reporting"]
        assert "none surfaced" in r
        assert "599" in r

    def test_openai_announcement_url_in_sources(self):
        assert OPENAI_AXIOS_URL in _mechanism()["source_urls"]


class TestCorrection674:
    def test_false_premise_quoted(self):
        p = _mechanism()["correction_to_673"]["false_premise_quoted"]
        assert "corpus holds no verified AI-lab licensing/payment leg for Axios" in p

    def test_verdict_false(self):
        assert _mechanism()["correction_to_673"]["verdict"] == "premise FALSE"

    def test_corpus_contradiction_mechanism_53(self):
        txt = yaml.safe_dump(_mechanism()["correction_to_673"]["corpus_contradictions"])
        assert "Mechanism 53" in txt
        assert "Layer 2" in txt
        assert "directly funded journalist salaries" in txt

    def test_corpus_contradiction_mechanism_478(self):
        txt = yaml.safe_dump(_mechanism()["correction_to_673"]["corpus_contradictions"])
        assert "Mechanism 478" in txt
        assert "three-year deal" in txt

    def test_primary_source_confirmation(self):
        c = _mechanism()["correction_to_673"]["primary_source_confirmation_this_run"]
        assert "first-hand" in c
        assert "four-city newsroom" in c

    def test_mechanism_638_untouched(self):
        u = _mechanism()["correction_to_673"]["mechanism_638_block_untouched"]
        assert "left in place" in u
        assert "670" in u

    def test_revised_verdict_gradient_present(self):
        rv = _mechanism()["revised_verdict"]
        assert "gradient PRESENT" in rv["publication_level"]
        assert "Layer 2" in rv["publication_level"]

    def test_pair_level_confounds_preserved(self):
        rv = _mechanism()["revised_verdict"]
        assert "does not directly predict" in rv["pair_level_meta_vs_apple"]
        assert "stand" in rv["pair_level_meta_vs_apple"]

    def test_counterevidence_invalidated(self):
        ce = _mechanism()["revised_verdict"]["counterevidence_reweighted"]
        assert "INVALIDATED" in ce
        assert "funder-consistent" in ce
        assert "entity-neutral" in ce

    def test_axios_removed_from_clean_controls(self):
        cs = _mechanism()["revised_verdict"]["control_set_update"]
        assert "REMOVED" in cs
        assert "clean-control set" in cs

    def test_label_supersession(self):
        ls = _mechanism()["revised_verdict"]["label_supersession"]
        assert "gradient-absent" in ls
        assert "superseded" in ls
        assert "pair-misaligned" in ls


class TestResearchMethod674:
    def test_six_query_sets(self):
        rm = _mechanism()["research_method"]
        assert "6 browser.search query sets" in rm

    def test_two_first_hand_opens(self):
        rm = _mechanism()["research_method"]
        assert "2 first-hand browser.open reads" in rm
        assert "249 lines" in rm
        assert "123 lines" in rm

    def test_verbatim_urls_and_no_canonical(self):
        rm = _mechanism()["research_method"]
        assert "verbatim from Full-URL listings" in rm
        assert "no canonical" in rm

    def test_iteration_492_bounded_absence(self):
        rm = _mechanism()["research_method"]
        assert "iteration-492" in rm
        assert "none claimed as proof" in rm

    def test_meta_bounded_absence(self):
        s = _mechanism()["multlab_sweep_context"]
        assert "no new Meta publisher AI deals" in s["meta"]
        assert "13" in s["meta"]

    def test_openai_india_only(self):
        s = _mechanism()["multlab_sweep_context"]
        assert "India attribution blitz" in s["openai"]
        assert "624" in s["openai"]

    def test_anthropic_zero_deal_holds(self):
        s = _mechanism()["multlab_sweep_context"]
        assert "zero-deal posture holds" in s["anthropic"]
        assert "629" in s["anthropic"]

    def test_wmg_suno_out_of_scope(self):
        o = _mechanism()["multlab_sweep_context"]["out_of_scope_noted"]
        assert "Warner Music Group" in o
        assert "not mapped" in o

    def test_novelty_block(self):
        n = _mechanism()["novelty_verification"]
        txt = yaml.safe_dump(n)
        assert "mechanism_639" in txt
        assert "638" in txt
        assert "first-hand" in txt
        assert "control-set removal" in txt


class TestConfoundersRanked674:
    def test_four_ranked_confounders(self):
        cs = _mechanism()["ranked_confounders"]
        assert len(cs) == 4
        assert [c["rank"] for c in cs] == [1, 2, 3, 4]
        assert {c["strength"] for c in cs} == {"strong", "moderate", "weak"}

    def test_strong_confounders_two(self):
        cs = _mechanism()["ranked_confounders"]
        strong = [c for c in cs if c["strength"] == "strong"]
        assert len(strong) == 2
        assert any("adversarial" in c["confounder"] for c in strong)
        assert any("pair-level" in c["confounder"] for c in strong)

    def test_statistical_discipline(self):
        sd = _mechanism()["statistical_discipline"]
        assert sd["correlation_not_causation"] is True
        assert sd["is_significant"] is False
        assert sd["no_tone_scores"] is True
        assert sd["qualitative_only"] is True

    def test_caution_present(self):
        c = _mechanism()["caution"]
        assert "premise correction only" in c
        assert "not newsroom capture" in c


class TestRotationCycleGuard674:
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

    def test_window_670_674_closes_b_to_c(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("C", "674"),
            ("B", "673"),
            ("A", "672"),
            ("E", "671"),
            ("D", "670"),
        ], f"rotation window 670-674 wrong: {observed}"

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
        # Post-commit anchor: the #674 main commit. Patched in the followup
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
        assert sha.startswith(ANCHORED_SHA), f"anchor not yet patched: {sha}"
        assert subject.startswith("Type C #674:"), (
            f"post-commit anchor broken: newest main is not #674: {subject!r}"
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
        sample = "Type C #674: OpenAI x Axios Layer-2 leg Sep 2026 status"
        for p in guard_patterns:
            m = re.search(p, sample)
            assert m and m.group(1) == "C" and m.group(2) == "674", (
                f"rotation regex {p!r} fails to match a real subject "
                "(double-backslash bug?)"
            )


class TestDocSyncRatchet674:
    def test_readme_has_674_row(self):
        assert "#674" in read_readme()

    def test_arch_has_674_row(self):
        assert "674" in read_arch()

    def test_readme_row_mentions_axios_correction(self):
        assert "Axios" in read_readme()
        assert "correction" in read_readme().lower()

    def test_log_starts_with_674(self):
        assert read_log_start().startswith("#674 Type C:")

    def test_def_test_count_matches(self):
        # The README row for #674 must carry this file's own def-test count.
        n = _count_def_tests()
        assert str(n) in read_readme(), (
            f"README #674 row should mention this file's def-test count {n}"
        )


class TestNoBrittlePatterns674:
    def test_yaml_reparses_clean(self):
        m = _mechanism()
        assert isinstance(m["mechanism_id"], int)
        assert isinstance(m["iteration"], int)
        assert isinstance(m["ranked_confounders"], list)

    def test_mechanism_key_naming(self):
        assert MECH_KEY.startswith("mechanism_639_")
        assert MECH_KEY in _openai()

    def test_no_em_dash_or_curly_quotes_in_mechanism(self):
        text = _mechanism_text()
        assert "\u2014" not in text, "em dash found in mechanism block"
        assert "\u2018" not in text and "\u2019" not in text, "curly quote in mechanism block"

    def test_mechanism_text_ascii_only(self):
        text = _mechanism_text()
        bad = [c for c in text if ord(c) > 127]
        assert not bad, f"non-ASCII chars in mechanism block: {set(bad)!r}"

    def test_type_c_674_main_commit_unique_and_anchored(self):
        # Novelty anchor: exactly one "Type C #674:" main commit post-followup
        # (deselected pre-commit per the #565 convention; the followup and
        # doc-sync commits are "Type C #674 followup:" / "Type C #674
        # doc-sync:" and do NOT match the main-commit filter).
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type C #674:", l)]
        assert len(mains) == 1, f"expected exactly one Type C #674 main commit, got {len(mains)}"
        assert mains[0].startswith(ANCHORED_SHA), (
            f"main commit SHA does not match patched anchor: {mains[0][:12]}"
        )
