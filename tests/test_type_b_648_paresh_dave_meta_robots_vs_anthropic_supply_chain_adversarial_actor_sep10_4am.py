"""Type B #648: Paresh Dave (WIRED) adversarial-actor selection asymmetry.

SECOND dedicated Type B mechanism on Paresh Dave (mechanism_id 623, next
free pre-commit; max numeric mechanism_id was 622). Distinct from mechanism 8
(emotional register on internal dysfunction: 'gulag'/'piece of shit' Meta vs
'quietly scrapped' OpenAI / 'paid off' Google). New angle, new articles:

(a) Meta arm: Aug 28 2026 WIRED "Sources: Meta is testing robots from ABB
and others to handle data center tasks such as swapping cables and resetting
servers as it seeks to lower labor costs". Antagonist = Meta (cost-cutting
employer); victim vector = workers ("fear for their jobs"). Tone -0.30
hand-assigned this run (MANUAL ILLUSTRATIVE). Snippet-bounded
characterization (WIRED direct fetch blocked; no canonical URL invented, per
the #647 convention). Source URLs verbatim from search Full-URL listings and
first-hand seattlemetromagazine author-page attribution.

(b) Anthropic arm: March 2026 WIRED trilogy "Anthropic Denies It Could
Sabotage AI Tools During War" (Mar 20), "Pentagon's 'Attempt to Cripple'
Anthropic Is Troubling, Judge Says" (Mar 24), "Anthropic Supply-Chain-Risk
Designation Halted by Judge" (Mar 26). Antagonist = Pentagon/DoD; victim
vector = Anthropic (company deserving judicial protection). Tone +0.25
hand-assigned this run (MANUAL ILLUSTRATIVE). Attribution verified
first-hand via seattlemetromagazine.com author page; article text
characterization snippet-bounded.

Counterevidence: Dave's Apr 9 2026 "Meta Cafeteria Workers Did What Execs
Won't: Took on ICE and Won" is positive Meta labor coverage where the
adversary is ICE, not Meta. This proves the register is genuinely
worker-sympathetic rather than Meta-hostile per se, and bounds the claim: in
employer-vs-labor conflicts Meta lands in the antagonist slot; in
company-vs-government conflicts the company lands in the victim slot.

Illustrative delta (anthropic minus meta) = 0.25 - (-0.30) = +0.55;
p_value, cohens_d, ci_95 NOT_CALCULATED; is_significant False (Aug 28
standing rule). VERDICT: WITHIN-WRITER ADVERSARIAL-ACTOR SELECTION, but NOT a
falsification pin: per #647 the WIRED-Anthropic direct prediction is neutral
(no deal), so no named financial gradient predicts this pair. Correlation is
not causation per the Aug 28 rule: STRONG news-peg (the antagonist follows
the facts: Meta voluntarily testing labor-replacing robots vs Pentagon
designating Anthropic a risk) and genre (court-beat language inherits the
judge's own 'troubling'/'illegally punishing' framing) confounds carry the
gap before any incentive effect is invoked; no newsroom-behavior claim is
made. NOT a falsification-family member. NOT a pure asymmetry pin.

Novelty vs prior work: mechanism 8 used different articles (Jun 12 'piece of
shit' exposé, May 14 'Dark Mood', etc.) and a different angle (emotional
register). The Aug 28 robots piece and the March Anthropic trilogy are
new-to-corpus as Dave-byline mechanisms (git-grep zero hits pre-commit for
the robots URL and 'Anthropic Supply-Chain-Risk Designation Halted by Judge'
outside this run's files). First adversarial-actor-selection mechanism on
Dave; second Type B mechanism on the reporter overall (sibling of #8).

Rotation: Type B follows Type A (#647) per A,B,C,D,E. Rotation guard
deselected pre-commit per the #565 followup convention; anchor patched in
the followup commit once the main commit SHA is known.
"""

import ast
import glob
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIRED_PATH = os.path.join(REPO_ROOT, "profiles", "wired.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = "adversarial_actor_selection_asymmetry"
FILENAME = "test_type_b_648_paresh_dave_meta_robots_vs_anthropic_supply_chain_adversarial_actor_sep10_4am.py"

META_TONE = -0.30
ANTHROPIC_TONE = 0.25
EXPECTED_DELTA = 0.55

META_URLS = [
    "https://biztoc.com/x/454337b9dce86e40",
    "https://cryptopanic.com/news/33294835/Meta-tests-data-center-robots-as-workers-fear-for-their-jobs",
    "https://agntbox.com/inside-metas-push-to-put-robots-to-work-in-data-centers-2026-09-08/",
]
ANTHROPIC_URLS = [
    "https://www.seattlemetromagazine.com/author/paresh-dave/",
]

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. The rotation-guard class is deselected pre-commit.
ANCHORED_SHA = "09384bf"


def _wired():
    with open(WIRED_PATH) as f:
        return yaml.safe_load(f)


def _dave():
    matches = [j for j in _wired()["key_journalists"]
               if j.get("name") == "Paresh Dave"]
    assert len(matches) == 1, f"expected exactly one Paresh Dave entry, got {len(matches)}"
    return matches[0]


def _mechanism():
    cc = _dave().get("cross_entity_coverage_analysis", {})
    assert MECH_KEY in cc, f"{MECH_KEY} missing from Paresh Dave cross_entity_coverage_analysis"
    return cc[MECH_KEY]


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


class TestIterationMetadata648:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 648

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 623

    def test_mechanism_id_unique_repo_wide(self):
        seen = {}
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                if int(m.group(1)) == 623:
                    seen.setdefault(623, []).append(path)
        assert len(seen.get(623, [])) == 1, f"mechanism_id 623 not unique: {seen.get(623)}"

    def test_type_is_b(self):
        assert _mechanism()["type"] == "B"

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_block_key_matches(self):
        assert _mechanism()["block_key"] == "type_b_648_paresh_dave_meta_robots_vs_anthropic_supply_chain_adversarial_actor_sep10"

    def test_distinct_from_mechanism_8(self):
        cc = _dave()["cross_entity_coverage_analysis"]
        assert cc["mechanism_number"] == 8, "mechanism 8 must still be present as sibling"
        assert MECH_KEY != "emotional_register_asymmetry"

    def test_no_duplicate_648_file(self):
        others = [p for p in glob.glob(os.path.join(TESTS_DIR, "test_type_b_648_*.py"))
                  if os.path.basename(p) != FILENAME]
        assert not others, f"duplicate #648 test files: {others}"


class TestDaveArms648:
    def test_meta_arm_date_and_antagonist(self):
        meta = _mechanism()["meta_arm"]
        assert meta["date"] == "2026-08-28"
        assert meta["antagonist"] == "Meta (cost-cutting employer)"
        assert meta["victim_vector"] == "workers fear for jobs"
        assert meta["byline"] == "Paresh Dave"
        assert meta["publication"] == "WIRED"

    def test_meta_arm_urls_verbatim(self):
        urls = _mechanism()["meta_arm"]["source_urls"]
        for u in META_URLS:
            assert u in urls, f"meta URL missing: {u}"

    def test_meta_arm_labor_cost_quote(self):
        quotes = _mechanism()["meta_arm"]["evidence_quotes"]
        assert any("lower labor costs" in q for q in quotes)
        assert any("fear for their jobs" in q for q in quotes)

    def test_anthropic_trilogy_three_articles(self):
        arts = _mechanism()["anthropic_arm"]["articles"]
        titles = [a["title"] for a in arts]
        assert len(arts) == 3
        assert "Anthropic Denies It Could Sabotage AI Tools During War" in titles
        assert "Pentagon's 'Attempt to Cripple' Anthropic Is Troubling, Judge Says" in titles
        assert "Anthropic Supply-Chain-Risk Designation Halted by Judge" in titles

    def test_anthropic_arm_antagonist_is_pentagon(self):
        anth = _mechanism()["anthropic_arm"]
        assert anth["antagonist"] == "Pentagon / US Department of Defense"
        assert anth["victim_vector"] == "Anthropic (company deserving judicial protection)"
        assert anth["dates"] == "2026-03-20, 2026-03-24, 2026-03-26"

    def test_anthropic_attribution_url_verbatim(self):
        urls = _mechanism()["anthropic_arm"]["source_urls"]
        for u in ANTHROPIC_URLS:
            assert u in urls, f"anthropic URL missing: {u}"

    def test_snippet_bounded_label_on_both_arms(self):
        assert _mechanism()["meta_arm"]["sourcing"] == "snippet_bounded"
        assert _mechanism()["anthropic_arm"]["sourcing"] == "snippet_bounded"

    def test_counterevidence_cafeteria_workers_present(self):
        ce = _mechanism()["counterevidence"]
        assert ce["date"] == "2026-04-09"
        assert "Cafeteria Workers" in ce["title"]
        assert "ICE" in ce["reading"]


class TestScorerDelta648:
    def test_delta_math(self):
        s = _mechanism()["asymmetry_scorer"]
        assert s["meta_tone"] == META_TONE
        assert s["anthropic_tone"] == ANTHROPIC_TONE
        assert abs(s["illustrative_delta_anthropic_minus_meta"] - EXPECTED_DELTA) < 1e-9
        assert abs((ANTHROPIC_TONE - META_TONE) - EXPECTED_DELTA) < 1e-9

    def test_manual_illustrative_only(self):
        text = _mechanism_text()
        assert "MANUAL ILLUSTRATIVE" in text
        s = _mechanism()["asymmetry_scorer"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"
        assert s["is_significant"] is False
        assert s["statistical_contract"] == "degenerate_n1_per_arm"

    def test_verdict_boundaries(self):
        verdict = _mechanism()["asymmetry_scorer"]["verdict"]
        assert "NOT a falsification pin" in verdict
        assert "NOT a falsification-family member" in verdict
        assert "NOT a pure asymmetry pin" in verdict

    def test_confounder_strengths_ranked(self):
        c = _mechanism()["confounders_ranked"]
        assert len(c["strong"]) == 2
        assert len(c["moderate"]) == 3
        assert len(c["weak"]) == 2
        assert any("follows the facts" in s for s in c["strong"])
        assert any("snippet-bounded" in s for s in c["moderate"])

    def test_cross_refs_name_prior_work(self):
        refs = _mechanism()["cross_references"]
        assert "mechanism 8" in refs
        assert "#647" in refs
        assert "#638" in refs


class TestFinancialContext648:
    def test_conde_nast_openai_deal_named(self):
        fc = _mechanism()["financial_context"]
        assert "$5-10M/yr" in fc
        assert "OpenAI" in fc

    def test_anthropic_direct_prediction_neutral(self):
        fc = _mechanism()["financial_context"]
        assert "neutral" in fc
        assert "no deal" in fc

    def test_correlational_boundary(self):
        fc = _mechanism()["financial_context"]
        assert "Correlation only, not causation" in fc


class TestRotationCycleGuard648:
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

    def test_window_644_648_closes_a_to_b(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("B", "648"),
            ("A", "647"),
            ("E", "646"),
            ("D", "645"),
            ("C", "644"),
        ], f"rotation window 644-648 wrong: {observed}"

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["B", "A", "E", "D", "C"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                f"rotation broken: {a} -> {b} is not a valid cycle edge"
            )

    def test_anchor_is_main_patch_in_followup(self):
        # Post-commit anchor: the #648 main commit. Patched in the followup
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
        assert subject.startswith("Type B #648:"), (
            f"post-commit anchor broken: newest main is not #648: {subject!r}"
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
        sample = "Type B #648: Paresh Dave adversarial-actor selection"
        for p in guard_patterns:
            m = re.search(p, sample)
            assert m and m.group(1) == "B" and m.group(2) == "648", (
                f"rotation regex {p!r} fails to match a real subject "
                "(double-backslash bug?)"
            )


class TestDocSyncRatchet648:
    def test_readme_has_648_row(self):
        assert "#648" in read_readme() or "648" in read_readme()

    def test_arch_has_648_row(self):
        assert "648" in read_arch()

    def test_readme_row_mentions_dave(self):
        assert "Paresh Dave" in read_readme()

    def test_log_starts_with_648(self):
        assert read_log_start().startswith("#648 Type B:")

    def test_def_test_count_matches(self):
        # The README row for #648 must carry this file's own def-test count.
        n = _count_def_tests()
        assert str(n) in read_readme(), (
            f"README #648 row should mention this file's def-test count {n}"
        )


def read_log_start():
    with open(LOG_PATH) as f:
        return f.read()


class TestNoBrittlePatterns648:
    def test_yaml_reparses_clean(self):
        p = _wired()
        dave = [j for j in p["key_journalists"] if j.get("name") == "Paresh Dave"][0]
        m = dave["cross_entity_coverage_analysis"][MECH_KEY]
        assert isinstance(m["mechanism_id"], int)
        assert isinstance(m["meta_arm"]["tone_score"], float)
        assert isinstance(m["anthropic_arm"]["tone_score"], float)
        assert isinstance(m["asymmetry_scorer"]["is_significant"], bool)

    def test_no_em_dash_in_mechanism(self):
        assert "\u2014" not in _mechanism_text()
        src = open(os.path.join(TESTS_DIR, FILENAME)).read()
        assert "\u2014" not in src

    def test_all_urls_http_or_https(self):
        urls = list(_mechanism()["meta_arm"]["source_urls"]) + \
            list(_mechanism()["anthropic_arm"]["source_urls"]) + \
            [_mechanism()["counterevidence"]["source_url"]]
        assert urls, "no URLs recorded"
        for u in urls:
            assert u.startswith(("http://", "https://")), f"bad URL: {u!r}"

    def test_no_zero_coverage_claims(self):
        text = _mechanism_text().lower()
        assert "zero coverage" not in text
        assert "no coverage" not in text

    def test_no_engine_significance_claims(self):
        text = _mechanism_text().lower()
        assert "statistically significant" not in text
        assert "p < 0.05" not in text
        assert "p<0.05" not in text

    def test_research_method_names_evidence_tiers(self):
        rm = _mechanism()["research_method"]
        assert "snippet-bounded" in rm
        assert "verbatim" in rm

    def test_artifact_readiness_present(self):
        assert "analysis.json" in _mechanism()["artifact_readiness"]
