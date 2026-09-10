"""Type B #638: Sarah Perez (TechCrunch Consumer News Editor) within-writer
trust register across entities.

FIRST dedicated Type B mechanism on Sarah Perez (mechanism_id 617, next free
pre-commit; max numeric mechanism_id was 616). Within-writer comparison across
two Perez bylines on two entities, SAME publication, SAME consumer-AI-agent
category, 4 days apart:

(a) Meta arm: Sep 8 2026 TechCrunch "Meta debuts its Muse AI agent. Will
consumers trust it?", trust-interrogating launch register, tone -0.45
hand-assigned this run (MANUAL ILLUSTRATIVE). Full text read first-hand via
techcrunch.com direct fetch. Headline poses the trust question; lede couples
the launch to the $18B multistate settlement; a dedicated "Could Meta's
history hurt Muse adoption?" section recites Meta's 2011-2026
privacy-violation record. Meta's own safeguards (Secure VM, Sentinel, no
ads-data sharing) are relayed as "claims" needing "deeper investigation".

(b) Google arm: Sep 4 2026 TechCrunch "Google's Gemini Spark can now manage
your Google Photos library", capability-news register, tone +0.05
hand-assigned this run (MANUAL ILLUSTRATIVE). Full text read first-hand via
techcrunch.com direct fetch. Headline announces a capability; zero
interrogation of Google's privacy record despite Gemini Spark gaining access
to the user's entire Google Photos library; the single skeptical paragraph
targets industry AI-hype, not Google trust.

Illustrative delta (meta minus google) = -0.45 - 0.05 = -0.50; p_value,
cohens_d NOT_CALCULATED; is_significant False (Aug 28 standing rule).
VERDICT: WITHIN-WRITER TRUST REGISTER, but NOT a falsification pin: no named
financial gradient predicts this pair (no documented TechCrunch/Yahoo-Google
payer relationship; the Apollo-Anthropic XPV chain documented in #633
predicts softer ANTHROPIC coverage, not Google). Correlation is not causation
per the Aug 28 rule: STRONG news-peg (launch vs feature expansion) and
settlement-recency confounds carry the gap before any incentive effect is
invoked; no newsroom-behavior claim is made. NOT a falsification-family
member. NOT a pure asymmetry pin.

Novelty vs prior Perez work: mechanism #210 (Type A, iteration 218) studied
Perez on camera WEARABLES (Google +0.75 / Meta -0.80 / Apple +0.60,
May-Aug 2026 window) - different study type, different category, different
article set; cross-referenced, not duplicated. The #633 run explicitly
deferred the Muse piece ("rejected as studied"); this run takes it as the
Meta arm of a NEW matched pair against the Sep 4 Gemini Spark piece.

Rotation: Type B follows Type A (#637) per A,B,C,D,E. Rotation guard
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

MECH_KEY = "type_b_638_sarah_perez_techcrunch_meta_muse_vs_google_gemini_spark_trust_register_sep09"
FILENAME = "test_type_b_638_sarah_perez_techcrunch_muse_vs_gemini_spark_sep09_6pm.py"

META_TONE = -0.45
GOOGLE_TONE = 0.05
EXPECTED_DELTA = -0.50

META_URL = "https://techcrunch.com/2026/09/08/meta-debuts-its-muse-ai-agent-will-consumers-trust-it/"
GOOGLE_URL = "https://techcrunch.com/2026/09/04/googles-gemini-spark-can-now-manage-your-google-photos-library/"
AUTHOR_URL = "https://techcrunch.com/author/sarah-perez/"


def _journalists():
    with open(JOURNALISTS_PATH) as f:
        return yaml.safe_load(f)


def _perez():
    matches = [j for j in _journalists()["journalists"]
               if j.get("name") == "Sarah Perez"]
    assert len(matches) == 1, f"expected exactly one Sarah Perez entry, got {len(matches)}"
    return matches[0]


def _mechanism():
    cc = _perez().get("competitor_coverage", {})
    assert MECH_KEY in cc, f"{MECH_KEY} missing from Sarah Perez competitor_coverage"
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


class TestIterationMetadata638:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 638

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 617

    def test_mechanism_id_unique_repo_wide(self):
        import glob
        seen = {}
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                mid = int(m.group(1))
                if mid == 617:
                    seen.setdefault(mid, []).append(path)
        assert len(seen.get(617, [])) == 1, f"mechanism_id 617 not unique: {seen.get(617)}"

    def test_type_is_b(self):
        assert _mechanism()["type"] == "B"

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_block_key_matches(self):
        assert _mechanism()["block_key"] == MECH_KEY


class TestPerezArms638:
    def test_four_day_window_same_writer_same_category(self):
        m = _mechanism()
        assert m["meta_arm"]["date"] == "2026-09-08"
        assert m["google_arm"]["date"] == "2026-09-04"
        assert m["meta_arm"]["publication"] == m["google_arm"]["publication"] == "techcrunch"
        assert m["meta_arm"]["author_byline"] == m["google_arm"]["author_byline"] == "Sarah Perez"
        assert "consumer" in m["meta_arm"]["genre"] and "consumer" in m["google_arm"]["genre"]

    def test_arm_urls_first_hand_verbatim(self):
        m = _mechanism()
        assert m["meta_arm"]["url"] == META_URL
        assert m["google_arm"]["url"] == GOOGLE_URL
        assert m["meta_arm"]["evidence_tier"] == m["google_arm"]["evidence_tier"]
        assert "first-hand" in m["meta_arm"]["evidence_tier"]

    def test_meta_arm_headline_asks_trust_question(self):
        m = _mechanism()
        assert m["meta_arm"]["title"].endswith("Will consumers trust it?"), (
            "the trust question in the headline is the register hinge"
        )

    def test_meta_arm_history_section_quotes(self):
        m = _mechanism()
        joined = " ".join(m["meta_arm"]["key_quotes"])
        assert "Could Meta's history hurt Muse adoption?" in joined
        assert "$18 billion multistate settlement" in joined
        assert "once again trust Meta" in joined

    def test_google_arm_capability_register(self):
        m = _mechanism()
        assert m["google_arm"]["title"] == "Google's Gemini Spark can now manage your Google Photos library"
        joined = " ".join(m["google_arm"]["key_quotes"])
        assert "143,206 photos and videos" in joined
        assert "revolutionary" in joined

    def test_google_arm_no_trust_interrogation(self):
        m = _mechanism()
        assert "trust" not in m["google_arm"]["title"].lower()
        notes = m["google_arm"]["register_notes"]
        # the mirror history question is named only as an absent mirror
        assert "No trust question in the headline" in notes
        assert "Zero interrogation of Google's privacy record" in notes

    def test_byline_attribution_urls_verbatim(self):
        m = _mechanism()
        assert AUTHOR_URL in m["meta_arm"]["byline_attribution_urls"]
        assert AUTHOR_URL in m["google_arm"]["byline_attribution_urls"]
        for u in (META_URL, GOOGLE_URL, AUTHOR_URL):
            assert u.startswith("https://"), f"bad URL: {u}"


class TestScorerDelta638:
    def test_delta_math(self):
        m = _mechanism()["asymmetry_scorer"]
        assert m["meta_tone"] == META_TONE
        assert m["google_tone"] == GOOGLE_TONE
        assert abs((META_TONE - GOOGLE_TONE) - EXPECTED_DELTA) < 1e-9
        assert m["delta_meta_minus_google"] == EXPECTED_DELTA
        assert m["delta_calc"] == "-0.45 - 0.05 = -0.50"

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
        assert "WITHIN-WRITER TRUST REGISTER" in v

    def test_confounder_strengths_ranked(self):
        confs = _mechanism()["confounders_ranked"]
        strengths = [c["strength"] for c in confs]
        assert strengths.count("STRONG") >= 2, f"need STRONG news-peg+settlement confounds, got {strengths}"
        assert "WEAK" in strengths

    def test_cross_refs_name_prior_work(self):
        refs = " ".join(_mechanism()["cross_refs"])
        for tag in ("#210", "#633", "#632", "#305"):
            assert tag in refs, f"cross-ref {tag} missing"
        assert "deferred the Perez Muse piece as studied" in refs


class TestFinancialContext638:
    def test_apollo_yahoo_techcrunch_chain_named(self):
        fc = _mechanism()["financial_context"]
        assert "Apollo Global Management" in fc
        assert "Yahoo" in fc
        assert "TechCrunch" in fc

    def test_no_techcrunch_google_deal_claimed(self):
        fc = _mechanism()["financial_context"]
        assert "No documented TechCrunch-to-Meta" in fc
        assert "TechCrunch-to-Google" in fc

    def test_anthropic_chain_scoped_away_from_google_arm(self):
        fc = _mechanism()["financial_context"]
        assert "Anthropic XPV" in fc
        assert "not Anthropic" in fc

    def test_correlational_boundary(self):
        assert "Correlational boundary only" in _mechanism()["financial_context"]
        assert "no named incentive gradient" in _mechanism()["financial_context"]


class TestRotationCycleGuard638:
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

    def test_window_634_638_closes_a_to_b(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("B", "638"),
            ("A", "637"),
            ("E", "636"),
            ("D", "635"),
            ("C", "634"),
        ], f"rotation window 634-638 wrong: {observed}"

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
        # Post-commit anchor: the #638 main commit. Patched in the followup
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
        assert sha.startswith("PATCH_ME_IN_FOLLOWUP"), f"anchor not yet patched: {sha}"
        assert subject.startswith("Type B #638:"), (
            f"post-commit anchor broken: newest main is not #638: {subject!r}"
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
        sample = "Type B #638: Sarah Perez trust register"
        for p in guard_patterns:
            m = re.search(p, sample)
            assert m and m.group(1) == "B" and m.group(2) == "638", (
                f"rotation regex {p!r} fails to match a real subject "
                "(double-backslash bug?)"
            )


class TestDocSyncRatchet638:
    def test_readme_has_638_row(self):
        assert re.search(r"#638", read_readme()), "README.md missing the #638 test-table row"

    def test_arch_has_638_row(self):
        assert re.search(r"#638", read_arch()), "docs/ARCHITECTURE.md missing the #638 tree row"

    def test_prior_rows_intact(self):
        readme, arch = read_readme(), read_arch()
        for n in ("633", "634", "635", "636", "637"):
            assert re.search(rf"#{n}", readme), f"README.md lost the #{n} row"
            assert re.search(rf"#{n}", arch), f"docs/ARCHITECTURE.md lost the #{n} row"

    def test_readme_row_test_count_matches(self):
        m = re.search(rf"`{re.escape(FILENAME)}`\s*\|\s*(\d+)\s*\|", read_readme())
        assert m, "README #638 row missing or malformed"
        assert int(m.group(1)) == _count_def_tests(), (
            f"README row says {m.group(1)} but file carries {_count_def_tests()}"
        )

    def test_readme_row_says_638(self):
        line = next(
            (ln for ln in read_readme().splitlines() if FILENAME in ln),
            None,
        )
        assert line is not None, "README missing the #638 row entirely"
        assert "#638" in line, "README #638 row does not reference #638"

    def test_log_starts_with_638(self):
        assert read_log().startswith("#638 Type B:")


class TestNoBrittlePatterns638:
    def test_yaml_reparses_clean(self):
        d = _journalists()
        perez = [j for j in d["journalists"] if j.get("name") == "Sarah Perez"][0]
        assert perez["competitor_coverage"][MECH_KEY]["mechanism_id"] == 617

    def test_no_em_dash_in_mechanism(self):
        text = yaml.safe_dump(_mechanism(), allow_unicode=True)
        assert "\u2014" not in text, "em dash leaked into the #638 mechanism"

    def test_all_urls_http_or_https(self):
        m = _mechanism()
        urls = [m["meta_arm"]["url"], m["google_arm"]["url"]]
        urls.extend(m["meta_arm"]["byline_attribution_urls"])
        urls.extend(m["google_arm"]["byline_attribution_urls"])
        urls.extend(_perez()["source_urls"])
        urls.append(_perez()["career"][0]["source_url"])
        for u in urls:
            assert u.startswith("http"), f"bad URL: {u}"

    def test_no_zero_coverage_claims(self):
        dumped = yaml.safe_dump(_mechanism(), allow_unicode=True).lower()
        assert "zero coverage" not in dumped
        assert "no perez byline" not in dumped
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
