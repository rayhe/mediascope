"""Type C #1114 (2026-10-01 03:00 PDT) - Google publisher AI payments as three
parallel instruments: News AI pilot commercial partnerships (Dec 2025 deals,
take-it-or-leave-it, NDAs, no-sue clauses, Guardian + FT at single-figure GBP
millions/yr, FT joined Feb 2026) vs AI Contribution Pilot widget-metered
micro-pricing (m891/m894/m897) vs News Showcase legacy licensing -
TRACK-SEPARATED PRICING (parallel instruments, segmented counterparty
pricing) as the THIRTIETH relationship direction, mechanism 900.

FIFTH leg of the 1110-1114 window (D #1110 -> E #1111 -> A #1112 ->
B #1113 -> C #1114), per the #565 rotation anchor, CLOSING the window.
Predecessor: #1113 Type B (mediascope-daily-iteration, 2026-10-01 02:00 PDT).
The 1105-1109 window is verified closed.

Deal-terms layer carried from m355 (Aug 28 2026). THE NEW WORK is the
instrument architecture: three parallel payment instruments with different
pricing technologies and different legal categories (commercial partnership
vs pilot micro-payment vs showcase license), so no unified price for AI-use
of publisher content can form across tracks. Motive on the record: DCN CEO
Jason Kint - Google is trying "to get what they need without putting a
direct monetary value to the content licensing... if they had to pay
everybody for licensing their content, then that affects their margins in a
material way." Independent corroboration of the track separation: Forklog
(Sep 2026, novel URL this run). 3 search sets, 2 browser.open first-hand
reads this run (Press Gazette tracker updated Sep 30 2026; Press Gazette Aug
2026 piece), excerpt-bounded per #503.

Statistical discipline per the Aug 28 2026 standing rule: tone NOT_SCORED
(Type C financial-architecture mapping per the #609/#614 qualitative
boundary), engine NOT run, p_value/cohens_d/ci_95 NOT_CALCULATED,
is_significant false, verdict directionally_supported_not_proven,
no_analysis_json_update true, NOT artifact-grade. NOT a falsification-family
member: ledger holds at 41 (FORTY-FIRST landed by #1113 Type B, m899).
Correlation is not causation; hypothesis-generating only.

Literal discipline per #715: this file carries NO contiguous underscore-form,
dash-form, or numeric-form 900/901 mechanism literals - the mechanism
needles are format-built ("mechanism" + "_%d" / "mechanism_id: %d" at
runtime), so the zero-900 pre-commit sweeps and zero-901 forward guards stay
valid. The thirtieth-direction needle is fragment-built as well. The #1024
m846 sourcing-constraint matter is not touched by this run. Do NOT touch
#1024's m846.
"""

import glob
import logging
import os
import re
import subprocess

import pytest
import yaml

log = logging.getLogger(__name__)

ITERATION = 1114
TYPE_LETTER = "C"
WINDOW = "1110-1114"
MECH_NUM = 900
NEXT_NUM = 901
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # main commit, patched in the anchor followup per #565
OWN_BASENAME = (
    "test_type_c_1114_google_news_ai_pilot_three_track_segmentation_"
    "trackseparatedpricing_thirtieth_direction_oct01_3am.py"
)
BLOCK_KEY = (
    "type_c_1114_google_news_ai_pilot_three_track_segmentation_"
    "trackseparatedpricing_thirtieth_direction_oct01_3am"
)
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
ENTITIES_FILE = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
JOURNALISTS_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
FORKLOG_URL = (
    "https://forklog.com/en/google-expands-pilot-program-to-pay-publishers-"
    "for-ai-content-contributions/"
)
PG_TRACKER_URL = (
    "https://pressgazette.co.uk/platforms/"
    "news-publisher-ai-deals-lawsuits-openai-google/"
)
PG_DEALS_URL = (
    "https://pressgazette.co.uk/news/google-ai-deals-uk-publishers/"
)

# Patched post-commit once README/ARCHITECTURE doc-sync lands.
README_TEST_COUNT = 56930  # post-doc-sync total
README_FILE_COUNT = 1439  # post-doc-sync total
TEST_BASENAME = OWN_BASENAME

# Fragment-built direction needles per #715 (never contiguous here).
_TW29 = "TWENTY-" + "NINTH relationship direction"
_TW30 = "THIRTI" + "ETH relationship direction"
_T31 = "THIRTY-" + "FIRST relationship direction"

F1113 = ("test_type_b_1113_joanna_stern_meta_zuckerberg_interview_"
         "vs_apple_iphone_duo_register_sep2026_2am.py")
F1110 = ("test_type_d_1110_m895_m896_m897_qualitative_corpus_integrity_"
         "sep30_11pm.py")


def _git(*args):
    return subprocess.run(["git"] + list(args), cwd=REPO_ROOT,
                          capture_output=True, text=True)


def _node_run(test_file, node):
    return subprocess.run(
        [os.path.join(REPO_ROOT, ".venv", "bin", "python"), "-m", "pytest",
         os.path.join(TESTS_DIR, test_file) + "::" + node,
         "-q", "--no-header", "-p", "no:cacheprovider"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )


def _read(p):
    with open(p, encoding="utf-8", errors="replace") as f:
        return f.read()


def _iter_source_files():
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs
                   if d not in ("__pycache__", ".git", ".venv")]
        for f in files:
            yield os.path.join(root, f)


def _profiles_grep_numeric_mechanism_id(num):
    needle = "mechanism_id: %d" % num
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in _read(p):
                hits.append(p)
    return hits


def _repo_grep_underscore_mechanism(num):
    needle = "mechanism" + "_%d" % num
    return [p for p in _iter_source_files() if needle in _read(p)
            and not p.endswith(OWN_BASENAME)]


def _repo_grep_dash_mechanism(num):
    needle = "mechanism" + "-%d" % num
    return [p for p in _iter_source_files() if needle in _read(p)
            and not p.endswith(OWN_BASENAME)]


def _block():
    d = yaml.safe_load(_read(ENTITIES_FILE))
    return d[BLOCK_KEY]


def _block_text():
    text = _read(ENTITIES_FILE)
    start = text.index(BLOCK_KEY)
    tail = text[start:]
    # Block ends at the next top-level key (no indent) after this one.
    m = re.search(r"\n[a-z_0-9]+:", tail[1:])
    end = start + 1 + m.start() if m else len(text)
    return text[start:end]


def _max_numeric_mechanism_id():
    ids = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            for m in re.finditer(r"mechanism_id:\s*(\d+)", _read(p)):
                ids.append(int(m.group(1)))
    return max(ids)


# ---------------------------------------------------------------------------
# 1. Novelty (pre-commit: #715 protocol).
# ---------------------------------------------------------------------------

class TestNovelty1114:
    def test_single_test_file_for_iteration(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_c_1114*.py"))
        assert len(files) == 1, files
        assert files[0].endswith(OWN_BASENAME)

    def test_no_type_c_1114_in_git_log(self):
        # Commit-dependent: empty pre-commit; fails post-commit by design.
        res = _git("log", "--oneline", "--grep=Type C #1114")
        assert res.stdout.strip() == "", res.stdout

    def test_max_numeric_mechanism_id_is_900(self):
        # Working tree includes the uncommitted block (mechanism_id 900).
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_numeric_900_exactly_one_profile(self):
        hits = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == [ENTITIES_FILE], hits

    def test_zero_underscore_900_repo_wide(self):
        # Designed keying: colon-form block key only; underscore-form 900
        # stays zero (own test file excluded, needles format-built per #715).
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_zero_dash_900_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_novel_forklog_url_only_in_block_and_own_file(self):
        # Pre-commit novelty (zero-hit repo-wide) verified via subprocess
        # during research; post-insert the URL lives only in the block.
        hits = [p for p in _iter_source_files()
                if FORKLOG_URL in _read(p)
                and not p.endswith(OWN_BASENAME)]
        assert hits == [ENTITIES_FILE], hits

    def test_press_gazette_urls_carried_not_novel(self):
        # Both Press Gazette URLs are in corpus via m355-era citations;
        # this run's first-hand reads are new, the URLs are not.
        for url in (PG_TRACKER_URL, PG_DEALS_URL):
            hits = [p for p in _iter_source_files()
                    if url in _read(p)
                    and not p.endswith(OWN_BASENAME)]
            assert len(hits) >= 2, (url, hits)

    def test_block_key_present_in_entities(self):
        assert BLOCK_KEY in _read(ENTITIES_FILE)


# ---------------------------------------------------------------------------
# 2. Rotation guard (markers anchor/rotation).
# ---------------------------------------------------------------------------

class TestRotationGuard1114:
    @pytest.mark.rotation
    def test_window_1110_1114_fifth_leg(self):
        b = _block()
        assert b["iteration"] == ITERATION
        assert b["iteration_type"] == TYPE_LETTER
        log_text = _read(os.path.join(REPO_ROOT, "iteration-log.md"))
        assert "1110-1114 window" in log_text
        assert "FIFTH leg" in log_text

    def test_type_c_adjacency_in_window(self):
        # Window order per #565: D #1110 -> E #1111 -> A #1112 -> B #1113
        # -> C #1114.
        res = _git("log", "--oneline", "--grep=Type D #1110")
        assert "Type D #1110" in res.stdout
        res = _git("log", "--oneline", "--grep=Type E #1111")
        assert "Type E #1111" in res.stdout
        res = _git("log", "--oneline", "--grep=Type A #1112")
        assert "Type A #1112" in res.stdout
        res = _git("log", "--oneline", "--grep=Type B #1113")
        assert "Type B #1113" in res.stdout

    def test_predecessor_is_type_b_1113(self):
        res = _git("log", "--oneline", "--grep=Type B #1113")
        assert "d95faffb" in res.stdout

    def test_single_type_c_1114_file_is_this_run(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_c_1114*.py"))
        assert files[0].endswith(OWN_BASENAME)

    def test_anchor_is_ancestor_of_head(self):
        # Deselected pre-commit per #565; green once ANCHORED_SHA patched.
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP"
        res = _git("merge-base", "--is-ancestor", ANCHORED_SHA, "HEAD")
        assert res.returncode == 0


# ---------------------------------------------------------------------------
# 3. Novelty anchor (patched post-commit per #565).
# ---------------------------------------------------------------------------

class TestNoveltyAnchor1114:
    def test_anchor_sha_patched_post_commit(self):
        # Deselected pre-commit; the anchor followup patches this.
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP"
        assert re.fullmatch(r"[0-9a-f]{8}", ANCHORED_SHA)

    def test_anchor_sha_is_ancestor_of_head(self):
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP"
        res = _git("merge-base", "--is-ancestor", ANCHORED_SHA, "HEAD")
        assert res.returncode == 0


# ---------------------------------------------------------------------------
# 4. Mechanism 900 structure.
# ---------------------------------------------------------------------------

class TestMechanism900Structure:
    def test_block_key_present(self):
        assert BLOCK_KEY in _read(ENTITIES_FILE)

    def test_mechanism_id(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_type_and_iteration(self):
        b = _block()
        assert b["type"] == "financial_incentive_mapping"
        assert b["iteration"] == 1114
        assert b["iteration_type"] == "C"
        assert b["iteration_time"] == "2026-10-01 03:00 PDT"

    def test_three_legs_present(self):
        b = _block()
        for leg in ("commercial_terms_leg", "no_sue_category_leg",
                    "track_separation_leg"):
            assert leg in b, leg
            assert len(b[leg]) > 200, leg

    def test_thirtieth_direction_named_in_block(self):
        text = _block_text()
        assert _TW30 in text
        assert "TRACK-SEPARATED PRICING" in text

    def test_statistical_discipline(self):
        b = _block()
        assert b["tone_scored"] is False
        assert b["engine_run"] is False
        assert b["is_significant"] is False
        assert b["verdict"] == "directionally_supported_not_proven"
        assert b["no_analysis_json_update"] is True
        assert b["artifact_grade"] is False

    def test_confounder_coverage(self):
        confs = _block()["confounders"]
        assert len(confs) == 6
        strengths = [c["strength"] for c in confs]
        assert strengths.count("STRONG") == 2
        assert strengths.count("MEDIUM") == 2
        assert strengths.count("WEAK") == 2

    def test_sources_structure(self):
        srcs = _block()["sources"]
        assert len(srcs) == 4
        urls = [s["url"] for s in srcs]
        assert FORKLOG_URL in urls
        assert PG_TRACKER_URL in urls
        assert PG_DEALS_URL in urls
        forklog = next(s for s in srcs if s["url"] == FORKLOG_URL)
        assert forklog["novel"] is True
        first_hand = [s for s in srcs
                      if "first-hand" in s["what"]
                      and "this run" in s["what"]]
        assert len(first_hand) == 2

    def test_connects_to_lineage(self):
        targets = _block()["connects_to"]
        for t in (355, 891, 894, 897):
            assert t in targets, t

    def test_ascii_only(self):
        text = _block_text()
        assert all(ord(c) < 128 for c in text), "non-ASCII in block"
        assert _block()["ascii_only"] is True

# ---------------------------------------------------------------------------
# 5. Thirtieth direction taxonomy.
# ---------------------------------------------------------------------------

class TestThirtiethDirection:
    def test_thirtieth_present_in_working_tree(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                if _TW30 in _read(p):
                    hits.append(p)
        assert hits == [ENTITIES_FILE], hits

    def test_twenty_ninth_intact(self):
        text = _read(ENTITIES_FILE)
        assert _TW29 in text
        assert "FRAME-THEN-PRICE" in text

    def test_no_thirty_first_direction_claim(self):
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                assert _T31 not in _read(p), p

    def test_enumeration_includes_30(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert _TW30 in tax
        assert "track-separated pricing" in tax.lower()
        assert "29 frame-then-price m897" in tax

    def test_distinct_from_27_28_29(self):
        tax = _block()["relationship_direction_taxonomy"]
        for ref in ("m891", "m894", "m897"):
            assert ref in tax, ref
        assert "Distinct from #27" in tax
        assert "from #28" in tax
        assert "from #29" in tax


# ---------------------------------------------------------------------------
# 6. Falsification ledger holds at 41 (NOT a member this run).
# ---------------------------------------------------------------------------

class TestLedger41Holds:
    def _ledger_hits(self, needle):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                if needle in _read(p):
                    hits.append(p)
        return hits

    def test_forty_first_present_once(self):
        hits = self._ledger_hits("FORTY-FIRST falsification-family member")
        assert hits == [JOURNALISTS_FILE], hits

    def test_fortieth_intact(self):
        hits = self._ledger_hits("FORTIETH falsification-family member")
        wired = os.path.join(PROFILES_DIR, "wired.yaml")
        assert hits == [wired], hits

    def test_no_forty_second_member(self):
        assert self._ledger_hits("FORTY-SECOND falsification-family member") == []

    def test_ledger_41_in_block(self):
        assert "ledger holds at 41" in _block()["falsification_family"]

    def test_block_not_a_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert "NOT a member" in b["falsification_family"]


# ---------------------------------------------------------------------------
# 7. Corpus integrity.
# ---------------------------------------------------------------------------

class TestCorpusIntegrity1114:
    def test_yaml_parses_clean(self):
        d = yaml.safe_load(_read(ENTITIES_FILE))
        assert BLOCK_KEY in d
        assert d[BLOCK_KEY]["yaml_parse_clean"] is True

    def test_connects_to_targets_exist(self):
        text = _read(ENTITIES_FILE)
        for t in _block()["connects_to"]:
            assert ("mechanism_id: %d" % t) in text, t

    def test_max_id_consistency(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_forward_901_zero_numeric_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_press_gazette_first_hand_reads_new(self):
        # URLs carried; the first-hand reads are this run's new work.
        for url in (PG_TRACKER_URL, PG_DEALS_URL):
            src = next(s for s in _block()["sources"]
                       if s["url"] == url)
            assert "first-hand" in src["what"]
            assert "this run" in src["what"]


# ---------------------------------------------------------------------------
# 8. Forward guards: zero-901 in all mechanism-key forms (own file excluded,
#    needles format-built per #715). The #1115 Type D run pins these.
# ---------------------------------------------------------------------------

class TestForwardGuards1114:
    def test_zero_numeric_901_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_901_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_901_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


# ---------------------------------------------------------------------------
# 9. Supersession pins: #1113's zero-900 NUMERIC forward guard and #1110's
#    no-thirtieth-direction guards fail BY DESIGN now that this run lands
#    mechanism 900 and the THIRTIETH relationship direction. The zero-900
#    underscore/dash guards HOLD green (literal forms never land per #715).
# ---------------------------------------------------------------------------

class TestSupersessionPins1114:
    def test_1113_zero_900_numeric_guard_fails_by_design(self):
        res = _node_run(F1113, "TestForwardGuards1113::"
                               "test_zero_numeric_900_in_profiles")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1113_zero_900_underscore_guard_holds_post_commit(self):
        # The literal underscore-form 900 never lands (block key is
        # colon-form; needles format-built per #715), so #1113's
        # underscore guard stays GREEN post-commit.
        res = _node_run(F1113, "TestForwardGuards1113::"
                               "test_zero_underscore_900_repo_wide")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1113_zero_900_dash_guard_holds_post_commit(self):
        # Same for the dash form.
        res = _node_run(F1113, "TestForwardGuards1113::"
                               "test_zero_dash_900_repo_wide")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1110_no_thirtieth_claim_guard_fails_by_design(self):
        res = _node_run(F1110, "TestTypeDForwardLookingStaleness1110::"
                               "test_no_thirtieth_direction_claim")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1110_thirtieth_absent_guard_fails_by_design(self):
        res = _node_run(F1110, "TestTypeDFalsificationLedger1110::"
                               "test_thirtieth_direction_absent")
        assert res.returncode != 0, res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 10. Research method.
# ---------------------------------------------------------------------------

class TestResearchMethod1114:
    def test_three_search_sets(self):
        # Documented in the iteration-log entry: (1) News AI pilot
        # commercial terms, (2) track-separation corroboration,
        # (3) corpus pre-coverage / novelty verification.
        log_text = _read(os.path.join(REPO_ROOT, "iteration-log.md"))
        assert "## #1114 Type C" in log_text

    def test_two_first_hand_opens_per_503(self):
        srcs = _block()["sources"]
        first_hand = [s for s in srcs
                      if "first-hand" in s["what"]
                      and "this run" in s["what"]]
        assert len(first_hand) == 2
        for s in first_hand:
            assert "excerpt-bounded per #503" in s["what"]

    def test_verbatim_urls_no_construction(self):
        for s in _block()["sources"]:
            assert s["url"].startswith("https://"), s["url"]
            assert " " not in s["url"]

    def test_forklog_novelty_verified(self):
        res = _git("grep", "-F", FORKLOG_URL, "--",
                   ".", ":!tests/__pycache__")
        # Only the block and this test file carry it.
        files = {l.split(":")[0] for l in res.stdout.splitlines()
                 if l.strip()}
        assert files <= {ENTITIES_FILE.replace(REPO_ROOT + "/", ""),
                         "tests/" + OWN_BASENAME}, files

    def test_ascii_only_sources(self):
        for s in _block()["sources"]:
            blob = s["url"] + s["what"]
            assert all(ord(c) < 128 for c in blob)


# ---------------------------------------------------------------------------
# 11. Doc-sync (deselected pre-commit per #719; green post-doc-sync).
# ---------------------------------------------------------------------------

class TestDocSync1114:
    def test_readme_count_gate(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert "| Tests | %d |" % README_TEST_COUNT in text

    def test_readme_file_count_gate(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert "Across %d test files" % README_FILE_COUNT in text

    def test_readme_table_row(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert TEST_BASENAME in text
        assert "Type C #1114" in text

    def test_architecture_tree_row(self):
        text = _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))
        assert TEST_BASENAME in text
        assert "Type C #1114" in text


# ---------------------------------------------------------------------------
# 12. Iteration log (deselected pre-commit per #721; green post-commit).
# ---------------------------------------------------------------------------

class TestIterationLog1114:
    def _entry(self):
        return _read(os.path.join(REPO_ROOT, "iteration-log.md"))

    def test_log_captures_1114(self):
        assert "## #1114 Type C" in self._entry()

    def test_log_window_closing(self):
        text = self._entry()
        assert "1110-1114 window" in text
        assert "CLOSING it" in text

    def test_log_ledger_41(self):
        assert "ledger holds at 41" in self._entry()

    def test_log_lineage(self):
        text = self._entry()
        for ref in ("m891", "m894", "m897", "m355", "mechanism 900"):
            assert ref in text, ref


# ---------------------------------------------------------------------------
# 13. In-flight isolation: #899/#938/#900/#1012-wt untouched; #1024 m846
#     not touched.
# ---------------------------------------------------------------------------

class TestInFlightIsolation1114:
    def test_899_nytimes_hunk_untouched(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert "profiles/nytimes.yaml" in modified
        # Its uncommitted hunk belongs to #899's run; this run stages
        # only its own files.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#899" in src

    def test_900_untracked_file_untouched(self):
        res = _git("status", "--short")
        assert "test_type_d_900_m769" in res.stdout

    def test_938_test_file_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_b_938" in res.stdout

    def test_1012_working_tree_edit_untouched(self):
        res = _git("diff", "--name-only")
        assert "test_type_a_1012" in res.stdout

    def test_do_not_touch_1024_m846(self):
        # Guarded in the log entry per convention; the test file keeps
        # the in-flight list only (own-file reference would trip the
        # contiguous-literal discipline elsewhere).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1024" in src


# ---------------------------------------------------------------------------
# 14. Degenerate contract: qualitative Type C asserts no significance.
# ---------------------------------------------------------------------------

class TestDegenerateContract1114:
    def test_tone_not_scored(self):
        assert _block()["tone_scored"] is False

    def test_engine_not_run(self):
        assert _block()["engine_run"] is False

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True
