"""Type C #694: Microsoft x Nine Entertainment (Jul 3 2026) - Microsoft's first
news-content AI deal in Asia-Pacific; Copilot real-time grounding in Nine
mastheads (AFR, SMH, The Age, Brisbane Times, WAToday); eighth leg of the
Microsoft publisher-leverage architecture.

Deal (Jul 3 2026, 71 days pre-run): Microsoft Copilot may reference the text
of Nine's masthead content beyond paywalled previews during AI searches to
contextualise and ground outputs; Copilot displays snippets, headlines and
summaries and directs audiences to Nine's mastheads for the full story.
First-of-its-kind in Australia (Microsoft announcement); first of its kind
for Microsoft in the Asia Pacific Region (Tory Maguire, Nine MD Publishing).
Quantum, duration, exclusivity all undisclosed - materiality unmeasurable.
Training rights unconfirmed (retrieval/grounding scoped, not model training).

Primary source: Microsoft's own announcement
https://news.microsoft.com/source/asia/2026/07/03/nine-microsoft-copilot-agreement/
Corroboration: Press Gazette AI-deals tracker, B&T, Mediaweek, AdNews.
Sep 2026 status ACTIVE per the #599 convention (bounded absence of exit
reporting per the iteration-492 rule).

This run also surfaced two companion findings kept out of the mechanism to
stay single-topic: the Reach-Amazon usage-based Nova/Alexa deal (Mar 2 2026,
Press Gazette, new-to-corpus, candidate for a future Type C Amazon-leg
mechanism) and the Feb 2026 FT join of Google's News AI pilot (already in
corpus per competitor-coverage-research.yaml lines 2760/8693/10241).

Qualitative financial mapping only: no asymmetry scorer run, tone scores
NOT_SCORED, p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False.
NOT a falsification-family member - ledger stays at 19 after #693's
NINETEENTH. No analysis.json update warranted.

Rotation: Type C follows Type B (#693) per A,B,C,D,E. Rotation guard,
doc-sync, and novelty-anchor tests deselected pre-commit per the #565
followup convention; anchor patched in the followup commit once the
main commit SHA is known.
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

MECH_KEY = "mechanism_651_microsoft_nine_entertainment_apac_first_copilot_grounding_jul2026"
TEST_BASENAME = "test_type_c_694_microsoft_nine_apac_first_copilot_deal_sep12_4am.py"
FILENAME = TEST_BASENAME

MSFT_URL = "https://news.microsoft.com/source/asia/2026/07/03/nine-microsoft-copilot-agreement/"
PRESSGAZETTE_URL = "https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/"
BANDT_URL = "https://www.bandt.com.au/nine-inks-deal-to-let-microsoft-copilot-reference-paywalled-content-in-ai-searches/"
MEDIAWEEK_URL = "https://www.mediaweek.com.au/nine-microsoft-australian-first-ai-agreement"
ADNEWS_URL = "https://www.adnews.com.au/news/nine-closes-ai-content-deal-with-microsoft"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. The rotation-guard class is deselected pre-commit.
ANCHORED_SHA = "PENDING"


def _entities():
    with open(ENTITIES_PATH) as f:
        return yaml.safe_load(f)


def _microsoft():
    return _entities()["entities"]["microsoft"]


def _mechanism():
    m = _microsoft()
    assert MECH_KEY in m, "%s missing from entities.microsoft" % MECH_KEY
    return m[MECH_KEY]


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
    return open(README_PATH).read()


def read_arch():
    return open(ARCH_PATH).read()


def read_log_start():
    return open(LOG_PATH).read(200)


class TestIterationMetadata694:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 694

    def test_rotation_type(self):
        assert _mechanism()["rotation"] == "Type C"

    def test_date_analyzed(self):
        assert _mechanism()["date_analyzed"] == "2026-09-12"

    def test_time_pdt(self):
        assert _mechanism()["time_pdt"] == "04:00"

    def test_job_and_goal(self):
        assert _mechanism()["job_id"] == "mediascope-daily-iteration"
        assert _mechanism()["goal_id"] == "goal_54093bda4145"

    def test_type_field(self):
        assert _mechanism()["type"] == "financial_incentive_mapping"

    def test_single_mech_key(self):
        with open(ENTITIES_PATH) as f:
            raw = f.read()
        assert raw.count(MECH_KEY) == 1


class TestDealLegFormalization694:
    def test_mechanism_id(self):
        assert _mechanism()["mechanism_id"] == 651
        assert isinstance(_mechanism()["mechanism_id"], int)

    def test_announcement_date(self):
        assert _mechanism()["announcement_date"] == "2026-07-03"

    def test_counterparties(self):
        parties = _mechanism()["deal_parties"]
        assert "Microsoft" in parties["payer"]
        assert "Copilot" in parties["payer"]
        assert "Nine" in parties["counterparty"]

    def test_mastheads(self):
        mast = _mechanism()["deal_parties"]["mastheads"]
        for name in [
            "Australian Financial Review",
            "Sydney Morning Herald",
            "The Age",
            "Brisbane Times",
            "WAToday",
        ]:
            assert name in mast, "masthead missing: %s" % name

    def test_deal_structure_grounding(self):
        struct = _mechanism()["deal_structure"]
        assert "beyond paywalled previews" in struct["access"]
        assert "snippets, headlines and summaries" in struct["display"]
        assert "training_rights" in struct
        assert "unconfirmed" in struct["training_rights"]

    def test_terms_undisclosed(self):
        terms = _mechanism()["deal_terms"]
        assert "undisclosed" in terms["quantum"]
        assert "undisclosed" in terms["duration"]

    def test_apac_first_claim(self):
        claim = _mechanism()["apac_first_claim"]["claim"]
        assert "Asia Pacific" in claim
        assert "first" in claim.lower()
        assert "evidence_tier" in _mechanism()["apac_first_claim"]

    def test_executive_quotes_three(self):
        quotes = _mechanism()["executive_quotes"]
        assert len(quotes) == 3
        joined = " ".join(quotes)
        assert "Matt Stanton" in joined
        assert "Jane Livesey" in joined
        assert "Tory Maguire" in joined

    def test_source_urls(self):
        urls = _mechanism()["source_urls"]
        assert len(urls) == 5
        for u in (MSFT_URL, PRESSGAZETTE_URL, BANDT_URL, MEDIAWEEK_URL, ADNEWS_URL):
            assert u in urls, "source URL missing: %s" % u
        for u in urls:
            assert u.startswith(("http://", "https://")), "bad URL: %r" % u

    def test_status_active(self):
        assert "ACTIVE" in _mechanism()["status_sep2026"]
        assert "#599" in _mechanism()["status_sep2026"]

    def test_architecture_context_eighth_leg(self):
        ctx = " ".join(_mechanism()["architecture_context"])
        assert "Eighth" in ctx
        assert "septuple" in ctx


class TestCrossReferences694:
    def test_axel_springer_arc(self):
        joined = " ".join(_mechanism()["cross_references"])
        assert "#604" in joined

    def test_pcm_cn_bilateral(self):
        joined = " ".join(_mechanism()["cross_references"])
        assert "#684" in joined
        assert "m645" in joined

    def test_septuple_stack(self):
        joined = " ".join(_mechanism()["cross_references"])
        assert "septuple_publisher_leverage" in joined

    def test_india_geographic_pin(self):
        joined = " ".join(_mechanism()["cross_references"])
        assert "#624" in joined
        assert "m609" in joined

    def test_meta_bundle_shape(self):
        joined = " ".join(_mechanism()["cross_references"])
        assert "331" in joined


class TestNovelty694:
    def test_single_694_file_on_disk(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_c_694*"))
        assert files == [os.path.join(TESTS_DIR, FILENAME)], files

    def test_no_duplicate_651_mechanism_key(self):
        count = 0
        for path in glob.glob(
            os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True
        ):
            text = open(path).read()
            count += len(re.findall(r"^    mechanism_651_microsoft_nine", text, re.M))
        assert count == 1, "mechanism_651 key appears %d times" % count

    def test_no_prior_dedicated_nine_mechanism(self):
        # Prior mentions: none. This pins that the only mechanism whose
        # name names Nine Entertainment is the one this run added.
        names = []

        def walk(o):
            if isinstance(o, dict):
                for k, v in o.items():
                    if (
                        isinstance(k, str)
                        and k.startswith("mechanism_")
                        and isinstance(v, dict)
                    ):
                        nm = v.get("mechanism_name")
                        if isinstance(nm, str) and "Nine" in nm:
                            names.append(nm)
                    walk(v)
            elif isinstance(o, list):
                for v in o:
                    walk(v)

        walk(_entities())
        dedicated = [n for n in names if "Nine Entertainment" in n]
        assert dedicated == [_mechanism()["mechanism_name"]], dedicated

    def test_max_numeric_is_651(self):
        ids = []
        with open(ENTITIES_PATH) as f:
            raw = f.read()
        ids = [int(x) for x in re.findall(r"mechanism_(\d+)_", raw)]
        assert max(ids) == 651, "max mechanism id in entities is %d" % max(ids)

    def test_novelty_verification_pins(self):
        nov = " ".join(_mechanism()["novelty_verification"])
        assert "Zero test_type_c_694 files on disk pre-commit" in nov
        assert "No Type C #694 in git log pre-commit" in nov
        assert "Max numeric mechanism id pre-commit 650" in nov


class TestResearchMethod694:
    def test_method_describes_queries(self):
        method = _mechanism()["research_method"]
        assert "2 browser.search query sets" in method
        assert "1 first-hand browser.open read" in method

    def test_verbatim_url_discipline(self):
        method = _mechanism()["research_method"]
        assert "verbatim from Full-URL listings" in method
        assert "no canonical URLs constructed" in method

    def test_bounded_absence(self):
        method = _mechanism()["research_method"]
        assert "iteration-492" in method
        assert "bounded absence" in method

    def test_no_zero_coverage_claim(self):
        method = _mechanism()["research_method"]
        assert "no zero-coverage claims" in method

    def test_primary_source_attribution(self):
        focus = _mechanism()["type_c_focus"]
        assert "news.microsoft.com" in focus
        assert "primary source" in focus

    def test_microsoft_url_in_sources(self):
        assert MSFT_URL in _mechanism()["source_urls"]


class TestStatisticalDiscipline694:
    def test_scorer_none(self):
        sd = _mechanism()["statistical_discipline"]
        # YAML 1.1 parses unquoted `none` as the string "none"; this matches
        # the mechanism_645 statistical_discipline convention.
        assert sd["scorer"] == "none"

    def test_no_tone_scores(self):
        sd = _mechanism()["statistical_discipline"]
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"

    def test_not_significant(self):
        sd = _mechanism()["statistical_discipline"]
        assert sd["is_significant"] is False
        assert sd["qualitative_only"] is True
        assert sd["correlation_not_causation"] is True
        assert sd["artifact_grade"] is False

    def test_not_falsification_member(self):
        fam = _mechanism()["falsification_family"]
        assert "NOT a member" in fam["membership"]
        assert "ledger stays at 19" in fam["membership"]

    def test_qualitative_boundary_convention(self):
        fam = _mechanism()["falsification_family"]
        assert "#609" in fam["boundary_note"]
        assert "#614" in fam["boundary_note"]

    def test_no_analysis_json_update(self):
        assert "No analysis.json update warranted" in _mechanism()["artifact_readiness"]


class TestRotationCycleGuard694:
    # Deselected pre-commit per the #565 followup convention; the rotation
    # window only closes once the #694 main commit exists.
    ANCHORED_SHA = ANCHORED_SHA

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

    def test_window_690_694_closes_b_to_c(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("C", "694"),
            ("B", "693"),
            ("A", "692"),
            ("E", "691"),
            ("D", "690"),
        ], "rotation window 690-694 wrong: %r" % (observed,)

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
                "rotation broken: %s -> %s is not a valid cycle edge" % (a, b)
            )

    def test_anchor_is_main_patch_in_followup(self):
        # Post-commit anchor: the #694 main commit. Patched in the followup
        # per the #565 convention once the main commit SHA is known.
        pytest.skip("anchor patched in followup per #565 convention")

    def test_rotation_guard_regex_actually_matches(self):
        # #632 process note: a rotation guard whose regex never matches is a
        # silent no-op. Verify the guard regexes match a real main-commit
        # subject (the double-backslash r"...#(\d+)..." form silently matches
        # nothing). Written as a semantic check rather than a literal-pattern
        # check so the test cannot defeat itself by containing the pattern.
        src = open(os.path.join(TESTS_DIR, TEST_BASENAME)).read()
        patterns = re.findall(r're\.search\(r"([^"]+)"', src)
        guard_patterns = [p for p in patterns if p.startswith("Type (")]
        assert guard_patterns, "no rotation-guard regex found in this file"
        sample = "Type C #694: Microsoft x Nine Entertainment APAC-first Copilot grounding deal"
        for p in guard_patterns:
            m = re.search(p, sample)
            assert m and m.group(1) == "C" and m.group(2) == "694", (
                "rotation regex %r fails to match a real subject "
                "(double-backslash bug?)" % (p,)
            )


class TestDocSyncRatchet694:
    # Fails pre-commit by design per the #565 followup convention; the README
    # test-file table row and ARCHITECTURE tree row land in the doc-sync commit.
    def test_readme_has_694_row(self):
        assert "test_type_c_694" in read_readme()

    def test_arch_has_694_row(self):
        assert "test_type_c_694" in read_arch()

    def test_readme_row_mentions_nine(self):
        assert "Nine Entertainment" in read_readme()

    def test_log_starts_with_694(self):
        assert read_log_start().startswith("#694 Type C:")

    def test_def_test_count_matches(self):
        # The README row for #694 must carry this file's own def-test count.
        n = _count_def_tests()
        assert str(n) in read_readme(), (
            "README #694 row should mention this file's def-test count %d" % n
        )


class TestNoBrittlePatterns694:
    def test_yaml_reparses_clean(self):
        m = _mechanism()
        assert isinstance(m["mechanism_id"], int)
        assert isinstance(m["source_urls"], list)
        sd = m["statistical_discipline"]
        assert isinstance(sd["is_significant"], bool)
        assert isinstance(sd["qualitative_only"], bool)

    def test_no_em_dash_in_mechanism(self):
        # chr() construction keeps this source file itself ASCII-only; the
        # AGENTS.md trap is muse.write emitting real U+2028/U+2029 bytes.
        forbidden = [chr(0x2014), chr(0x2028), chr(0x2029)]
        text = _mechanism_text()
        src = open(os.path.join(TESTS_DIR, TEST_BASENAME)).read()
        for ch in forbidden:
            assert ch not in text, "forbidden U+%04X in mechanism" % ord(ch)
            assert ch not in src, "forbidden U+%04X in test file" % ord(ch)

    def test_all_urls_http_or_https(self):
        urls = _mechanism()["source_urls"]
        assert urls, "no URLs recorded"
        for u in urls:
            assert u.startswith(("http://", "https://")), "bad URL: %r" % (u,)
