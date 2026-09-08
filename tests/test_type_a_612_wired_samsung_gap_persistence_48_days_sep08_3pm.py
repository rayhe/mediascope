"""
Type A #612 - Competitor Coverage Deep Dive: WIRED x Samsung Galaxy Glasses
selection-gap persistence check at 48 days - Sep 8 2026 15:00 PDT

Extends mechanism 374 (hardware_parity_table_aug29, 38-day gap as of Aug 29)
to 48 days (Jul 22 to Sep 8 2026). Bounded search-engine verification with
the identical query as the Aug 29 check (site:wired.com Samsung Galaxy
Glasses) returns no WIRED standalone article this run, the same result as
Aug 29. The site operator is unsupported by this engine, so the claim is a
search-index-bounded absence per the iteration-492 rule, never a
corpus-proven zero. The Boone Ashworth Aug 2 category-headline piece carries
the single known WIRED in-passing mention (mechanism 89); it is not a
standalone article and does not close the gap.

Product newsworthiness is intact: fall 2026 shipping window active, fresh
third-party corroboration (martincid.com crawl 7h ago, TechTimes Unpacked
piece crawl 18h ago, Wikipedia updated 15 days ago, Android Police Jul 23
hands-on), quoting 12MP Sony IMX681 with autofocus (a capability Meta
Ray-Ban fixed-focus lacks) and 379 to 499 USD pricing matching the Meta
Ray-Ban Gen 2 bracket. The old-news defense does not apply. In the same
window the Meta privacy-framing cycle continued in peer publications (The
Times Sep 7 2026 London street-test, pervert glasses framing, 7M sold 2025
figure, autumn Snap and Google entries named).

MANUAL ILLUSTRATIVE, NOT empirical (standing rule Aug 28 2026).
Carried illustrative arms from mechanism 374: Meta [-0.72, -0.82, -0.78,
-0.65, -0.7], Samsung [0.1, 0.08, 0.05, 0.12, 0.07]. Current venv engine on
these synthetic arrays: welch t=-25.34, p=1.04e-06; cohens_d=-16.03.
Finding layer refuses: p_value/cohens_d/ci_95 NOT_CALCULATED,
is_significant False. The engine-side significance on synthetic inputs vs
the finding-layer refusal is the standing engine/finding divergence, not an
oversight. NOT a falsification-family member: this is a selection-gap
persistence extension in the mechanism 39/42/89/374 lineage.

608-612 rotation-cycle guard closing E->A (anchor patched in followup per
the #565 convention). No em dashes anywhere in this file.
"""
import glob
import os
import re
import subprocess

import pytest
import yaml

from mediascope.score.statistical import welch_t_test, cohens_d

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIRED_PATH = os.path.join(REPO_ROOT, "profiles", "wired.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")

MECH_KEY = "gap_persistence_48_day_check_sep08_612"
FILENAME = "test_type_a_612_wired_samsung_gap_persistence_48_days_sep08_3pm.py"
META_TONES = [-0.72, -0.82, -0.78, -0.65, -0.7]
SAMSUNG_TONES = [0.1, 0.08, 0.05, 0.12, 0.07]
GAP_DAYS = 48
GAP_START = "2026-07-22"
ENGINE_T = -25.340748822079505
ENGINE_P = 1.0386087222857895e-06
ENGINE_D = -16.02689677840004

MARTINCID_URL = "https://www.martincid.com/technology-sv/samsung-android-xr-glasses-warby-parker-gentle-monster-2/"
TECHTIMES_URL = "https://Www.techtimes.com/articles/321249/20260722/samsung-galaxy-unpacked-2026-two-folds-titanium-fix-first-ai-glasses.htm"
WIKI_URL = "https://en.wikipedia.org/wiki/Samsung_Galaxy_Glasses"
ANDROIDPOLICE_URL = "https://www.androidpolice.com/hands-on-with-samsungs-ray-ban-meta-rival-smartglasses/"
TIMES_URL = "https://www.thetimes.com/uk/technology-uk/article/meta-glasses-rayban-privacy-recording-ai-0l82sx8sw"


def _wired():
    with open(WIRED_PATH) as f:
        return yaml.safe_load(f)


def _mechanism():
    return _wired()["competitor_relationships"]["samsung"][MECH_KEY]


def read_readme():
    with open(README_PATH) as f:
        return f.read()


def read_arch():
    with open(ARCH_PATH) as f:
        return f.read()


def _count_def_tests():
    import ast
    path = os.path.join(REPO_ROOT, "tests", FILENAME)
    tree = ast.parse(open(path).read())
    return sum(
        isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
        and n.name.startswith("test_")
        for n in ast.walk(tree)
    )


class TestIterationMetadata612:
    def test_mechanism_id_is_601_next_free_numeric(self):
        assert _mechanism()["mechanism_id"] == 601

    def test_iteration_number_is_612(self):
        assert _mechanism()["iteration"] == 612

    def test_iteration_type_is_a(self):
        assert _mechanism()["iteration_type"] == "A"

    def test_publication_focus_is_wired(self):
        assert _mechanism()["publication_focus"] == "WIRED"

    def test_entity_pair_samsung_vs_meta(self):
        assert _mechanism()["entity_pair"] == "Samsung vs Meta"

    def test_iteration_time_is_15_00_pdt(self):
        assert _mechanism()["iteration_time"] == "2026-09-08 15:00 PDT"

    def test_scheduled_job_id(self):
        assert _mechanism()["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_goal_id(self):
        assert _mechanism()["goal_id"] == "goal_54093bda4145"


class TestGapPersistence612:
    def test_gap_days_is_48(self):
        assert _mechanism()["gap_days"] == GAP_DAYS

    def test_gap_start_jul_22(self):
        assert _mechanism()["gap_start"] == GAP_START

    def test_gap_check_date_sep_08(self):
        assert _mechanism()["gap_check_date"] == "2026-09-08"

    def test_prior_check_38_days_mechanism_374(self):
        assert _mechanism()["prior_check"] == "2026-08-29 (38 days, mechanism 374)"

    def test_gap_extended_38_to_48_days(self):
        assert _mechanism()["gap_days"] - 38 == 10

    def test_search_verification_names_bounded_engine(self):
        sv = _mechanism()["search_verification_sep08"]
        assert "site:wired.com Samsung Galaxy Glasses" in sv
        assert "No results found" in sv
        assert "search-index-bounded absence" in sv

    def test_search_verification_disclaims_site_operator(self):
        assert "site operator is unsupported" in _mechanism()["search_verification_sep08"]

    def test_ashworth_mention_is_in_passing_not_standalone(self):
        known = _mechanism()["known_wired_mention"]
        assert "Ashworth" in known
        assert "mechanism 89" in known
        assert "not a standalone article" in known

    def test_finding_states_bounded_absence(self):
        assert "search-index-bounded" in _mechanism()["finding"]

    def test_finding_rejects_old_news_defense(self):
        assert "old-news defense does not apply" in _mechanism()["finding"]

    def test_finding_correlation_not_causation(self):
        assert "Correlation is not causation" in _mechanism()["finding"]

    def test_not_falsification_family_member(self):
        assert "NOT a falsification-family member" in __doc__
        assert "mechanism 39/42/89/374 lineage" in __doc__


class TestPeerCoverage612:
    def _peers(self):
        return _mechanism()["peer_coverage_freshness"]

    def test_four_peer_surfaces(self):
        assert len(self._peers()) == 4

    def test_martincid_url_verbatim(self):
        urls = [p["url"] for p in self._peers()]
        assert MARTINCID_URL in urls

    def test_techtimes_url_verbatim_with_capital_w(self):
        urls = [p["url"] for p in self._peers()]
        assert TECHTIMES_URL in urls

    def test_wikipedia_url_verbatim(self):
        urls = [p["url"] for p in self._peers()]
        assert WIKI_URL in urls

    def test_android_police_url_verbatim(self):
        urls = [p["url"] for p in self._peers()]
        assert ANDROIDPOLICE_URL in urls

    def test_all_peer_urls_http(self):
        for p in self._peers():
            assert p["url"].startswith("http"), f"non-http peer URL: {p['url']!r}"

    def test_all_peer_urls_have_verbatim_source_note(self):
        for p in self._peers():
            assert "verbatim Full-URL listing" in p["url_source"], (
                f"peer missing verbatim source note: {p['source']}"
            )

    def test_techtimes_key_detail_autofocus_advantage(self):
        tt = next(p for p in self._peers() if p["source"] == "techtimes.com")
        assert "autofocus" in tt["key_detail"]
        assert "Meta Ray-Ban fixed-focus lacks" in tt["key_detail"]

    def test_freshness_notes_present(self):
        notes = " ".join(
            str(p.get("crawl_note", "")) + str(p.get("updated", "")) for p in self._peers()
        )
        assert "7h ago" in notes
        assert "18h ago" in notes
        assert "15 days ago" in notes

    def test_meta_cycle_comparator_times_sep_07(self):
        assert TIMES_URL == _mechanism()["meta_cycle_url"]
        assert "pervert glasses" in _mechanism()["meta_cycle_comparator"]
        assert "7M sold 2025" in _mechanism()["meta_cycle_comparator"]

    def test_meta_cycle_url_source_verbatim(self):
        assert "verbatim Full-URL listing" in _mechanism()["meta_cycle_url_source"]


class TestScorerReproduction612:
    def test_method_manual_illustrative(self):
        assert _mechanism()["asymmetry_scorer_result"]["method"] == "manual_illustrative"

    def test_p_value_not_calculated(self):
        assert _mechanism()["asymmetry_scorer_result"]["p_value"] == "NOT_CALCULATED"

    def test_cohens_d_not_calculated(self):
        assert _mechanism()["asymmetry_scorer_result"]["cohens_d"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        assert _mechanism()["asymmetry_scorer_result"]["is_significant"] is False

    def test_carried_arms_match_374(self):
        arms = _mechanism()["carried_illustrative_arms"]
        assert arms["meta_tones"] == META_TONES
        assert arms["samsung_tones"] == SAMSUNG_TONES

    def test_carried_arms_marked_synthetic(self):
        assert "NOT empirical" in _mechanism()["carried_illustrative_arms"]["note"]

    def test_engine_welch_reproduces_t(self):
        t, p = welch_t_test(META_TONES, SAMSUNG_TONES)
        assert round(t, 2) == round(ENGINE_T, 2)

    def test_engine_welch_reproduces_p(self):
        t, p = welch_t_test(META_TONES, SAMSUNG_TONES)
        assert abs(p - ENGINE_P) / ENGINE_P < 1e-6

    def test_engine_cohens_d_reproduces(self):
        d = cohens_d(META_TONES, SAMSUNG_TONES)
        assert round(d, 2) == round(ENGINE_D, 2)

    def test_engine_drift_check_names_current_values(self):
        note = _mechanism()["asymmetry_scorer_result"]["engine_drift_check"]
        assert "-25.340748822079505" in note
        assert "-16.02689677840004" in note
        assert "Aug 29 YAML-recorded -9.14" in note

    def test_statistical_discipline_standing_rule(self):
        disc = _mechanism()["asymmetry_scorer_result"]["statistical_discipline"]
        assert "Aug 28 2026 standing rule" in disc
        assert "correlation_not_causation" in disc
        assert "iteration-492 rule" in disc

    def test_cross_references_39_42_89_374(self):
        assert _mechanism()["cross_references"] == [39, 42, 89, 374]

    def test_discovery_summary_extends_374(self):
        assert "38 days (mechanism 374, Aug 29) to 48 days (Sep 8)" in (
            _mechanism()["discovery_summary"]
        )

    def test_research_method_names_iteration_492(self):
        assert "iteration-492 rule" in _mechanism()["research_method"]

    def test_legitimate_factors_four(self):
        assert len(_mechanism()["legitimate_factors"]) == 4

    def test_strong_confounder_market_share(self):
        strong = [
            f for f in _mechanism()["legitimate_factors"] if f["strength"] == "strong"
        ]
        assert len(strong) == 1
        assert "70 percent" in strong[0]["factor"]


class TestNoBrittlePatterns612:
    def test_exactly_one_612_file(self):
        files = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_a_612_*.py"))
        assert len(files) == 1

    def test_no_duplicate_mechanism_601_keys(self):
        count = 0
        for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for fn in files:
                if fn.endswith(".yaml"):
                    with open(os.path.join(root, fn)) as f:
                        count += f.read().count(MECH_KEY)
        assert count == 1, f"mechanism key appears {count} times"

    def test_no_em_dash_in_mechanism(self):
        import yaml as _yaml
        assert "\u2014" not in _yaml.safe_dump(_mechanism())

    def test_no_em_dash_in_test_file(self):
        with open(os.path.join(REPO_ROOT, "tests", FILENAME)) as f:
            assert "\u2014" not in f.read()

    def test_no_absolute_zero_coverage_claim(self):
        assert "no zero-coverage claims" in _mechanism()["research_method"]

    def test_own_corpus_commits_rejected_circular(self):
        assert "rejected as circular" in _mechanism()["research_method"]

    def test_peer_urls_verbatim_not_constructed(self):
        import json
        blob = json.dumps(_mechanism()["peer_coverage_freshness"])
        for url in (MARTINCID_URL, TECHTIMES_URL, WIKI_URL, ANDROIDPOLICE_URL):
            assert url in blob


class TestRotationCycleGuard612:
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

    def test_window_608_612_closes_e_to_a(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("A", "612"),
            ("E", "611"),
            ("D", "610"),
            ("C", "609"),
            ("B", "608"),
        ], f"rotation window 608-612 wrong: {observed}"

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

    def test_anchor_is_main_a9378e3(self):
        # Post-commit anchor: the #612 main commit. Patched in the followup
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
        assert sha.startswith("a9378e3"), f"anchor drifted: {sha}"
        assert subject.startswith("Type A #612:"), (
            f"post-commit anchor broken: newest main is not #612: {subject!r}"
        )


class TestDocSyncRatchet612:
    def test_readme_row_for_612(self):
        readme = read_readme()
        assert re.search(r"#612", readme), "README.md missing the #612 test-table row"

    def test_arch_row_for_612(self):
        arch = read_arch()
        assert re.search(r"#612", arch), "docs/ARCHITECTURE.md missing the #612 tree row"

    def test_611_row_survives_in_readme(self):
        readme = read_readme()
        assert re.search(r"#611", readme), "README.md lost the #611 row"

    def test_611_row_survives_in_arch(self):
        arch = read_arch()
        assert re.search(r"#611", arch), "docs/ARCHITECTURE.md lost the #611 row"

    def test_readme_row_carries_correct_test_count(self):
        readme = read_readme()
        m = re.search(
            r"`" + re.escape(FILENAME) + r"` \| (\d+)",
            readme,
        )
        assert m, "README #612 row missing or malformed"
        assert int(m.group(1)) == _count_def_tests(), (
            f"README row says {m.group(1)} but file carries {_count_def_tests()}"
        )
