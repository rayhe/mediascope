"""Type C #679: Apple News/News+ x Conde Nast revenue-share leg formalization
(Mar 2019 launch; 16+ titles incl WIRED) - the ONLY confirmed closed Apple
payer leg at WIRED's parent.

First dedicated deal-level mechanism on Apple's standing revenue-share leg
at Conde Nast (mechanism 642, next free, max pre-commit 641). Two first-hand
reads this run: TheStreet Nov 24 2025 (Apple News loses a longstanding media
partner, 96 lines; Semafor-via-TheStreet seven-figures-per-year Conde Nast
revenue datum) and Press Gazette 100k Club 2026 (223 lines; Enders Analysis
Jan 20 2026: Apple News+ 1.7M UK subscribers, UK publisher-shared 50 percent
pool approx $136m/yr). Terms: 50/50 subscription split with engagement-time
publisher allocation; publishers keep 100 percent of own ad revenue (Recode
Feb 2019 via 9to5Mac); News Partner Program in-app 85 percent carve-out
(Macworld 2021). Conde Nast posture: CEO Roger Lynch 2019 "jury is out",
inherited deal, no cannibalization observed, retained exit option ("we have
options"). Sep 2026 status ACTIVE per the #599 convention (bounded absence
of exit reporting per the iteration-492 rule). Gradient: Apple-payer PRESENT
at Conde Nast (one confirmed closed leg, modest quantum) vs Meta $0 AI legs
(mechanism 331 bundle excludes Conde Nast); tone-predictor grade WEAK
(engagement-time pool split not coverage-linked; modest quantum; arms-length
posture). No tone scores; qualitative only; correlation not causation.

Research method: 3 browser.search query sets + 2 first-hand browser.open
reads. All URLs verbatim from Full-URL listings; Lynch quotes and
title-set details search-snippet attested where noted. No zero-coverage
claims.

Rotation: Type C follows Type B (#678) per A,B,C,D,E. Rotation guard,
doc-sync, and novelty-anchor classes deselected pre-commit per the #565
followup convention; anchor patched in the followup commit once the main
commit SHA is known.
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

MECH_KEY = "mechanism_642_apple_news_plus_conde_nast_revenue_share_leg"
FILENAME = "test_type_c_679_apple_news_plus_conde_nast_revenue_share_leg_sep11_12pm.py"

THESTREET_URL = "https://www.thestreet.com/latest-news/apple-news-loses-a-longstanding-media-partner"
PRESSGAZETTE_URL = "https://pressgazette.co.uk/paywalls/biggest-subscription-news-websites-2026/"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. The rotation-guard class is deselected pre-commit.
ANCHORED_SHA = "TBD"


def _entities():
    with open(ENTITIES_PATH) as f:
        return yaml.safe_load(f)


def _apple():
    return _entities()["entities"]["apple"]


def _mechanism():
    a = _apple()
    assert MECH_KEY in a, f"{MECH_KEY} missing from entities.apple"
    return a[MECH_KEY]


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


class TestIterationMetadata679:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 679

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 642

    def test_mechanism_id_unique_repo_wide(self):
        # Per the #674 convention: only this run's mechanism_id is asserted
        # unique (legacy ids like 80 have pre-existing corpus collisions).
        seen = []
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                if int(m.group(1)) == 642:
                    seen.append(path)
        assert len(seen) == 1, f"mechanism_id 642 not unique: {seen}"
        assert seen[0].endswith("competitor-entities.yaml")

    def test_rotation_type_c(self):
        assert _mechanism()["rotation"] == "Type C"

    def test_job_and_goal_ids(self):
        m = _mechanism()
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_type_c_focus_names_first_dedicated(self):
        assert "first dedicated deal-level mechanism" in _mechanism()["type_c_focus"]


class TestDealLegFormalization679:
    def test_launch_terms(self):
        m = _mechanism()
        assert m["deal_structure"]["launch"].startswith("Mar 2019")
        assert "50 percent" in m["deal_structure"]["subscription_split"]
        assert "engagement time" in m["deal_structure"]["subscription_split"]

    def test_publisher_ad_revenue_retained(self):
        assert "100 percent" in _mechanism()["deal_structure"]["publisher_ad_revenue"]

    def test_news_partner_program_carveout(self):
        assert "85 percent" in _mechanism()["deal_structure"]["news_partner_program"]

    def test_conde_nast_titles(self):
        presence = _mechanism()["conde_nast_presence"]
        assert "16+" in presence["titles"]
        assert "WIRED" in presence["titles"]

    def test_lynch_posture(self):
        posture = _mechanism()["conde_nast_presence"]["ceo_posture"]
        assert "jury is out" in posture
        assert "we have options" in posture

    def test_seven_figures_datum(self):
        assert "seven figures" in _mechanism()["conde_nast_presence"]["revenue_quantum"]

    def test_scale_2026_quantified(self):
        scale = _mechanism()["scale_2026"]
        assert "1.7 million" in scale["uk_subscribers"]
        assert "$136m" in scale["uk_publisher_pool"]

    def test_status_active(self):
        status = _mechanism()["status_sep_2026"]
        assert status["verdict"] == "ACTIVE"
        assert "CNN" in status["renegotiation_context"]

    def test_gradient_present_meta_zero(self):
        rel = _mechanism()["asymmetry_relevance"]
        assert "PRESENT" in rel["gradient"]
        assert "Meta $0" in rel["gradient"]

    def test_tone_predictor_weak(self):
        rel = _mechanism()["asymmetry_relevance"]
        assert rel["tone_predictor_grade"] == "WEAK"
        assert rel["no_tone_claim"] is True

    def test_six_ranked_confounders(self):
        confs = _mechanism()["confounders_ranked"]
        assert len(confs) == 6
        ranks = [c["rank"] for c in confs]
        assert ranks == [1, 2, 3, 4, 5, 6]
        assert all(c["strength"] in ("strong", "moderate", "weak") for c in confs)

    def test_first_strong_confounders(self):
        confs = {c["rank"]: c for c in _mechanism()["confounders_ranked"]}
        assert confs[1]["strength"] == "strong"
        assert "not coverage-linked" in confs[1]["confounder"]
        assert confs[3]["strength"] == "strong"
        assert "arms-length" in confs[3]["confounder"]


class TestCrossReferences679:
    def test_reversal_phase_block_cited(self):
        xrefs = " ".join(_mechanism()["cross_references"])
        assert "mechanism 574" in xrefs

    def test_quad_channel_cited(self):
        xrefs = " ".join(_mechanism()["cross_references"])
        assert "mechanism 136" in xrefs

    def test_siri_ai_silence_check_cited(self):
        xrefs = " ".join(_mechanism()["cross_references"])
        assert "mechanism 606" in xrefs

    def test_meta_bundle_cited(self):
        xrefs = " ".join(_mechanism()["cross_references"])
        assert "mechanism 331" in xrefs

    def test_ddm_news_plus_leg_cited(self):
        xrefs = " ".join(_mechanism()["cross_references"])
        assert "mechanism 534" in xrefs

    def test_conventions_cited(self):
        xrefs = " ".join(_mechanism()["cross_references"])
        assert "#599" in xrefs
        assert "#492" in xrefs

    def test_distinct_from_574_and_136(self):
        focus = _mechanism()["type_c_focus"]
        assert "Distinct from mechanism 574" in focus
        assert "mechanism 136" in focus


class TestNovelty679:
    def test_single_679_file_on_disk(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_c_679*"))
        assert files == [os.path.join(TESTS_DIR, FILENAME)], files

    def test_no_duplicate_642_mechanism_key(self):
        count = 0
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path).read()
            count += len(re.findall(r"^    mechanism_642_apple_news_plus", text, re.M))
        assert count == 1, f"mechanism_642 key appears {count} times"

    def test_no_prior_dedicated_news_plus_conde_nast_mechanism(self):
        # Prior mentions are portfolio lines (5640/5958), mechanism 136
        # Channel-1 naming, mechanism 534 DDM commingle, and the wired.yaml
        # line-254 estimate. No prior block names an Apple News+ x Conde Nast
        # deal-level mechanism.
        text = open(ENTITIES_PATH).read()
        names = re.findall(r"mechanism_name: '([^']*News\+[^']*)'", text)
        dedicated = [n for n in names if "Conde Nast" in n and "revenue-share" in n]
        assert dedicated == [_mechanism()["mechanism_name"]], dedicated

    def test_siri_ai_still_unsigned_carried(self):
        # The focus carries #619's Siri-AI-unsigned status into the Sep 2026
        # verdict (News+ is the ONLY closed Apple leg because the Siri AI
        # per-use talks remain unsigned).
        assert "unsigned per #619" in _mechanism()["mechanism_name"]


class TestResearchMethod679:
    def test_first_hand_thestreet_source(self):
        assert THESTREET_URL in _mechanism()["sources"]

    def test_first_hand_pressgazette_source(self):
        assert PRESSGAZETTE_URL in _mechanism()["sources"]

    def test_research_method_names_query_sets_and_opens(self):
        rm = _mechanism()["research_method"]
        assert "3 browser.search query sets" in rm
        assert "2 first-hand browser.open reads" in rm
        assert "TheStreet Nov 24 2025" in rm
        assert "Press Gazette 100k Club" in rm

    def test_no_canonical_urls_constructed(self):
        rm = _mechanism()["research_method"]
        assert "verbatim from Full-URL listings" in rm

    def test_bounded_absence_discipline(self):
        rm = _mechanism()["research_method"]
        assert "iteration-492 rule" in rm
        status = _mechanism()["status_sep_2026"]["basis"]
        assert "bounded absence" in status

    def test_precommit_novelty_greps_documented(self):
        rm = _mechanism()["research_method"]
        assert "zero test_type_c_679 files on disk" in rm
        assert "zero mechanism_642 keys repo-wide" in rm

    def test_snippet_attestation_flagged(self):
        rm = _mechanism()["research_method"]
        assert "search-snippet attested" in rm


class TestStatisticalDiscipline679:
    def test_no_scorer_run(self):
        sd = _mechanism()["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["tone_scores"] == "NOT_SCORED"

    def test_qualitative_only(self):
        sd = _mechanism()["statistical_discipline"]
        assert sd["scope"] == "qualitative financial mapping only"
        assert sd["correlation_not_causation"] is True
        assert sd["no_coverage_tone_claim"] is True

    def test_correlational_note_names_weak_grade(self):
        note = _mechanism()["statistical_discipline"]["correlational_note"]
        assert "WEAK" in note

    def test_verification_block(self):
        v = _mechanism()["verification"]
        assert v["yaml_parse_clean"] is True
        assert v["iteration"] == 679
        assert v["type"] == "C"
        assert v["date"] == "2026-09-11 12:00 PDT"


class TestRotationCycleGuard679:
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

    def test_window_675_679_closes_b_to_c(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("C", "679"),
            ("B", "678"),
            ("A", "677"),
            ("E", "676"),
            ("D", "675"),
        ], f"rotation window 675-679 wrong: {observed}"

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
        # Post-commit anchor: the #679 main commit. Patched in the followup
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
        assert subject.startswith("Type C #679:"), (
            f"post-commit anchor broken: newest main is not #679: {subject!r}"
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
        sample = "Type C #679: Apple News/News+ x Conde Nast revenue-share leg"
        for p in guard_patterns:
            m = re.search(p, sample)
            assert m and m.group(1) == "C" and m.group(2) == "679", (
                f"rotation regex {p!r} fails to match a real subject "
                "(double-backslash bug?)"
            )


class TestDocSyncRatchet679:
    def test_readme_has_679_row(self):
        assert "#679" in read_readme()

    def test_arch_has_679_row(self):
        assert "679" in read_arch()

    def test_readme_row_mentions_apple_news_plus(self):
        assert "Apple News+" in read_readme()
        assert "Conde Nast" in read_readme()

    def test_log_starts_with_679(self):
        assert read_log_start().startswith("#679 Type C:")

    def test_def_test_count_matches(self):
        # The README row for #679 must carry this file's own def-test count.
        n = _count_def_tests()
        assert str(n) in read_readme(), (
            f"README #679 row should mention this file's def-test count {n}"
        )


class TestNoBrittlePatterns679:
    def test_yaml_reparses_clean(self):
        m = _mechanism()
        assert isinstance(m["mechanism_id"], int)
        assert isinstance(m["iteration"], int)
        assert isinstance(m["confounders_ranked"], list)

    def test_mechanism_key_naming(self):
        assert MECH_KEY.startswith("mechanism_642_")
        assert MECH_KEY in _apple()

    def test_no_em_dash_or_curly_quotes_in_mechanism(self):
        text = _mechanism_text()
        assert "\u2014" not in text, "em dash found in mechanism block"
        assert "\u2018" not in text and "\u2019" not in text, "curly quote in mechanism block"

    def test_mechanism_text_ascii_only(self):
        text = _mechanism_text()
        bad = [c for c in text if ord(c) > 127]
        assert not bad, f"non-ASCII chars in mechanism block: {set(bad)!r}"

    def test_type_c_679_main_commit_unique_and_anchored(self):
        # Novelty anchor: exactly one "Type C #679:" main commit post-followup
        # (deselected pre-commit per the #565 convention; the followup and
        # doc-sync commits are "Type C #679 followup:" / "Type C #679
        # doc-sync:" and do NOT match the main-commit filter).
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type C #679:", l)]
        assert len(mains) == 1, f"expected exactly one Type C #679 main commit, got {len(mains)}"
        assert mains[0].startswith(ANCHORED_SHA), (
            f"main commit SHA does not match patched anchor: {mains[0][:12]}"
        )
