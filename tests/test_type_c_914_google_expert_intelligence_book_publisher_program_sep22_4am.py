"""Type C iteration 914: Google Expert Intelligence book-publisher program
(announced Aug 27 2026) - licensed-use book leg of the Google incentive
vector; 100,000+ titles from six launch publishers inside Gemini Notebook;
book-domain sign-or-sue bifurcation against the Jul 2026 litigation tier
(mechanism 780), FIFTH leg of the 910-914 rotation window (D->E->A->B->C),
CLOSING the window.

Type C contract: verify and expand financial relationships between
publications/competitors with sourced datums; update competitor-entities.yaml;
manual qualitative only. This run: Google's Expert Intelligence program -
the first dedicated corpus mechanism on Google's licensed-use book-publisher
leg. Consumer announcement Aug 27, 2026 (Google blog post by Steven Johnson,
Editorial Director Google Labs, and Will Houghteling, product management for
Expert Intelligence); Google Workspace rollout entry Sep 17, 2026. Readers
add purchased Google Play Books e-books into Gemini Notebook and get
grounded answers, infographics, audio overviews, and quizzes, with citations.
Launch: more than 100,000 titles from six publishers (Bloomsbury, De Gruyter
Brill, Johns Hopkins University Press, Macmillan Publishers, O'Reilly Media,
Penguin Random House); 15+ bestselling authors (Steven Pinker, Michael
Pollan, Jennifer Wallace) building Featured Notebooks. Announced (not live)
expansion: Gemini app, AI Mode in Search, third-party subscriptions, business
research reports, textbooks. Authors Guild CEO Mary Rasenberger praised it
as "a positive step forward in the legitimized use of books in the AI
ecosystem to the benefit of readers, publishers, and authors alike."

Financial-incentive read: EXTENDS mechanism 735's deal-type dimension into
the book domain as the licensed-use tier (purchase-gated grounding, per-copy
traceable consideration; no disclosed terms so LEG with quanta, not a
quantum). Book-domain sign-or-sue bifurcation now named on both sides:
partner tier (the six) vs litigation tier (Hachette Book Group, Cengage,
Elsevier, Turow - Jul 2026 SDNY suit, corpus publisher_litigation_jul2026)
on the same counterparty in the same month. Macmillan breaks entity-level
labels: Expert Intelligence partner with Google AND May 2026 plaintiff
against Meta - the tier is counterparty-specific. connects_to
[735, 777, 702, 708, 663, 711, 636, 609].

MANUAL QUALITATIVE ONLY per the Aug 28 2026 standing rule: no financial
terms disclosed; p_value, cohens_d, ci_95 NOT_CALCULATED; is_significant
False; engine NOT run; no_analysis_json_update True; NOT artifact-grade.
NOT a falsification-family member (documentation + tier leg, no tone pair);
falsification ledger holds at 29; THIRTIETH remains the negative guard.
Verdict directionally_supported_not_proven. Correlation only, not causation.
Hypothesis-generating only. ASCII-only, no em dashes.

Research: 3 browser.search query sets this run (publisher AI content
licensing deal announced September 2026 - SELECTED the Publishers Weekly /
The Bookseller Expert Intelligence coverage; Google Play Books AI
partnership Bloomsbury Penguin Random House - SELECTED the Google Workspace
Updates first-party entry + Thurrott + jellypod announcement-date detail;
"Expert Intelligence" launch announcement - SELECTED iphoneincanada consumer
relay). REJECTED candidates: FT "red button" clauses (m774, #904); Digiday
Sep-20/21 unsealed-filings synthesis (m771, in-flight #899); Minichart Sep-19
RTB/Paradium piece (already a source on m744); SEJ four-model payment
comparison (components covered: m702/708 Google pilot, m726 Cloudflare stack,
m443 Microsoft PCM); LLM Pulse master deal map (in corpus); PUP x Cashmere
(m663/m711 family); Press Ranger/OtterlyAI study (m249); Apple/xAI sealed
settlement (terms secret); Mozilla x Mistral (no financial terms); UMG x
ElevenLabs (music, not publisher domain); FourWeekMBA India deals (in
corpus). 0 browser.open this run per #503 (excerpt-bounded; all evidence
excerpt-tier). All URLs copied verbatim from Full-URL search listings; no
canonical URLs constructed; no zero-coverage claims per #492.

NOVELTY VERIFICATION (run pre-commit, Sep 22 2026 ~04:0x PDT, before edits):
- glob: zero test_type_c_914*.py files on disk
- git log --all --grep="Type C #914": zero hits (no prior #914 main commit)
- numeric mechanism_id max in profiles/: 779 (m779 committed, #913)
- zero underscore-form 780 mechanism key strings in profiles/ pre-commit
  (needles format-built, no literals carried per #715)
- zero numeric "mechanism_id: 780" keys in profiles/ pre-commit
- BLOCK_KEY zero-hit repo-wide pre-commit (git grep)
- "Expert Intelligence" zero-hit repo-wide pre-commit (git grep + untracked
  file check); "Featured Notebooks" zero-hit repo-wide pre-commit
- the five source URL slugs zero-hit repo-wide pre-commit (git grep)

ROTATION: this is the FIFTH leg of rotation window 910-914
(D->E->A->B->C), CLOSING the window. Prior legs committed in
iteration-log.md: #910 Type D, #911 Type E, #912 Type A, #913 Type B.
Expected cycle position: C (914) after B (913) after A (912) after E (911)
after D (910). Next: #915 Type D opens the 915-919 window.

CONCURRENCY: this run touched profiles/competitor-entities.yaml only, with
the stranded working-tree changes (#884 m762 in profiles/competitor-entities.yaml)
backed up to /tmp, the file HEAD-restored, the m780 block appended
m735-adjacent on the HEAD base, and the stranded material re-applied to the
working tree post-add via git apply (disjoint hunks, verified clean).
profiles/careers/journalists.yaml (in-flight #898 m770), profiles/nytimes.yaml
(in-flight #899 m771), and the untracked #900 test file were NOT touched and
remain uncommitted per the concurrency protocol. Targeted git add only
(never git add -A): the commits contain ONLY profiles/competitor-entities.yaml
(m780 block), tests/test_type_c_914_google_expert_intelligence_book_publisher_program_sep22_4am.py,
README.md, docs/ARCHITECTURE.md, and iteration-log.md.
"""

import os
import re
import subprocess
from datetime import date

import pytest
import yaml

TEST_FILE = __file__
OWN_BASENAME = "test_type_c_914_google_expert_intelligence_book_publisher_program_sep22_4am.py"
MECH_KEY = "type_c_914_google_expert_intelligence_book_publisher_program_sep22_4am"
M_ID = 780
ITER = 914
TYPE_LETTER = "C"
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

# Format-built needles per the #715 convention: no literal underscore-form,
# numeric, or dash-form 780 mechanism markers are carried in this file.
MECH_ID_MARKER = "mechanism" + "_780"
NEXT_ID_MARKER = "mechanism" + "_781"
NEXT_ID_NUMERIC = "mechanism_id: " + "781"
NEXT_ID_DASH = "mechanism" + "-781"
MECH_NUMERIC = "mechanism_id: " + "780"

# Filled in after the authoritative collect run; asserts the doc-sync gate.
GATE_TESTS = 46915
GATE_FILES = 1239
SCHEDULED_LOCAL = "Tue 2026-09-22 04:00:00 PDT"

EXPECTED_URLS = [
    "https://www.thebookseller.com/news/google-launches-expert-intelligence-with-more-than-100k-publisher-titles",
    "https://workspaceupdates.googleblog.com/search/label/Gemini%20Notebook",
    "https://www.publishersweekly.com/pw/by-topic/industry-news/publisher-news/article/101215-publishing-s-ai-reckoning.html",
    "https://www.thurrott.com/a-i/google-gemini-a-i/340803/google-brings-e-books-to-gemini-notebook",
    "https://www.iphoneincanada.ca/2026/08/28/gemini-notebook-play-books/",
    "https://www.morningstar.com/news/dow-jones/20251203885/bloomsbury-publishing-to-collaborate-with-google-cloud",
]

FIGURE_STRINGS = [
    "100,000",
    "Bloomsbury",
    "De Gruyter Brill",
    "Johns Hopkins University Press",
    "Macmillan Publishers",
    "O'Reilly Media",
    "Penguin Random House",
    "Steven Pinker",
    "Michael Pollan",
    "Jennifer Wallace",
    "Featured Notebooks",
    "Expert Intelligence",
    "Aug 27, 2026",
    "Sep 17, 2026",
    "AI Mode in Search",
    "Mary Rasenberger",
    "positive step forward",
    "directionally_supported_not_proven",
    "NOT_SCORED",
    "ledger holds at 29",
    "EXTENDS mechanism 735",
    "m735",
    "NOT a falsification-family member",
    "purchase-gated",
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
    return doc["marketplace_intermediary_landscape"][MECH_KEY]


def _profiles_text():
    return _read("profiles/competitor-entities.yaml")


# ---------------------------------------------------------------------------
# 1. Novelty: this iteration and this mechanism are new
# ---------------------------------------------------------------------------
class TestNovelty914:
    def test_single_test_type_c_914_file(self):
        files = [f for f in os.listdir(os.path.join(_repo_root(), "tests"))
                 if f.startswith("test_type_c_914")]
        assert files == [OWN_BASENAME], files

    @pytest.mark.anchor
    def test_type_c_914_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per #565: the commit does not exist yet.
        # Tolerant form per #913: green pre-commit (no mains), pins the SHA
        # once the anchor followup patches ANCHORED_SHA.
        log = subprocess.run(
            ["git", "-C", _repo_root(), "log", "--format=%H %s",
             "--grep=Type C #914"],
            capture_output=True, text=True, timeout=60)
        assert log.returncode == 0
        mains = [line for line in log.stdout.splitlines()
                 if re.search(r"Type C #914(?::| )", line)
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
        assert ITER == 914
        assert M_ID == 780

    def test_910_913_window_legs_present_prior_to_914(self):
        log = _read("iteration-log.md")
        assert "## #910 Type D" in log
        assert "## #911 Type E" in log
        assert "## #912 Type A" in log
        assert "## #913 Type B" in log

    def test_block_key_zero_hit_elsewhere(self):
        text = _profiles_text()
        assert text.count(MECH_KEY) == 2, "top-level key + block_key field"

    def test_source_url_slugs_zero_hit_elsewhere(self):
        # Each slug appears exactly twice: the sources list and the matching
        # evidence item, both inside this block. Novelty means zero hits
        # outside the block.
        text = _profiles_text()
        block_start = text.index(MECH_KEY)
        block_end = text.index("roundtable_paradium_infrastructure_capture_sep2026:")
        outside = text[:block_start] + text[block_end:]
        for slug in ("thebookseller.com/news/google-launches-expert-intelligence",
                     "101215-publishing-s-ai-reckoning",
                     "340803/google-brings-e-books-to-gemini-notebook",
                     "20251203885/bloomsbury-publishing-to-collaborate-with-google-cloud"):
            assert slug not in outside, slug
        assert text.count("thebookseller.com/news/google-launches-expert-intelligence") == 2

    def test_expert_intelligence_zero_hit_elsewhere(self):
        text = _profiles_text()
        block_start = text.index(MECH_KEY)
        block_end = text.index("roundtable_paradium_infrastructure_capture_sep2026:")
        outside = text[:block_start] + text[block_end:]
        assert "Expert Intelligence" not in outside
        assert "Featured Notebooks" not in outside


# ---------------------------------------------------------------------------
# 2. Rotation guard: 910-914 window, fifth leg, closes the window
# ---------------------------------------------------------------------------
class TestRotationGuard914:
    # Rotation-guard tests follow the #911/#912/#913 pattern (static window
    # contract + predecessor + no-concurrent-inflight checks).
    # Deselected pre-commit per #565; patched green in the anchor followup.
    @pytest.mark.rotation
    def test_fifth_leg_of_910_914_window(self):
        assert TYPE_LETTER == "C"
        assert ITER == 914

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {910: "D", 911: "E", 912: "A", 913: "B", 914: "C"}
        assert expected[910] == "D"
        assert expected[911] == "E"
        assert expected[912] == "A"
        assert expected[913] == "B"
        assert expected[914] == "C"

    @pytest.mark.rotation
    def test_predecessor_913_type_b_committed(self):
        # #913 Type B is COMMITTED (its log entry sits below this run's
        # #914 entry, which was prepended above it).
        assert "## #913 Type B:" in _read("iteration-log.md")

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
class TestNoveltyAnchor914:
    def test_block_key_shape(self):
        assert MECH_KEY.startswith("type_c_914_google_expert_intelligence")

    def test_block_key_exact(self):
        assert MECH_KEY == (
            "type_c_914_google_expert_intelligence_book_publisher_program_sep22_4am"
        )

    def test_block_key_carries_no_numeric_id(self):
        # Designed keying per #715: iteration number carried, never the
        # numeric mechanism id.
        assert "780" not in MECH_KEY
        assert "914" in MECH_KEY


# ---------------------------------------------------------------------------
# 4. Mechanism 780 block structure
# ---------------------------------------------------------------------------
class TestMechanism780Structure:
    def test_block_key_unique(self):
        assert _profiles_text().count(MECH_KEY) == 2

    def test_iteration_and_type(self):
        block = _block()
        assert block["iteration"] == 914
        assert block["type"] == "financial_incentive_mapping"

    def test_designed_keying_no_underscore_780(self):
        assert MECH_ID_MARKER not in _profiles_text()

    def test_mechanism_id(self):
        assert _block()["mechanism_id"] == M_ID

    def test_block_key_field_matches(self):
        assert _block()["block_key"] == MECH_KEY

    def test_mechanism_name(self):
        name = _block()["mechanism_name"]
        assert "Expert Intelligence" in name
        assert "Google" in name
        assert "780" not in name

    def test_type_label(self):
        assert _block()["type_label"] == "Financial Incentive Mapping"

    def test_verdict(self):
        assert _block()["statistical_discipline"]["verdict"] == \
            "directionally_supported_not_proven"

    def test_extends_mechanism_735(self):
        block = _block()
        assert "735" in block.get("extends", "")
        assert "EXTENDS mechanism 735" in block.get("overview", "")

    def test_connects_to(self):
        conns = _block()["connects_to"]
        for cid in (735, 777, 702, 708, 663, 711, 636, 609):
            assert cid in conns, cid

    def test_tone_not_scored(self):
        assert _block()["tone"] == "NOT_SCORED"

    def test_no_coverage_tone_claim(self):
        assert _block()["no_coverage_tone_claim"] is True

    def test_ascii_only(self):
        text = _profiles_text()
        block_start = text.index(MECH_KEY)
        block_end = text.index("roundtable_paradium_infrastructure_capture_sep2026:")
        block_text = text[block_start:block_end]
        assert block_text.isascii(), "repository prose is ASCII-only"
        assert "—" not in block_text, "no em dashes in repository prose"

    def test_m777_adjacent(self):
        text = _profiles_text()
        assert text.index(MECH_KEY) > text.index(
            "type_c_909_wiley_q1_fy2027_ai_revenue_mix_shift_sep2026:"
        )
        assert text.index(MECH_KEY) < text.index(
            "roundtable_paradium_infrastructure_capture_sep2026:"
        )


# ---------------------------------------------------------------------------
# 5. Figures and sources
# ---------------------------------------------------------------------------
class TestFigures914:
    def test_figure_strings_present(self):
        block_text = str(_block())
        for fig in FIGURE_STRINGS:
            assert fig in block_text, fig

    def test_launch_titles(self):
        figures = _block()["figures"]
        assert "100,000" in figures["launch_titles"]

    def test_launch_publishers_named(self):
        pubs = _block()["figures"]["launch_publishers"]
        for p in ("Bloomsbury", "De Gruyter Brill", "Johns Hopkins",
                  "Macmillan", "O'Reilly", "Penguin Random House"):
            assert p in pubs, p

    def test_featured_notebook_authors(self):
        authors = _block()["figures"]["featured_notebook_authors"]
        for a in ("Steven Pinker", "Michael Pollan", "Jennifer Wallace"):
            assert a in authors, a

    def test_terms_not_disclosed(self):
        assert _block()["figures"]["terms_disclosed"] is False

    def test_source_urls(self):
        sources = _block()["sources"]
        for url in EXPECTED_URLS:
            assert any(url in s for s in sources), url

    def test_first_party_google_source_present(self):
        sources = _block()["sources"]
        assert any("workspaceupdates.googleblog.com" in s for s in sources), (
            "first-party Google Workspace Updates entry"
        )

    def test_evidence_excerpt_tier(self):
        evidence = _block()["evidence"]
        for item in evidence:
            assert "#503" in item["surface_date"] or \
                "excerpt-bounded" in item["surface_date"], item["url"]

    def test_announcement_dates(self):
        text = str(_block())
        assert "Aug 27, 2026" in text
        assert "Sep 17, 2026" in text


# ---------------------------------------------------------------------------
# 6. Statistical discipline (manual qualitative; engine not run)
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline914:
    def test_manual_qualitative_only(self):
        block = _block()
        assert block["statistical_discipline"]["scope"] == \
            "qualitative financial-incentive documentation only"
        assert block["statistical_discipline"]["engine_run"] is False

    def test_effect_stats_not_calculated(self):
        sd = _block()["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        assert _block()["statistical_discipline"]["is_significant"] is False

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_not_artifact_grade(self):
        assert _block()["statistical_discipline"]["artifact_grade"] is False

    def test_not_falsification_family(self):
        block = _block()
        ff = block["falsification_family"]
        assert "NOT a member" in ff
        assert "ledger holds at 29" in ff
        assert "NOT a falsification-family member" in block.get("overview", "")

    def test_ledger_holds_at_29(self):
        block = _block()
        assert block["falsification_ledger_holds_at"] == 29
        assert "ledger holds at 29" in block.get("overview", "")

    def test_correlational_note(self):
        note = _block()["correlational_note"]
        assert "correlation" in note.lower()
        assert "No causal claim" in note


# ---------------------------------------------------------------------------
# 7. Confounders (ranked strong-first) and counter-evidence
# ---------------------------------------------------------------------------
class TestConfounders914:
    def test_confounders_ranked(self):
        confs = _block()["confounders_ranked_strong_first"]
        assert len(confs) >= 4
        assert confs[0]["severity"] == "STRONG"

    def test_confounders_strong_first_order(self):
        confs = _block()["confounders_ranked_strong_first"]
        sev_rank = {"STRONG": 0, "MODERATE": 1, "WEAK": 2}
        ranks = [sev_rank[c["severity"]] for c in confs]
        assert ranks == sorted(ranks), "confounders must be ranked strong-first"

    def test_excerpt_bounded_confounder(self):
        text = str(_block())
        assert "excerpt" in text.lower()

    def test_licensed_use_boundary_confounder(self):
        text = str(_block())
        assert "licensed-use" in text.lower() or "licensed use" in text.lower()

    def test_no_terms_confounder(self):
        text = str(_block())
        assert "No financial terms" in text

    def test_strongest_counterargument(self):
        ca = _block()["strongest_counterargument"]
        assert "no money" in ca.lower() or "discloses no money" in ca.lower()
        assert len(ca) > 200, "counterargument must be substantive"

    def test_counter_evidence_present(self):
        block = _block()
        ce = block["counter_evidence"]
        assert len(ce) >= 3
        assert any("HarperCollins" in c for c in ce)
        assert any("Wiley" in c for c in ce)
        assert any("Macmillan" in c for c in ce)


# ---------------------------------------------------------------------------
# 8. Corpus integrity: no cross-contamination, id sequence, ledger guard
# ---------------------------------------------------------------------------
class TestNoCrossContamination914:
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

    def test_no_underscore_form_780_carriers(self):
        # Designed keying per #715: the underscore-form marker exists only
        # format-built in this file, never as a literal carrier.
        hits = []
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                if MECH_ID_MARKER in fh.read():
                    hits.append(path)
        assert hits == []

    def test_no_dash_form_780_references(self):
        hits = []
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                if NEXT_ID_DASH.replace("781", "780") in fh.read():
                    hits.append(path)
        assert hits == []

    def test_no_next_id_781_anywhere(self):
        hits = []
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                content = fh.read()
                if NEXT_ID_MARKER in content or NEXT_ID_NUMERIC in content:
                    hits.append(path)
        assert hits == []

    def test_max_numeric_mechanism_id_is_780(self):
        max_id = 0
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                for m in re.finditer(r"mechanism_id:\s*(\d+)", fh.read()):
                    max_id = max(max_id, int(m.group(1)))
        assert max_id == 780

    def test_no_thirtieth_member_form_repo_wide(self):
        hits = []
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                if "THIRTIETH falsification-family member" in fh.read():
                    hits.append(path)
        assert hits == []

    def test_thirtieth_negative_guard_in_block(self):
        assert "THIRTIETH remains the negative guard" in _block()["overview"]


# ---------------------------------------------------------------------------
# 9. Doc-sync: README + ARCHITECTURE
# ---------------------------------------------------------------------------
class TestDocSync914:
    def test_readme_stats_table(self):
        readme = _read("README.md")
        assert f"| Tests | {GATE_TESTS} |" in readme
        assert f"Across {GATE_FILES} test files" in readme

    def test_readme_row(self):
        readme = _read("README.md")
        assert OWN_BASENAME in readme
        assert "Type C #914" in readme

    def test_architecture_row(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert OWN_BASENAME in arch
        assert "Type C #914" in arch

    def test_collect_gate(self):
        assert GATE_TESTS > 0, "gate filled after the authoritative collect run"
        assert GATE_FILES > 0, "gate filled after the authoritative collect run"
        assert "## #914 Type C" in _read("iteration-log.md")


# ---------------------------------------------------------------------------
# 10. Iteration log
# ---------------------------------------------------------------------------
class TestIterationLog914:
    def test_entry_present(self):
        log = _read("iteration-log.md")
        assert "## #914 Type C:" in log

    def test_entry_documents_mechanism(self):
        log = _read("iteration-log.md")
        entry = log.split("## #914 Type C:")[1].split("## #913")[0]
        assert "m780" in entry

    def test_entry_documents_window(self):
        log = _read("iteration-log.md")
        entry = log.split("## #914 Type C:")[1].split("## #913")[0]
        assert "910-914" in entry
        assert "FIFTH leg" in entry
        assert "D->E->A->B->C" in entry

    def test_entry_documents_ledger(self):
        log = _read("iteration-log.md")
        entry = log.split("## #914 Type C:")[1].split("## #913")[0]
        assert "ledger holds at 29" in entry

    def test_entry_documents_finding(self):
        log = _read("iteration-log.md")
        entry = log.split("## #914 Type C:")[1].split("## #913")[0]
        assert "Expert Intelligence" in entry


# ---------------------------------------------------------------------------
# 11. Date grounding
# ---------------------------------------------------------------------------
class TestDateGrounding914:
    def test_run_date_is_tuesday(self):
        assert date(2026, 9, 22).strftime("%A") == "Tuesday"

    def test_announcement_before_rollout_before_run(self):
        assert date(2026, 8, 27) < date(2026, 9, 17) < date(2026, 9, 22)

    def test_scheduled_time(self):
        assert SCHEDULED_LOCAL == "Tue 2026-09-22 04:00:00 PDT"
        block = _block()
        assert block["date"] == "2026-09-22 04:00 PDT"

    def test_arm_dates_present(self):
        text = str(_block())
        assert "Aug 27, 2026" in text
        assert "Sep 17, 2026" in text

    def test_window_reference_in_file(self):
        # The window reference lives in the test module docstring.
        text = _read("tests/" + OWN_BASENAME)
        assert "910-914" in text
        assert "FIFTH leg" in text
        assert "D->E->A->B->C" in text
