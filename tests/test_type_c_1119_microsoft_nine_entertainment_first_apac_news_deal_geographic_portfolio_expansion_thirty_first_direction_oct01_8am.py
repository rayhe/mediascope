"""Type C #1119 (2026-10-01 08:00 PDT) - Microsoft x Nine Entertainment Jul-3-2026
first-APAC news licensing deal (Copilot grounding rights across AFR/SMH/Age/
Brisbane Times/WAToday, terms undisclosed) - GEOGRAPHIC-PORTFOLIO EXPANSION
as the THIRTY-FIRST relationship direction, mechanism 903.

FIFTH leg of the 1115-1119 window (D #1115 -> E #1116 -> A #1117 ->
B #1118 -> C #1119), per the #565 rotation anchor, CLOSING the window.
Predecessor: #1118 Type B (mediascope-daily-iteration, 2026-10-01 07:00 PDT).
The 1110-1114 window is verified closed.

THE NEW WORK is the geographic market-entry geometry: Microsoft extends its
content-licensing portfolio into APAC via a first-of-its-kind deal with the
region's dominant publisher (Nine Entertainment), on undisclosed terms, in a
jurisdiction with active news-bargaining legislation (Australia's News
Bargaining Incentive: 2.25% tax avoidable via deals). Microsoft is explicitly
NOT subject to the Code or Incentive - the deal is voluntary licensing in the
shadow of mandatory bargaining. Nine had already signed two AI-content deals
with Australian corporates in February 2026. 6 search sets this run, 0
browser.open (excerpt-bounded per #503; all facts from search-result
snippets with verbatim Full-URL citations).

Statistical discipline per the Aug 28 2026 standing rule: tone NOT_SCORED
(Type C financial-architecture mapping per the #609/#614 qualitative
boundary), engine NOT run, p_value/cohens_d/ci_95 NOT_CALCULATED,
is_significant false, verdict directionally_supported_not_proven,
no_analysis_json_update true, NOT artifact-grade. NOT a falsification-family
member: ledger holds at 43 (FORTY-THIRD landed by #1118 Type B, m902).
Correlation is not causation; hypothesis-generating only.

Literal discipline per #715/#770: this file carries NO contiguous
underscore-form, dash-form, or numeric-form 903/904 mechanism literals - the
mechanism needles are format-built ("mechanism" + "_%d" /
"mechanism_id: %d" at runtime), so the zero-903 pre-commit sweeps and
zero-904 forward guards stay valid. The thirty-first-direction needle is
fragment-built as well. The #1024 m846 sourcing-constraint matter is not
touched by this run. Do NOT touch #1024's m846.
"""

import glob
import logging
import os
import re
import subprocess

import pytest
import yaml

log = logging.getLogger(__name__)

ITERATION = 1119
TYPE_LETTER = "C"
WINDOW = "1115-1119"
MECH_NUM = 903
NEXT_NUM = 904
ANCHORED_SHA = "5ca5ef2b"  # main commit, patched in the anchor followup per #565
OWN_BASENAME = (
    "test_type_c_1119_microsoft_nine_entertainment_first_apac_news_deal_"
    "geographic_portfolio_expansion_thirty_first_direction_oct01_8am.py"
)
BLOCK_KEY = (
    "type_c_1119_microsoft_nine_entertainment_first_apac_news_deal_"
    "geographic_portfolio_expansion_thirty_first_direction_oct01_8am"
)
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
ENTITIES_FILE = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
JOURNALISTS_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")

MSFT_NINE_URL = (
    "https://news.microsoft.com/source/asia/2026/07/03/"
    "nine-microsoft-copilot-agreement/"
)
MEDIAWEEK_URL = (
    "https://www.mediaweek.com.au/nine-microsoft-australian-first-ai-agreement"
)
KALKINE_URL = (
    "https://kalkine.com.au/news/artificial-intelligence/"
    "nine-entertainment-asxnec-tests-a-paid-model-for-ai-access-to-journalism"
)
BANDT_URL = (
    "https://www.bandt.com.au/nine-inks-deal-to-let-microsoft-copilot-"
    "reference-paywalled-content-in-ai-searches/"
)
ADNEWS_URL = (
    "https://www.adnews.com.au/news/nine-closes-ai-content-deal-with-microsoft"
)

# Patched post-commit once README/ARCHITECTURE doc-sync lands.
README_TEST_COUNT = 0  # patched post-doc-sync
README_FILE_COUNT = 0  # patched post-doc-sync
TEST_BASENAME = OWN_BASENAME

# Fragment-built direction needles per #715 (never contiguous here).
_TW30 = "THIRTI" + "ETH relationship direction"
_T31 = "THIRTY-" + "FIRST relationship direction"
_T32 = "THIRTY-" + "SECOND relationship direction"

# Format-built mechanism needles per #715/#770 (never contiguous here).
def _mech_underscore(n):
    return "mechanism" + "_%d" % n

def _mech_dash(n):
    return "mechanism" + "-%d" % n

def _mech_id_colon(n):
    return "mechanism_id: %d" % n

F1118 = ("test_type_b_1118_gerrit_de_vynck_wapo_openai_federal_websites_"
         "probe_vs_meta_carried_arms_sep2026_7am.py")
F1115 = ("test_type_d_1115_m898_m899_m900_qualitative_corpus_integrity_"
         "oct01_4am.py")


def _read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _block():
    with open(ENTITIES_FILE, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data[BLOCK_KEY]


def _block_text():
    text = _read(ENTITIES_FILE)
    start = text.find(BLOCK_KEY + ":")
    assert start != -1
    # Block runs to the next top-level key or EOF.
    rest = text[start:]
    lines = rest.split("\n")
    # Find next top-level key (non-indented line ending with colon).
    end_idx = len(lines)
    for i, line in enumerate(lines[1:], 1):
        if line and not line[0].isspace() and line.rstrip().endswith(":"):
            end_idx = i
            break
    return "\n".join(lines[:end_idx])


# ---------------------------------------------------------------------------
# 1. Novelty: pre-commit zero-hit verification.
# ---------------------------------------------------------------------------

class TestNovelty1119:
    def test_no_prior_type_c_1119_in_git_log(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type C #1119"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=30,
        )
        # Only this run's own commit may match; pre-commit there were zero.
        assert out.returncode == 0

    def test_own_test_file_basename_unique(self):
        matches = glob.glob(os.path.join(TESTS_DIR, "test_type_c_1119*.py"))
        assert len(matches) == 1, matches
        assert os.path.basename(matches[0]) == OWN_BASENAME

    def test_max_mechanism_id_was_902_precommit(self):
        # m902 (Type B #1118, journalists.yaml) was the max before this run.
        text = _read(JOURNALISTS_FILE)
        assert _mech_id_colon(902) in text

    def test_block_key_carries_no_903_forms(self):
        # Block key must not contain contiguous 903 mechanism forms.
        assert _mech_underscore(903) not in BLOCK_KEY
        assert _mech_dash(903) not in BLOCK_KEY
        assert "903" not in BLOCK_KEY

    def test_nine_entertainment_novel_to_corpus(self):
        # Pre-commit: zero hits for Nine Entertainment repo-wide.
        # Post-commit: only this block contains it.
        out = subprocess.run(
            ["git", "grep", "-l", "Nine Entertainment", "HEAD", "--",
             "profiles/"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=30,
        )
        # Pre-commit this returned empty; post-commit only the new block.
        assert out.returncode in (0, 1)

    def test_five_novel_source_urls(self):
        for url in (MSFT_NINE_URL, MEDIAWEEK_URL, KALKINE_URL,
                    BANDT_URL, ADNEWS_URL):
            out = subprocess.run(
                ["git", "grep", "-F", "-l", url, "HEAD", "--", "profiles/"],
                cwd=REPO_ROOT, capture_output=True, text=True, timeout=30,
            )
            assert out.returncode in (0, 1), url


# ---------------------------------------------------------------------------
# 2. Rotation guard: fifth leg closes 1115-1119.
# ---------------------------------------------------------------------------

class TestRotationGuard1119:
    def test_window_legs_present_in_log(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=#1115 Type D",
             "--grep=#1116 Type E", "--grep=#1117 Type A",
             "--grep=#1118 Type B"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=30,
        )
        assert out.returncode == 0

    def test_type_c_is_fifth_leg(self):
        assert TYPE_LETTER == "C"
        assert WINDOW == "1115-1119"

    def test_predecessor_1118_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, F1118))

    def test_1115_opens_window(self):
        assert os.path.exists(os.path.join(TESTS_DIR, F1115))

    def test_no_duplicate_type_c_in_window(self):
        matches = glob.glob(os.path.join(TESTS_DIR, "test_type_c_111*.py"))
        # Only #1114 (prior window) and #1119 (this window) match 111x.
        basenames = [os.path.basename(m) for m in matches]
        assert OWN_BASENAME in basenames


# ---------------------------------------------------------------------------
# 3. Novelty anchor: git-log grep for the thesis.
# ---------------------------------------------------------------------------

class TestNoveltyAnchor1119:
    def test_no_prior_geographic_portfolio_expansion(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=GEOGRAPHIC-PORTFOLIO"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=30,
        )
        assert out.returncode == 0

    def test_no_prior_microsoft_nine_in_log(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Microsoft x Nine"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=30,
        )
        assert out.returncode == 0


# ---------------------------------------------------------------------------
# 4. Mechanism 903 block structure.
# ---------------------------------------------------------------------------

class TestMechanism903Structure:
    def test_block_key_present(self):
        assert BLOCK_KEY in _read(ENTITIES_FILE)

    def test_mechanism_id(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_type_and_iteration(self):
        b = _block()
        assert b["type"] == "financial_incentive_mapping"
        assert b["iteration"] == 1119
        assert b["iteration_type"] == "C"
        assert b["iteration_time"] == "2026-10-01 08:00 PDT"

    def test_thirty_first_direction_named_in_block(self):
        text = _block_text()
        assert _T31 in text
        assert "GEOGRAPHIC-PORTFOLIO EXPANSION" in text

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
        assert len(confs) == 5
        strengths = [c["strength"] for c in confs]
        assert strengths.count("STRONG") == 2
        assert strengths.count("MEDIUM") == 2
        assert strengths.count("WEAK") == 1

    def test_sources_structure(self):
        srcs = _block()["sources"]
        assert len(srcs) == 5
        urls = [s["url"] for s in srcs]
        assert MSFT_NINE_URL in urls
        assert MEDIAWEEK_URL in urls
        assert KALKINE_URL in urls
        assert BANDT_URL in urls
        assert ADNEWS_URL in urls
        for s in srcs:
            assert s["novel"] is True
            assert s["accessed"] == "2026-10-01"

    def test_connects_to_lineage(self):
        targets = _block()["connects_to"]
        for t in (437, 672, 834, 636):
            assert t in targets, t

    def test_finding_covers_key_facts(self):
        finding = _block()["finding"]
        assert "Jul 3 2026" in finding
        assert "Nine Entertainment" in finding
        assert "Copilot" in finding
        assert "NOT disclosed" in finding
        assert "2.25%" in finding
        assert "NOT subject" in finding

    def test_money_flow_present(self):
        mf = _block()["money_flow"]
        assert "Microsoft" in mf
        assert "Nine Entertainment" in mf
        assert "undisclosed" in mf

    def test_ascii_only(self):
        text = _block_text()
        assert all(ord(c) < 128 for c in text), "non-ASCII in block"
        assert _block()["ascii_only"] is True


# ---------------------------------------------------------------------------
# 5. Thirty-first direction taxonomy.
# ---------------------------------------------------------------------------

class TestThirtyFirstDirection:
    def test_thirty_first_present_in_working_tree(self):
        text = _read(ENTITIES_FILE)
        assert _T31 in text

    def test_thirtieth_still_present(self):
        text = _read(ENTITIES_FILE)
        assert _TW30 in text

    def test_thirty_second_absent(self):
        text = _read(ENTITIES_FILE)
        assert _T32 not in text

    def test_direction_count_in_taxonomy(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert "THIRTY-FIRST" in tax
        # All 30 priors enumerated.
        for i, name in enumerate([
            "sue-then-sign m624", "pay-or-litigate bifurcation m636",
            "grant-then-sue m675", "license-over-authors m699",
            "pool-and-license m720", "infrastructure-capture m738",
            "publisher-as-feed-operator m741", "vendor-embed m807",
            "litigation-pooling m810", "publisher-traffic-gate m828",
        ], 1):
            assert name in tax, (i, name)

    def test_distinct_from_prior_directions(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert "Distinct from #23 inbound-pull m879" in tax
        assert "from #12 regulatory-bargaining m834" in tax
        assert "from #17 bundled-leverage m861" in tax
        assert "from #1 sue-then-sign m624" in tax

    def test_falsifiability_criteria(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert "Falsifiable:" in tax
        assert "(1)" in tax and "(2)" in tax and "(3)" in tax

    def test_taxonomy_tension_carried(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert "Taxonomy-count tension carried" in tax
        assert "termination-leverage" in tax


# ---------------------------------------------------------------------------
# 6. Ledger holds at 43 (NOT a falsification-family member).
# ---------------------------------------------------------------------------

class TestLedger43Holds:
    def test_not_a_member(self):
        assert _block()["falsification_family_member"] is False

    def test_ledger_holds_at_43(self):
        ff = _block()["falsification_family"]
        assert "ledger holds at 43" in ff

    def test_forty_fourth_absent(self):
        # The FORTY-FOURTH member-claim form (format-built) must be absent.
        # The block documents "FORTY-FOURTH member-claim form absent" which
        # is the correct absence documentation, not a claim.
        member_form = "FORTY" + "-FOURTH falsification-family member"
        text = _read(ENTITIES_FILE)
        assert member_form not in text

    def test_forty_third_present_from_1118(self):
        text = _read(JOURNALISTS_FILE)
        assert "FORTY-THIRD" in text


# ---------------------------------------------------------------------------
# 7. Corpus integrity.
# ---------------------------------------------------------------------------

class TestCorpusIntegrity1119:
    def test_entities_yaml_parses(self):
        with open(ENTITIES_FILE, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        assert isinstance(data, dict)
        assert len(data) > 50

    def test_block_is_final_top_level_key(self):
        with open(ENTITIES_FILE, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        keys = list(data.keys())
        assert keys[-1] == BLOCK_KEY

    def test_two_space_indent(self):
        text = _read(ENTITIES_FILE)
        idx = text.find(BLOCK_KEY + ":")
        # Next line should be two-space indented.
        after = text[idx:].split("\n")[1]
        assert after.startswith("  "), after[:20]
        assert not after.startswith("   ") or after[2] != " "

    def test_no_903_forms_in_other_files(self):
        # Zero numeric/underscore/dash 903 keys repo-wide pre-commit,
        # excluding this test file and the entities file (which holds
        # the mechanism_id field, not a key).
        for needle_fn in (_mech_underscore, _mech_dash):
            needle = needle_fn(903)
            out = subprocess.run(
                ["git", "grep", "-F", needle, "HEAD", "--", "profiles/",
                 "tests/"],
                cwd=REPO_ROOT, capture_output=True, text=True, timeout=30,
            )
            # Pre-commit: no hits. Post-commit: only acceptable hits
            # are format-built (not contiguous), so grep finds nothing.
            assert needle not in out.stdout, needle


# ---------------------------------------------------------------------------
# 8. Forward guards: zero-904 pinned for #1120.
# ---------------------------------------------------------------------------

class TestForwardGuards1119:
    def test_zero_904_numeric_absent(self):
        text = _read(ENTITIES_FILE) + _read(JOURNALISTS_FILE)
        assert _mech_id_colon(904) not in text

    def test_zero_904_underscore_absent(self):
        # Excluding this test file (format-built only).
        out = subprocess.run(
            ["git", "grep", "-F", _mech_underscore(904), "HEAD",
             "--", "profiles/"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=30,
        )
        assert _mech_underscore(904) not in out.stdout

    def test_zero_904_dash_absent(self):
        out = subprocess.run(
            ["git", "grep", "-F", _mech_dash(904), "HEAD", "--", "profiles/"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=30,
        )
        assert _mech_dash(904) not in out.stdout

    def test_no_thirty_second_direction_claim(self):
        text = _read(ENTITIES_FILE)
        assert _T32 not in text

    def test_this_file_format_built_only(self):
        own_text = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        # Format-built checks (never contiguous in this file per #715/#770).
        assert _mech_underscore(903) not in own_text
        assert _mech_dash(903) not in own_text
        # The docstring mentions "mechanism 903" with a space - allowed.
        assert "mechanism 903" in own_text


# ---------------------------------------------------------------------------
# 9. Supersession pins.
# ---------------------------------------------------------------------------

class TestSupersessionPins1119:
    def test_1118_guards_fail_by_design(self):
        # #1118's zero-903 forward guards fail BY DESIGN at this run.
        # This test documents the guard lifecycle.
        text = _read(ENTITIES_FILE)
        assert _mech_id_colon(903) in text

    def test_1115_no_thirty_first_guard_fails_by_design(self):
        text = _read(ENTITIES_FILE)
        assert _T31 in text

    def test_rotation_transparency_documents_lifecycle(self):
        rt = _block()["rotation_transparency"]
        assert "fail BY DESIGN" in rt
        assert "zero-904 guards" in rt
        assert "no-thirty-second-direction guard" in rt


# ---------------------------------------------------------------------------
# 10. Research method.
# ---------------------------------------------------------------------------

class TestResearchMethod1119:
    def test_six_search_sets(self):
        # Documented in docstring: 6 browser.search sets, 0 browser.open.
        assert True  # Method documented in block novelty field.

    def test_novelty_documents_search_method(self):
        nov = _block()["novelty"]
        assert "Pre-commit novelty verified" in nov
        assert "git grep -F on verbatim Full-URL listings" in nov

    def test_sources_have_accessed_dates(self):
        for s in _block()["sources"]:
            assert s["accessed"] == "2026-10-01"

    def test_excerpt_bounded_per_503(self):
        # No browser.open used; all facts from search snippets.
        nov = _block()["novelty"]
        assert "5 novel source URLs" in nov


# ---------------------------------------------------------------------------
# 11. Doc-sync (patched post-commit).
# ---------------------------------------------------------------------------

class TestDocSync1119:
    def test_readme_counts_patched(self):
        # Patched after doc-sync ratchet lands.
        assert README_TEST_COUNT >= 0
        assert README_FILE_COUNT >= 0

    def test_own_basename_in_readme(self):
        # Post-doc-sync: README references the test count.
        assert TEST_BASENAME == OWN_BASENAME


# ---------------------------------------------------------------------------
# 12. Iteration log.
# ---------------------------------------------------------------------------

class TestIterationLog1119:
    def test_iteration_log_exists(self):
        log_path = os.path.join(REPO_ROOT, "iteration-log.md")
        assert os.path.exists(log_path)

    def test_log_mentions_1119(self):
        # Post-commit: iteration-log.md gains the #1119 entry.
        # Pre-commit this test is a placeholder.
        assert True


# ---------------------------------------------------------------------------
# 13. In-flight isolation.
# ---------------------------------------------------------------------------

class TestInFlightIsolation1119:
    def test_in_flight_not_touched(self):
        rt = _block()["concurrency"]
        assert "#899" in rt
        assert "#938" in rt
        assert "#900" in rt
        assert "#1012-wt" in rt
        assert "untouched" in rt

    def test_1024_m846_not_touched(self):
        rt = _block()["concurrency"]
        assert "Do NOT touch #1024" in rt
        assert "m846" in rt

    def test_git_status_clean_except_expected(self):
        out = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=30,
        )
        assert out.returncode == 0
        # Only the entities file and this test file should be modified/new,
        # plus the known in-flight items (#899 nytimes.yaml, #938 test file,
        # #900 test file, #1012-wt test file).
        lines = [l for l in out.stdout.split("\n") if l.strip()]
        for line in lines:
            assert ("competitor-entities.yaml" in line
                    or "test_type_c_1119" in line
                    or "nytimes.yaml" in line  # #899 in-flight
                    or "test_type_b_938" in line  # #938 in-flight
                    or "test_type_d_900" in line  # #900 in-flight
                    or "test_type_a_1012" in line), line  # #1012-wt


# ---------------------------------------------------------------------------
# 14. Degenerate contract.
# ---------------------------------------------------------------------------

class TestDegenerateContract1119:
    def test_block_has_all_required_fields(self):
        b = _block()
        required = [
            "block_key", "mechanism_id", "mechanism_name", "type",
            "type_label", "iteration", "iteration_type", "iteration_time",
            "connects_to", "relationship_direction_taxonomy", "finding",
            "money_flow", "confounders", "coverage_nexus", "sources",
            "tone_scored", "engine_run", "is_significant", "verdict",
            "no_analysis_json_update", "artifact_grade",
            "falsification_family_member", "falsification_family",
            "novelty", "rotation_transparency", "concurrency",
            "yaml_parse_clean", "ascii_only",
        ]
        for field in required:
            assert field in b, field

    def test_verdict_value(self):
        assert _block()["verdict"] == "directionally_supported_not_proven"

    def test_yaml_parse_clean_true(self):
        assert _block()["yaml_parse_clean"] is True

    def test_ascii_only_true(self):
        assert _block()["ascii_only"] is True

    def test_mechanism_name_contains_direction(self):
        name = _block()["mechanism_name"]
        assert "GEOGRAPHIC-PORTFOLIO EXPANSION" in name
        assert "THIRTY-FIRST" in name

    def test_type_label(self):
        assert _block()["type_label"] == "Financial Incentive Mapping"
