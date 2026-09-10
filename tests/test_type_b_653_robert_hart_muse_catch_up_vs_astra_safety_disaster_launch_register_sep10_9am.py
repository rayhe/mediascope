"""Type B #653: Robert Hart (The Verge) launch-week register differentiation.

SECOND dedicated Type B mechanism on Robert Hart (mechanism_id 626, next
free pre-commit; max numeric mechanism_id was 625). Distinct from mechanism
599 / #608 (cross-entity constancy via incident coverage: OpenAI DseWiki
wiki-incident adversarial -0.65 vs Meta AI-app clickbait adversarial -0.50).
New angle, new articles:

(a) Meta arm: Sep 8 2026 3:00pm The Verge "Meta bets on AI agent Muse to
catch up in AI race" (byline Robert Hart per technewstube attribution).
Register = market-legitimacy defeat: "catch up in AI race", "ailing
position in the AI race", "regain ground after years of setbacks and
failures", and the in-text debunk of Meta's "world's first personal AI
agent built for everyone" claim ("a claim the competitive lineup does not
support on its face"). Tone -0.35 hand-assigned this run (MANUAL
ILLUSTRATIVE). Snippet-bounded via verbatim reprint mirrors (theverge.com
policy-blocked for first-hand fetch per #608 convention).

(b) OpenAI arm: circa Sep 2 2026 The Verge "Researchers fear safety disaster
ahead of OpenAI's Astra release" (byline Robert Hart per mirror
follow-topics blocks). Register = pre-launch safety watchdog applied to the
licensing partner: researcher alarm centered, company communications
criticized ("plans on being extremely reliant on chain-of-thought
monitoring for safety"), non-response to The Verge's confirmation request
noted, chief scientist Pachocki "voiced fears of 'a race into
unmonitorability kicked off by confused reporting'". Tone -0.25
hand-assigned this run (MANUAL ILLUSTRATIVE). Snippet-bounded; date circa
from 8d crawl age at Sep 10 2026.

Finding: register differentiation WITHIN constancy. Both arms adversarial
(replicating #608's cross-entity constancy at launch-week granularity), but
the CRITICISM TYPE differs: market-legitimacy attack on the Meta launch vs
safety-watchdog attack on the OpenAI launch. The Vox Media (Verge parent)
May 29 2024 OpenAI content-licensing deal predicts softer OpenAI coverage;
Hart's pre-launch safety-disaster piece weakens that financial-determinist
reading for this journalist without contradicting it as a named gradient
(reporter-level, not publication-level; strong genre confounds). NOT a
falsification-family member. NOT a pure asymmetry pin. Correlation only,
not causation. NOT a causal claim about editorial influence.

Illustrative delta (OpenAI minus Meta) = -0.25 - (-0.35) = +0.10;
p_value, cohens_d, ci_95 NOT_CALCULATED; is_significant False (Aug 28
standing rule); statistical_contract degenerate_n1_per_arm.

Novelty vs prior work: second Hart mechanism; #608 used different articles
(Sep 5 DseWiki incident piece, ~Jun 7 Stepback clickbait column) and a
different angle (incident-response constancy). The Sep 8 Muse launch piece
and the circa-Sep-2 Astra safety piece are new-to-corpus as Hart-byline
mechanisms (git-grep zero hits pre-commit for both URL stems). First
launch-week register-differentiation mechanism on Hart; sibling of
mechanism 599.

Rotation: Type B follows Type A (#652) per A,B,C,D,E. Rotation guard
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
CAREERS_PATH = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = "mechanism_626_robert_hart_muse_catch_up_vs_astra_safety_disaster_launch_register_sep10"
FILENAME = "test_type_b_653_robert_hart_muse_catch_up_vs_astra_safety_disaster_launch_register_sep10_9am.py"

META_TONE = -0.35
OPENAI_TONE = -0.25
EXPECTED_DELTA = 0.10

META_URLS = [
    "https://thetechstreetnow.com/meta-bets-on-ai-agent-muse-to-catch-up-in-ai-race/",
    "https://technewstube.com/theverge/1865479/meta-bets-ai-agent-muse-to-catch-up-ai-race/",
    "https://rocketnews.com/2026/09/meta-bets-on-ai-agent-muse-to-catch-up-in-ai-race/",
    "https://www.brocker.org/meta-muse-consumer-ai-agent-launch",
]
OPENAI_URLS = [
    "https://newsatw.com/researchers-fear-safety-disaster-ahead-of-openais-astra-release/",
    "https://onlinetechguru.co.uk/researchers-fear-safety-disaster-ahead-of-openais-astra-release/",
    "https://best-technologies.info/tech/researchers-fear-safety-disaster-ahead-of-openais-astra-release/",
    "https://canadian-reviews.ca/researchers-fear-safety-disaster-ahead-of-openais-astra-release/",
]

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. The rotation-guard class is deselected pre-commit.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"


def _careers():
    with open(CAREERS_PATH) as f:
        return yaml.safe_load(f)


def _hart():
    matches = []
    for j in _careers()["journalists"]:
        if isinstance(j, dict) and j.get("name") == "Robert Hart":
            matches.append(j)
    assert len(matches) == 1, f"expected exactly one Robert Hart entry, got {len(matches)}"
    return matches[0]


def _mechanism():
    hart = _hart()
    assert MECH_KEY in hart, f"{MECH_KEY} missing from Robert Hart entry"
    return hart[MECH_KEY]


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


class TestIterationMetadata653:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 653

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 626

    def test_mechanism_id_unique_repo_wide(self):
        seen = {}
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                if int(m.group(1)) == 626:
                    seen.setdefault(626, []).append(path)
        assert len(seen.get(626, [])) == 1, f"mechanism_id 626 not unique: {seen.get(626)}"

    def test_type_is_b(self):
        assert _mechanism()["type"] == "B"

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_block_key_matches(self):
        assert _mechanism()["block_key"] == "type_b_653_robert_hart_muse_catch_up_vs_astra_safety_disaster_launch_register_sep10"

    def test_distinct_from_mechanism_599(self):
        hart = _hart()
        assert "mechanism_599_robert_hart_tarbell_fellowship_cross_entity_constancy_sep08" in hart, \
            "mechanism 599 must still be present as sibling"
        assert MECH_KEY != "mechanism_599_robert_hart_tarbell_fellowship_cross_entity_constancy_sep08"

    def test_no_duplicate_653_file(self):
        others = [p for p in glob.glob(os.path.join(TESTS_DIR, "test_type_b_653_*.py"))
                  if os.path.basename(p) != FILENAME]
        assert not others, f"duplicate #653 test files: {others}"


class TestHartArms653:
    def test_meta_arm_date_and_byline(self):
        meta = _mechanism()["meta_arm"]
        assert meta["date"] == "2026-09-08"
        assert "Robert Hart" in meta["piece"]
        assert "The Verge" in meta["piece"]

    def test_meta_arm_urls_verbatim(self):
        urls = _mechanism()["meta_arm"]["source_urls"]
        for u in META_URLS:
            assert u in urls, f"meta URL missing: {u}"

    def test_meta_arm_market_defeat_quotes(self):
        quotes = _mechanism()["meta_arm"]["evidence_quotes"]
        assert any("catch up in AI race" in q for q in quotes)
        assert any("ailing position" in q for q in quotes)
        assert any("setbacks and failures" in q for q in quotes)

    def test_meta_arm_worlds_first_debunk_quote(self):
        quotes = _mechanism()["meta_arm"]["evidence_quotes"]
        assert any("does not support on its face" in q for q in quotes)

    def test_meta_arm_register_is_market_defeat(self):
        assert _mechanism()["meta_arm"]["register"] == "market_legitimacy_defeat"

    def test_openai_arm_circa_date(self):
        oai = _mechanism()["openai_arm"]
        assert oai["date"].startswith("circa 2026-09-02")
        assert "Robert Hart" in oai["piece"]

    def test_openai_arm_urls_verbatim(self):
        urls = _mechanism()["openai_arm"]["source_urls"]
        for u in OPENAI_URLS:
            assert u in urls, f"openai URL missing: {u}"

    def test_openai_arm_safety_watchdog_quotes(self):
        quotes = _mechanism()["openai_arm"]["evidence_quotes"]
        assert any("safety disaster" in q for q in quotes)
        assert any("chain-of-thought monitoring" in q for q in quotes)
        assert any("did not respond to The Verge" in q for q in quotes)

    def test_openai_arm_register_is_safety_watchdog(self):
        assert _mechanism()["openai_arm"]["register"] == "safety_watchdog_prelaunch"

    def test_snippet_bounded_label_on_both_arms(self):
        assert "Snippet-bounded" in _mechanism()["meta_arm"]["source_note"]
        assert "Snippet-bounded" in _mechanism()["openai_arm"]["source_note"]


class TestScorerDelta653:
    def test_delta_math(self):
        s = _mechanism()["asymmetry_scorer"]
        assert s["meta_tone"] == META_TONE
        assert s["openai_tone"] == OPENAI_TONE
        assert abs(s["illustrative_delta_openai_minus_meta"] - EXPECTED_DELTA) < 1e-9
        assert abs((OPENAI_TONE - META_TONE) - EXPECTED_DELTA) < 1e-9

    def test_manual_illustrative_only(self):
        text = _mechanism_text()
        assert "MANUAL" in text
        s = _mechanism()["asymmetry_scorer"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"
        assert s["is_significant"] is False
        assert s["statistical_contract"] == "degenerate_n1_per_arm"

    def test_verdict_boundaries(self):
        verdict = _mechanism()["asymmetry_scorer"]["verdict"]
        assert "NOT a falsification-family member" in verdict
        assert "NOT a pure asymmetry pin" in verdict
        assert "Correlation only, not causation" in verdict

    def test_constancy_replicated(self):
        verdict = _mechanism()["asymmetry_scorer"]["verdict"]
        assert "#608" in verdict or "constancy" in verdict.lower()

    def test_confounder_strengths_ranked(self):
        c = _mechanism()["confounders_ranked"]
        assert len(c["strong"]) == 2
        assert len(c["moderate"]) == 2
        assert len(c["weak"]) == 2
        assert any("Genre peg" in s for s in c["strong"])
        assert any("snippet-bounded" in s for s in c["strong"])

    def test_cross_refs_name_prior_work(self):
        refs = _mechanism()["cross_references"]
        joined = " ".join(refs)
        assert "599" in joined
        assert "#652" in joined
        assert "#647" in joined


class TestFinancialContext653:
    def test_vox_openai_licensing_deal_named(self):
        fc = _mechanism()["financial_context"]
        assert "May 29, 2024" in fc
        assert "OpenAI" in fc
        assert "licensing" in fc

    def test_gradient_weakened_not_contradicted(self):
        fc = _mechanism()["financial_context"]
        assert "weakening" in fc
        assert "Correlation only, not causation" in fc

    def test_tarbell_context_bounded(self):
        fc = _mechanism()["financial_context"]
        assert "Tarbell" in fc
        assert "structural context only" in fc


class TestRotationCycleGuard653:
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

    def test_window_649_653_closes_a_to_b(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("B", "653"),
            ("A", "652"),
            ("E", "651"),
            ("D", "650"),
            ("C", "649"),
        ], f"rotation window 649-653 wrong: {observed}"

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
        # Post-commit anchor: the #653 main commit. Patched in the followup
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
        assert subject.startswith("Type B #653:"), (
            f"post-commit anchor broken: newest main is not #653: {subject!r}"
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
        sample = "Type B #653: Robert Hart launch-week register differentiation"
        for p in guard_patterns:
            m = re.search(p, sample)
            assert m and m.group(1) == "B" and m.group(2) == "653", (
                f"rotation regex {p!r} fails to match a real subject "
                "(double-backslash bug?)"
            )


class TestDocSyncRatchet653:
    def test_readme_has_653_row(self):
        assert "#653" in read_readme()

    def test_arch_has_653_row(self):
        assert "653" in read_arch()

    def test_readme_row_mentions_hart(self):
        assert "Robert Hart" in read_readme()

    def test_log_starts_with_653(self):
        assert read_log_start().startswith("#653 Type B:")

    def test_def_test_count_matches(self):
        # The README row for #653 must carry this file's own def-test count.
        n = _count_def_tests()
        assert str(n) in read_readme(), (
            f"README #653 row should mention this file's def-test count {n}"
        )


def read_log_start():
    with open(LOG_PATH) as f:
        return f.read()


class TestNoBrittlePatterns653:
    def test_yaml_reparses_clean(self):
        hart = _hart()
        m = hart[MECH_KEY]
        assert isinstance(m["mechanism_id"], int)
        assert isinstance(m["meta_arm"]["tone_illustrative"], float)
        assert isinstance(m["openai_arm"]["tone_illustrative"], float)
        assert isinstance(m["asymmetry_scorer"]["is_significant"], bool)

    def test_no_em_dash_in_mechanism(self):
        assert "\u2014" not in _mechanism_text()
        src = open(os.path.join(TESTS_DIR, FILENAME)).read()
        assert "\u2014" not in src

    def test_all_urls_http_or_https(self):
        urls = list(_mechanism()["meta_arm"]["source_urls"]) + \
            list(_mechanism()["openai_arm"]["source_urls"])
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
        assert "Snippet-bounded" in rm or "snippet-bounded" in rm
        assert "verbatim" in rm

    def test_artifact_readiness_present(self):
        assert "analysis.json" in _mechanism()["artifact_readiness"]
