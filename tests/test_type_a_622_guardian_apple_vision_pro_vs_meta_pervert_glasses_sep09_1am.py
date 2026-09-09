"""Type A #622: The Guardian x Apple Vision Pro aspirational register vs
Meta pervert-glasses adversarial register.

FIRST dedicated Type A mechanism under guardian.yaml
competitor_relationships.apple (mechanism_id 607, next free pre-commit;
max numeric mechanism_id was 606). Apple arm: Samuel Gibbs Vision Pro
review (Aug 2024, "lives up to the hype", +0.35) plus Guardian reviews
roundup ("stunning potential with big trade-offs", +0.10), both
aspirational/positive-lean with zero surveillance framing of the camera
array. Meta arm: Barbara Speed opinion "Why I'll never be convinced by
Meta's 'pervert' glasses" (Aug 5, 2026, -0.60), adversarial surveillance
register. Illustrative delta (Meta minus Apple) -0.825; p_value, cohens_d
NOT_CALCULATED; is_significant False (Aug 28 standing rule).
Zero-financial-gradient CONTROL: Apple $0, Meta $0, no deal either side, so
the register gap is incident/news-value driven, not money driven.
NOT a falsification-family member.

Rotation: Type A follows Type E (#621) per A,B,C,D,E. Rotation guard
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
GUARDIAN_PATH = os.path.join(REPO_ROOT, "profiles", "guardian.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = "mechanism_607_guardian_apple_vision_pro_aspirational_vs_meta_pervert_glasses"
FILENAME = "test_type_a_622_guardian_apple_vision_pro_vs_meta_pervert_glasses_sep09_1am.py"

APPLE_TONES = [0.35, 0.10]
META_TONES = [-0.60]
EXPECTED_DELTA = -0.825

GIBBS_MIRROR_URL = "http://richardhartley.com/2024/08/vision-pro-review-apples-cutting-edge-headset-lives-up-to-the-hype/"
ROUNDUP_URL = "https://www.theguardian.com/technology/2024/jan/30/apple-vision-pro-reviews-roundup-stunning-potential-with-big-trade-offs"
SHORT_URL = "https://www.youtube.com/shorts/Cb8gV-uNBnM"
BUZZSUMO_URL = "https://buzzsumo.com/journalist/barbara-speed-145324357/"
BIZTOC_URL = "https://biztoc.com/x/84569d50c96ed261"


def _guardian():
    with open(GUARDIAN_PATH) as f:
        return yaml.safe_load(f)


def _entity():
    return _guardian()["competitor_relationships"]["apple"]


def _mechanism():
    return _entity()[MECH_KEY]


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


class TestIterationMetadata622:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 622

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 607

    def test_mechanism_id_unique_repo_wide(self):
        hits = []
        for fname in os.listdir(os.path.join(REPO_ROOT, "profiles")):
            if not fname.endswith(".yaml"):
                continue
            text = open(os.path.join(REPO_ROOT, "profiles", fname)).read()
            hits.extend(re.findall(r"mechanism_id: 607\b", text))
        assert len(hits) == 1, f"mechanism_id 607 appears {len(hits)} times"

    def test_iteration_type_a(self):
        assert _mechanism()["iteration_type"] == "A"

    def test_scheduled_job_id(self):
        assert _mechanism()["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_goal_id(self):
        assert _mechanism()["goal_id"] == "goal_54093bda4145"

    def test_iteration_log_has_622_entry_newest_first(self):
        assert read_log().startswith("#622 Type A:"), (
            "iteration-log.md is not newest-first at #622"
        )

    def test_mechanism_is_first_under_apple_entity(self):
        keys = [k for k in _entity() if k.startswith("mechanism_")]
        assert keys == [MECH_KEY], f"apple entity has unexpected mechanism keys: {keys}"


class TestAppleEntityStructure622:
    def test_apple_entity_exists(self):
        assert "apple" in _guardian()["competitor_relationships"]

    def test_financial_tie_none(self):
        assert _entity()["financial_tie"] == "none"

    def test_estimated_value_zero(self):
        assert _entity()["estimated_value"] == "$0"

    def test_coverage_prediction_neutral_stands(self):
        assert _entity()["coverage_prediction"] == "neutral"
        assert _mechanism()["coverage_prediction_stands"] == "neutral"

    def test_financial_channel_zero_both_sides(self):
        assert _mechanism()["financial_channel"] == "$0 both sides"

    def test_tone_arrays_pinned(self):
        assert _mechanism()["manual_illustrative_tones_meta"] == META_TONES
        assert _mechanism()["manual_illustrative_tones_apple"] == APPLE_TONES

    def test_delta_reproduces_from_pinned_arrays(self):
        meta_avg = sum(META_TONES) / len(META_TONES)
        apple_avg = sum(APPLE_TONES) / len(APPLE_TONES)
        delta = meta_avg - apple_avg
        assert abs(delta - EXPECTED_DELTA) < 1e-9, f"delta drifted: {delta}"
        assert _mechanism()["illustrative_delta_meta_minus_apple"] == EXPECTED_DELTA

    def test_illustrative_discipline_markers(self):
        m = _mechanism()
        assert m["p_value"] == "NOT_CALCULATED"
        assert m["cohens_d"] == "NOT_CALCULATED"
        assert m["is_significant"] is False

    def test_gibbs_article_attribution(self):
        a = _mechanism()["articles_apple"][0]
        assert a["author"] == "Samuel Gibbs"
        assert a["url"] == GIBBS_MIRROR_URL
        assert a["evidence_tier"] == "full_text_mirror"
        assert "The Guardian" in a["attribution_note"]

    def test_roundup_article_url_verbatim_guardian(self):
        a = _mechanism()["articles_apple"][1]
        assert a["url"] == ROUNDUP_URL

    def test_speed_article_attribution(self):
        a = _mechanism()["articles_meta"][0]
        assert a["author"] == "Barbara Speed"
        assert a["date"] == "2026-08-05"
        assert a["url"] == SHORT_URL
        assert BUZZSUMO_URL in a["attribution_note"]
        assert BIZTOC_URL in a["attribution_note"]

    def test_everyone_hates_elon_activist_not_podcast(self):
        m = _mechanism()
        framing = m["articles_meta"][0]["framing"]
        assert "Everyone Hates Elon" in framing
        assert "podcast" not in m["summary"].lower()


class TestConfounders622:
    def test_four_strong_confounders(self):
        strong = _mechanism()["confounders_ranked"]["strong"]
        assert len(strong) == 4

    def test_incident_news_value_strong_first(self):
        strong = _mechanism()["confounders_ranked"]["strong"]
        assert "Incident-driven news value" in strong[0]

    def test_form_factor_skew_ranked(self):
        joined = " ".join(_mechanism()["confounders_ranked"]["strong"])
        assert "Form-factor skew" in joined

    def test_genre_skew_ranked(self):
        joined = " ".join(_mechanism()["confounders_ranked"]["strong"])
        assert "Genre skew" in joined

    def test_timing_skew_ranked(self):
        joined = " ".join(_mechanism()["confounders_ranked"]["strong"])
        assert "Timing skew" in joined

    def test_reporter_skew_moderate(self):
        moderate = _mechanism()["confounders_ranked"]["moderate"]
        assert any("Reporter skew" in c for c in moderate)

    def test_not_falsification_family(self):
        finding = _mechanism()["finding"]
        assert "NOT a falsification-family member" in finding

    def test_zero_gradient_control_named(self):
        assert "Zero-financial-gradient CONTROL" in _mechanism()["finding"]


class TestRotationCycleGuard622:
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

    def test_window_618_622_closes_d_e_to_a(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("A", "622"),
            ("E", "621"),
            ("D", "620"),
            ("C", "619"),
            ("B", "618"),
        ], f"rotation window 618-622 wrong: {observed}"

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["A", "E", "D", "C", "B"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                f"rotation broken: {a} -> {b} is not a valid cycle edge"
            )

    def test_anchor_is_main_patch_in_followup(self):
        # Post-commit anchor: the #622 main commit. Patched in the followup
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
        assert subject.startswith("Type A #622:"), (
            f"post-commit anchor broken: newest main is not #622: {subject!r}"
        )


class TestDocSyncRatchet622:
    def test_readme_has_622_row(self):
        assert re.search(r"#622", read_readme()), "README.md missing the #622 test-table row"

    def test_arch_has_622_row(self):
        assert re.search(r"#622", read_arch()), "docs/ARCHITECTURE.md missing the #622 tree row"

    def test_prior_rows_intact(self):
        readme, arch = read_readme(), read_arch()
        for n in ("617", "618", "619", "620", "621"):
            assert re.search(rf"#{n}", readme), f"README.md lost the #{n} row"
            assert re.search(rf"#{n}", arch), f"docs/ARCHITECTURE.md lost the #{n} row"

    def test_readme_row_test_count_matches(self):
        m = re.search(rf"`{re.escape(FILENAME)}`\s*\|\s*(\d+)\s*\|", read_readme())
        assert m, "README #622 row missing or malformed"
        assert int(m.group(1)) == _count_def_tests(), (
            f"README row says {m.group(1)} but file carries {_count_def_tests()}"
        )

    def test_readme_row_says_622(self):
        line = next(
            (ln for ln in read_readme().splitlines() if FILENAME in ln),
            None,
        )
        assert line is not None, "README missing the #622 row entirely"
        assert "#622" in line, "README #622 row does not reference #622"


class TestNoBrittlePatterns622:
    def test_yaml_reparses_clean(self):
        d = _guardian()
        assert d["competitor_relationships"]["apple"][MECH_KEY]["mechanism_id"] == 607

    def test_no_em_dash_in_mechanism(self):
        text = yaml.safe_dump(_mechanism(), allow_unicode=True)
        assert "\u2014" not in text, "em dash leaked into the #622 mechanism"

    def test_all_urls_http_or_https(self):
        for arm in ("articles_apple", "articles_meta"):
            for a in _mechanism()[arm]:
                if a.get("url"):
                    assert a["url"].startswith("http"), f"bad URL: {a['url']}"

    def test_direct_fetch_disclaimer(self):
        method = _mechanism()["research_method"]
        assert "policy-blocked" in method

    def test_evidence_tiers_bounded(self):
        apple = _mechanism()["articles_apple"]
        meta = _mechanism()["articles_meta"]
        assert apple[0]["evidence_tier"] == "full_text_mirror"
        assert apple[1]["evidence_tier"] == "headline_bounded"
        assert meta[0]["evidence_tier"] == "full_transcript_excerpt_bounded"

    def test_no_fabricated_guardian_url(self):
        urls = [a["url"] for a in _mechanism()["articles_meta"]]
        for u in urls:
            assert "theguardian.com/commentisfree" not in u, (
                "guessed Guardian opinion URL; must remain absent per verbatim-only rule"
            )

    def test_no_engine_significance_claims(self):
        dumped = yaml.safe_dump(_mechanism(), allow_unicode=True).lower()
        assert "p_value" in dumped
        assert "significant true" not in dumped
