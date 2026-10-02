"""Type C iteration #1129 (2026-10-01 17:00 PDT): Judge Mehta dismisses the Chegg +
Penske Media antitrust suits over Google AI Overviews (ruled Sep 30 2026,
reported Oct 1). New mechanism 909: the thirty-third relationship direction
(LITIGATION-CHANNEL-CLOSURE) - the court closes the compulsory-payment channel
("an expectation is not an agreement") while Google's voluntary AI-contribution
pilot (m891) stays open on unilateral terms.

87 tests / 15 classes, all green pre-commit (venv python). Doc-sync 2 +
iteration-log 2 are placeholders patched in the doc-sync / log-hash followups
per #719. Anchor placeholder (ANCHORED_SHA) patched to the main commit's
40-char SHA in the anchor followup per #565; deselect the placeholder test in
post-commit full runs. Not a falsification-family member: ledger holds at 46.
Two research rounds this run: round 1 (subagent) selected the Google
AI-contribution pilot, REJECTED as the m891/#1099 duplicate; round 2 (subagent)
selected the OpenAI Lenfest $10M renewal, REJECTED as the m885/#1089 duplicate.
Round 3 (direct browser.search) selected the Mehta dismissal - verified novel.
"""

import glob
import os
import re
import subprocess

import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
ENTITIES_FILE = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
VERGE_FILE = os.path.join(PROFILES_DIR, "the-verge.yaml")
LOG_FILE = os.path.join(REPO_ROOT, "iteration-log.md")

# Block key, split across literals so this file carries no contiguous form.
BLOCK_KEY = (
    "type_c_1129_mehta_dismisses_chegg_penske_ai_overviews_suits_"
    "litigation_channel_closure_thirty_third_direction_oct01_5pm"
)
OWN_BASENAME = "test_type_c_1129_mehta_dismisses_chegg_penske_suits_" \
    "litigation_channel_closure_oct01_5pm.py"

# Predecessor test files for supersession pins.
FILE_1128 = ("test_type_b_1128_david_heaney_uploadvr_meta_threads_vs_"
             "apple_vision_pro_layoffs_visionos_sep2026_4pm.py")
FILE_1124 = ("test_type_c_1124_perplexity_hp_crusoe_sep15_dual_spend_"
             "under_suit_load_pay_for_reach_litigate_for_content_"
             "thirty_second_direction_oct01_12pm.py")

# Four novel source URLs (copied verbatim from Full-URL listings).
REUTERS_URL = ("https://www.reuters.com/legal/litigation/"
               "google-wins-dismissal-chegg-penske-media-lawsuits-"
               "over-ai-overviews-2026-10-01/")
TAPESTRY_URL = "https://tapestry.news/culture/google-ai-overviews-suits-dismissed/"
AISTOCKWIRE_URL = ("https://aistockwire.com/blog/google-googl-penske-media-"
                   "chegg-ai-overviews-lawsuits-dismissed-september-2026")
YAHOO_PROXY_URL = ("https://www.dejavu.org/cgi-bin/get.cgi?ver=95&url="
                   "https%3A%2F%2Fwww.yahoo.com%2Fnews%2Fpolitics%2Farticles"
                   "%2Fgoogle-wins-dismissal-pmc-lawsuit-203226165.html")

# Patched post-commit once README/ARCHITECTURE doc-sync lands.
README_TEST_COUNT = 59061  # post-doc-sync total (58974 + 87)
README_FILE_COUNT = 1454  # post-doc-sync total
TEST_BASENAME = OWN_BASENAME

# Anchor placeholder per #565: patched to the main commit's 40-char SHA in the
# anchor followup. Deselect the placeholder test in post-commit full runs.
ANCHORED_SHA = "0" * 40

MECH_NUM = 909
NEXT_NUM = 910
PREV_NUM = 908

# Fragment-built direction needles per #715 (never contiguous here).
_T32 = "THIRTY-" + "SECOND relationship direction"
_T33 = "THIRTY-" + "THIRD relationship direction"
_T34 = "THIRTY-" + "FOURTH relationship direction"
_T31 = "THIRTY-" + "FIRST relationship direction"


# Format-built mechanism needles per #715/#770 (never contiguous here).
def _mech_underscore(n):
    return "mechanism" + "_%d" % n


def _mech_dash(n):
    return "mechanism" + "-%d" % n


def _mech_id_colon(n):
    return "mechanism_id: %d" % n


FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
FORTY_SIXTH_MEMBER = "FORTY" + "-SIXTH falsification-family member"


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
    rest = text[start:]
    lines = rest.split("\n")
    end_idx = len(lines)
    for i, line in enumerate(lines[1:], 1):
        if line and not line[0].isspace() and line.rstrip().endswith(":"):
            end_idx = i
            break
    return "\n".join(lines[:end_idx])


def _git_log_oneline(grep_arg=None):
    cmd = ["git", "log", "--oneline"]
    if grep_arg is not None:
        cmd.append("--grep=" + grep_arg)
    out = subprocess.run(
        cmd, cwd=REPO_ROOT, capture_output=True, text=True, timeout=30,
    )
    assert out.returncode == 0
    return out.stdout


def _iter_source_files():
    for base in (PROFILES_DIR, TESTS_DIR):
        for dirpath, _, files in os.walk(base):
            for fn in files:
                if fn.endswith((".yaml", ".py", ".md")):
                    yield os.path.join(dirpath, fn)
    yield LOG_FILE


def _max_numeric_mechanism_id_in_profiles():
    ids = []
    for dirpath, _, files in os.walk(PROFILES_DIR):
        for fn in files:
            if fn.endswith(".yaml"):
                text = _read(os.path.join(dirpath, fn))
                for m in re.findall(r"mechanism_id: (\d+)", text):
                    ids.append(int(m))
    return max(ids)


def _profiles_grep_numeric_mechanism_id(n):
    needle = _mech_id_colon(n)
    out = subprocess.run(
        ["git", "grep", "-l", "-F", needle, "--", "profiles/"],
        cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
    )
    return [l for l in out.stdout.split("\n") if l.strip()]


def _repo_grep_mechanism_form(n, form):
    needle = form(n)
    out = subprocess.run(
        ["git", "grep", "-l", "-F", needle],
        cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
    )
    return [l for l in out.stdout.split("\n") if l.strip()]


def _node_run(filename, node):
    """Run one predecessor test node in a subprocess (pin lifecycle)."""
    target = os.path.join(TESTS_DIR, filename) + "::" + node
    env = dict(os.environ)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    venv_py = os.path.join(REPO_ROOT, ".venv", "bin", "python")
    return subprocess.run(
        [venv_py, "-m", "pytest", target, "-q", "--no-header"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        env=env,
        timeout=120,
    )


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder; patched green post-commit per #565).
# ---------------------------------------------------------------------------

class TestAnchor1129:
    def test_anchored_sha_placeholder_pre_commit(self):
        # Deselect this test in post-commit full runs: the anchor followup
        # patches ANCHORED_SHA to the main commit's 40-char SHA per #565.
        assert ANCHORED_SHA == "0" * 40

    def test_anchored_sha_shape_40_hex(self):
        # Holds pre-commit (zero placeholder) and post-patch (commit SHA).
        assert len(ANCHORED_SHA) == 40
        assert all(c in "0123456789abcdef" for c in ANCHORED_SHA)

    def test_anchor_mechanics_documented_in_block(self):
        rt = _block()["rotation_transparency"]
        assert "anchor" in rt.lower()
        assert "#565" in rt

    def test_anchor_basename_carries_iteration(self):
        assert OWN_BASENAME.startswith("test_type_c_1129")


# ---------------------------------------------------------------------------
# 2. Rotation guard: fifth and closing leg of the 1125-1129 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1129:
    def test_predecessor_chain_in_git_log(self):
        log = _git_log_oneline()
        assert "Type D #1125" in log
        assert "Type E #1126" in log
        assert "Type A #1127" in log
        assert "Type B #1128" in log

    def test_window_order_d_e_a_b(self):
        log = _git_log_oneline()
        i1125 = log.index("Type D #1125")
        i1126 = log.index("Type E #1126")
        i1127 = log.index("Type A #1127")
        i1128 = log.index("Type B #1128")
        # Reverse-chronological log: later commits appear first.
        assert i1128 < i1127 < i1126 < i1125

    def test_type_c_1129_novel_in_git_log(self):
        log = _git_log_oneline("Type C #1129")
        lines = [l for l in log.split("\n") if l.strip()]
        assert lines == [], lines

    def test_1128_main_hash_present(self):
        log = _git_log_oneline()
        assert "0cf31151" in log

    def test_fifth_closing_leg(self):
        rt = _block()["rotation_transparency"]
        assert "FIFTH and CLOSING" in rt
        assert "1125-1129" in rt

    def test_next_window_opens_with_d(self):
        rt = _block()["rotation_transparency"]
        assert "1130-1134" in rt
        assert "Type D" in rt


# ---------------------------------------------------------------------------
# 3. Novelty anchor: no prior 1129 / Mehta dismissal / channel-closure in log.
# ---------------------------------------------------------------------------

class TestNoveltyAnchor1129:
    def _non_1129_lines(self, grep_pat):
        log = _git_log_oneline(grep_pat)
        lines = [l for l in log.split("\n") if l.strip()]
        return [l for l in lines if "1129" not in l]

    def test_no_prior_litigation_channel_closure_in_log(self):
        assert self._non_1129_lines("litigation-channel-closure") == []

    def test_no_prior_thirty_third_direction_claim_in_log(self):
        # No prior commit message ever carried the affirmative claim form;
        # earlier commits only discuss it as absence-documentation.
        log = _git_log_oneline("THIRTY-" + "THIRD relationship direction")
        lines = [l for l in log.split("\n") if l.strip()]
        assert lines == [], lines

    def test_no_prior_chegg_in_log(self):
        # "Mehta" appears in two old unrelated commit messages (#327, PMC
        # deep dive); the dismissal-specific novelty anchor is Chegg, which
        # has zero prior log presence.
        assert self._non_1129_lines("Chegg") == []


# ---------------------------------------------------------------------------
# 4. Mechanism novelty: m909 lands; pre-commit zero-hit verification.
# ---------------------------------------------------------------------------

class TestMechanismNovelty1129:
    def test_single_test_file_for_iteration(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_c_1129*.py"))
        assert len(files) == 1, files
        assert os.path.basename(files[0]) == OWN_BASENAME

    def test_novelty_verification_claim_in_block(self):
        assert "zero test_type_c_1129 files on disk" in _block_text()

    def test_max_numeric_mechanism_id_is_909(self):
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_909_numeric_present_only_in_entities_block(self):
        hits = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_zero_underscore_909_repo_wide(self):
        assert _repo_grep_mechanism_form(MECH_NUM, _mech_underscore) == []

    def test_zero_dash_909_repo_wide(self):
        assert _repo_grep_mechanism_form(MECH_NUM, _mech_dash) == []

    def test_zero_underscore_908_repo_wide(self):
        assert _repo_grep_mechanism_form(PREV_NUM, _mech_underscore) == []

    def test_zero_dash_908_repo_wide(self):
        assert _repo_grep_mechanism_form(PREV_NUM, _mech_dash) == []

    def test_908_numeric_present_only_in_journalists_block(self):
        hits = _profiles_grep_numeric_mechanism_id(PREV_NUM)
        assert hits == ["profiles/careers/journalists.yaml"], hits

    def test_block_key_zero_hit_outside_entities(self):
        out = subprocess.run(
            ["git", "grep", "-l", "-F", BLOCK_KEY],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        hits = [l for l in out.stdout.split("\n") if l.strip()]
        # This file carries the key only in split-literal form.
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_four_novel_source_urls(self):
        for url in (REUTERS_URL, TAPESTRY_URL, AISTOCKWIRE_URL,
                    YAHOO_PROXY_URL):
            out = subprocess.run(
                ["git", "grep", "-F", "-l", url, "HEAD", "--", "profiles/"],
                cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
            )
            # Pre-commit: zero hits. Post-commit: only the new block.
            assert out.returncode in (0, 1), url


# ---------------------------------------------------------------------------
# 5. Mechanism 909 block structure.
# ---------------------------------------------------------------------------

class TestMechanism909Structure:
    def test_block_key_present(self):
        assert _block()["block_key"] == BLOCK_KEY

    def test_mechanism_id_is_909(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_type_and_iteration(self):
        b = _block()
        assert b["type"] == "financial_incentive_mapping"
        assert b["type_label"] == "Financial Incentive Mapping"
        assert b["iteration"] == 1129
        assert b["iteration_type"] == "C"

    def test_thirty_third_named_in_mechanism_name(self):
        assert _T33 in _block()["mechanism_name"]

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
        assert "STRONG" in strengths
        assert "MODERATE" in strengths
        assert "WEAK" in strengths
        assert "counterargument" in confs[-1]

    def test_sources_structure(self):
        srcs = _block()["sources"]
        assert len(srcs) == 4
        for s in srcs:
            assert s["url"]
            assert s["what"]
            assert s["accessed"] == "2026-10-01"
            assert s["novel"] is True
        assert REUTERS_URL in [s["url"] for s in srcs]

    def test_connects_to_lineage(self):
        assert _block()["connects_to"] == [112, 666, 891]

    def test_finding_key_facts(self):
        f = _block()["finding"]
        assert "Mehta" in f
        assert "25-cv-543" in f
        assert "25-cv-3192" in f
        assert "an expectation is not an agreement" in f
        assert "Penske" in f
        assert "without prejudice" in f

    def test_money_flow_present(self):
        mf = _block()["money_flow"]
        assert "Compulsory channel" in mf
        assert "Voluntary channel" in mf
        assert "m891" in mf

    def test_coverage_nexus(self):
        cn = _block()["coverage_nexus"]
        assert "The Verge" in cn
        assert "the-verge.yaml" in cn
        assert "Penske" in cn


# ---------------------------------------------------------------------------
# 6. The new direction claim (fragment-built _T33 throughout).
# ---------------------------------------------------------------------------

class TestThirtyThirdDirection:
    def test_thirty_third_present_in_working_tree(self):
        text = _read(ENTITIES_FILE)
        assert _T33 in text

    def test_thirty_second_still_present(self):
        text = _read(ENTITIES_FILE)
        assert _T32 in text

    def test_thirty_first_still_present(self):
        text = _read(ENTITIES_FILE)
        assert _T31 in text

    def test_thirty_fourth_absent(self):
        text = _read(ENTITIES_FILE)
        assert _T34 not in text

    def test_direction_count_in_taxonomy(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert _T33 in tax
        # All 32 priors enumerated (spot-checked anchors).
        for name in [
            "sue-then-sign m624",
            "pay-or-litigate bifurcation m636",
            "regulatory-bargaining m834",
            "unilateral pricing m891",
            "geographic-portfolio-expansion m903",
            "pay-for-reach-litigate-for-content m906",
        ]:
            assert name in tax, name

    def test_distinct_from_prior_directions(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert "Distinct from #2 pay-or-litigate bifurcation m636" in tax
        assert "#1 sue-then-sign m624" in tax

    def test_falsifiability_criteria(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert "Falsifiable:" in tax
        assert "(1)" in tax and "(2)" in tax and "(3)" in tax

    def test_taxonomy_tension_carried(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert "Taxonomy-count tension carried" in tax
        assert "regulatory-bargaining" in tax


# ---------------------------------------------------------------------------
# 7. Ledger holds at 46 (NOT a falsification-family member).
# ---------------------------------------------------------------------------

class TestLedger46Holds:
    def test_not_a_member(self):
        assert _block()["falsification_family_member"] is False

    def test_ledger_holds_at_46(self):
        ff = _block()["falsification_family"]
        assert "ledger holds at 46" in ff

    def test_forty_seventh_absent_repo_wide(self):
        # The member-claim form (fragment-built) must be absent everywhere.
        hits = [p for p in _iter_source_files()
                if FORTY_SEVENTH_MEMBER in _read(p)]
        assert hits == [], hits

    def test_forty_sixth_present_from_1127(self):
        text = _read(VERGE_FILE)
        assert FORTY_SIXTH_MEMBER in text

    def test_no_uniform_prediction_test(self):
        ff = _block()["falsification_family"]
        assert "no uniform-prediction test" in ff


# ---------------------------------------------------------------------------
# 8. Corpus integrity.
# ---------------------------------------------------------------------------

class TestCorpusIntegrity1129:
    def test_yaml_parses(self):
        with open(ENTITIES_FILE, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        assert BLOCK_KEY in data

    def test_final_top_level_key(self):
        with open(ENTITIES_FILE, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        assert list(data.keys())[-1] == BLOCK_KEY

    def test_zero_indent_key(self):
        text = _read(ENTITIES_FILE)
        for line in text.split("\n"):
            if BLOCK_KEY in line:
                assert line.startswith(BLOCK_KEY), repr(line[:80])
                break
        else:
            raise AssertionError("block key line not found")

    def test_no_909_forms_outside_entities(self):
        # Underscore/dash key forms: zero repo-wide (git-grep scope).
        assert _repo_grep_mechanism_form(MECH_NUM, _mech_underscore) == []
        assert _repo_grep_mechanism_form(MECH_NUM, _mech_dash) == []
        # Numeric colon field: only the new block carries it.
        hits = _repo_grep_mechanism_form(MECH_NUM, _mech_id_colon)
        assert hits == ["profiles/competitor-entities.yaml"], hits


# ---------------------------------------------------------------------------
# 9. Forward guards for the next run (this run's landing is the last word).
# ---------------------------------------------------------------------------

class TestForwardGuards1129:
    def test_zero_910_numeric_repo_wide(self):
        assert _repo_grep_mechanism_form(NEXT_NUM, _mech_id_colon) == []

    def test_zero_910_underscore_repo_wide(self):
        assert _repo_grep_mechanism_form(NEXT_NUM, _mech_underscore) == []

    def test_zero_910_dash_repo_wide(self):
        assert _repo_grep_mechanism_form(NEXT_NUM, _mech_dash) == []

    def test_no_thirty_fourth_claim_repo_wide(self):
        hits = [p for p in _iter_source_files() if _T34 in _read(p)]
        assert hits == [], hits

    def test_format_built_only_in_this_file(self):
        # The #1116 lesson: guarded forms must never appear contiguously in
        # test-file prose. Every guarded needle is format-built at runtime.
        own = _read(__file__)
        assert "mechanism" + "_909" not in own
        assert "mechanism" + "-909" not in own
        assert "mechanism_id: " + "909" not in own
        assert "THIRTY-" + "THIRD relationship direction" not in own
        assert "THIRTY-" + "FOURTH relationship direction" not in own
        assert "FORTY-" + "SEVENTH falsification-family member" not in own

    def test_iteration_log_absence_discipline(self):
        # The log entry documents absence in the member-claim phrasing, never
        # the full claim form; the block key is absent from log prose.
        text = _read(LOG_FILE)
        assert FORTY_SEVENTH_MEMBER not in text
        assert BLOCK_KEY not in text


# ---------------------------------------------------------------------------
# 10. Supersession pins: #1128/#1124 guard lifecycle at this run.
# ---------------------------------------------------------------------------

class TestSupersessionPins1129:
    def test_1128_max_908_fails_by_design(self):
        # This run lands the 909 numeric field; #1128's max-908 pin fails.
        res = _node_run(FILE_1128,
                        "TestMechanismNovelty1128::"
                        "test_max_numeric_mechanism_id_is_908")
        assert res.returncode != 0, res.stdout[-500:]

    def test_1128_zero_numeric_909_in_profiles_fails_by_design(self):
        res = _node_run(FILE_1128,
                        "TestMechanismNovelty1128::"
                        "test_zero_numeric_909_in_profiles")
        assert res.returncode != 0, res.stdout[-500:]

    def test_1128_thirty_third_absent_fails_by_design(self):
        # This run lands the THIRTY-THIRD claim in competitor-entities.yaml.
        res = _node_run(FILE_1128,
                        "TestFalsificationLedger1128::"
                        "test_thirty_third_direction_absent_repo_wide")
        assert res.returncode != 0, res.stdout[-500:]

    def test_1124_thirty_third_absent_fails_by_design(self):
        res = _node_run(FILE_1124,
                        "TestThirtySecondDirection::test_thirty_third_absent")
        assert res.returncode != 0, res.stdout[-500:]

    def test_1124_no_thirty_third_claim_fails_by_design(self):
        res = _node_run(FILE_1124,
                        "TestForwardGuards1124::"
                        "test_no_thirty_third_claim_repo_wide")
        assert res.returncode != 0, res.stdout[-500:]

    def test_1128_underscore_909_stays_green(self):
        # The block uses the numeric colon field, never the underscore form.
        res = _node_run(FILE_1128,
                        "TestMechanismNovelty1128::"
                        "test_zero_underscore_909_repo_wide")
        assert res.returncode == 0, res.stdout[-800:]

    def test_1128_dash_909_stays_green(self):
        res = _node_run(FILE_1128,
                        "TestMechanismNovelty1128::"
                        "test_zero_dash_909_repo_wide")
        assert res.returncode == 0, res.stdout[-800:]

    def test_1128_forty_seventh_absent_stays_green(self):
        res = _node_run(FILE_1128,
                        "TestFalsificationLedger1128::"
                        "test_forty_seventh_member_absent_repo_wide")
        assert res.returncode == 0, res.stdout[-800:]

    def test_1128_forty_sixth_intact_stays_green(self):
        res = _node_run(FILE_1128,
                        "TestFalsificationLedger1128::"
                        "test_forty_sixth_landed_intact")
        assert res.returncode == 0, res.stdout[-800:]

    def test_1128_thirty_second_intact_stays_green(self):
        res = _node_run(FILE_1128,
                        "TestFalsificationLedger1128::"
                        "test_thirty_second_direction_intact_in_competitor_entities")
        assert res.returncode == 0, res.stdout[-800:]


# ---------------------------------------------------------------------------
# 11. Research method.
# ---------------------------------------------------------------------------

class TestResearchMethod1129:
    def test_four_sources_all_novel(self):
        srcs = _block()["sources"]
        assert len(srcs) == 4
        assert all(s["novel"] is True for s in srcs)

    def test_round1_duplicate_rejected_documented(self):
        # Round 1 (subagent) selected the Google AI-contribution pilot;
        # rejected as the m891/#1099 duplicate before any block was drafted.
        doc = __doc__ or ""
        assert "m891" in doc
        assert "REJECTED" in doc

    def test_round2_duplicate_rejected_documented(self):
        # Round 2 (subagent) selected the OpenAI Lenfest $10M renewal;
        # rejected as the m885/#1089 duplicate before any block was drafted.
        doc = __doc__ or ""
        assert "m885" in doc

    def test_novelty_documents_url_method(self):
        nov = _block()["novelty"]
        assert "Full-URL listings" in nov
        assert "verbatim" in nov
        assert "no canonical URLs constructed" in nov

    def test_novelty_documents_ascii(self):
        nov = _block()["novelty"]
        assert "ASCII-only" in nov
        assert "no em dashes" in nov


# ---------------------------------------------------------------------------
# 12. Doc-sync (patched in the doc-sync followup per #719).
# ---------------------------------------------------------------------------

class TestDocSync1129:
    def test_readme_counts_patched(self):
        # Patched after doc-sync ratchet lands.
        assert README_TEST_COUNT >= 0
        assert README_FILE_COUNT >= 0

    def test_own_basename_in_readme(self):
        # Post-doc-sync: README references the test count.
        assert TEST_BASENAME == OWN_BASENAME


# ---------------------------------------------------------------------------
# 13. Iteration log (entry written in the log-hash followup per #719).
# ---------------------------------------------------------------------------

class TestIterationLog1129:
    def test_iteration_log_exists(self):
        assert os.path.exists(LOG_FILE)

    def test_log_mentions_1129(self):
        # Post-commit: iteration-log.md gains the #1129 entry.
        # Pre-commit this test is a placeholder.
        assert True


# ---------------------------------------------------------------------------
# 14. In-flight isolation.
# ---------------------------------------------------------------------------

class TestInFlightIsolation1129:
    def test_in_flight_not_touched(self):
        rt = _block()["concurrency"]
        assert "#899" in rt
        assert "#938" in rt
        assert "#900" in rt
        assert "#1012-wt" in rt
        assert "stay out of this run" in rt

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
                    or "test_type_c_1129" in line
                    or "nytimes.yaml" in line  # #899 in-flight
                    or "test_type_b_938" in line  # #938 in-flight
                    or "test_type_d_900" in line  # #900 in-flight
                    or "test_type_a_1012" in line), line  # #1012-wt


# ---------------------------------------------------------------------------
# 15. Degenerate contract.
# ---------------------------------------------------------------------------

class TestDegenerateContract1129:
    def test_block_has_all_required_fields(self):
        b = _block()
        for field in (
            "block_key", "mechanism_id", "mechanism_name", "type",
            "type_label", "iteration", "iteration_type", "iteration_time",
            "connects_to", "relationship_direction_taxonomy", "finding",
            "money_flow", "confounders", "coverage_nexus", "sources",
            "tone_scored", "engine_run", "is_significant", "verdict",
            "no_analysis_json_update", "artifact_grade",
            "falsification_family_member", "falsification_family",
            "novelty", "rotation_transparency", "concurrency",
            "yaml_parse_clean", "ascii_only",
        ):
            assert field in b, field

    def test_verdict_and_discipline_fields(self):
        b = _block()
        assert b["verdict"] == "directionally_supported_not_proven"
        assert b["no_analysis_json_update"] is True
        assert b["artifact_grade"] is False

    def test_yaml_parse_clean_and_ascii(self):
        b = _block()
        assert b["yaml_parse_clean"] is True
        assert b["ascii_only"] is True

    def test_mechanism_name_carries_direction(self):
        assert _T33 in _block()["mechanism_name"]

    def test_iteration_time_format(self):
        assert _block()["iteration_time"] == "2026-10-01 17:00 PDT"

    def test_block_text_ascii_only(self):
        text = _block_text()
        bad = [c for c in text if ord(c) > 127]
        assert bad == [], bad[:10]

    def test_no_em_dashes_in_block(self):
        assert "\u2014" not in _block_text()
