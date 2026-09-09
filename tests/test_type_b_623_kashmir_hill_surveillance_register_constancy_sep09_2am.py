"""Type B #623: Kashmir Hill (NYT) surveillance-register constancy across
entities.

FIRST dedicated Type B mechanism on Kashmir Hill's competitor_coverage
(mechanism_id 608, next free pre-commit; max numeric mechanism_id was 607).
Within-writer comparison across three Hill bylines on three entity classes:

(a) Meta arm: Feb 13 2026 NYT NameTag exposé, co-bylined Hill + Kalley
Huang + Mike Isaac, adversarial investigative register on Meta's internal
facial-recognition plans for Ray-Ban glasses (leaked Reality Labs memo,
"dynamic political environment" quote), tone -0.80 carried from the
nytimes.yaml Hill cross-entity analysis tone_score.

(b) Clearview AI arm: Jan 18 2020 NYT "The Secretive Company That Might
End Privacy as We Know It", solo Hill byline, adversarial investigative
register on a facial-recognition startup (3B scraped images, triggered 8
federal class actions and a 40+ org PCLOB letter), tone -0.85 manual
illustrative this run.

(c) Automaker arm: Mar 11 2024 NYT "Automakers Are Sharing Consumers'
Driving Behavior With Insurance Companies", Hill byline, adversarial
investigative register on GM/Honda/Kia/Hyundai driver-data sales to
LexisNexis/Verisk (GM cut ties 11 days later; Wyden/Markey Senate letter
to the FTC), tone -0.75 manual illustrative this run.

Illustrative delta (meta minus non-meta avg) = -0.80 - (-0.80) = 0.00;
p_value, cohens_d NOT_CALCULATED; is_significant False (Aug 28 standing
rule). CONSTANCY verdict: Hill applies the same adversarial
surveillance-register to Meta, to a startup, and to automakers. The
register tracks the surveillance behavior (non-consensual biometric or
behavioral data collection), not the entity. EXTENDS the falsification
family (#538, #548, #553, #563, #568, #578, #583, #588, #608 is the
mechanism id here not an iteration, #613); this run becomes the 11th
falsification-family member at the iteration level. NOT a pure asymmetry
pin. Distinct from the publication-level nytimes.yaml Hill analysis
(zero-coverage claims there predate the iteration-492 rule; this
journalist-level mechanism makes NO zero-coverage claims, all comparator
arms are positive Hill bylines).

Rotation: Type B follows Type A (#622) per A,B,C,D,E. Rotation guard
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
NYTIMES_PATH = os.path.join(REPO_ROOT, "profiles", "nytimes.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = "type_b_623_kashmir_hill_surveillance_register_constancy"
FILENAME = "test_type_b_623_kashmir_hill_surveillance_register_constancy_sep09_2am.py"

META_TONES = [-0.80]
NON_META_TONES = [-0.85, -0.75]
EXPECTED_DELTA = 0.00

NAMETAG_MIRROR_URL = "https://www.macrumors.com/2026/02/13/meta-facial-recognition-smart-glasses/"
NAMETAG_BYLINE_URL = "https://pxlnv.com/linklog/meta-ray-bans-facial-recognition/"
NAMETAG_BYLINE_URL2 = "https://www.tipranks.com/news/the-fly/meta-planning-to-add-facial-recognition-tech-to-smart-glasses-ny-times-reports-thefly"
CLEARVIEW_WIKI_URL = "https://en.wikipedia.org/wiki/Clearview_AI"
CLEARVIEW_COURT_URL = "https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1:2020cv01296/532050/51/"
AUTOMAKER_ARCHIVE_URL = "https://web.archive.org/web/20240311090514/https://www.nytimes.com/2024/03/11/technology/carmakers-driver-tracking-insurance.html"
AUTOMAKER_IMPACT_URL = "https://www.autoblog.com/2024/03/25/gm-cuts-ties-with-some-third-party-data-brokers-after-nyt-report/"
AUTOMAKER_SENATE_URL = "https://www.fastcompany.com/91175277/general-motors-texas-driver-data-ron-wyden-ed-markey?s=04"


def _journalists():
    with open(JOURNALISTS_PATH) as f:
        return yaml.safe_load(f)


def _hill():
    matches = [j for j in _journalists()["journalists"]
               if j.get("name") == "Kashmir Hill"]
    assert len(matches) == 1, f"expected exactly one Kashmir Hill entry, got {len(matches)}"
    return matches[0]


def _mechanism():
    cc = _hill().get("competitor_coverage", {})
    assert MECH_KEY in cc, f"{MECH_KEY} missing from Kashmir Hill competitor_coverage"
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


class TestIterationMetadata623:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 623

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 608

    def test_mechanism_id_unique_repo_wide(self):
        import glob
        hits = []
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path).read()
            hits.extend(re.findall(r"mechanism_id: 608\b", text))
        assert len(hits) == 1, f"mechanism_id 608 appears {len(hits)} times"

    def test_iteration_type_b(self):
        assert _mechanism()["type"] == "B"

    def test_scheduled_job_id(self):
        assert _mechanism()["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_goal_id(self):
        assert _mechanism()["goal_id"] == "goal_54093bda4145"

    def test_iteration_log_has_623_entry_newest_first(self):
        assert read_log().startswith("#623 Type B:"), (
            "iteration-log.md is not newest-first at #623"
        )

    def test_mechanism_is_first_on_hill_competitor_coverage(self):
        cc = _hill().get("competitor_coverage", {})
        assert list(cc.keys()) == [MECH_KEY], (
            f"Hill competitor_coverage should hold only the #623 block, got {list(cc.keys())}"
        )

    def test_author_attribution(self):
        assert _mechanism()["author"] == "Kit (with Ray)"

    def test_date(self):
        assert _mechanism()["date"] == "2026-09-09 02:00 PDT"


class TestHillArms623:
    def test_meta_arm_nametag(self):
        arm = _mechanism()["meta_arm"]
        assert arm["date"] == "2026-02-13"
        assert "Kashmir Hill" in arm["byline"]
        assert "Kalley Huang" in arm["byline"]
        assert "Mike Isaac" in arm["byline"]
        assert arm["manual_illustrative_tone"] == -0.80
        assert arm["register"] == "adversarial_investigative_expose"

    def test_meta_arm_tone_carried_from_nytimes_yaml(self):
        assert "nytimes.yaml" in _mechanism()["meta_arm"]["tone_provenance"]

    def test_meta_arm_memo_quote(self):
        arm = _mechanism()["meta_arm"]
        assert "dynamic political environment" in arm["key_evidence"]

    def test_meta_arm_urls_verbatim(self):
        urls = _mechanism()["meta_arm"]["source_urls"]
        assert NAMETAG_MIRROR_URL in urls
        assert NAMETAG_BYLINE_URL in urls
        assert NAMETAG_BYLINE_URL2 in urls

    def test_clearview_arm(self):
        arm = [a for a in _mechanism()["comparator_arms"] if a["entity"] == "clearview_ai"][0]
        assert arm["date"] == "2020-01-18"
        assert arm["byline"] == "Kashmir Hill"
        assert arm["manual_illustrative_tone"] == -0.85
        assert arm["register"] == "adversarial_investigative_expose"
        assert "End Privacy as We Know It" in arm["title"]

    def test_clearview_arm_impact(self):
        arm = [a for a in _mechanism()["comparator_arms"] if a["entity"] == "clearview_ai"][0]
        assert "8 federal class actions" in arm["documented_impact"]
        assert "40+" in arm["documented_impact"]

    def test_clearview_arm_urls_verbatim(self):
        arm = [a for a in _mechanism()["comparator_arms"] if a["entity"] == "clearview_ai"][0]
        assert CLEARVIEW_WIKI_URL in arm["source_urls"]
        assert CLEARVIEW_COURT_URL in arm["source_urls"]

    def test_automaker_arm(self):
        arm = [a for a in _mechanism()["comparator_arms"] if a["entity"] == "automakers"][0]
        assert arm["date"] == "2024-03-11"
        assert arm["byline"] == "Kashmir Hill"
        assert arm["manual_illustrative_tone"] == -0.75
        assert arm["register"] == "adversarial_investigative_expose"

    def test_automaker_arm_impact(self):
        arm = [a for a in _mechanism()["comparator_arms"] if a["entity"] == "automakers"][0]
        assert "LexisNexis" in arm["documented_impact"]
        assert "Wyden" in arm["documented_impact"]

    def test_automaker_arm_urls_verbatim(self):
        arm = [a for a in _mechanism()["comparator_arms"] if a["entity"] == "automakers"][0]
        assert AUTOMAKER_ARCHIVE_URL in arm["source_urls"]
        assert AUTOMAKER_IMPACT_URL in arm["source_urls"]
        assert AUTOMAKER_SENATE_URL in arm["source_urls"]

    def test_all_three_arms_same_register(self):
        m = _mechanism()
        registers = {m["meta_arm"]["register"]}
        registers.update(a["register"] for a in m["comparator_arms"])
        assert registers == {"adversarial_investigative_expose"}, (
            f"register split breaks the constancy claim: {registers}"
        )

    def test_comparator_arms_are_positive_bylines(self):
        m = _mechanism()
        for a in m["comparator_arms"]:
            assert "Kashmir Hill" in a["byline"], (
                "comparator arms must be positive Hill bylines per the iteration-492 rule"
            )


class TestScorerConstancy623:
    def test_delta_reproduces_from_pinned_tones(self):
        meta_avg = sum(META_TONES) / len(META_TONES)
        non_meta_avg = sum(NON_META_TONES) / len(NON_META_TONES)
        assert round(meta_avg - non_meta_avg, 2) == EXPECTED_DELTA

    def test_mechanism_delta_matches(self):
        assert _mechanism()["asymmetry_scorer_result_illustrative"]["delta_meta_minus_non_meta"] == 0.00

    def test_delta_calc_string(self):
        calc = _mechanism()["asymmetry_scorer_result_illustrative"]["delta_calc"]
        assert "-0.80" in calc and "0.00" in calc

    def test_no_significance_claims(self):
        s = _mechanism()["asymmetry_scorer_result_illustrative"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["is_significant"] is False

    def test_verdict_is_constancy(self):
        assert _mechanism()["verdict"].startswith("SURVEILLANCE-REGISTER CONSTANCY")

    def test_extends_falsification_family(self):
        verdict = _mechanism()["verdict"]
        for n in ("538", "548", "553", "563", "568", "578", "583", "588", "613"):
            assert f"#{n}" in verdict, f"falsification-family member #{n} missing from verdict"

    def test_not_pure_asymmetry_pin(self):
        assert "NOT a pure asymmetry pin" in _mechanism()["verdict"]

    def test_correlation_not_causation(self):
        s = _mechanism()["asymmetry_scorer_result_illustrative"]
        assert s["correlation_not_causation"] is True

    def test_confounders_ranked(self):
        confs = _mechanism()["confounders_ranked"]
        strengths = [c["strength"] for c in confs]
        assert strengths.count("STRONG") >= 2
        assert "WEAK" in strengths


class TestRotationCycleGuard623:
    """Rotation guard, deselected pre-commit per the #565 followup convention.

    Asserts the post-commit anchor, so it runs green only in the followup
    commit after the main commit SHA is known. Pre-commit it is deselected.
    """

    def _mains(self):
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [s for s in out if re.match(r"^Type [A-E] #\d+:", s)]
        assert len(mains) >= 5
        return mains

    def test_window_619_623_closes_a_to_b(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("B", "623"),
            ("A", "622"),
            ("E", "621"),
            ("D", "620"),
            ("C", "619"),
        ], f"rotation window 619-623 wrong: {observed}"

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
        # Post-commit anchor: the #623 main commit. Patched in the followup
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
        assert sha.startswith("PATCH_IN_FOLLOWUP"), f"anchor drifted: {sha}"
        assert subject.startswith("Type B #623:"), (
            f"post-commit anchor broken: newest main is not #623: {subject!r}"
        )


class TestDocSyncRatchet623:
    def test_readme_has_623_row(self):
        assert re.search(r"#623", read_readme()), "README.md missing the #623 test-table row"

    def test_arch_has_623_row(self):
        assert re.search(r"#623", read_arch()), "docs/ARCHITECTURE.md missing the #623 tree row"

    def test_prior_rows_intact(self):
        readme, arch = read_readme(), read_arch()
        for n in ("618", "619", "620", "621", "622"):
            assert re.search(rf"#{n}", readme), f"README.md lost the #{n} row"
            assert re.search(rf"#{n}", arch), f"docs/ARCHITECTURE.md lost the #{n} row"

    def test_readme_row_test_count_matches(self):
        m = re.search(rf"`{re.escape(FILENAME)}`\s*\|\s*(\d+)\s*\|", read_readme())
        assert m, "README #623 row missing or malformed"
        assert int(m.group(1)) == _count_def_tests(), (
            f"README row says {m.group(1)} but file carries {_count_def_tests()}"
        )

    def test_readme_row_says_623(self):
        line = next(
            (ln for ln in read_readme().splitlines() if FILENAME in ln),
            None,
        )
        assert line is not None, "README missing the #623 row entirely"
        assert "#623" in line, "README #623 row does not reference #623"

    def test_log_starts_with_623(self):
        assert read_log().startswith("#623 Type B:")


class TestNoBrittlePatterns623:
    def test_yaml_reparses_clean(self):
        d = _journalists()
        hill = [j for j in d["journalists"] if j.get("name") == "Kashmir Hill"][0]
        assert hill["competitor_coverage"][MECH_KEY]["mechanism_id"] == 608

    def test_no_em_dash_in_mechanism(self):
        text = yaml.safe_dump(_mechanism(), allow_unicode=True)
        assert "\u2014" not in text, "em dash leaked into the #623 mechanism"

    def test_all_urls_http_or_https(self):
        m = _mechanism()
        urls = list(m["meta_arm"]["source_urls"])
        for a in m["comparator_arms"]:
            urls.extend(a["source_urls"])
        for u in urls:
            assert u.startswith("http"), f"bad URL: {u}"

    def test_no_zero_coverage_claims(self):
        dumped = yaml.safe_dump(_mechanism(), allow_unicode=True).lower()
        assert "zero investigative" not in dumped
        assert "zero coverage" not in dumped
        assert "no hill byline" not in dumped
        assert "has written zero" not in dumped

    def test_no_engine_significance_claims(self):
        dumped = yaml.safe_dump(_mechanism(), allow_unicode=True).lower()
        assert "p_value" in dumped
        assert "significant true" not in dumped

    def test_no_fabricated_nytimes_url(self):
        urls = list(_mechanism()["meta_arm"]["source_urls"])
        for a in _mechanism()["comparator_arms"]:
            urls.extend(a["source_urls"])
        for u in urls:
            assert "nytimes.com/2026/02/13/technology/meta-nametag" not in u, (
                "guessed NYT NameTag URL; must remain absent per verbatim-only rule"
            )

    def test_research_method_names_evidence_tiers(self):
        method = _mechanism()["research_method"]
        assert "policy-blocked" in method
        assert "iteration-492" in method

    def test_artifact_readiness_present(self):
        assert "analysis.json" in _mechanism()["artifact_readiness"]
