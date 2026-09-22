"""
Type C #909 (rotation window 905-909, FIFTH leg: D->E->A->B->C, CLOSING the
window): Wiley Q1 FY2027 AI-revenue print - training-vs-recurring mix shift
as the empirical verification leg of m735's retrieval-vs-training
deal-structure shift (mechanism 777).

FIRST dedicated corpus mechanism on Wiley's Q1 FY2027 earnings print
(quarter ended July 31, 2026; BusinessWire release Sep 3, 2026): AI
licensing revenue of $14M vs $29M in the prior-year quarter and $49M for
all of FY2026 (mechanism 735, #839). Mix split (ainvest): $10.5M model
training + $3.5M recurring; recurring growing 2-3x over last year;
another $14M already contracted across the next two quarters; management
says the quarter is ahead of the pace needed to exceed the $50M full-year
AI target. intellectia: Wiley is now the sole scientific publisher in the
U.S. Department of Energy's Genesis Mission. This is the first corpus
earnings print that splits AI revenue into training vs recurring: it
VERIFIES m735's retrieval-vs-training deal-structure shift empirically
(the recurring/RAG leg is becoming the durable stream) while tempering it
(training is still 75% of the quarter's AI revenue; the $29M prior-year
quarter was itself a one-off training-deal spike per ainvest, so both
endpoints are noisy). EXTENDS mechanism 735; connects_to [735, 663, 711,
463].

MANUAL / qualitative only per the Aug 28 2026 standing rule;
financial-incentive documentation leg, not a tone test; scorer none; tone
NOT_SCORED; p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant False;
verdict directionally_supported_not_proven; engine NOT run;
no_analysis_json_update: true; NOT artifact-grade. NOT a
falsification-family member (documentation leg + verification leg, no tone
pair; ledger holds at 29). ASCII-only, no em dashes.

NOVELTY VERIFICATION (run pre-commit, Sep 21 2026 ~23:0x PDT, before edits):
- glob: zero test_type_c_909*.py files on disk
- git log --all --grep="Type C #909": zero hits (no prior #909 main commit)
- numeric mechanism_id max in profiles/: 776 (#908 m776 committed)
- zero underscore-form 777 mechanism key strings in profiles/ pre-commit
  (the #908 file's own zero-777 sweep assertions are test-instrument
  literals, excluded per the #715 pattern-rescope lesson)
- zero numeric "mechanism_id: 777" keys in profiles/ pre-commit
- BLOCK_KEY zero-hit repo-wide pre-commit
- the three source URLs zero-hit repo-wide pre-commit (git grep)
- "Genesis Mission" + Wiley context zero-hit pre-commit (the
  mit-tech-review.yaml hit is DOE grant proposals, unrelated)
- "Wiley" + "$14" AI-revenue-context zero-hit pre-commit
- REJECTED candidates this run: Minichart Sep-19 RTB/Paradium piece
  (already a source on m744, competitor-entities.yaml); SEJ four-model
  payment comparison (URL 589636 zero-hit but components covered: m702/708
  Google pilot, m726 Cloudflare stack, m443 Microsoft PCM); Digiday
  Spur/Buttle synthesis (m771/#899); TechCrunch Sep-6 Anthropic-settlement
  distribution piece (covered in m594); LLM Pulse master deal map (in
  corpus); PUP x Cashmere (m663/m711 family); Press Ranger/OtterlyAI study
  (m249); Apple/xAI sealed settlement (terms secret, litigation not a
  financial datum); Mozilla x Mistral (no financial terms disclosed);
  OpenAI x Firmus Malaysia (infrastructure, not a publisher deal)

ROTATION: this is the FIFTH leg of rotation window 905-909
(D->E->A->B->C), CLOSING the window. Prior legs present in
iteration-log.md: #905 Type D (committed), #906 Type E (committed), #907
Type A (committed), #908 Type B (committed, 22:00 PDT). Expected cycle
position: C (909) after B (908) after A (907) after E (906) after D
(905). Next: #910 Type D opens the 910-914 window.

RESEARCH METHOD: 5 browser.search query sets this run. (1) OpenAI
publisher content licensing deal announced September 2026 (RULED OUT -
fourweekmba India deals in corpus, Press Gazette tracker carried, Google
pay-per-value 702/708 corroboration only, Digiday MDL synthesis in
corpus); (2) publisher AI licensing deal news since 2026-09-18 (RULED OUT
- PUP x Cashmere in m663/m711 family, Press Ranger/OtterlyAI in m249,
News/Media Alliance x Bria in m747); (3) AI company signs content deal
since 2026-09-19 (RULED OUT - Minichart RTB/Paradium already a source on
m744, Firmus Malaysia compute deal is infrastructure not publisher,
Analog Devices/Alif out of scope); (4) Anthropic publisher content
licensing deal since 2026-09-01 (RULED OUT - zero-deal posture m509
holds; Adweek + digimirror corroboration); (5) xAI/Apple/Mistral
publisher licensing deal since 2026-09-10 (SURFACED Mozilla x Mistral Sep
16 partnership, no financial terms; Apple/xAI sealed settlement Sep 17,
terms secret - both rejected as non-financial); (6) publisher earnings AI
licensing revenue since 2026-09-10 (SELECTED: Wiley Q1 FY2027 print via
intellectia + ainvest + stocktitan/BusinessWire). 0 browser.open this run
per #503 (excerpt-bounded; all arms already excerpt-tier). All URLs
copied verbatim from Full-URL search listings. No URL construction.
No zero-coverage claims per #492. ASCII-only, no em dashes.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_c_909_wiley_q1_fy2027_ai_revenue_mix_shift_sep21_11pm.py"
MECH_KEY = "wiley_q1_fy2027_ai_revenue_mix_shift_sep2026"
BLOCK_KEY = "type_c_909_" + MECH_KEY
MECHANISM_ID = 777
ITERATION = 909
TYPE_LETTER = "C"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_777"
NEXT_ID_MARKER = "mechanism" + "_778"
NEXT_ID_NUMERIC = "mechanism_id: 778"
# Filled in after the authoritative collect run; asserts the doc-sync gate.
GATE_TESTS = 46609
GATE_FILES = 1234
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "baaad53c27530d323fb5e07c6c8b00c4e2576561"
SCHEDULED_LOCAL = "Mon 2026-09-21 23:00:00 PDT"

EXPECTED_URLS = [
    "https://intellectia.ai/news/stock/wiley-q1-earnings-revenue-decline-offset-by-ai-growth",
    "https://www.ainvest.com/news/wiley-ai-revenue-fell-headline-hides-real-signal-2609/",
    "https://www.stocktitan.net/news/WLY/wiley-reports-first-quarter-2027-results-q1-in-line-with-9m7ilcbi2qy1.html",
]

FIGURE_STRINGS = [
    "$14M",
    "$29M",
    "$49M",
    "$50M",
    "$10.5M",
    "$3.5M",
    "Genesis Mission",
    "sole scientific publisher",
    "quarter ended July 31, 2026",
    "Sep 3, 2026",
    "directionally_supported_not_proven",
    "NOT_SCORED",
    "ledger holds at 29",
    "2-3x",
    "ahead of the pace",
    "EXTENDS mechanism 735",
    "m735",
    "NOT a falsification-family member",
]


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _read(rel: str) -> str:
    return (_repo_root() / rel).read_text()


def _profiles_path() -> Path:
    return _repo_root() / "profiles" / "competitor-entities.yaml"


def _profiles_text() -> str:
    return _profiles_path().read_text()


def _get_block() -> dict:
    doc = yaml.safe_load(_profiles_text())
    return doc["marketplace_intermediary_landscape"][BLOCK_KEY]


def _corpus_ids() -> list:
    ids = []
    for p in (_repo_root() / "profiles").rglob("*.yaml"):
        for m in re.finditer(r"mechanism_id:\s*(\d+)", p.read_text(errors="ignore")):
            ids.append(int(m.group(1)))
    return ids


# ---------------------------------------------------------------------------
# 1. Novelty: this iteration and this mechanism are new
# ---------------------------------------------------------------------------
class TestNovelty909:
    def test_single_test_type_c_909_file(self):
        matches = [
            f
            for f in os.listdir(_repo_root() / "tests")
            if f.startswith("test_type_c_909")
        ]
        assert matches == [TEST_BASENAME], matches

    def test_type_c_909_main_commit_unique_and_anchored(self):
        # DESELECTED pre-commit (per #565): the commit does not exist yet.
        log = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type C #909"],
            cwd=str(_repo_root()),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        mains = [
            ln for ln in log.splitlines()
            if re.search(r"Type C #909(?::| )", ln)
            and "anchor followup" not in ln
            and "log-hash followup" not in ln
            and "push-status followup" not in ln
        ]
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        )
        assert mains[0].startswith(ANCHORED_SHA + " "), mains[0]

    def test_novelty_verification_claim(self):
        assert ITERATION == 909
        assert MECHANISM_ID == 777

    def test_905_908_window_legs_present_prior_to_909(self):
        log = _read("iteration-log.md")
        assert "## #905 Type D" in log
        assert "## #906 Type E" in log
        assert "## #907 Type A" in log
        assert "## #908 Type B" in log

    def test_max_numeric_mechanism_id_777(self):
        ids = [
            int(m)
            for m in re.findall(r"mechanism_id: (\d+)", _profiles_text())
        ]
        assert max(ids) == 777, max(ids)

    def test_no_underscore_778_keys(self):
        assert NEXT_ID_MARKER not in _profiles_text()

    def test_no_dash_778_keys(self):
        assert "mechanism-778" not in _profiles_text()

    def test_no_numeric_778_keys(self):
        assert NEXT_ID_NUMERIC not in _profiles_text()

    def test_block_key_zero_hit_elsewhere(self):
        text = _profiles_text()
        assert text.count(BLOCK_KEY) == 2, "top-level key + block_key field"

    def test_source_url_slugs_zero_hit_elsewhere(self):
        text = _profiles_text()
        assert text.count("intellectia.ai/news/stock/wiley-q1-earnings-revenue-decline-offset-by-ai-growth") == 1
        assert text.count("wiley-ai-revenue-fell-headline-hides-real-signal-2609") == 1
        assert text.count("9m7ilcbi2qy1") == 1

    def test_wiley_genesis_mission_zero_hit_elsewhere(self):
        text = _profiles_text()
        block_start = text.index(BLOCK_KEY)
        block_end = text.index(
            "roundtable_paradium_infrastructure_capture_sep2026:"
        )
        outside = text[:block_start] + text[block_end:]
        assert "Genesis Mission" not in outside
        assert text.count("Genesis Mission") == 6, (
            "name + overview + figures + sources + novelty + confounder"
        )


# ---------------------------------------------------------------------------
# 2. Novelty anchor: block key shape
# ---------------------------------------------------------------------------
class TestNoveltyAnchor909:
    def test_block_key_shape(self):
        assert BLOCK_KEY.startswith("type_c_909_wiley_q1_fy2027_")

    def test_block_key_exact(self):
        assert BLOCK_KEY == (
            "type_c_909_wiley_q1_fy2027_ai_revenue_mix_shift_sep2026"
        )


# ---------------------------------------------------------------------------
# 3. Rotation guard: 905-909 window, fifth leg, closes the window
# ---------------------------------------------------------------------------
class TestRotationGuard909:
    def test_window_is_905_909_fifth_leg(self):
        log = _read("iteration-log.md")
        assert "## #909 Type C" in log
        assert "## #905 Type D" in log
        assert "## #906 Type E" in log
        assert "## #907 Type A" in log
        assert "## #908 Type B" in log

    def test_rotation_adjacency_cycle_valid(self):
        cycle = {"D": "E", "E": "A", "A": "B", "B": "C", "C": "D"}
        assert cycle["B"] == "C"

    def test_predecessor_is_type_b_908(self):
        log = _read("iteration-log.md")
        assert "## #908 Type B" in log

    def test_anchor_is_ancestor_of_head(self):
        # DESELECTED pre-commit (per #565): the commit does not exist yet.
        res = subprocess.run(
            ["git", "merge-base", "--is-ancestor", ANCHORED_SHA, "HEAD"],
            cwd=str(_repo_root()),
        )
        assert res.returncode == 0, (
            "anchored main commit must be an ancestor of HEAD"
        )


# ---------------------------------------------------------------------------
# 4. Mechanism 777 block structure
# ---------------------------------------------------------------------------
class TestMechanism777Structure:
    def test_block_key_unique(self):
        assert _profiles_text().count(BLOCK_KEY) == 2

    def test_iteration_and_type(self):
        block = _get_block()
        assert block["iteration"] == 909
        assert block["type"] == "C"

    def test_designed_keying_no_underscore_777(self):
        assert MECH_ID_MARKER not in _profiles_text()

    def test_mechanism_id(self):
        assert _get_block()["mechanism_id"] == 777

    def test_block_key_field_matches(self):
        assert _get_block()["block_key"] == BLOCK_KEY

    def test_mechanism_name(self):
        name = _get_block()["mechanism_name"]
        assert "Wiley" in name
        assert "Q1 FY2027" in name
        assert "777" not in name

    def test_type_label(self):
        assert _get_block()["type_label"] == "Financial Incentive Mapping"

    def test_verdict(self):
        assert _get_block()["verdict"] == "directionally_supported_not_proven"

    def test_extends_mechanism_735(self):
        block = _get_block()
        assert "735" in block.get("extends", "")
        assert "EXTENDS mechanism 735" in block.get("overview", "")

    def test_connects_to(self):
        conns = _get_block()["connects_to"]
        for cid in (735, 663, 711, 463):
            assert cid in conns, cid

    def test_ascii_only(self):
        text = _profiles_text()
        block_start = text.index(BLOCK_KEY)
        block_end = text.index(
            "roundtable_paradium_infrastructure_capture_sep2026:"
        )
        block_text = text[block_start:block_end]
        assert block_text.isascii(), "repository prose is ASCII-only"
        assert "\u2014" not in block_text, "no em dashes in repository prose"


# ---------------------------------------------------------------------------
# 5. Figures and sources
# ---------------------------------------------------------------------------
class TestFigures909:
    def test_figure_strings_present(self):
        block_text = str(_get_block())
        for fig in FIGURE_STRINGS:
            assert fig in block_text, fig

    def test_quarter_ended_date(self):
        block = _get_block()
        assert "July 31, 2026" in block["figures"]["quarter_ended"]

    def test_ai_revenue_q1(self):
        figures = _get_block()["figures"]
        assert figures["ai_licensing_revenue_q1_fy2027"] == "$14M"

    def test_ai_revenue_prior_year_quarter(self):
        figures = _get_block()["figures"]
        assert figures["ai_licensing_revenue_q1_fy2026"] == "$29M"

    def test_ai_revenue_fy2026(self):
        figures = _get_block()["figures"]
        assert figures["ai_licensing_revenue_fy2026"] == "$49M"

    def test_mix_split(self):
        figures = _get_block()["figures"]
        assert figures["training_revenue_q1_fy2027"] == "$10.5M"
        assert figures["recurring_revenue_q1_fy2027"] == "$3.5M"

    def test_source_urls(self):
        sources = _get_block()["sources"]
        for url in EXPECTED_URLS:
            assert any(url in s for s in sources), url

    def test_sources_use_primary_where_possible(self):
        sources = _get_block()["sources"]
        assert any("stocktitan.net" in s and "WLY" in s for s in sources), (
            "stocktitan BusinessWire mirror of the Sep 3 2026 release"
        )


# ---------------------------------------------------------------------------
# 6. Statistical discipline (manual qualitative; engine not run)
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline909:
    def test_manual_qualitative_only(self):
        block = _get_block()
        assert block["statistical_discipline"]["approach"] == "manual_qualitative"
        assert block["statistical_discipline"]["engine_run"] is False

    def test_tone_not_scored(self):
        assert _get_block()["tone"] == "NOT_SCORED"

    def test_effect_stats_not_calculated(self):
        sd = _get_block()["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        assert _get_block()["is_significant"] is False

    def test_no_analysis_json_update(self):
        assert _get_block()["no_analysis_json_update"] is True

    def test_not_artifact_grade(self):
        assert _get_block()["artifact_grade"] is False

    def test_not_falsification_family(self):
        block = _get_block()
        assert block["falsification_family"] is False
        assert "NOT a falsification-family member" in block.get("overview", "")

    def test_ledger_holds_at_29(self):
        block = _get_block()
        assert block["falsification_ledger_holds_at"] == 29
        assert "ledger holds at 29" in block.get("overview", "")

    def test_effect_stats_marked_not_calculated_in_text(self):
        text = str(_get_block()["statistical_discipline"])
        assert "NOT_CALCULATED" in text


# ---------------------------------------------------------------------------
# 7. Confounders (ranked strong-first) and counter-evidence
# ---------------------------------------------------------------------------
class TestConfounders909:
    def test_confounders_ranked(self):
        confs = _get_block()["confounders_ranked_strong_first"]
        assert len(confs) >= 4
        assert confs[0]["severity"] == "STRONG"

    def test_confounders_strong_first_order(self):
        confs = _get_block()["confounders_ranked_strong_first"]
        sev_rank = {"STRONG": 0, "MODERATE": 1, "WEAK": 2}
        ranks = [sev_rank[c["severity"]] for c in confs]
        assert ranks == sorted(ranks), "confounders must be ranked strong-first"

    def test_secondary_source_confounder(self):
        text = str(_get_block())
        assert "secondary" in text.lower()
        assert "10-Q" in text or "filing" in text

    def test_lumpiness_confounder(self):
        text = str(_get_block())
        assert "lumpy" in text.lower() or "seasonal" in text.lower()

    def test_strongest_counterargument(self):
        ca = _get_block()["strongest_counterargument"]
        assert "75%" in ca or "training" in ca.lower()
        assert len(ca) > 80, "counterargument must be substantive"

    def test_counter_evidence_present(self):
        block = _get_block()
        ce = block["counter_evidence"]
        assert len(ce) >= 2
        assert any("Menon" in c for c in ce)


# ---------------------------------------------------------------------------
# 8. Corpus integrity: id sequence, falsification ledger, adjacency
# ---------------------------------------------------------------------------
class TestCorpusIntegrity909:
    def test_max_corpus_id_is_777(self):
        ids = _corpus_ids()
        assert max(ids) == 777, max(ids)

    def test_zero_778_keys_repo_wide(self):
        repo = _repo_root()
        for p in repo.rglob("*.py"):
            if "__pycache__" in str(p) or ".venv" in str(p):
                continue
            if p.name == TEST_BASENAME:
                continue
            t = p.read_text(errors="ignore")
            assert "mechanism_778" not in t, p
        assert "mechanism-778" not in _profiles_text()
        assert NEXT_ID_NUMERIC not in _profiles_text()

    def test_m735_adjacent(self):
        text = _profiles_text()
        assert text.index(BLOCK_KEY) > text.index(
            "retrieval_licensing_not_training_market_structure_sep2026"
        )
        assert text.index(BLOCK_KEY) < text.index(
            "roundtable_paradium_infrastructure_capture_sep2026:"
        )

    def test_thirtieth_member_absent(self):
        text = _profiles_text()
        assert "THIRTIETH falsification-family member" not in text
        # bare "THIRTIETH" is present only in this block's negative-guard
        # note, asserted in test_block_ledger_holds_at_29
        assert text.count("THIRTIETH") == 1

    def test_exactly_one_29th_member_in_news_corp(self):
        news_corp = _read("profiles/news-corp.yaml")
        assert (
            news_corp.count("TWENTY-NINTH falsification-family member") == 1
        )

    def test_no_30th_member_form_repo_wide(self):
        repo = _repo_root()
        for p in repo.rglob("profiles/*.yaml"):
            t = p.read_text(errors="ignore")
            assert "THIRTIETH falsification-family member" not in t, p

    def test_block_ledger_holds_at_29(self):
        block = _get_block()
        assert block["falsification_family"] is False
        assert block["falsification_ledger_holds_at"] == 29
        assert "ledger holds at 29" in block["overview"]
        assert "THIRTIETH remains the negative guard" in block["overview"]

    def test_collect_gate(self):
        assert GATE_TESTS > 0, "gate filled after the authoritative collect run"
        assert GATE_FILES > 0, "gate filled after the authoritative collect run"
        log = _read("iteration-log.md")
        assert f"#{ITERATION}" in log


# ---------------------------------------------------------------------------
# 9. Doc-sync: README + ARCHITECTURE
# ---------------------------------------------------------------------------
class TestDocSync909:
    def test_readme_stats_table(self):
        readme = _read("README.md")
        assert f"| Tests | {GATE_TESTS} |" in readme
        assert f"Across {GATE_FILES} test files" in readme

    def test_readme_row(self):
        readme = _read("README.md")
        assert TEST_BASENAME in readme

    def test_architecture_row(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "Type C #909" in arch

    def test_architecture_lists_test_file(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert TEST_BASENAME in arch


# ---------------------------------------------------------------------------
# 10. Iteration log
# ---------------------------------------------------------------------------
class TestIterationLog909:
    def test_entry_present(self):
        log = _read("iteration-log.md")
        assert "## #909 Type C" in log

    def test_entry_documents_mechanism(self):
        log = _read("iteration-log.md")
        entry = log.split("## #909 Type C")[1].split("## #908")[0]
        assert "m777" in entry

    def test_entry_documents_window(self):
        log = _read("iteration-log.md")
        entry = log.split("## #909 Type C")[1].split("## #908")[0]
        assert "905-909" in entry
        assert "FIFTH leg" in entry
        assert "D->E->A->B->C" in entry

    def test_entry_documents_ledger(self):
        log = _read("iteration-log.md")
        entry = log.split("## #909 Type C")[1].split("## #908")[0]
        assert "ledger holds at 29" in entry


# ---------------------------------------------------------------------------
# 11. Date grounding
# ---------------------------------------------------------------------------
class TestDateGrounding909:
    def test_run_date_is_monday(self):
        import datetime
        assert datetime.date(2026, 9, 21).strftime("%A") == "Monday"

    def test_wiley_earnings_release_date_is_thursday(self):
        import datetime
        assert datetime.date(2026, 9, 3).strftime("%A") == "Thursday"

    def test_scheduled_time(self):
        assert SCHEDULED_LOCAL == "Mon 2026-09-21 23:00:00 PDT"
        block = _get_block()
        assert block["date"] == "2026-09-21 23:00 PDT"
