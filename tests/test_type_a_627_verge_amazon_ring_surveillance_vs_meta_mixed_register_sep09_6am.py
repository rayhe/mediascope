"""Type A #627: The Verge x Amazon Ring surveillance register vs
Meta mixed product register.

FIRST dedicated Type A mechanism under the-verge.yaml
competitor_relationships.amazon (mechanism_id 610, next free pre-commit;
max numeric mechanism_id was 609). Amazon arm: Jennifer Pattison Tuohy
"Amazon Ring's lost dog ad sparks backlash amid fears of mass surveillance"
(Feb 11, 2026, -0.80, full-text mirror) + "Ring says its new encryption
limits what it can give police" (Aug 26, 2026, -0.60, listing-bounded),
both adversarial surveillance register. Meta arm (framing carried from
#425, tones hand-assigned this run): virtual-writing GA feature-drop
(+0.45, May 14 2026), iterative AI update (+0.20, Jul 27 2026),
expansion-pause deficit (-0.30, Jan 6 2026). Illustrative delta
(Meta minus Amazon) +0.82; p_value, cohens_d, ci_95 NOT_CALCULATED;
is_significant False (Aug 28 standing rule). Zero-financial-gradient
CONTROL: Amazon $0, Meta $0, no deal either side, so the register gap is
event/genre-driven, not money-driven. NOT a falsification-family member.

Rotation: Type A follows Type E (#626) per A,B,C,D,E. Rotation guard
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
VERGE_PATH = os.path.join(REPO_ROOT, "profiles", "the-verge.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = "mechanism_610_verge_amazon_ring_surveillance_vs_meta_mixed_register"
FILENAME = "test_type_a_627_verge_amazon_ring_surveillance_vs_meta_mixed_register_sep09_6am.py"

AMAZON_TONES = [-0.80, -0.60]
META_TONES = [0.45, 0.20, -0.30]
EXPECTED_DELTA = 0.8167

SEARCH_PARTY_WRAPPER_URL = "https://www.dejavu.org/cgi-bin/get.cgi?ver=95&url=https%3A%2F%2Fwww.theverge.com%2Ftech%2F876866%2Fring-search-party-super-bowl-ad-online-backlash"
META_URLS = [
    "https://www.theverge.com/tech/930941/meta-ray-ban-display-virtual-neural-handwriting-apps-developer",
    "https://www.theverge.com/tech/971604/metas-ray-ban-display-glasses-get-an-ai-update",
    "https://www.theverge.com/news/856216/meta-ray-ban-display-smart-glasses-international-expansion-paused",
]


def _verge():
    with open(VERGE_PATH) as f:
        return yaml.safe_load(f)


def _entity():
    return _verge()["competitor_relationships"]["amazon"]


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


class TestIterationMetadata627:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 627

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 610

    def test_mechanism_id_unique_repo_wide(self):
        hits = []
        for fname in os.listdir(os.path.join(REPO_ROOT, "profiles")):
            if not fname.endswith(".yaml"):
                continue
            text = open(os.path.join(REPO_ROOT, "profiles", fname)).read()
            hits.extend(re.findall(r"mechanism_id: 610\b", text))
        assert len(hits) == 1, f"mechanism_id 610 appears {len(hits)} times"

    def test_iteration_type_a(self):
        assert _mechanism()["iteration_type"] == "A"

    def test_scheduled_job_id(self):
        assert _mechanism()["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_goal_id(self):
        assert _mechanism()["goal_id"] == "goal_54093bda4145"

    def test_iteration_log_has_627_entry_newest_first(self):
        assert read_log().startswith("#627 Type A:"), (
            "iteration-log.md is not newest-first at #627"
        )

    def test_mechanism_is_first_under_amazon_entity(self):
        keys = [k for k in _entity() if k.startswith("mechanism_")]
        assert keys == [MECH_KEY], f"amazon entity has unexpected mechanism keys: {keys}"


class TestAmazonEntityStructure627:
    def test_amazon_entity_exists(self):
        assert "amazon" in _verge()["competitor_relationships"]

    def test_financial_tie_none(self):
        assert _entity()["financial_tie"] == "none"

    def test_estimated_value_zero(self):
        assert _entity()["estimated_value"] == "$0"

    def test_coverage_prediction_neutral(self):
        assert _entity()["coverage_prediction"] == "neutral"

    def test_tone_arrays_pinned(self):
        scorer = _mechanism()["asymmetry_scorer_manual_illustrative"]
        assert scorer["target_tones"] == META_TONES
        assert scorer["peer_tones"] == AMAZON_TONES
        assert scorer["target_entity"] == "meta"
        assert scorer["peer_entities"] == ["amazon"]

    def test_delta_reproduces_from_pinned_arrays(self):
        meta_avg = sum(META_TONES) / len(META_TONES)
        amazon_avg = sum(AMAZON_TONES) / len(AMAZON_TONES)
        delta = meta_avg - amazon_avg
        assert abs(delta - EXPECTED_DELTA) < 1e-3, f"delta drifted: {delta}"
        assert abs(_mechanism()["asymmetry_scorer_manual_illustrative"]["delta_manual_illustrative"] - EXPECTED_DELTA) < 1e-9

    def test_illustrative_discipline_markers(self):
        scorer = _mechanism()["asymmetry_scorer_manual_illustrative"]
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["confidence_interval_95"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False
        assert "MANUAL ILLUSTRATIVE ONLY" in scorer["scorer"]

    def test_search_party_article_attribution(self):
        a = _mechanism()["amazon_articles"][0]
        assert a["author"] == "Jennifer Pattison Tuohy"
        assert a["date"] == "2026-02-11"
        assert a["url"] == SEARCH_PARTY_WRAPPER_URL
        assert a["evidence_tier"] == "full_text_mirror"
        assert a["manual_illustrative_tone"] == -0.80

    def test_encryption_article_listing_bounded(self):
        a = _mechanism()["amazon_articles"][1]
        assert a["author"] == "Jennifer Pattison Tuohy"
        assert a["date"] == "2026-08-26"
        assert a.get("url") in (None, ""), "listing-bounded article must not carry a URL"
        assert a["evidence_tier"] == "listing_bounded"
        assert a["manual_illustrative_tone"] == -0.60

    def test_meta_articles_verbatim_urls(self):
        urls = [a["url"] for a in _mechanism()["meta_articles_same_domain"]]
        assert urls == META_URLS

    def test_no_constructed_verge_canonical_url(self):
        dumped = yaml.safe_dump(_mechanism(), allow_unicode=True)
        assert "https://www.theverge.com/tech/876866" not in dumped, (
            "decoded canonical Verge URL constructed; only the verbatim wrapper URL is allowed"
        )


class TestConfounders627:
    def test_strong_confounders(self):
        strong = _mechanism()["confounders_ranked"]["strong"]
        assert len(strong) == 2

    def test_event_genre_skew_strong_first(self):
        strong = _mechanism()["confounders_ranked"]["strong"]
        assert "Event-genre skew" in strong[0]

    def test_reporter_skew_strong(self):
        strong = _mechanism()["confounders_ranked"]["strong"]
        assert "Reporter skew" in strong[1]

    def test_moderate_and_weak_confounders(self):
        ranked = _mechanism()["confounders_ranked"]
        assert len(ranked["moderate"]) == 2
        assert len(ranked["weak"]) == 2

    def test_not_falsification_family(self):
        finding = _mechanism()["finding"]
        assert "NOT a falsification-family member" in finding

    def test_zero_gradient_control_named(self):
        assert "zero-financial-gradient CONTROL" in _mechanism()["finding"]


class TestRotationCycleGuard627:
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

    def test_window_623_627_closes_e_d_c_b_to_a(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("A", "627"),
            ("E", "626"),
            ("D", "625"),
            ("C", "624"),
            ("B", "623"),
        ], f"rotation window 623-627 wrong: {observed}"

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

    def test_anchor_is_main_bad4573(self):
        # Post-commit anchor: the #627 main commit. Patched in the followup
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
        assert sha.startswith("bad4573"), f"anchor drifted: {sha}"
        assert subject.startswith("Type A #627:"), (
            f"post-commit anchor broken: newest main is not #627: {subject!r}"
        )


class TestDocSyncRatchet627:
    def test_readme_has_627_row(self):
        assert re.search(r"#627", read_readme()), "README.md missing the #627 test-table row"

    def test_arch_has_627_row(self):
        assert re.search(r"#627", read_arch()), "docs/ARCHITECTURE.md missing the #627 tree row"

    def test_prior_rows_intact(self):
        readme, arch = read_readme(), read_arch()
        for n in ("622", "623", "624", "625", "626"):
            assert re.search(rf"#{n}", readme), f"README.md lost the #{n} row"
            assert re.search(rf"#{n}", arch), f"docs/ARCHITECTURE.md lost the #{n} row"

    def test_readme_row_test_count_matches(self):
        m = re.search(rf"`{re.escape(FILENAME)}`\s*\|\s*(\d+)\s*\|", read_readme())
        assert m, "README #627 row missing or malformed"
        assert int(m.group(1)) == _count_def_tests(), (
            f"README row says {m.group(1)} but file carries {_count_def_tests()}"
        )

    def test_readme_row_says_627(self):
        line = next(
            (ln for ln in read_readme().splitlines() if FILENAME in ln),
            None,
        )
        assert line is not None, "README missing the #627 row entirely"
        assert "#627" in line, "README #627 row does not reference #627"


class TestNoBrittlePatterns627:
    def test_yaml_reparses_clean(self):
        d = _verge()
        assert d["competitor_relationships"]["amazon"][MECH_KEY]["mechanism_id"] == 610

    def test_no_em_dash_in_mechanism(self):
        text = yaml.safe_dump(_mechanism(), allow_unicode=True)
        assert "\u2014" not in text, "em dash leaked into the #627 mechanism"

    def test_all_urls_http_or_https(self):
        for arm in ("amazon_articles", "meta_articles_same_domain"):
            for a in _mechanism()[arm]:
                if a.get("url"):
                    assert a["url"].startswith("http"), f"bad URL: {a['url']}"

    def test_direct_fetch_disclaimer(self):
        method = _mechanism()["research_method"]
        assert "policy-blocked" in method

    def test_evidence_tiers_bounded(self):
        amazon = _mechanism()["amazon_articles"]
        meta = _mechanism()["meta_articles_same_domain"]
        assert amazon[0]["evidence_tier"] == "full_text_mirror"
        assert amazon[1]["evidence_tier"] == "listing_bounded"
        assert all(a["evidence_tier"] == "framing_carried_tone_hand_assigned" for a in meta)

    def test_no_engine_significance_claims(self):
        dumped = yaml.safe_dump(_mechanism(), allow_unicode=True).lower()
        assert "p_value" in dumped
        assert "significant true" not in dumped
