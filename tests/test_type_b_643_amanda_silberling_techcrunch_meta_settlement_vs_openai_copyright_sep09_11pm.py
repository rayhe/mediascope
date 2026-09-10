"""Type B #643: Amanda Silberling (TechCrunch Senior Writer) within-writer
accountability register across entities.

FIRST dedicated Type B mechanism on Amanda Silberling (mechanism_id 620, next
free pre-commit; max numeric mechanism_id was 619). Within-writer comparison
across two Silberling bylines on two entities, SAME publication, SAME
legal/regulatory-accountability category, 7 days apart:

(a) Meta arm: Aug 26 2026 TechCrunch "Meta's $18B child-safety deal hinges on
age-verification tech that doesn't work well", accountability-skeptical
register, tone -0.40 hand-assigned this run (MANUAL ILLUSTRATIVE). Full text
read first-hand via techcrunch.com direct fetch. Headline undercuts the deal;
lede contextualizes $18B against Meta's $200B-plus 2025 revenue; "hasn't
admitted wrongdoing" frame; litigator quote characterizes the settlement as
"the political story" the AGs extracted; close notes Meta's full-page ads
omitting the changes came from a lawsuit, and 30% of the payment contingent
on TikTok/YouTube compliance.

(b) OpenAI arm: Sep 2 2026 TechCrunch "US government sides with OpenAI on
issue of training LLMs on copyrighted material", straight legal-news register,
tone +0.05 hand-assigned this run (MANUAL ILLUSTRATIVE). Full text read
first-hand via techcrunch.com direct fetch. Headline states the news peg
neutrally; the NYT's opposing position is stated; no publisher-side
counter-voices are quoted to stress-test the brief's claims; the piece notes
the brief "is not a ruling" but the closing line grants the intervention
weight.

Illustrative delta (meta minus openai) = -0.40 - 0.05 = -0.45; p_value,
cohens_d NOT_CALCULATED; is_significant False (Aug 28 standing rule).
VERDICT: WITHIN-WRITER ACCOUNTABILITY REGISTER, but NOT a falsification pin:
no named financial gradient predicts this pair (no documented
TechCrunch/Yahoo-OpenAI payer relationship; the Apollo-Anthropic XPV chain
documented in #633 predicts softer ANTHROPIC coverage, not OpenAI).
Correlation is not causation per the Aug 28 rule: STRONG news-peg (scrutiny
of a settlement IS the story vs a third-party endorsement IS the story) and
genre (analysis/second-day vs first-day news brief) confounds carry the gap
before any incentive effect is invoked; no newsroom-behavior claim is made.
NOT a falsification-family member. NOT a pure asymmetry pin.

Novelty vs prior work: the settlement URL appears in corpus only as context
(test_lucas_ropek_techcrunch_same_day_settlement_infrastructure_vocabulary_bifurcation_aug26.py,
test_techcrunch_yahoo_openai_chatgpt_ads_europe_coverage_selection_silence_aug27.py,
profiles/competitor-coverage-research.yaml) - never as a Silberling-byline
mechanism. The OpenAI copyright URL is new-to-corpus this run (git-grep zero
hits pre-commit). First Type B mechanism on Amanda Silberling (zero
journalists.yaml mentions pre-commit; entry created this run before the
trailing jacob_krol: mapping key).

Rotation: Type B follows Type A (#642) per A,B,C,D,E. Rotation guard
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
JOURNALISTS_PATH = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = "type_b_643_amanda_silberling_techcrunch_meta_settlement_vs_openai_copyright_register_sep09"
FILENAME = "test_type_b_643_amanda_silberling_techcrunch_meta_settlement_vs_openai_copyright_sep09_11pm.py"

META_TONE = -0.40
OPENAI_TONE = 0.05
EXPECTED_DELTA = -0.45

META_URL = "https://techcrunch.com/2026/08/26/metas-18b-child-safety-deal-hinges-on-age-verification-tech-that-doesnt-work-well/"
OPENAI_URL = "https://techcrunch.com/2026/09/02/u-s-government-sides-with-openai-on-issue-of-training-llms-on-copyrighted-material/"
AUTHOR_URL = "https://techcrunch.com/author/amanda-silberling/"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. The rotation-guard class is deselected pre-commit.
ANCHORED_SHA = "7caee04"


def _journalists():
    with open(JOURNALISTS_PATH) as f:
        return yaml.safe_load(f)


def _silberling():
    matches = [j for j in _journalists()["journalists"]
               if j.get("name") == "Amanda Silberling"]
    assert len(matches) == 1, f"expected exactly one Amanda Silberling entry, got {len(matches)}"
    return matches[0]


def _mechanism():
    cc = _silberling().get("competitor_coverage", {})
    assert MECH_KEY in cc, f"{MECH_KEY} missing from Amanda Silberling competitor_coverage"
    return cc[MECH_KEY]


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


def read_log():
    with open(LOG_PATH) as f:
        return f.read()


class TestIterationMetadata643:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 643

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 620

    def test_mechanism_id_unique_repo_wide(self):
        import glob
        seen = {}
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                mid = int(m.group(1))
                if mid == 620:
                    seen.setdefault(mid, []).append(path)
        assert len(seen.get(620, [])) == 1, f"mechanism_id 620 not unique: {seen.get(620)}"

    def test_type_is_b(self):
        assert _mechanism()["type"] == "B"

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_block_key_matches(self):
        assert _mechanism()["block_key"] == MECH_KEY


class TestSilberlingArms643:
    def test_seven_day_window_same_writer_same_category(self):
        m = _mechanism()
        assert m["meta_arm"]["date"] == "2026-08-26"
        assert m["openai_arm"]["date"] == "2026-09-02"
        assert m["meta_arm"]["publication"] == m["openai_arm"]["publication"] == "techcrunch"
        assert m["meta_arm"]["author_byline"] == m["openai_arm"]["author_byline"] == "Amanda Silberling"
        assert "legal" in m["meta_arm"]["genre"] and "legal" in m["openai_arm"]["genre"]

    def test_arm_urls_first_hand_verbatim(self):
        m = _mechanism()
        assert m["meta_arm"]["url"] == META_URL
        assert m["openai_arm"]["url"] == OPENAI_URL
        assert m["meta_arm"]["evidence_tier"] == m["openai_arm"]["evidence_tier"]
        assert "first-hand" in m["meta_arm"]["evidence_tier"]

    def test_meta_arm_headline_undercuts_deal(self):
        m = _mechanism()
        assert m["meta_arm"]["title"].endswith("doesn't work well"), (
            "the deal-undercutting headline is the register hinge"
        )

    def test_meta_arm_settlement_quotes(self):
        m = _mechanism()
        joined = " ".join(m["meta_arm"]["key_quotes"])
        assert "hasn't admitted wrongdoing" in joined
        assert "political story" in joined
        assert "30% of Meta's settlement payment" in joined
        assert "$200 billion in total revenue" in joined

    def test_openai_arm_straight_register(self):
        m = _mechanism()
        assert m["openai_arm"]["title"] == "US government sides with OpenAI on issue of training LLMs on copyrighted material"
        joined = " ".join(m["openai_arm"]["key_quotes"])
        assert "20-page brief" in joined
        assert "favorable to AI companies" in joined

    def test_openai_arm_nyt_position_stated_but_untested(self):
        m = _mechanism()
        joined = " ".join(m["openai_arm"]["key_quotes"])
        assert "The New York Times" in joined
        notes = m["openai_arm"]["register_notes"]
        # the frame gap is named explicitly, not a one-sidedness claim
        assert "frame gap" in notes
        assert "not stenography" in notes

    def test_byline_attribution_urls_verbatim(self):
        m = _mechanism()
        assert AUTHOR_URL in m["meta_arm"]["byline_attribution_urls"]
        assert AUTHOR_URL in m["openai_arm"]["byline_attribution_urls"]
        for u in (META_URL, OPENAI_URL, AUTHOR_URL):
            assert u.startswith("https://"), f"bad URL: {u}"


class TestScorerDelta643:
    def test_delta_math(self):
        m = _mechanism()["asymmetry_scorer"]
        assert m["meta_tone"] == META_TONE
        assert m["openai_tone"] == OPENAI_TONE
        assert abs((META_TONE - OPENAI_TONE) - EXPECTED_DELTA) < 1e-9
        assert m["delta_meta_minus_openai"] == EXPECTED_DELTA
        assert m["delta_calc"] == "-0.40 - 0.05 = -0.45"

    def test_manual_illustrative_only(self):
        m = _mechanism()["asymmetry_scorer"]
        assert m["method"].startswith("MANUAL ILLUSTRATIVE")
        assert m["p_value"] == "NOT_CALCULATED"
        assert m["cohens_d"] == "NOT_CALCULATED"
        assert m["is_significant"] is False

    def test_verdict_boundaries(self):
        v = _mechanism()["verdict"]
        assert "NOT a falsification pin" in v
        assert "NOT a falsification-family member" in v
        assert "NOT a pure asymmetry pin" in v
        assert "correlation is not causation" in v.lower()
        assert "WITHIN-WRITER ACCOUNTABILITY REGISTER" in v

    def test_confounder_strengths_ranked(self):
        confs = _mechanism()["confounders_ranked"]
        strengths = [c["strength"] for c in confs]
        assert strengths.count("STRONG") >= 2, f"need STRONG news-peg+genre confounds, got {strengths}"
        assert "WEAK" in strengths

    def test_cross_refs_name_prior_work(self):
        refs = " ".join(_mechanism()["cross_refs"])
        for tag in ("#638", "#633", "#305", "#642"):
            assert tag in refs, f"cross-ref {tag} missing"
        assert "SILBERLING-BYLINE" in refs


class TestFinancialContext643:
    def test_apollo_yahoo_techcrunch_chain_named(self):
        fc = _mechanism()["financial_context"]
        assert "Apollo Global Management" in fc
        assert "Yahoo" in fc
        assert "TechCrunch" in fc

    def test_no_techcrunch_openai_deal_claimed(self):
        fc = _mechanism()["financial_context"]
        assert "No documented TechCrunch-to-Meta" in fc
        assert "TechCrunch-to-OpenAI" in fc

    def test_anthropic_chain_scoped_away_from_openai_arm(self):
        fc = _mechanism()["financial_context"]
        assert "Anthropic XPV" in fc
        assert "not Anthropic" in fc

    def test_correlational_boundary(self):
        assert "Correlational boundary only" in _mechanism()["financial_context"]
        assert "no named incentive gradient" in _mechanism()["financial_context"]


class TestRotationCycleGuard643:
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

    def test_window_639_643_closes_a_to_b(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("B", "643"),
            ("A", "642"),
            ("E", "641"),
            ("D", "640"),
            ("C", "639"),
        ], f"rotation window 639-643 wrong: {observed}"

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
        # Post-commit anchor: the #643 main commit. Patched in the followup
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
        assert subject.startswith("Type B #643:"), (
            f"post-commit anchor broken: newest main is not #643: {subject!r}"
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
        sample = "Type B #643: Amanda Silberling accountability register"
        for p in guard_patterns:
            m = re.search(p, sample)
            assert m and m.group(1) == "B" and m.group(2) == "643", (
                f"rotation regex {p!r} fails to match a real subject "
                "(double-backslash bug?)"
            )


class TestDocSyncRatchet643:
    def test_readme_has_643_row(self):
        assert re.search(r"#643", read_readme()), "README.md missing the #643 test-table row"

    def test_arch_has_643_row(self):
        assert re.search(r"#643", read_arch()), "docs/ARCHITECTURE.md missing the #643 tree row"

    def test_prior_rows_intact(self):
        readme, arch = read_readme(), read_arch()
        for n in ("638", "639", "640", "641", "642"):
            assert re.search(rf"#{n}", readme), f"README.md lost the #{n} row"
            assert re.search(rf"#{n}", arch), f"docs/ARCHITECTURE.md lost the #{n} row"

    def test_readme_row_test_count_matches(self):
        m = re.search(rf"`{re.escape(FILENAME)}`\s*\|\s*(\d+)\s*\|", read_readme())
        assert m, "README #643 row missing or malformed"
        assert int(m.group(1)) == _count_def_tests(), (
            f"README row says {m.group(1)} but file carries {_count_def_tests()}"
        )

    def test_readme_row_says_643(self):
        line = next(
            (ln for ln in read_readme().splitlines() if FILENAME in ln),
            None,
        )
        assert line is not None, "README missing the #643 row entirely"
        assert "#643" in line, "README #643 row does not reference #643"

    def test_log_starts_with_643(self):
        assert read_log().startswith("#643 Type B:")


class TestNoBrittlePatterns643:
    def test_yaml_reparses_clean(self):
        d = _journalists()
        silberling = [j for j in d["journalists"] if j.get("name") == "Amanda Silberling"][0]
        assert silberling["competitor_coverage"][MECH_KEY]["mechanism_id"] == 620

    def test_no_em_dash_in_mechanism(self):
        text = yaml.safe_dump(_mechanism(), allow_unicode=True)
        assert "\u2014" not in text, "em dash leaked into the #643 mechanism"

    def test_all_urls_http_or_https(self):
        m = _mechanism()
        urls = [m["meta_arm"]["url"], m["openai_arm"]["url"]]
        urls.extend(m["meta_arm"]["byline_attribution_urls"])
        urls.extend(m["openai_arm"]["byline_attribution_urls"])
        urls.extend(_silberling()["source_urls"])
        urls.append(_silberling()["career"][0]["source_url"])
        for u in urls:
            assert u.startswith("http"), f"bad URL: {u}"

    def test_no_zero_coverage_claims(self):
        dumped = yaml.safe_dump(_mechanism(), allow_unicode=True).lower()
        assert "zero coverage" not in dumped
        assert "no silberling byline" not in dumped
        assert "has written zero" not in dumped
        assert "never written" not in dumped

    def test_no_engine_significance_claims(self):
        dumped = yaml.safe_dump(_mechanism(), allow_unicode=True).lower()
        assert "p_value" in dumped
        assert "significant true" not in dumped

    def test_research_method_names_evidence_tiers(self):
        method = _mechanism()["research_method"]
        assert "first-hand" in method
        assert "iteration-492" in method
        assert "byline" in method.lower()

    def test_artifact_readiness_present(self):
        assert "analysis.json" in _mechanism()["artifact_readiness"]
