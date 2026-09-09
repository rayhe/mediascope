"""Type B #628: Samuel Gibbs (Guardian consumer technology editor) within-writer
genre register across entities.

FIRST dedicated Type B mechanism on Samuel Gibbs (mechanism_id 611, next free
pre-commit; max numeric mechanism_id was 610). Within-writer comparison across
two Gibbs bylines on two entity classes:

(a) Meta arm: Sep 17 2025 Guardian launch announcement "Meta announces first
Ray-Ban smart glasses with in-built augmented reality display", neutral-positive
announcement register, tone +0.10 hand-assigned this run (MANUAL ILLUSTRATIVE).
Full text read first-hand via the richardhartley.com full-text mirror
(verbatim URL from search results); theguardian.com direct fetch policy-blocked
per standing rule. Zero privacy-alarm vocabulary; the single evaluative jab
("ill-fated Google Glass") lands on a competitor, not Meta.

(b) Apple arm: Aug 16 2024 Guardian hands-on review "Vision Pro review:
Apple's cutting-edge headset lives up to the hype", aspirational review
register, tone +0.35 carried from #622 at the identical value (no rescoring).
Same mirror domain as the Meta arm (richardhartley.com), so the evidence tier
is symmetric across arms.

Illustrative delta (meta minus apple) = 0.10 - 0.35 = -0.25; p_value,
cohens_d NOT_CALCULATED; is_significant False (Aug 28 standing rule).
VERDICT: WITHIN-WRITER GENRE REGISTER. Gibbs shows no anti-Meta register; the
-0.25 gap is fully explained by the STRONG genre confound (hands-on review is
inherently evaluative, launch announcement inherently neutral-descriptive).
NOT a falsification-family member: Guardian-Apple $0 and Guardian-Meta $0, so
the incentive theory predicts nothing for this pair (same zero-financial-
gradient boundary as #622). NOT a pure asymmetry pin.

Rotation: Type B follows Type A (#627) per A,B,C,D,E. Rotation guard
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

MECH_KEY = "type_b_628_samuel_gibbs_guardian_within_writer_genre_register"
FILENAME = "test_type_b_628_samuel_gibbs_guardian_within_writer_genre_register_sep09_7am.py"

META_TONE = 0.10
APPLE_TONE = 0.35
EXPECTED_DELTA = -0.25

META_MIRROR_URL = "https://www.richardhartley.com/2025/09/meta-announces-first-ray-ban-smart-glasses-with-in-built-augmented-reality-display/"
APPLE_MIRROR_URL = "http://richardhartley.com/2024/08/vision-pro-review-apples-cutting-edge-headset-lives-up-to-the-hype/"
BYLINE_ATTR_URL1 = "https://aspicts.substack.com/p/nvidia-invests-5b-in-intel-china"
BYLINE_ATTR_URL2 = "https://www.iask.ca/news/dc07e04941e6cdcc29771d5371057133/meta-announces-first-ray-ban-smart-glasses-with-in-built-augmented-reality-display"
CAREER_URL = "https://me.sh/profile/samuel-gibbs"


def _journalists():
    with open(JOURNALISTS_PATH) as f:
        return yaml.safe_load(f)


def _gibbs():
    matches = [j for j in _journalists()["journalists"]
               if j.get("name") == "Samuel Gibbs"]
    assert len(matches) == 1, f"expected exactly one Samuel Gibbs entry, got {len(matches)}"
    return matches[0]


def _mechanism():
    cc = _gibbs().get("competitor_coverage", {})
    assert MECH_KEY in cc, f"{MECH_KEY} missing from Samuel Gibbs competitor_coverage"
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


class TestIterationMetadata628:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 628

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 611

    def test_mechanism_id_unique_repo_wide(self):
        import glob
        seen = {}
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                mid = int(m.group(1))
                seen.setdefault(mid, []).append(path)
        assert len(seen[611]) == 1, f"mechanism_id 611 not unique: {seen[611]}"

    def test_iteration_type_b(self):
        assert _mechanism()["type"] == "B"

    def test_scheduled_job_id(self):
        assert _mechanism()["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_goal_id(self):
        assert _mechanism()["goal_id"] == "goal_54093bda4145"

    def test_iteration_log_has_628_entry_newest_first(self):
        assert read_log().startswith("#628 Type B:")

    def test_mechanism_is_first_on_gibbs_competitor_coverage(self):
        cc = _gibbs().get("competitor_coverage", {})
        assert list(cc.keys()) == [MECH_KEY], f"unexpected blocks: {list(cc.keys())}"

    def test_author_attribution(self):
        m = _mechanism()
        assert m["meta_arm"]["author_byline"] == "Samuel Gibbs"
        assert m["apple_arm"]["author_byline"] == "Samuel Gibbs"
        assert m["author"] == "Kit (with Ray)"

    def test_date(self):
        assert _mechanism()["date"] == "2026-09-09 07:00 PDT"


class TestGibbsArms628:
    def test_meta_arm_title(self):
        assert _mechanism()["meta_arm"]["title"] == (
            "Meta announces first Ray-Ban smart glasses with in-built "
            "augmented reality display"
        )

    def test_meta_arm_tone_hand_assigned(self):
        meta = _mechanism()["meta_arm"]
        assert meta["tone_score"] == META_TONE == 0.10
        assert "hand-assigned this run" in meta["tone_basis"]
        assert "MANUAL ILLUSTRATIVE" in meta["tone_basis"]

    def test_meta_arm_mirror_url_verbatim(self):
        assert _mechanism()["meta_arm"]["mirror_url"] == META_MIRROR_URL
        assert META_MIRROR_URL.startswith("https://www.richardhartley.com/2025/09/")

    def test_meta_arm_ill_fated_google_glass_quote(self):
        quotes = _mechanism()["meta_arm"]["key_quotes"]
        jab = [q for q in quotes if "ill-fated Google Glass" in q]
        assert len(jab) == 1, "the evaluative jab must be pinned verbatim"
        assert "Meta" not in jab[0].replace("Meta Ray-Ban Display", ""), (
            "the jab lands on Google Glass, not Meta"
        )

    def test_meta_arm_led_privacy_note_factual(self):
        quotes = _mechanism()["meta_arm"]["key_quotes"]
        led = [q for q in quotes if "LED alerts others" in q]
        assert len(led) == 1
        for alarm in ("creepy", "pervert", "surveillance", "spying", "dystopian"):
            assert alarm not in " ".join(quotes).lower(), (
                f"alarm vocabulary leaked into the Meta arm quotes: {alarm}"
            )

    def test_meta_arm_zero_alarm_vocabulary(self):
        notes = _mechanism()["meta_arm"]["register_notes"]
        assert "Zero privacy-alarm vocabulary" in notes
        assert "Barbara Speed" in notes, "same-publication contrast must name Speed"

    def test_apple_arm_title(self):
        assert "lives up to the hype" in _mechanism()["apple_arm"]["title"]

    def test_apple_arm_tone_carried_from_622(self):
        apple = _mechanism()["apple_arm"]
        assert apple["tone_score"] == APPLE_TONE == 0.35
        assert "carried from #622" in apple["tone_basis"]
        assert "no rescoring" in apple["tone_basis"]

    def test_apple_arm_mirror_url_verbatim(self):
        assert _mechanism()["apple_arm"]["mirror_url"] == APPLE_MIRROR_URL
        assert APPLE_MIRROR_URL.startswith("http://richardhartley.com/2024/08/")

    def test_comparator_arms_are_positive_bylines(self):
        m = _mechanism()
        assert m["meta_arm"]["author_byline"] == "Samuel Gibbs"
        assert m["apple_arm"]["author_byline"] == "Samuel Gibbs"
        assert "both comparator arms are positive Gibbs bylines" in m["design"]


class TestScorerDelta628:
    def test_delta_reproduces_from_pinned_tones(self):
        assert round(META_TONE - APPLE_TONE, 2) == EXPECTED_DELTA

    def test_mechanism_delta_matches(self):
        assert _mechanism()["asymmetry_scorer"]["delta_meta_minus_apple"] == EXPECTED_DELTA

    def test_delta_calc_string(self):
        assert _mechanism()["asymmetry_scorer"]["delta_calc"] == "0.10 - 0.35 = -0.25"

    def test_no_significance_claims(self):
        s = _mechanism()["asymmetry_scorer"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["is_significant"] is False
        assert s["method"].startswith("MANUAL ILLUSTRATIVE")

    def test_verdict_is_genre_register(self):
        assert _mechanism()["verdict"].startswith("WITHIN-WRITER GENRE REGISTER")

    def test_not_falsification_family_member(self):
        assert "NOT a falsification-family member" in _mechanism()["verdict"]

    def test_not_pure_asymmetry_pin(self):
        assert "NOT a pure asymmetry pin" in _mechanism()["verdict"]

    def test_correlation_not_causation(self):
        assert "correlation not causation" in _mechanism()["financial_context"]

    def test_confounders_ranked(self):
        confs = _mechanism()["confounders_ranked"]
        strengths = [c["strength"] for c in confs]
        assert strengths.count("STRONG") == 2
        assert any("Genre skew" in c["text"] for c in confs if c["strength"] == "STRONG")
        assert any("Timing skew" in c["text"] for c in confs if c["strength"] == "STRONG")


class TestRotationCycleGuard628:
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

    def test_window_624_628_closes_a_to_b(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("B", "628"),
            ("A", "627"),
            ("E", "626"),
            ("D", "625"),
            ("C", "624"),
        ], f"rotation window 624-628 wrong: {observed}"

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
        # Post-commit anchor: the #628 main commit. Patched in the followup
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
        assert sha.startswith("6b28cd45cea35149b20c154be3e11a8de10116cc"), f"anchor drifted: {sha}"
        assert subject.startswith("Type B #628:"), (
            f"post-commit anchor broken: newest main is not #628: {subject!r}"
        )


class TestDocSyncRatchet628:
    def test_readme_has_628_row(self):
        assert re.search(r"#628", read_readme()), "README.md missing the #628 test-table row"

    def test_arch_has_628_row(self):
        assert re.search(r"#628", read_arch()), "docs/ARCHITECTURE.md missing the #628 tree row"

    def test_prior_rows_intact(self):
        readme, arch = read_readme(), read_arch()
        for n in ("623", "624", "625", "626", "627"):
            assert re.search(rf"#{n}", readme), f"README.md lost the #{n} row"
            assert re.search(rf"#{n}", arch), f"docs/ARCHITECTURE.md lost the #{n} row"

    def test_readme_row_test_count_matches(self):
        m = re.search(rf"`{re.escape(FILENAME)}`\s*\|\s*(\d+)\s*\|", read_readme())
        assert m, "README #628 row missing or malformed"
        assert int(m.group(1)) == _count_def_tests(), (
            f"README row says {m.group(1)} but file carries {_count_def_tests()}"
        )

    def test_readme_row_says_628(self):
        line = next(
            (ln for ln in read_readme().splitlines() if FILENAME in ln),
            None,
        )
        assert line is not None, "README missing the #628 row entirely"
        assert "#628" in line, "README #628 row does not reference #628"

    def test_log_starts_with_628(self):
        assert read_log().startswith("#628 Type B:")


class TestNoBrittlePatterns628:
    def test_yaml_reparses_clean(self):
        d = _journalists()
        gibbs = [j for j in d["journalists"] if j.get("name") == "Samuel Gibbs"][0]
        assert gibbs["competitor_coverage"][MECH_KEY]["mechanism_id"] == 611

    def test_no_em_dash_in_mechanism(self):
        text = yaml.safe_dump(_mechanism(), allow_unicode=True)
        assert "\u2014" not in text, "em dash leaked into the #628 mechanism"

    def test_all_urls_http_or_https(self):
        m = _mechanism()
        urls = [m["meta_arm"]["mirror_url"], m["apple_arm"]["mirror_url"]]
        urls.extend(m["meta_arm"]["byline_attribution_urls"])
        urls.extend(_gibbs()["source_urls"])
        urls.append(_gibbs()["career"][0]["source_url"])
        for u in urls:
            assert u.startswith("http"), f"bad URL: {u}"

    def test_no_zero_coverage_claims(self):
        dumped = yaml.safe_dump(_mechanism(), allow_unicode=True).lower()
        assert "zero coverage" not in dumped
        assert "no gibbs byline" not in dumped
        assert "has written zero" not in dumped
        assert "never written" not in dumped

    def test_no_engine_significance_claims(self):
        dumped = yaml.safe_dump(_mechanism(), allow_unicode=True).lower()
        assert "p_value" in dumped
        assert "significant true" not in dumped

    def test_research_method_names_evidence_tiers(self):
        method = _mechanism()["research_method"]
        assert "policy-blocked" in method
        assert "iteration-492" in method
        assert "full-text mirror" in method

    def test_artifact_readiness_present(self):
        assert "analysis.json" in _mechanism()["artifact_readiness"]
