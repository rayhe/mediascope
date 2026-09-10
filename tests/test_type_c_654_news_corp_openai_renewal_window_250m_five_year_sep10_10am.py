"""Type C #654: News Corp (Dow Jones) x OpenAI renewal window (Sep 2026 status)
- 28 months after the May 22 2024 $250M/5yr deal, bounded Sep 2026 searches
surface NO renewal/extension/renegotiation/termination reporting; renewal
status treated ACTIVE per the #599 convention, AFFIRMATIVELY CONFIRMED by CEO
Robert Thomson on the Q4 FY2026 call (Aug 5 2026): "We have trusted content
relationships with OpenAI and Meta, and are in advanced discussions with
several other companies" (Reuters; WSJ/Bruell self-report). SEVENTH and final
major member of the #609 first-gen OpenAI publisher renewal cohort (after FT,
Atlantic, Conde Nast via #609; Time via #639; Vox via #644; Dotdash Meredith
via #649). Press Gazette tracker (crawled 19h before this run) independently
re-confirms the in-corpus DDM $16M/yr datum (mechanism 534 Adweek), cross-source
corroboration of the cohort payout scale ($50M/yr News Corp vs $16M/yr DDM).
Meta Mar 2026 leg stands (up to $50M/yr, 6 months in); Anthropic/Perplexity
bounded absence; zero-deal entity set unchanged.

Extends mechanism 519 (News Corp x OpenAI deal structure) and mechanism 594
(News Corp five-leg AI revenue architecture, which never mapped renewal status)
with the first dedicated News Corp OpenAI renewal query set. Qualitative Type C
mapping. tone_scores NOT_SCORED; p_value, cohens_d, ci_95 NOT_CALCULATED
(standing rule Aug 28 2026). Correlational language only; no causal claim; no
coverage-tone claim. BOUNDS the falsification family rather than joining it.

Rotation: Type C follows Type B (#653) per A,B,C,D,E. Rotation guard,
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

MECH_KEY = "mechanism_627_news_corp_openai_renewal_window_250m_five_year_sep2026"
FILENAME = "test_type_c_654_news_corp_openai_renewal_window_250m_five_year_sep10_10am.py"

ANCHORED_SHA = "ad0974f146f3151988eb70777604a079997daa99"


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


class TestIterationMetadata654:
    def test_mechanism_id_627(self):
        assert _mechanism()["mechanism_id"] == 627

    def test_iteration_654(self):
        assert _mechanism()["iteration"] == 654

    def test_type_c(self):
        m = _mechanism()
        assert m["rotation"] == "Type C"
        assert m["type"] == "financial_incentive_mapping"

    def test_date_time_pdt(self):
        m = _mechanism()
        assert m["date_analyzed"] == "2026-09-10"
        assert m["time_pdt"] == "10:00"

    def test_job_and_goal(self):
        m = _mechanism()
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_mechanism_name_mentions_news_corp(self):
        assert "News Corp" in _mechanism()["mechanism_name"]

    def test_mechanism_name_mentions_renewal_window(self):
        assert "Renewal Window" in _mechanism()["mechanism_name"]

    def test_mechanism_name_mentions_seventh(self):
        assert "Seventh Member" in _mechanism()["mechanism_name"]

    def test_mechanism_name_mentions_250m_five_year(self):
        assert "$250M/5yr" in _mechanism()["mechanism_name"]


class TestMechanismPlacement627:
    def test_nested_under_entities_openai(self):
        with open(ENTITIES_PATH, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        assert MECH_KEY in data["entities"]["openai"]

    def test_sibling_mechanisms_same_parent(self):
        with open(ENTITIES_PATH, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        parent = data["entities"]["openai"]
        assert "mechanism_519_newscorp_openai_dual_payer_woo_and_sue" in parent
        assert "mechanism_624_dotdash_meredith_openai_renewal_window_rsl_leg_sep2026" in parent

    def test_no_em_dash_in_block(self):
        assert "\u2014" not in _block_text(), "em dash found in the mechanism_627 block"

    def test_ascii_quotes_only_in_block(self):
        assert "\u2019" not in _block_text()
        assert "\u201c" not in _block_text()


class TestDealStructureAndWindow:
    def test_announcement_date(self):
        assert _mechanism()["deal_structure"]["announced"].startswith("2024-05-22")

    def test_value_250m_five_years(self):
        value = _mechanism()["deal_structure"]["value"]
        assert "$250M over five years" in value
        assert "never officially disclosed" in value

    def test_cash_plus_credits(self):
        value = _mechanism()["deal_structure"]["value"]
        assert "cash and credits" in value
        assert "Bloomberg Law" in value

    def test_content_scope_covers_wsj_group(self):
        scope = _mechanism()["deal_structure"]["content_scope"]
        for masthead in ("WSJ", "New York Post", "Barron", "Times", "Sun"):
            assert masthead in scope, f"masthead {masthead} missing from scope"

    def test_elapsed_28_months(self):
        assert _mechanism()["deal_structure"]["elapsed_months"] == 28

    def test_expiry_estimate_may_2029(self):
        assert "May 2029" in _mechanism()["deal_structure"]["expiry_estimate"]

    def test_renewal_not_due(self):
        assert _mechanism()["deal_structure"]["renewal_due"] is False

    def test_status_active(self):
        assert _mechanism()["status"] == "ACTIVE"

    def test_active_convention_599(self):
        conv = _mechanism()["status_convention"]
        assert "#599" in conv
        assert "ACTIVE" in conv


class TestRenewalQuerySets:
    def test_four_query_sets(self):
        assert len(_mechanism()["renewal_window_query_sets"]) == 4

    def test_query_set_1_no_renewal_reporting(self):
        result = _mechanism()["renewal_window_query_sets"][0]["result"]
        assert "NO renewal/extension/renegotiation/termination reporting" in result

    def test_query_set_1_only_announcement_resurfaces(self):
        result = _mechanism()["renewal_window_query_sets"][0]["result"]
        assert "May 2024 announcement re-surfaces" in result

    def test_query_set_2_litigation_noise_not_renewal(self):
        result = _mechanism()["renewal_window_query_sets"][1]["result"]
        assert "NO News Corp-OpenAI renewal items" in result
        assert "litigation noise" in result

    def test_query_set_3_press_gazette_no_renewal_note(self):
        result = _mechanism()["renewal_window_query_sets"][2]["result"]
        assert "no renewal note" in result
        assert "22 May 2024" in result

    def test_query_set_4_thomson_q4_fy2026_confirmation(self):
        result = _mechanism()["renewal_window_query_sets"][3]["result"]
        assert "Q4 FY2026" in result
        assert "trusted content relationships with OpenAI and Meta" in result

    def test_query_set_4_advanced_discussions_watch_item(self):
        result = _mechanism()["renewal_window_query_sets"][3]["result"]
        assert "advanced discussions" in result
        assert "no new signed deal announced" in result

    def test_thomson_affirmative_confirmation_quote(self):
        conf = _mechanism()["affirmative_confirmation"]
        assert "trusted content relationships with OpenAI and Meta" in conf
        assert "Aug 5 2026" in conf

    def test_confirmation_extends_aug15_test(self):
        conf = _mechanism()["affirmative_confirmation"]
        assert "Aug 15 Type C test" in conf


class TestCohortMembership:
    def test_seventh_member(self):
        assert "SEVENTH member of the #609" in _mechanism()["cohort_membership"]

    def test_prior_members_listed(self):
        cohort = _mechanism()["cohort_membership"]
        for token in ("#609", "#639", "#644", "#649"):
            assert token in cohort, f"cohort token {token} missing"

    def test_ap_separate_elapsed_term_case(self):
        assert "mechanism 615" in _mechanism()["cohort_membership"]

    def test_axel_springer_dated_expiry(self):
        cohort = _mechanism()["cohort_membership"]
        assert "mechanism 597" in cohort
        assert "#604" in cohort

    def test_last_unmapped_major_leg(self):
        assert "last unmapped major first-gen publisher leg" in _mechanism()["cohort_membership"]

    def test_first_dedicated_news_corp_query_set(self):
        nv = " ".join(_mechanism()["novelty_verification"])
        assert "FIRST corpus dedicated renewal-window mapping for the News Corp x OpenAI deal" in nv


class TestPositiveControls:
    def test_jul_2026_local_news_control(self):
        pcs = " ".join(_mechanism()["positive_controls"])
        assert "Jul 2026 local-news $5M OpenAI renewal" in pcs

    def test_control_is_informative(self):
        pcs = " ".join(_mechanism()["positive_controls"])
        assert "renewals get covered" in pcs

    def test_news_corp_specific_control_meta_leg(self):
        pcs = " ".join(_mechanism()["positive_controls"])
        assert "Mar 2026 Meta leg was WSJ self-reported" in pcs

    def test_control_names_bruell(self):
        pcs = " ".join(_mechanism()["positive_controls"])
        assert "Alexandra Bruell" in pcs
        assert "mechanism 549" in pcs

    def test_renewal_event_would_surface(self):
        pcs = " ".join(_mechanism()["positive_controls"])
        assert "would likewise surface" in pcs


class TestPressGazetteCorroboration:
    def test_tracker_crawled_19h(self):
        assert "crawled 19h before this run" in _mechanism()["press_gazette_corroboration"]

    def test_ddm_16m_update_quoted(self):
        pg = _mechanism()["press_gazette_corroboration"]
        assert "at least $16m per year to Dotdash Meredith" in pg

    def test_corroborates_in_corpus_adweek_datum(self):
        pg = _mechanism()["press_gazette_corroboration"]
        assert "Adweek Nov 2024" in pg
        assert "mechanism 534 fixed_payment_reported" in pg

    def test_payout_scale_contrast(self):
        pg = _mechanism()["press_gazette_corroboration"]
        assert "$50M/yr News Corp vs $16M/yr DDM" in pg

    def test_cross_source_corroboration_not_novel_claim(self):
        pg = _mechanism()["press_gazette_corroboration"]
        assert "cross-source corroboration" in pg


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
        assert "expected, not surprising" in confs[0]["confounder"]
        assert "never officially disclosed" in confs[1]["confounder"]

    def test_moderate_confounders(self):
        confs = _mechanism()["ranked_confounders"]
        assert "news judgment" in confs[2]["confounder"]
        assert "not deal text" in confs[3]["confounder"]

    def test_counterargument_dual_payer_stack(self):
        assert "dual-payer template" in _mechanism()["strongest_counterargument"]

    def test_counterargument_combined_stack(self):
        assert "$100M/yr stack" in _mechanism()["strongest_counterargument"]

    def test_counterargument_tumbler_ridge_against_prediction(self):
        assert "Tumbler Ridge -0.55" in _mechanism()["strongest_counterargument"]

    def test_cross_references(self):
        xrefs = " ".join(_mechanism()["cross_references"])
        for token in ("Mechanism 519", "Mechanism 594", "#609", "#599", "#649", "#644", "#639", "#604", "Mechanism 616", "Mechanism 549"):
            assert token in xrefs, f"cross-reference {token} missing"

    def test_statistical_discipline(self):
        sd = _mechanism()["statistical_discipline"]
        assert "p_value NOT_CALCULATED" in sd
        assert "is_significant False" in sd
        assert "tone_scores NOT_SCORED" in sd


class TestNovelty654:
    def test_first_news_corp_renewal_mapping(self):
        nv = " ".join(_mechanism()["novelty_verification"])
        assert "FIRST corpus dedicated renewal-window mapping for the News Corp x OpenAI deal" in nv

    def test_seventh_cohort_member(self):
        nv = " ".join(_mechanism()["novelty_verification"])
        assert "SEVENTH and final major member of the #609 first-gen cohort" in nv

    def test_zero_627_keys_precommit(self):
        nv = " ".join(_mechanism()["novelty_verification"])
        assert "Zero mechanism_627 keys repo-wide pre-commit" in nv

    def test_zero_test_type_c_654_files(self):
        nv = " ".join(_mechanism()["novelty_verification"])
        assert "Zero test_type_c_654 files on disk pre-commit" in nv

    def test_not_falsification_member(self):
        nv = " ".join(_mechanism()["novelty_verification"])
        assert "NOT a falsification-family member" in nv

    def test_source_urls_count_and_key_urls(self):
        urls = _mechanism()["source_urls"]
        assert len(urls) == 10
        joined = " ".join(urls)
        assert "https://www.thewrap.com/news-corp-openai-multi-year-licensing-deal/" in joined
        assert "https://www.theregister.com/2024/05/23/openai_news_corp/?td=rt-9cs" in joined
        assert "https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/" in joined
        assert "https://www.reuters.com/business/media-telecom/wsj-publisher-news-corp-beats-revenue-estimates-real-estate-dow-jones-strength-2026-08-05/" in joined
        assert "https://www.wsj.com/business/media/news-corp-revenue-rises-with-growth-across-all-segments-d5313004" in joined

    def test_urls_verbatim_no_construction(self):
        for u in _mechanism()["source_urls"]:
            assert u.startswith("http"), f"non-verbatim URL form: {u}"

    def test_meta_leg_and_anthropic_sweep(self):
        m = _mechanism()
        assert "mechanism 549" in m["meta_leg_status"]
        assert "mechanism 539" in m["anthropic_perplexity_sweep"]


class TestRotationCycleGuard654:
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

    def test_window_650_654_closes_b_to_c(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("C", "654"),
            ("B", "653"),
            ("A", "652"),
            ("E", "651"),
            ("D", "650"),
        ], f"rotation window 650-654 wrong: {observed}"

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
        # Post-commit anchor: the #654 main commit. Patched in the followup
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
        assert subject.startswith("Type C #654:"), (
            f"post-commit anchor broken: newest main is not #654: {subject!r}"
        )

    def test_rotation_guard_regex_actually_matches(self):
        # #632 process note: a rotation guard whose regex never matches is a
        # silent no-op. Verify the guard regexes match a real main-commit
        # subject. Written as a semantic check so the test cannot defeat
        # itself by containing the literal pattern.
        src = open(os.path.join(TESTS_DIR, FILENAME)).read()
        patterns = re.findall(r're\.search\(r"([^"]+)"', src)
        guard_patterns = [p for p in patterns if p.startswith("Type (")]
        assert guard_patterns, "no rotation-guard regex found in this file"
        sample = "Type C #654: News Corp OpenAI renewal window"
        for p in guard_patterns:
            assert re.search(p, sample), f"guard pattern {p!r} fails on sample"


class TestDocSyncRatchet654:
    def _readme(self):
        return _read(README_PATH)

    def _arch(self):
        return _read(ARCH_PATH)

    def test_readme_has_654_row(self):
        assert re.search(r"#654", self._readme()), "README.md missing the #654 test-table row"

    def test_arch_has_654_row(self):
        assert re.search(r"#654", self._arch()), "docs/ARCHITECTURE.md missing the #654 tree row"

    def test_prior_rows_intact(self):
        readme, arch = self._readme(), self._arch()
        for n in ("649", "650", "652", "653"):
            assert re.search(rf"#{n}", readme), f"README.md lost the #{n} row"
        for n in ("649", "650", "652", "653"):
            assert re.search(rf"#{n}", arch), f"docs/ARCHITECTURE.md lost the #{n} row"

    def test_readme_row_test_count_matches(self):
        m = re.search(rf"`{re.escape(FILENAME)}`\s*\|\s*(\d+)\s*\|", self._readme())
        assert m, "README #654 row missing or malformed"
        assert int(m.group(1)) == _count_def_tests(), (
            f"README row says {m.group(1)} but file carries {_count_def_tests()}"
        )

    def test_readme_row_says_654(self):
        line = next(
            (ln for ln in self._readme().splitlines() if FILENAME in ln),
            None,
        )
        assert line is not None, "README missing the #654 row entirely"
        assert "#654" in line, "README #654 row does not reference #654"

    def test_log_starts_with_654(self):
        assert _read(LOG_PATH).lstrip().startswith("#654 Type C:")
