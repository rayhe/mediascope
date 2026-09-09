"""Type A #617: The Verge x Samsung launch-cycle register gradient.

FIRST dedicated Type A mechanism under the-verge.yaml
competitor_relationships.samsung (mechanism_id 604, next free pre-commit;
max numeric mechanism_id was 603). Three Verge Samsung-side items in the
Mar-Jul 2026 launch cycle (launch-commitment, leak, hands-on) run
product-forward registers with privacy vocabulary confined to dek level,
vs the Meta-side Victoria Song trilogy (Jul 2026) running adversarial
escalation. Manual illustrative delta (target minus peer) -0.70; p_value,
cohens_d, ci_95 NOT_CALCULATED; is_significant False (Aug 28 standing
rule). Prediction-consistent with the advertising-softer hypothesis, but
launch-cycle genre is the STRONG rival explanation; no financial
attribution established. Does NOT join the falsification family.

Rotation: Type A follows Type E (#616) per A,B,C,D,E. Rotation guard
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

MECH_KEY = "mechanism_604_verge_samsung_launch_cycle_register"
FILENAME = "test_type_a_617_verge_samsung_launch_cycle_register_sep08_8pm.py"

SAMSUNG_TONES = [0.15, 0.10, 0.20]
META_TONES = [-0.55, -0.60, -0.50]
EXPECTED_DELTA = -0.70

SAMSUNG_URL_1 = "https://www.theverge.com/tech/890533/samsung-is-still-planning-to-launch-its-first-smart-glasses-in-2026"
SAMSUNG_URL_2 = "https://www.theverge.com/gadgets/919189/samsung-galaxy-glasses-leaked-images"
META_MIRROR_URL = "https://www.aivanet.com/2026/07/with-smart-glasses-meta-holds-all-the-cards-but-fails-to-play-them-well/"


def _verge():
    with open(VERGE_PATH) as f:
        return yaml.safe_load(f)


def _entity():
    return _verge()["competitor_relationships"]["samsung"]


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


class TestIterationMetadata617:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 617

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 604

    def test_mechanism_id_unique_repo_wide(self):
        hits = []
        for fname in os.listdir(os.path.join(REPO_ROOT, "profiles")):
            if not fname.endswith(".yaml"):
                continue
            text = open(os.path.join(REPO_ROOT, "profiles", fname)).read()
            hits.extend(re.findall(r"mechanism_id: 604\b", text))
        assert len(hits) == 1, f"mechanism_id 604 appears {len(hits)} times"

    def test_iteration_type_a(self):
        assert _mechanism()["iteration_type"] == "A"

    def test_scheduled_job_id(self):
        assert _mechanism()["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_goal_id(self):
        assert _mechanism()["goal_id"] == "goal_54093bda4145"

    def test_iteration_log_has_617_entry_newest_first(self):
        log = open(os.path.join(REPO_ROOT, "iteration-log.md")).read()
        assert log.startswith("#617 Type A:"), "iteration-log.md is not newest-first at #617"


class TestSamsungEntityStructure617:
    def test_samsung_entity_exists(self):
        assert "samsung" in _verge()["competitor_relationships"]

    def test_financial_tie_advertising(self):
        assert _entity()["financial_tie"] == "advertising"

    def test_estimated_value_ad_spend(self):
        assert "$9.7B" in _entity()["estimated_value"]

    def test_coverage_prediction_softer(self):
        assert _entity()["coverage_prediction"] == "softer"

    def test_description_notes_no_licensing_deal(self):
        desc = _entity()["description"]
        assert "No direct content licensing deal" in desc

    def test_description_contrasts_meta_zero(self):
        desc = _entity()["description"]
        assert "Q2 2025" in desc
        assert "$0" in desc


class TestSamsungSideArticles617:
    def test_three_samsung_items(self):
        assert len(_mechanism()["samsung_articles"]) == 3

    def test_item1_launch_commitment_url_verbatim(self):
        assert _mechanism()["samsung_articles"][0]["url"] == SAMSUNG_URL_1

    def test_item2_leak_url_verbatim(self):
        assert _mechanism()["samsung_articles"][1]["url"] == SAMSUNG_URL_2

    def test_item1_date_mar2026(self):
        assert _mechanism()["samsung_articles"][0]["date"] == "2026-03"

    def test_item2_date_apr27_2026(self):
        assert _mechanism()["samsung_articles"][1]["date"] == "2026-04-27"

    def test_item3_preston_hands_on_jul22(self):
        item = _mechanism()["samsung_articles"][2]
        assert item["author"] == "Dominic Preston"
        assert item["date"] == "2026-07-22"

    def test_item3_dek_verbatim(self):
        dek = _mechanism()["samsung_articles"][2]["dek_verbatim"]
        assert dek == (
            "With a camera on every pair, Google's and Samsung's AI glasses "
            "face the same privacy problems as Meta's."
        )

    def test_item1_slug_title_flagged(self):
        item = _mechanism()["samsung_articles"][0]
        assert "Slug-derived" in item["title_note"]

    def test_item2_price_bands(self):
        framing = _mechanism()["samsung_articles"][1]["key_framing"]
        assert "$379-$499" in framing
        assert "$600-$900" in framing

    def test_samsung_tones_list(self):
        tones = [a["manual_illustrative_tone"] for a in _mechanism()["samsung_articles"]]
        assert tones == SAMSUNG_TONES

    def test_samsung_avg_tone_0_15(self):
        scorer = _mechanism()["asymmetry_scorer_manual_illustrative"]
        assert abs(scorer["peer_avg_tone"] - 0.15) < 1e-9


class TestMetaComparator617:
    def test_three_meta_items(self):
        assert len(_mechanism()["meta_articles_same_domain"]) == 3

    def test_all_song(self):
        authors = [a["author"] for a in _mechanism()["meta_articles_same_domain"]]
        assert authors == ["Victoria Song"] * 3

    def test_meta_tones_carried_492(self):
        tones = [a["manual_illustrative_tone"] for a in _mechanism()["meta_articles_same_domain"]]
        assert tones == META_TONES

    def test_meta_avg_tone_minus_0_55(self):
        scorer = _mechanism()["asymmetry_scorer_manual_illustrative"]
        assert abs(scorer["target_avg_tone"] - (-0.55)) < 1e-9

    def test_pervert_glasses_editorial_present(self):
        titles = [a["title"] for a in _mechanism()["meta_articles_same_domain"]]
        assert "Leaning into 'pervert glasses' sure is a choice" in titles

    def test_holds_all_cards_mirror_url(self):
        item = _mechanism()["meta_articles_same_domain"][2]
        assert item["url"] == META_MIRROR_URL


class TestIllustrativeScoring617:
    def test_scorer_block_present(self):
        assert "asymmetry_scorer_manual_illustrative" in _mechanism()

    def test_tone_arrays_match_articles(self):
        scorer = _mechanism()["asymmetry_scorer_manual_illustrative"]
        assert scorer["peer_tones"] == SAMSUNG_TONES
        assert scorer["target_tones"] == META_TONES

    def test_delta_arithmetic_target_minus_peer(self):
        scorer = _mechanism()["asymmetry_scorer_manual_illustrative"]
        delta = scorer["target_avg_tone"] - scorer["peer_avg_tone"]
        assert abs(delta - EXPECTED_DELTA) < 1e-9

    def test_delta_logged_matches(self):
        assert abs(_mechanism()["asymmetry_scorer_manual_illustrative"]["delta_manual_illustrative"] - EXPECTED_DELTA) < 1e-9

    def test_window_covers_mar_to_jul(self):
        scorer = _mechanism()["asymmetry_scorer_manual_illustrative"]
        assert scorer["window"] == "2026-03 to 2026-07-26"

    def test_publication_slug_verge(self):
        scorer = _mechanism()["asymmetry_scorer_manual_illustrative"]
        assert scorer["publication_slug"] == "the-verge"


class TestStatisticalDiscipline617:
    def test_p_value_not_calculated(self):
        assert _mechanism()["asymmetry_scorer_manual_illustrative"]["p_value"] == "NOT_CALCULATED"

    def test_cohens_d_not_calculated(self):
        assert _mechanism()["asymmetry_scorer_manual_illustrative"]["cohens_d"] == "NOT_CALCULATED"

    def test_ci_not_calculated(self):
        assert _mechanism()["asymmetry_scorer_manual_illustrative"]["confidence_interval_95"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        assert _mechanism()["asymmetry_scorer_manual_illustrative"]["is_significant"] is False

    def test_manual_illustrative_only_string(self):
        assert "MANUAL ILLUSTRATIVE ONLY" in _mechanism()["statistical_discipline"]

    def test_standing_rule_cited(self):
        assert "Aug 28 2026" in _mechanism()["statistical_discipline"]

    def test_no_zero_coverage_claim(self):
        finding = _mechanism()["finding"]
        discipline = _mechanism()["statistical_discipline"]
        assert "ZERO" not in finding
        assert "zero-coverage" in discipline or "No zero-coverage" in discipline


class TestFinancialTriangulation617:
    def test_ad_channel_consistent_direction(self):
        tri = _mechanism()["financial_triangulation"]
        assert "$9.7B" in tri["samsung_ad_channel"]
        assert "consistent with that prediction" in tri["samsung_ad_channel"]

    def test_meta_zero_channel(self):
        tri = _mechanism()["financial_triangulation"]
        assert "Q2 2025" in tri["meta_zero_channel"]
        assert "$0" in tri["meta_zero_channel"]

    def test_correlation_not_causation(self):
        tri = _mechanism()["financial_triangulation"]
        assert "No financial attribution is" in tri["correlation_not_causation"]

    def test_no_licensing_deal_samsung(self):
        assert "licensing" in _entity()["description"].lower()


class TestConfounders617:
    def test_strong_genre_skew_first(self):
        strong = _mechanism()["confounders_ranked"]["strong"]
        assert "genre" in strong[0].lower() or "Genre" in strong[0]

    def test_launch_cycle_artifact_named(self):
        finding = _mechanism()["finding"]
        assert "launch-cycle" in finding

    def test_timing_skew_ranked(self):
        joined = " ".join(_mechanism()["confounders_ranked"]["strong"])
        assert "Timing skew" in joined

    def test_reporter_skew_ranked_moderate(self):
        moderate = _mechanism()["confounders_ranked"]["moderate"]
        assert any("Reporter skew" in c for c in moderate)

    def test_not_falsification_family(self):
        finding = _mechanism()["finding"]
        assert "does NOT join the falsification" in finding


class TestRotationCycleGuard617:
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

    def test_window_613_617_closes_e_to_a(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("A", "617"),
            ("E", "616"),
            ("D", "615"),
            ("C", "614"),
            ("B", "613"),
        ], f"rotation window 613-617 wrong: {observed}"

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
        # Post-commit anchor: the #617 main commit. Patched in the followup
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
        assert subject.startswith("Type A #617:"), (
            f"post-commit anchor broken: newest main is not #617: {subject!r}"
        )


class TestDocSyncRatchet617:
    def test_readme_has_617_row(self):
        assert re.search(r"#617", read_readme()), "README.md missing the #617 test-table row"

    def test_arch_has_617_row(self):
        assert re.search(r"#617", read_arch()), "docs/ARCHITECTURE.md missing the #617 tree row"

    def test_prior_rows_intact(self):
        readme, arch = read_readme(), read_arch()
        for n in ("612", "613", "614", "615", "616"):
            assert re.search(rf"#{n}", readme), f"README.md lost the #{n} row"
            assert re.search(rf"#{n}", arch), f"docs/ARCHITECTURE.md lost the #{n} row"

    def test_readme_row_test_count_matches(self):
        m = re.search(rf"`{re.escape(FILENAME)}`\s*\|\s*(\d+)\s*\|", read_readme())
        assert m, "README #617 row missing or malformed"
        assert int(m.group(1)) == _count_def_tests(), (
            f"README row says {m.group(1)} but file carries {_count_def_tests()}"
        )


class TestNoBrittlePatterns617:
    def test_yaml_reparses_clean(self):
        d = _verge()
        assert d["competitor_relationships"]["samsung"][MECH_KEY]["mechanism_id"] == 604

    def test_no_em_dash_in_mechanism(self):
        text = yaml.safe_dump(_mechanism(), allow_unicode=True)
        assert "\u2014" not in text, "em dash leaked into the #617 mechanism"

    def test_all_urls_https_or_verbatim_sources(self):
        for a in _mechanism()["samsung_articles"]:
            if a.get("url"):
                assert a["url"].startswith("https://"), f"non-https URL: {a['url']}"

    def test_verge_direct_fetch_disclaimer(self):
        method = _mechanism()["research_method"]
        assert "policy-blocked" in method

    def test_evidence_tiers_bounded(self):
        tiers = [a.get("evidence_tier", "") for a in _mechanism()["samsung_articles"]]
        assert "excerpt_bounded" in tiers[0]
        assert "excerpt_bounded" in tiers[1]
        assert "in_corpus" in tiers[2]
