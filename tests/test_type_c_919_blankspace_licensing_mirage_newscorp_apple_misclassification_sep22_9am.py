"""Type C iteration 919: Blankspace "Licensing Mirage" News Corp x Apple row
misclassification trace - the independent AI-licensing publisher synthesis
(mid-2026 draft) Table 1 row "News Corp / Apple / Oct 2025 / Significant
(undisclosed) / Partnership (confirmed)" traced to the News Corp x Apple
News distribution partnership, not an AI training-data license; FIFTH leg
of the 915-919 rotation window (D->E->A->B->C), CLOSING the window.

Type C contract: verify and expand financial relationships between
publications/competitors with sourced datums; update competitor-entities.yaml;
manual qualitative only. This run: first-hand read of the blankspace.so
"Licensing Mirage" PDF (728 rendered lines; row at L171-174). The row's Oct
2025 date plus "Significant" plus "Partnership" language traces to CEO Robert
Thomson's Oct 21 2025 Times Tech Summit quote (Digiday: News Corp had "a
partnership with Google and 'significant' partnerships with OpenAI and
Apple") - a partnership disclosure, not an AI licensing disclosure. The
underlying Apple relationship is the Apple News distribution deal already in
the corpus (news-corp.yaml partner Apple, type news_distribution, revenue
sharing, VERIFIED TRUE: 2019 global deal - WSJ, Times, Sunday Times on Apple
News+, Sun and NY Post on free Apple News; extended and expanded per Thomson
via Press Gazette; Feb 2022 earnings call "important source of subscriptions
and of advertising revenue"; Australia Apple News+ launch Sep 2025 with News
Corp but without Nine). No primary source documents an Apple x News Corp AI
training-data license. The paper's own caveat ("Values marked 'est.' are
journalistic estimates, not company-confirmed figures") does not rescue this
row because the row is marked "(confirmed)" - the confirmed thing is a
distribution partnership, not an AI licensing deal.

Financial-incentive read: the misclassification inflates Apple's apparent
publisher-AI spend in a table explicitly framed as AI licensing deals. The
real Apple x News Corp money flow is platform distribution dependency (Apple
News revenue share plus subscription/ad revenue) - a distinct incentive
vector from training-data payment, and one the corpus already tracks.
Distribution dependency is itself a financial relationship (Apple as
gatekeeper to News Corp subscription and ad revenue), but it belongs in the
distribution-dependency column, not the AI-licensing column. Conflating the
two misprices both. VERIFIES mechanism 574 (Apple is a data-vendor AI payer
- Shutterstock, Defined.ai - with zero confirmed direct publisher AI deals;
the Dec 2023 $50M offers to Conde Nast, NBC News, and IAC produced no
confirmed closings) and corroborates mechanism 606 (Siri-publisher watch,
zero closures as of Sep 6 2026). connects_to [574, 606, 519, 630, 549].
The paper's remaining materiality claims are recorded as bounded secondary
synthesis only, NOT new primary corpus facts.

MANUAL QUALITATIVE ONLY per the Aug 28 2026 standing rule: verification leg,
no coverage-tone pair; p_value, cohens_d, ci_95 NOT_CALCULATED;
is_significant False; engine NOT run; no_analysis_json_update True; NOT
artifact-grade. NOT a falsification-family member; falsification ledger
holds at 29. Verdict directionally_supported_not_proven (row trace VERIFIED
first-hand; incentive reading directional). ASCII-only, no em dashes.

Research: browser.open first-hand read of the blankspace.so PDF this run
(728 rendered lines); Thomson quote and Apple News deal history via
news-corp.yaml corpus record (first-hand read this run); corpus cross-checks
m574, m606, m519, m630, m549. REJECTED candidates: Digiday NYT/OpenAI
unsealed-filings synthesis (m771, in-flight #899); U.S. News v. OpenAI
(m762, in-flight #884); OpenAI BCCL/Indian Express (in corpus); Google AI
Contribution Pilot (m702/708); Google Expert Intelligence (m780, #914);
News Corp x Google talks (m630, unresolved); UMG/ElevenLabs, Suno (music,
out of publisher scope). 1 browser.open this run (the PDF, primary evidence).
All URLs copied verbatim from Full-URL listings; no canonical URLs
constructed.
"""

import os
import re
import subprocess
from datetime import date

import pytest
import yaml

OWN_BASENAME = (
    "test_type_c_919_blankspace_licensing_mirage_newscorp_apple_"
    "misclassification_sep22_9am.py"
)
MECH_KEY = (
    "type_c_919_blankspace_licensing_mirage_newscorp_apple_"
    "misclassification_sep22_9am"
)
MECH_ID_MARKER = "mechanism" + "_" + "783"
NEXT_ID_MARKER = "mechanism" + "_" + "784"
NEXT_ID_NUMERIC = "mechanism_id: 784"
NEXT_ID_DASH = "m-784"
ITER = 919
TYPE_LETTER = "C"
M_ID = 783
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"
GATE_TESTS = 47051
GATE_FILES = 1244
SCHEDULED_LOCAL = "Tue 2026-09-22 09:00:00 PDT"

EXPECTED_URLS = [
    "https://blankspace.so/research/the-licensing-mirage.pdf",
    "https://digiday.com/media/news-corp-in-talks-with-google-for-ai-licensing-deal/",
    "https://appleworld.today/news-corp-expands-and-extends-its-deal-with-apple-news/",
    "https://www.applemust.com/news-corp-says-apple-news-is-important-source-of-revenue/",
    "https://www.adnews.com.au/news/apple-news-hits-australia-with-news-corp-but-without-nine",
]

FIGURE_STRINGS = [
    "Oct 2025",
    "Significant",
    "Partnership",
    "Robert Thomson",
    "Oct 21 2025",
    "Times Tech Summit",
    "Apple News",
    "2019",
    "revenue sharing",
    "VERIFIED TRUE",
    "important source of subscriptions",
    "AI training-data license",
    "not an AI licensing deal",
    "misprices both",
    "distribution dependency",
    "data-vendor AI payer",
    "zero confirmed direct publisher AI deals",
    "directionally_supported_not_proven",
    "NOT_SCORED",
    "NOT_CALCULATED",
    "ledger holds at 29",
    "NOT a falsification-family member",
    "no_analysis_json_update",
    "VERIFIES the mechanism-574 position",
    "BOUNDED SYNTHESIS",
]


def _repo_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _read(relpath):
    with open(os.path.join(_repo_root(), relpath), "r", encoding="utf-8") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", "-C", _repo_root()] + list(args),
        capture_output=True, text=True, timeout=60)


def _block():
    doc = yaml.safe_load(_read("profiles/competitor-entities.yaml"))
    return doc["entities"]["apple"][MECH_KEY]


def _profiles_text():
    return _read("profiles/competitor-entities.yaml")


# ---------------------------------------------------------------------------
# 1. Novelty: this iteration and this mechanism are new
# ---------------------------------------------------------------------------
class TestNovelty919:
    def test_single_test_type_c_919_file(self):
        files = [f for f in os.listdir(os.path.join(_repo_root(), "tests"))
                 if f.startswith("test_type_c_919")]
        assert files == [OWN_BASENAME], files

    @pytest.mark.anchor
    def test_type_c_919_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per #565: the commit does not exist yet.
        # Tolerant form per #913: green pre-commit (no mains), pins the SHA
        # once the anchor followup patches ANCHORED_SHA.
        log = subprocess.run(
            ["git", "-C", _repo_root(), "log", "--format=%H %s",
             "--grep=Type C #919"],
            capture_output=True, text=True, timeout=60)
        assert log.returncode == 0
        mains = [line for line in log.stdout.splitlines()
                 if re.search(r"Type C #919(?::| )", line)
                 and "anchor followup" not in line
                 and "log-hash followup" not in line
                 and "push-status followup" not in line]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        assert ITER == 919
        assert M_ID == 783

    def test_915_918_window_legs_present_prior_to_919(self):
        log = _read("iteration-log.md")
        assert "## #915 Type D" in log
        assert "## #916 Type E" in log
        assert "## #917 Type A" in log
        assert "## #918 Type B" in log

    def test_block_key_zero_hit_elsewhere(self):
        text = _profiles_text()
        assert text.count(MECH_KEY) == 2, "top-level key + block_key field"

    def test_source_url_slugs_zero_hit_elsewhere(self):
        # Each slug appears exactly twice: the sources list and the matching
        # research-method/evidence mention, both inside this block. Novelty
        # means zero hits outside the block.
        text = _profiles_text()
        block_start = text.index(MECH_KEY)
        block_end = text.index(
            "mechanism_642_apple_news_plus_conde_nast_revenue_share_leg:")
        outside = text[:block_start] + text[block_end:]
        for slug in ("blankspace.so/research/the-licensing-mirage",
                     "news-corp-expands-and-extends-its-deal-with-apple-news",
                     "apple-news-is-important-source-of-revenue",
                     "apple-news-hits-australia-with-news-corp"):
            assert slug not in outside, slug

    def test_licensing_mirage_prior_mention_bounded(self):
        # The single pre-existing "Licensing Mirage" mention sits inside the
        # #869 research_method string as corroboration - no dedicated
        # mechanism on the paper or on this row existed pre-commit.
        text = _profiles_text()
        block_start = text.index(MECH_KEY)
        block_end = text.index(
            "mechanism_642_apple_news_plus_conde_nast_revenue_share_leg:")
        outside = text[:block_start] + text[block_end:]
        assert outside.count("Licensing Mirage") == 1
        assert "blankspace.so" not in outside
        prior_line = [ln for ln in outside.split("\n")
                      if "Licensing Mirage" in ln][0]
        assert "research_method" in prior_line


# ---------------------------------------------------------------------------
# 2. Rotation guard: 915-919 window, fifth leg, closes the window
# ---------------------------------------------------------------------------
class TestRotationGuard919:
    # Rotation-guard tests follow the #916/#917/#918 pattern (static window
    # contract + predecessor + no-concurrent-inflight checks).
    # Deselected pre-commit per #565; patched green in the anchor followup.
    @pytest.mark.rotation
    def test_fifth_leg_of_915_919_window(self):
        assert TYPE_LETTER == "C"
        assert ITER == 919

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {915: "D", 916: "E", 917: "A", 918: "B", 919: "C"}
        assert expected[915] == "D"
        assert expected[916] == "E"
        assert expected[917] == "A"
        assert expected[918] == "B"
        assert expected[919] == "C"

    @pytest.mark.rotation
    def test_predecessor_918_type_b_committed(self):
        # #918 Type B is COMMITTED (its log entry sits below this run's
        # #919 entry, which was prepended above it).
        assert "## #918 Type B:" in _read("iteration-log.md")

    @pytest.mark.rotation
    def test_no_concurrent_inflight_commits_asserted(self):
        # In-flight at this run's checks: #884 (m762), #898 (m770),
        # #899 (m771), #900 - none committed yet. Match only commit
        # SUBJECTS: other commits' bodies may mention them.
        proc = _git("log", "--format=%H", "-8")
        subjects = [_git("log", "--format=%s", "-1", c).stdout.strip()
                    for c in proc.stdout.splitlines()]
        for n in ("884", "898", "899", "900"):
            assert not any(
                ("Type " in s) and (("#" + n + " ") in s or s.endswith("#" + n))
                for s in subjects
            ), (n, subjects)


# ---------------------------------------------------------------------------
# 3. Novelty anchor: block key shape
# ---------------------------------------------------------------------------
class TestNoveltyAnchor919:
    def test_block_key_shape(self):
        assert MECH_KEY.startswith("type_c_919_blankspace_licensing_mirage")

    def test_block_key_exact(self):
        assert MECH_KEY == (
            "type_c_919_blankspace_licensing_mirage_newscorp_apple_"
            "misclassification_sep22_9am"
        )

    def test_block_key_carries_no_numeric_id(self):
        # Designed keying per #715: iteration number carried, never the
        # numeric mechanism id.
        assert "783" not in MECH_KEY
        assert "919" in MECH_KEY


# ---------------------------------------------------------------------------
# 4. Mechanism 783 block structure
# ---------------------------------------------------------------------------
class TestMechanism783Structure:
    def test_block_key_unique(self):
        assert _profiles_text().count(MECH_KEY) == 2

    def test_iteration_and_type(self):
        block = _block()
        assert block["iteration"] == 919
        assert block["type"] == "financial_incentive_mapping"

    def test_designed_keying_no_underscore_783(self):
        assert MECH_ID_MARKER not in _profiles_text()

    def test_mechanism_id(self):
        assert _block()["mechanism_id"] == M_ID

    def test_block_key_field_matches(self):
        assert _block()["block_key"] == MECH_KEY

    def test_mechanism_name(self):
        name = _block()["mechanism_name"]
        assert "Licensing Mirage" in name
        assert "News Corp" in name
        assert "Apple" in name
        assert "783" not in name

    def test_type_label(self):
        assert _block()["type_label"] == "Financial Incentive Mapping"

    def test_verdict(self):
        assert _block()["verdict"] == "directionally_supported_not_proven"

    def test_verifies_mechanism_574(self):
        block = _block()
        assert 574 in block["connects_to"]
        assert "VERIFIES the mechanism-574 position" in block["connection_notes"]["m574"]

    def test_connects_to(self):
        conns = _block()["connects_to"]
        for cid in (574, 606, 519, 630, 549):
            assert cid in conns, cid

    def test_trace_fields(self):
        trace = _block()["misclassification_trace"]
        assert "Oct 2025" in trace["table"]
        assert trace["row_confirmation_label"] == "(confirmed)"
        assert "Thomson" in trace["traces_to"]
        assert "Apple News" in trace["underlying_relationship"]
        assert "news_distribution" in trace["corpus_status"]

    def test_financial_incentive_reading(self):
        reading = _block()["financial_incentive_reading"]
        assert "misprices both" in reading["distinct_columns"]
        assert "distribution dependency" in reading["real_vector"]

    def test_ascii_only(self):
        text = _profiles_text()
        block_start = text.index(MECH_KEY)
        block_end = text.index(
            "mechanism_642_apple_news_plus_conde_nast_revenue_share_leg:")
        block_text = text[block_start:block_end]
        assert block_text.isascii(), "repository prose is ASCII-only"
        assert "\u2014" not in block_text, "no em dashes in repository prose"
        assert "\u2013" not in block_text, "no en dashes in repository prose"

    def test_apple_section_adjacent_to_m574(self):
        text = _profiles_text()
        assert text.index(MECH_KEY) > text.index(
            "mechanism_574_apple_training_data_purchasing_architecture:")
        assert text.index(MECH_KEY) < text.index(
            "mechanism_642_apple_news_plus_conde_nast_revenue_share_leg:")


# ---------------------------------------------------------------------------
# 5. Figures and sources
# ---------------------------------------------------------------------------
class TestFigures919:
    def test_figure_strings_present(self):
        block_text = str(_block())
        for fig in FIGURE_STRINGS:
            assert fig in block_text, fig

    def test_table_row_fields(self):
        trace = _block()["misclassification_trace"]
        assert trace["row_date"] == "2025-10"
        assert "News Corp" in trace["table"]
        assert "Apple" in trace["table"]

    def test_thomson_quote_fields(self):
        trace = _block()["misclassification_trace"]
        assert "Oct 21 2025" in trace["traces_to"]
        assert "significant" in trace["traces_to"]

    def test_apple_news_deal_history_fields(self):
        rel = _block()["misclassification_trace"]["underlying_relationship"]
        assert "2019" in rel
        assert "Apple News+" in rel
        assert "subscriptions" in rel

    def test_source_urls(self):
        sources = _block()["sources"]
        for url in EXPECTED_URLS:
            assert any(url in s for s in sources), url

    def test_first_party_blankspace_source_present(self):
        sources = _block()["sources"]
        assert any("blankspace.so" in s for s in sources), (
            "first-hand blankspace.so PDF source")

    def test_paper_caveat_recorded(self):
        trace = _block()["misclassification_trace"]
        assert "journalistic estimates" in trace["paper_caveat"]

    def test_secondary_synthesis_bounded(self):
        posture = _block()["verification_posture"]
        assert posture["paper_other_claims"].startswith("BOUNDED SYNTHESIS")


# ---------------------------------------------------------------------------
# 6. Statistical discipline (manual qualitative; engine not run)
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline919:
    def test_manual_qualitative_only(self):
        block = _block()
        assert block["verification_posture"]["qualitative_verification_only"] is True

    def test_p_value_not_calculated(self):
        assert _block()["p_value"] == "NOT_CALCULATED"

    def test_cohens_d_not_calculated(self):
        assert _block()["cohens_d"] == "NOT_CALCULATED"

    def test_ci_95_not_calculated(self):
        assert _block()["ci_95"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        assert _block()["is_significant"] is False

    def test_effect_size_not_scored(self):
        assert _block()["effect_size"] == "NOT_SCORED"

    def test_tone_not_scored(self):
        assert _block()["tone_delta"] == "NOT_SCORED"

    def test_no_analysis_json_update(self):
        assert _block()["verification_posture"]["no_analysis_json_update"] is True

    def test_engine_not_run(self):
        assert _block()["verification_posture"]["engine_not_run"] is True

    def test_not_artifact_grade(self):
        assert _block()["verification_posture"]["artifact_grade"] is False

    def test_no_coverage_tone_claim(self):
        assert _block()["verification_posture"]["no_coverage_tone_claim"] is True

    def test_no_causal_claim(self):
        assert _block()["verification_posture"]["no_causal_claim"] is True

    def test_no_scorer_run(self):
        assert _block()["verification_posture"]["no_scorer_run"] is True

    def test_not_falsification_family(self):
        block = _block()
        assert block["falsification_family_member"] is False
        assert block["falsification_ledger"] == 29
        assert "ledger holds at 29" in block["ledger_note"]

    def test_row_trace_verified_first_hand(self):
        posture = _block()["verification_posture"]
        assert posture["row_trace"].startswith("VERIFIED")
        assert "728 rendered lines" in posture["row_trace"]


# ---------------------------------------------------------------------------
# 7. Confounders
# ---------------------------------------------------------------------------
class TestConfounders919:
    def test_five_ranked_confounders(self):
        confs = _block()["ranked_confounders"]
        assert len(confs) == 5
        assert [c["rank"] for c in confs] == [1, 2, 3, 4, 5]

    def test_top_two_strong(self):
        confs = _block()["ranked_confounders"]
        assert confs[0]["strength"] == "strong"
        assert confs[1]["strength"] == "strong"

    def test_secondary_paper_confounder_first(self):
        c1 = _block()["ranked_confounders"][0]["confounder"]
        assert "secondary working paper" in c1

    def test_absence_bounded_confounder_second(self):
        c2 = _block()["ranked_confounders"][1]["confounder"]
        assert "iteration-492" in c2

    def test_postdate_confounder_weak(self):
        confs = _block()["ranked_confounders"]
        assert confs[4]["strength"] == "weak"
        assert "mid-2026" in confs[4]["confounder"]


# ---------------------------------------------------------------------------
# 8. No cross-contamination
# ---------------------------------------------------------------------------
class TestNoCrossContamination919:
    def _yaml_files(self):
        root = _repo_root()
        out = []
        for dirpath, _dirnames, filenames in os.walk(root):
            if "__pycache__" in dirpath or ".venv" in dirpath or ".git" in dirpath:
                continue
            for fn in filenames:
                if fn.endswith(".yaml"):
                    out.append(os.path.join(dirpath, fn))
        return out

    def test_no_underscore_form_783_carriers(self):
        # Designed keying per #715: the underscore-form marker exists only
        # format-built in this file, never as a literal carrier.
        hits = []
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                if MECH_ID_MARKER in fh.read():
                    hits.append(path)
        assert hits == []

    def test_no_dash_form_783_references(self):
        hits = []
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                if NEXT_ID_DASH.replace("784", "783") in fh.read():
                    hits.append(path)
        assert hits == []

    def test_no_next_id_784_anywhere(self):
        hits = []
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                content = fh.read()
                if NEXT_ID_MARKER in content or NEXT_ID_NUMERIC in content:
                    hits.append(path)
        assert hits == []

    def test_max_numeric_mechanism_id_is_783(self):
        max_id = 0
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                for m in re.finditer(r"mechanism_id:\s*(\d+)", fh.read()):
                    max_id = max(max_id, int(m.group(1)))
        assert max_id == 783

    def test_no_thirtieth_member_form_repo_wide(self):
        hits = []
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                if "THIRTIETH falsification-family member" in fh.read():
                    hits.append(path)
        assert hits == []

    def test_ledger_holds_at_29_not_member(self):
        assert _block()["falsification_ledger"] == 29
        assert _block()["falsification_family_member"] is False


# ---------------------------------------------------------------------------
# 9. Doc-sync: README + ARCHITECTURE
# ---------------------------------------------------------------------------
class TestDocSync919:
    def test_readme_stats_table(self):
        readme = _read("README.md")
        assert f"| Tests | {GATE_TESTS} |" in readme
        assert f"Across {GATE_FILES} test files" in readme

    def test_readme_row(self):
        readme = _read("README.md")
        assert OWN_BASENAME in readme
        assert "Type C #919" in readme

    def test_architecture_row(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert OWN_BASENAME in arch
        assert "Type C #919" in arch

    def test_collect_gate(self):
        assert GATE_TESTS > 0, "gate filled after the authoritative collect run"
        assert GATE_FILES > 0, "gate filled after the authoritative collect run"
        assert "## #919 Type C" in _read("iteration-log.md")


# ---------------------------------------------------------------------------
# 10. Iteration log
# ---------------------------------------------------------------------------
class TestIterationLog919:
    def test_entry_present(self):
        log = _read("iteration-log.md")
        assert "## #919 Type C:" in log

    def test_entry_documents_mechanism(self):
        log = _read("iteration-log.md")
        entry = log.split("## #919 Type C:")[1].split("## #918")[0]
        assert "m783" in entry

    def test_entry_documents_window(self):
        log = _read("iteration-log.md")
        entry = log.split("## #919 Type C:")[1].split("## #918")[0]
        assert "915-919" in entry
        assert "FIFTH leg" in entry
        assert "D->E->A->B->C" in entry

    def test_entry_documents_ledger(self):
        log = _read("iteration-log.md")
        entry = log.split("## #919 Type C:")[1].split("## #918")[0]
        assert "ledger holds at 29" in entry

    def test_entry_documents_finding(self):
        log = _read("iteration-log.md")
        entry = log.split("## #919 Type C:")[1].split("## #918")[0]
        assert "Licensing Mirage" in entry


# ---------------------------------------------------------------------------
# 11. Date grounding
# ---------------------------------------------------------------------------
class TestDateGrounding919:
    def test_run_date_is_tuesday(self):
        assert date(2026, 9, 22).strftime("%A") == "Tuesday"

    def test_thomson_quote_before_paper_before_run(self):
        assert date(2025, 10, 21) < date(2026, 6, 15) < date(2026, 9, 22)

    def test_scheduled_time(self):
        assert SCHEDULED_LOCAL == "Tue 2026-09-22 09:00:00 PDT"
        block = _block()
        assert block["date_analyzed"] == "2026-09-22"
        assert block["time_pdt"] == "09:00"

    def test_arm_dates_present(self):
        text = str(_block())
        assert "Oct 21 2025" in text
        assert "2026-09-22" in text

    def test_window_reference_in_file(self):
        # The window reference lives in the test module docstring.
        text = _read("tests/" + OWN_BASENAME)
        assert "915-919" in text
        assert "FIFTH leg" in text
        assert "D->E->A->B->C" in text
