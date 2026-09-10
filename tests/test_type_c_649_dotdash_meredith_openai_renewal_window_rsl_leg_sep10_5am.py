"""Type C #649: Dotdash Meredith (People Inc) OpenAI renewal window (Sep 2026
status) - 28 months after the May 7 2024 deal, bounded Sep 2026 searches
surface NO renewal/extension/termination reporting, renewal status UNRESOLVED,
treated ACTIVE per the #599 Vox convention (sixth member of the #609 first-gen
OpenAI publisher renewal cohort) + NEW TO CORPUS Digiday Mar 25 2026 Jon
Roberts keynote (OpenAI/Meta legs multi-year all-you-can-eat, Microsoft PCM
pay-per-use, revenue-lag bound) + NEW TO CORPUS CJR Sep 2026 Really Simple
Licensing backing (Reddit, Yahoo, Medium, People Inc; ASCAP/BMI-model
publisher-side diversification, not a Meta-competitor incentive) + Meta Dec 5
2025 leg stands (Press Gazette tracker) + Anthropic/Perplexity bounded absence
(zero-deal entity set unchanged) + 2 strong / 2 moderate / 1 weak ranked
confounders + Roberts revenue-lag counterevidence.

Extends mechanism 534 (DDM x OpenAI deal structure, iteration 534) and
mechanism 539 (DDM triple-payer architecture, iteration 539) with the first
dedicated DDM OpenAI renewal query set. Qualitative Type C mapping.
tone_scores NOT_SCORED; p_value, cohens_d, ci_95 NOT_CALCULATED (standing rule
Aug 28 2026). Correlational language only; no causal claim; no coverage-tone
claim. BOUNDS the falsification family rather than joining it.

Rotation: Type C follows Type B (#648) per A,B,C,D,E. Rotation guard,
novelty anchor, and doc-sync classes deselected pre-commit per the #565
followup convention; anchor patched in the followup commit once the main
commit SHA is known.
"""

import ast
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

MECH_KEY = "mechanism_624_dotdash_meredith_openai_renewal_window_rsl_leg_sep2026"
FILENAME = "test_type_c_649_dotdash_meredith_openai_renewal_window_rsl_leg_sep10_5am.py"

ANCHORED_SHA = "f1cf194b58e91661d133775dceca1b1f31832d8d"


def _find_all(o, key, hits):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == key:
                hits.append(v)
            _find_all(v, key, hits)
    elif isinstance(o, list):
        for v in o:
            _find_all(v, key, hits)
    return hits


def _mechanism():
    with open(ENTITIES_PATH, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    hits = _find_all(data, MECH_KEY, [])
    assert len(hits) == 1, f"{MECH_KEY} occurs {len(hits)} times (want exactly 1)"
    return hits[0]


def _count_def_tests():
    path = os.path.join(TESTS_DIR, FILENAME)
    tree = ast.parse(open(path).read())
    return sum(
        isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
        and n.name.startswith("test_")
        for n in ast.walk(tree)
    )


def _read(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def _block_text():
    text = _read(ENTITIES_PATH)
    start = text.index("    " + MECH_KEY + ":")
    rest = text[start + len("    " + MECH_KEY + ":"):]
    m = re.search(r"\n    mechanism_\d", rest)
    return rest[: m.start()] if m else rest


class TestIterationMetadata649:
    def test_mechanism_id_624(self):
        assert _mechanism()["mechanism_id"] == 624

    def test_iteration_649(self):
        assert _mechanism()["iteration"] == 649

    def test_type_c(self):
        m = _mechanism()
        assert m["rotation"] == "Type C"
        assert m["type"] == "financial_incentive_mapping"

    def test_date_time_pdt(self):
        m = _mechanism()
        assert m["date_analyzed"] == "2026-09-10"
        assert m["time_pdt"] == "05:00"

    def test_job_and_goal(self):
        m = _mechanism()
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_mechanism_name_mentions_renewal_window(self):
        assert "Renewal Window" in _mechanism()["mechanism_name"]
        assert "No Renewal/Extension/Termination Reporting" in _mechanism()["mechanism_name"]

    def test_mechanism_name_mentions_rsl(self):
        assert "RSL" in _mechanism()["mechanism_name"]


class TestMechanismPlacement624:
    def test_nested_under_entities_openai(self):
        with open(ENTITIES_PATH, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        assert MECH_KEY in data["entities"]["openai"]

    def test_sibling_mechanisms_same_parent(self):
        with open(ENTITIES_PATH, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        parent = data["entities"]["openai"]
        assert "mechanism_534_dotdash_meredith_openai_earliest_lightcap_consumer_review_beat" in parent
        assert "mechanism_539_dotdash_meredith_triple_payer_openai_meta_microsoft_pcm" in parent

    def test_no_em_dash_in_block(self):
        assert "\u2014" not in _block_text(), "em dash found in the mechanism_624 block"

    def test_ascii_quotes_only_in_block(self):
        assert "\u2019" not in _block_text()
        assert "\u201c" not in _block_text()


class TestRenewalWindowMapping:
    def test_announcement_date(self):
        assert _mechanism()["renewal_window"]["announcement_date"] == "2024-05-07"

    def test_elapsed_28_months(self):
        assert _mechanism()["renewal_window"]["elapsed_months"] == 28

    def test_status_unresolved(self):
        assert _mechanism()["renewal_window"]["status"] == "UNRESOLVED"

    def test_active_per_599(self):
        assert "#599" in _mechanism()["renewal_window"]["convention"]
        assert "ACTIVE" in _mechanism()["renewal_window"]["convention"]

    def test_no_dated_expiry(self):
        assert "no dated expiry" in _mechanism()["renewal_window"]["stated_term"]

    def test_cohort_sixth_member(self):
        assert "sixth member of the #609" in _mechanism()["renewal_window"]["cohort_position"]

    def test_first_dedicated_ddm_query_set(self):
        assert "first dedicated DDM renewal query set" in _mechanism()["renewal_window"]["cohort_position"]

    def test_next_observable(self):
        assert "#604" in _mechanism()["renewal_window"]["next_observable"]


class TestPositiveControlAndTracker:
    def test_jul_2026_local_news_control(self):
        pc = _mechanism()["positive_control"]
        assert "Jul 2026" in pc["openai_local_news_renewal"]
        assert "$5M" in pc["openai_local_news_renewal"]

    def test_control_is_informative_not_artifact(self):
        assert "not a non-reporting artifact" in _mechanism()["positive_control"]["openai_local_news_renewal"]

    def test_press_gazette_currency(self):
        assert "Sep 7 2026" in _mechanism()["positive_control"]["press_gazette_tracker"]

    def test_press_gazette_lists_microsoft_and_meta_legs(self):
        tracker = _mechanism()["positive_control"]["press_gazette_tracker"]
        assert "Nov 2025 Microsoft leg" in tracker
        assert "Dec 2025 Meta leg" in tracker

    def test_tracker_is_curation_not_registry(self):
        assert "not an authoritative registry" in _mechanism()["positive_control"]["press_gazette_tracker"]


class TestRobertsConfirmation:
    def test_source_new_to_corpus(self):
        assert "NEW TO CORPUS" in _mechanism()["roberts_confirmation"]["source"]

    def test_source_details(self):
        src = _mechanism()["roberts_confirmation"]["source"]
        assert "Digiday Mar 25 2026" in src
        assert "Jon Roberts" in src
        assert "Vail" in src

    def test_all_you_can_eat_quote(self):
        assert "all you can eat" in _mechanism()["roberts_confirmation"]["openai_meta_all_you_can_eat"]

    def test_multi_year(self):
        assert "multi-year" in _mechanism()["roberts_confirmation"]["openai_meta_all_you_can_eat"]

    def test_full_access_scope(self):
        assert "full access" in _mechanism()["roberts_confirmation"]["openai_meta_all_you_can_eat"]

    def test_microsoft_a_la_carte_contrast(self):
        assert "pay-per-use" in _mechanism()["roberts_confirmation"]["microsoft_a_la_carte"]

    def test_revenue_lag_quote(self):
        assert "not yet a boom in the money" in _mechanism()["roberts_confirmation"]["revenue_lag"]

    def test_implication_corroborates_active(self):
        assert "ACTIVE" in _mechanism()["roberts_confirmation"]["implication"]


class TestRSLLeg:
    def test_rsl_new_to_corpus(self):
        assert "NEW TO CORPUS" in _mechanism()["rsl_leg"]["finding"]

    def test_backers(self):
        finding = _mechanism()["rsl_leg"]["finding"]
        assert "Reddit, Yahoo, and Medium" in finding
        assert "People Inc" in finding

    def test_september_2026(self):
        assert "September 2026" in _mechanism()["rsl_leg"]["finding"]

    def test_ascap_bmi_model(self):
        assert "ASCAP/BMI" in _mechanism()["rsl_leg"]["model"]

    def test_no_committed_ai_company(self):
        assert "no major AI company has committed" in _mechanism()["rsl_leg"]["model"]

    def test_publisher_side_disclosure(self):
        assert "NOT a Meta-competitor incentive" in _mechanism()["rsl_leg"]["disclosure"]

    def test_strategic_signal(self):
        assert "access leverage" in _mechanism()["rsl_leg"]["strategic_signal"]


class TestSweepsAndMetaLeg:
    def test_anthropic_perplexity_bounded_absence(self):
        sweep = _mechanism()["anthropic_perplexity_sweep"]["bounded_absence"]
        assert "no People Inc x Anthropic or x Perplexity" in sweep

    def test_bot_blocking_documented(self):
        assert "ClaudeBot" in _mechanism()["anthropic_perplexity_sweep"]["bounded_absence"]

    def test_zero_deal_set_unchanged(self):
        assert "unchanged this run" in _mechanism()["anthropic_perplexity_sweep"]["note"]

    def test_meta_leg_stands(self):
        meta = _mechanism()["meta_leg_status"]["press_gazette_dec_2025_list"]
        assert "Dec 5 2025" in meta
        assert "People Inc" in meta

    def test_meta_leg_no_renewal_due(self):
        assert "no renewal event due" in _mechanism()["meta_leg_status"]["press_gazette_dec_2025_list"]


class TestConfoundersAndCounterevidence:
    def test_five_confounders(self):
        assert len(_mechanism()["ranked_confounders"]) == 5

    def test_strength_profile(self):
        strengths = [c["strength"] for c in _mechanism()["ranked_confounders"]]
        assert strengths == ["strong", "strong", "moderate", "moderate", "weak"]

    def test_ranks_sequential(self):
        assert [c["rank"] for c in _mechanism()["ranked_confounders"]] == [1, 2, 3, 4, 5]

    def test_strong_confounders(self):
        confs = _mechanism()["ranked_confounders"]
        assert "absence of reporting is not proof" in confs[0]["confounder"]
        assert "not deal text" in confs[1]["confounder"]

    def test_counterargument_revenue_lag_bound(self):
        assert "revenue-lag" in _mechanism()["strongest_counterargument"]

    def test_counterargument_market_power(self):
        assert "market-power" in _mechanism()["strongest_counterargument"]

    def test_counterargument_null_predicts_no_tone(self):
        assert "predicts no tone effect" in _mechanism()["strongest_counterargument"]

    def test_cross_references(self):
        xrefs = " ".join(_mechanism()["cross_references"])
        for token in ("Mechanism 534", "Mechanism 539", "#609", "#599", "#644", "#634", "#604"):
            assert token in xrefs, f"cross-reference {token} missing"

    def test_statistical_discipline(self):
        sd = _mechanism()["statistical_discipline"]
        assert "p_value NOT_CALCULATED" in sd
        assert "is_significant False" in sd
        assert "tone_scores NOT_SCORED" in sd


class TestNovelty649:
    def test_first_ddm_renewal_mapping(self):
        nv = " ".join(_mechanism()["novelty_verification"])
        assert "FIRST corpus renewal-window mapping for the DDM-OpenAI deal" in nv

    def test_roberts_new_to_corpus(self):
        nv = " ".join(_mechanism()["novelty_verification"])
        assert "Digiday Mar 25 2026 Jon Roberts" in nv

    def test_rsl_new_to_corpus(self):
        nv = " ".join(_mechanism()["novelty_verification"])
        assert "Really Simple Licensing backing" in nv

    def test_not_falsification_member(self):
        nv = " ".join(_mechanism()["novelty_verification"])
        assert "NOT a falsification-family member" in nv

    def test_source_urls_count_and_key_urls(self):
        urls = _mechanism()["source_urls"]
        assert len(urls) == 10
        joined = " ".join(urls)
        assert "https://digiday.com/media/people-incs-jon-roberts-on-the-ai-licensing-boom-and-the-revenue-lag/" in joined
        assert "https://www.cjr.org/analysis/reddit-winning-ai-licensing-deals-openai-google-gemini-answers-rsl.php" in joined
        assert "https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/" in joined
        assert "https://llmpulse.ai/blog/ai-content-licensing-deals/" in joined

    def test_urls_verbatim_no_construction(self):
        for u in _mechanism()["source_urls"]:
            assert u.startswith("http"), f"non-verbatim URL form: {u}"


class TestRotationCycleGuard649:
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

    def test_window_645_649_closes_b_to_c(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("C", "649"),
            ("B", "648"),
            ("A", "647"),
            ("E", "646"),
            ("D", "645"),
        ], f"rotation window 645-649 wrong: {observed}"

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
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), "anchor not patched"
        out = subprocess.run(
            ["git", "log", "--format=%H"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        assert ANCHORED_SHA in out, "anchored SHA is not a repo commit"

    def test_main_commit_title_carries_649(self):
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        matches = [ln for ln in out if ln.split(" ", 1)[0] == ANCHORED_SHA]
        assert matches and "#649" in matches[0]


class TestDocSyncRatchet649:
    def _readme(self):
        return _read(README_PATH)

    def _arch(self):
        return _read(ARCH_PATH)

    def test_readme_has_649_row(self):
        assert re.search(r"#649", self._readme()), "README.md missing the #649 test-table row"

    def test_arch_has_649_row(self):
        assert re.search(r"#649", self._arch()), "docs/ARCHITECTURE.md missing the #649 tree row"

    def test_prior_rows_intact(self):
        readme, arch = self._readme(), self._arch()
        for n in ("644", "645", "646", "647", "648"):
            assert re.search(rf"#{n}", readme), f"README.md lost the #{n} row"
            assert re.search(rf"#{n}", arch), f"docs/ARCHITECTURE.md lost the #{n} row"

    def test_readme_row_test_count_matches(self):
        m = re.search(rf"`{re.escape(FILENAME)}`\s*\|\s*(\d+)\s*\|", self._readme())
        assert m, "README #649 row missing or malformed"
        assert int(m.group(1)) == _count_def_tests(), (
            f"README row says {m.group(1)} but file carries {_count_def_tests()}"
        )

    def test_readme_row_says_649(self):
        line = next(
            (ln for ln in self._readme().splitlines() if FILENAME in ln),
            None,
        )
        assert line is not None, "README missing the #649 row entirely"
        assert "#649" in line, "README #649 row does not reference #649"

    def test_log_starts_with_649(self):
        assert _read(LOG_PATH).lstrip().startswith("#649 Type C:")
