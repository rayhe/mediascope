"""Type B #663: Woo-Bobrowsky (WSJ) AI-researcher job-move register asymmetry.

FIRST dedicated Type B mechanism on the Woo+Bobrowsky byline pair
(mechanism_id 632, next free pre-commit; max numeric mechanism_id was 631).
Meghan Bobrowsky has prior repo mechanisms (#49 smart-glasses entity
targeting, #155 cross-publication brand stigma, #337 settlement-week
bifurcation) but none on the AI-researcher talent-war beat and none pairing
her with co-author Erin Woo. New angle, new arms, both opened first-hand
via browser.open this run (wsj.com rendered full text):

(a) Meta arm: Sep 9 2026 WSJ "Star AI Researcher Is Leaving Meta for
Anthropic" (byline Erin Woo and Meghan Bobrowsky per the piece footer).
Register = departure-as-desperation: "capped a frantic recruiting spree last
summer, when Meta threw money at researchers to try to catch up in the race
to build artificial intelligence", "The company has been fighting to get
back in the AI race", "a dirt-cheap coding agent", "Meta declined to
comment on his exit". Tone -0.40 hand-assigned this run (MANUAL
ILLUSTRATIVE). Date bounded: the piece states Tulloch announced his exit a
day after Meta launched its Muse AI agent on Sep 8 2026.

(b) Google arm: Aug 29 2026 WSJ "Thinking Machines Lab Co-Founder Barret
Zoph Joins Google" (byline Erin Woo and Meghan Bobrowsky per the piece
footer). Register = arrival-as-homecoming: Google spokesman Thomas
Schoenfelder quoted warmly near the top ("We look forward to Barret
returning to Google and bringing his RL and post-training expertise to
Gemini"), Zoph's credentials stated respectfully, the catch-up framing
confined to a single clause ("Google is seeking to catch up to Anthropic
and OpenAI in developing AI that can create code"). Tone +0.15
hand-assigned this run (MANUAL ILLUSTRATIVE). Date bounded: the piece
carries a "Corrected on Aug. 29" stamp.

Finding: gradient-absent but valence-confounded register asymmetry. Same
byline pair, same story type (AI-researcher job moves), about two weeks
apart: Meta's departure gets the desperation register, Google's arrival gets
the homecoming register with a welcoming company voice. No one-sided money
gradient exists at WSJ to explain the gap (corpus: News Corp balanced at
$50M/yr Meta + $50M/yr OpenAI), so this pair functions as a
gradient-absent control case. The STRONG news-valence confound (a departure
story is inherently more negative than an arrival story) is the leading
alternative explanation and bounds the entity-bias reading. NOT a
falsification-family member (no one-sided financial predictor exists here
to test). NOT a pure asymmetry pin. Correlation only, not causation. NOT a
causal claim about editorial influence.

Illustrative delta (Google minus Meta) = 0.15 - (-0.40) = +0.55;
p_value, cohens_d, ci_95 NOT_CALCULATED; is_significant False (Aug 28
standing rule); statistical_contract degenerate_n1_per_arm.

Novelty vs prior work: FIRST dedicated Type B on the Woo+Bobrowsky byline
pair; both WSJ URLs new-to-corpus (zero mechanism references pre-commit,
git-grep verified). Distinct from #371 (Kylie Robison WIRED talent-war
direction framing, mechanism 371; different journalist, different
publication, different pieces) and from Bobrowsky's prior mechanisms #49 /
#155 / #337 (smart-glasses and settlement angles, never the researcher
job-move beat). Same byline pair on mirrored job-move stories is a first
for the corpus.

Rotation: Type B follows Type A (#662) per A,B,C,D,E. Rotation guard
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

MECH_KEY = "mechanism_632_woo_bobrowsky_ai_researcher_departure_register_meta_desperation_vs_google_homecoming_aug29_sep09"
FILENAME = "test_type_b_663_woo_bobrowsky_ai_researcher_departure_register_asymmetry_sep10_8pm.py"

META_TONE = -0.40
GOOGLE_TONE = 0.15
EXPECTED_DELTA = 0.55

META_URLS = [
    "https://www.wsj.com/tech/ai/star-ai-researcher-is-leaving-meta-8906e4aa",
]
GOOGLE_URLS = [
    "https://www.wsj.com/tech/ai/thinking-machines-lab-co-founder-barret-zoph-joins-google-49f594e6",
]

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. The rotation-guard class is deselected pre-commit.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"


def _careers():
    with open(CAREERS_PATH) as f:
        return yaml.safe_load(f)


def _bobrowsky():
    matches = []
    for j in _careers()["journalists"]:
        if isinstance(j, dict) and j.get("name") == "Meghan Bobrowsky":
            matches.append(j)
    assert len(matches) == 1, f"expected exactly one Meghan Bobrowsky entry, got {len(matches)}"
    return matches[0]


def _mechanism():
    bobrowsky = _bobrowsky()
    assert MECH_KEY in bobrowsky, f"{MECH_KEY} missing from Meghan Bobrowsky entry"
    return bobrowsky[MECH_KEY]


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


class TestIterationMetadata663:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 663

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 632

    def test_mechanism_id_unique_repo_wide(self):
        seen = {}
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                if int(m.group(1)) == 632:
                    seen.setdefault(632, []).append(path)
        assert len(seen.get(632, [])) == 1, f"mechanism_id 632 not unique: {seen.get(632)}"

    def test_type_is_b(self):
        assert _mechanism()["type"] == "B"

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_block_key_matches(self):
        assert _mechanism()["block_key"] == "type_b_663_woo_bobrowsky_ai_researcher_departure_register_meta_desperation_vs_google_homecoming_aug29_sep09"

    def test_first_dedicated_type_b_on_woo_bobrowsky_pair(self):
        bobrowsky = _bobrowsky()
        dedicated = [k for k in bobrowsky
                     if k.startswith("mechanism_") and "crossref" not in k and "cross_ref" not in k]
        assert MECH_KEY in dedicated, f"mechanism 632 missing from dedicated list: {dedicated}"
        assert not any("woo_bobrowsky" in k and k != MECH_KEY for k in dedicated), (
            f"unexpected second Woo-Bobrowsky dedicated mechanism: {dedicated}"
        )

    def test_no_duplicate_663_file(self):
        others = [p for p in glob.glob(os.path.join(TESTS_DIR, "test_type_b_663_*.py"))
                  if os.path.basename(p) != FILENAME]
        assert not others, f"duplicate #663 test files: {others}"


class TestBobrowskyArms663:
    def test_meta_arm_date_and_byline(self):
        meta = _mechanism()["meta_arm"]
        assert meta["date"] == "2026-09-09"
        assert "Erin Woo" in meta["piece"]
        assert "Meghan Bobrowsky" in meta["piece"]
        assert "WSJ" in meta["piece"]

    def test_meta_arm_url_verbatim(self):
        urls = _mechanism()["meta_arm"]["source_urls"]
        for u in META_URLS:
            assert u in urls, f"meta URL missing: {u}"

    def test_meta_arm_desperation_quotes(self):
        quotes = _mechanism()["meta_arm"]["evidence_quotes"]
        assert any("frantic recruiting spree" in q for q in quotes)
        assert any("threw money at researchers" in q for q in quotes)
        assert any("fighting to get back in the AI race" in q for q in quotes)
        assert any("dirt-cheap coding agent" in q for q in quotes)
        assert any("declined to comment" in q for q in quotes)

    def test_meta_arm_register_is_departure_desperation(self):
        assert _mechanism()["meta_arm"]["register"] == "departure_as_desperation"

    def test_meta_arm_first_hand_note(self):
        note = _mechanism()["meta_arm"]["source_note"]
        assert "First-hand" in note
        assert "browser.open" in note

    def test_google_arm_date_and_byline(self):
        goog = _mechanism()["google_arm"]
        assert goog["date"] == "2026-08-29"
        assert "Erin Woo" in goog["piece"]
        assert "Meghan Bobrowsky" in goog["piece"]
        assert "WSJ" in goog["piece"]

    def test_google_arm_url_verbatim(self):
        urls = _mechanism()["google_arm"]["source_urls"]
        for u in GOOGLE_URLS:
            assert u in urls, f"google URL missing: {u}"

    def test_google_arm_homecoming_quotes(self):
        quotes = _mechanism()["google_arm"]["evidence_quotes"]
        assert any("We look forward to Barret returning to Google" in q for q in quotes)
        assert any("Thomas Schoenfelder" in q for q in quotes)
        assert any("vice president of research" in q for q in quotes)
        assert any("seeking to catch up to Anthropic and OpenAI" in q for q in quotes)

    def test_google_arm_register_is_arrival_homecoming(self):
        assert _mechanism()["google_arm"]["register"] == "arrival_as_homecoming"

    def test_google_arm_first_hand_note(self):
        note = _mechanism()["google_arm"]["source_note"]
        assert "First-hand" in note
        assert "browser.open" in note

    def test_same_byline_pair_both_arms(self):
        meta = _mechanism()["meta_arm"]["piece"]
        goog = _mechanism()["google_arm"]["piece"]
        for name in ("Erin Woo", "Meghan Bobrowsky"):
            assert name in meta and name in goog, f"{name} not on both arms"

    def test_arms_about_two_weeks_apart(self):
        assert _mechanism()["meta_arm"]["date"] == "2026-09-09"
        assert _mechanism()["google_arm"]["date"] == "2026-08-29"


class TestScorerDelta663:
    def test_delta_math(self):
        s = _mechanism()["asymmetry_scorer"]
        assert s["meta_tone"] == META_TONE
        assert s["google_tone"] == GOOGLE_TONE
        assert abs(s["illustrative_delta_google_minus_meta"] - EXPECTED_DELTA) < 1e-9
        assert abs((GOOGLE_TONE - META_TONE) - EXPECTED_DELTA) < 1e-9

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

    def test_verdict_gradient_absent_valence_confounded(self):
        verdict = _mechanism()["asymmetry_scorer"]["verdict"]
        assert "Gradient-absent" in verdict
        assert "valence-confounded" in verdict

    def test_confounder_strengths_ranked(self):
        c = _mechanism()["confounders_ranked"]
        assert len(c["strong"]) == 2
        assert len(c["moderate"]) == 2
        assert len(c["weak"]) == 2
        assert any("News-valence" in s for s in c["strong"])
        assert any("$1" in s or "pay package" in s for s in c["strong"])
        assert any("Murati" in s for s in c["moderate"])
        assert any("editor-written" in s or "headline" in s for s in c["moderate"])

    def test_counterevidence_present(self):
        ce = _mechanism()["counterevidence"]
        joined = " ".join(ce)
        assert "Jeff Dean" in joined
        assert "competitive models" in joined
        assert "Metz joining Meta" in joined or "Luke Metz" in joined

    def test_cross_refs_name_prior_work(self):
        refs = _mechanism()["cross_references"]
        joined = " ".join(refs)
        assert "#371" in joined
        assert "#662" in joined
        assert "#337" in joined
        assert "#49" in joined


class TestFinancialContext663:
    def test_balanced_ties_named(self):
        fc = _mechanism()["financial_context"]
        assert "$50M/yr Meta" in fc
        assert "$50M/yr OpenAI" in fc

    def test_no_onesided_gradient(self):
        fc = _mechanism()["financial_context"]
        assert "no one-sided" in fc or "balanced" in fc

    def test_correlation_not_causation(self):
        fc = _mechanism()["financial_context"]
        assert "Correlation, not causation" in fc

    def test_valence_confound_stronger_than_money(self):
        fc = _mechanism()["financial_context"]
        assert "news-valence confound" in fc


class TestRotationCycleGuard663:
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

    def test_window_659_663_closes_a_to_b(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("B", "663"),
            ("A", "662"),
            ("E", "661"),
            ("D", "660"),
            ("C", "659"),
        ], f"rotation window 659-663 wrong: {observed}"

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
        # Post-commit anchor: the #663 main commit. Patched in the followup
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
        assert subject.startswith("Type B #663:"), (
            f"post-commit anchor broken: newest main is not #663: {subject!r}"
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
        sample = "Type B #663: Woo-Bobrowsky AI-researcher job-move register asymmetry"
        for p in guard_patterns:
            m = re.search(p, sample)
            assert m and m.group(1) == "B" and m.group(2) == "663", (
                f"rotation regex {p!r} fails to match a real subject "
                "(double-backslash bug?)"
            )


class TestDocSyncRatchet663:
    def test_readme_has_663_row(self):
        assert "#663" in read_readme()

    def test_arch_has_663_row(self):
        assert "663" in read_arch()

    def test_readme_row_mentions_bobrowsky(self):
        assert "Bobrowsky" in read_readme()

    def test_log_starts_with_663(self):
        assert read_log_start().startswith("#663 Type B:")

    def test_def_test_count_matches(self):
        # The README row for #663 must carry this file's own def-test count.
        n = _count_def_tests()
        assert str(n) in read_readme(), (
            f"README #663 row should mention this file's def-test count {n}"
        )


class TestNoBrittlePatterns663:
    def test_yaml_reparses_clean(self):
        bobrowsky = _bobrowsky()
        m = bobrowsky[MECH_KEY]
        assert isinstance(m["mechanism_id"], int)
        assert isinstance(m["meta_arm"]["tone_illustrative"], float)
        assert isinstance(m["google_arm"]["tone_illustrative"], float)
        assert isinstance(m["asymmetry_scorer"]["is_significant"], bool)

    def test_no_em_dash_in_mechanism(self):
        assert "\u2014" not in _mechanism_text()
        src = open(os.path.join(TESTS_DIR, FILENAME)).read()
        assert "\u2014" not in src

    def test_all_urls_http_or_https(self):
        urls = list(_mechanism()["meta_arm"]["source_urls"]) + \
            list(_mechanism()["google_arm"]["source_urls"])
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
        assert "First-hand" in rm or "first-hand" in rm
        assert "verbatim" in rm

    def test_artifact_readiness_present(self):
        assert "analysis.json" in _mechanism()["artifact_readiness"]
