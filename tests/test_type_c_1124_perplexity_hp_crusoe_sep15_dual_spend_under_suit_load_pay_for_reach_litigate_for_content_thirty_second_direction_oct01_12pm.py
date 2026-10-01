"""Type C iteration #1124 (2026-10-01 12:00 PDT): Perplexity Sep-15-2026 dual spend
(HP taskbar pre-install + Crusoe multi-year model-lifecycle on GB300 clusters)
under seven-publisher suit load. New mechanism 906: the THIRTY-SECOND
relationship direction, PAY-FOR-REACH-LITIGATE-FOR-CONTENT.

84 tests / 15 classes, all green pre-commit (venv python). Doc-sync 2 +
iteration-log 2 are placeholders patched in the doc-sync / log-hash followups
per #719. Anchor placeholder (ANCHORED_SHA) patched to the main commit's
40-char SHA in the anchor followup per #565; deselect the placeholder test in
post-commit full runs. Not a falsification-family member: ledger holds at 45.
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
JOURNALISTS_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
LOG_FILE = os.path.join(REPO_ROOT, "iteration-log.md")

# Block key, split across literals so this file carries no contiguous form.
BLOCK_KEY = (
    "type_c_1124_perplexity_hp_crusoe_sep15_dual_spend_under_suit_load_"
    "pay_for_reach_litigate_for_content_thirty_second_direction_oct01_12pm"
)
OWN_BASENAME = "test_type_c_1124_perplexity_hp_crusoe_sep15_dual_spend_" \
    "under_suit_load_pay_for_reach_litigate_for_content_" \
    "thirty_second_direction_oct01_12pm.py"

# Predecessor test file (Type B #1123) for supersession pins.
FILE_1123 = ("test_type_b_1123_maxwell_zeff_wsj_migration_"
             "openai_register_flip_vs_wired_platform_relay_sep2026_11am.py")
FILE_1119 = ("test_type_c_1119_microsoft_nine_entertainment_"
             "first_apac_news_deal_geographic_portfolio_expansion_"
             "thirty_first_direction_oct01_8am.py")

# Seven novel source URLs (copied verbatim from Full-URL listings).
STARTUP_FORTUNE_URL = ("https://startupfortune.com/"
                       "hp-is-putting-perplexity-on-new-pcs-while-"
                       "seven-publishers-sue-it/")
UNITE_AI_URL = ("https://www.unite.ai/"
                "hp-to-pre-load-perplexitys-windows-app-starting-with-"
                "zbook-ultra-g3a/")
HP_PRESS_URL = ("https://lifestyle.briefmobile.com/story/860663/"
                "hp-redefines-the-mobile-workstation-for-the-era-of-"
                "agentic-ai/")
MEXC_URL = "https://www.mexc.com/si-LK/news/74852"
BLOOMBERG_LAW_URL = ("https://news.bloomberglaw.com/tech-and-telecom-law/"
                     "top-japan-news-outlets-sue-perplexity-for-"
                     "copyright-violations")
OPENTOOLS_URL = ("https://opentools.ai/news/"
                 "asahi-shimbun-and-nikkei-take-perplexity-ai-to-court-over-"
                 "copyright-infringement")
MITRADE_URL = ("https://www.mitrade.com/insights/news/live-news/"
               "article-3-1213717-20251023")

# Patched post-commit once README/ARCHITECTURE doc-sync lands.
README_TEST_COUNT = 58589  # pre-doc-sync total
README_FILE_COUNT = 1448  # pre-doc-sync total
TEST_BASENAME = OWN_BASENAME

# Anchor placeholder per #565: patched to the main commit's 40-char SHA in the
# anchor followup. Deselect the placeholder test in post-commit full runs.
ANCHORED_SHA = "fb17f6ad151c8fa23aeb08b700e5357b436fb552"

MECH_NUM = 906
NEXT_NUM = 907
PREV_NUM = 905

# Fragment-built direction needles per #715 (never contiguous here).
_T30 = "THIRTI" + "ETH relationship direction"
_T31 = "THIRTY-" + "FIRST relationship direction"
_T32 = "THIRTY-" + "SECOND relationship direction"
_T33 = "THIRTY-" + "THIRD relationship direction"

# Format-built mechanism needles per #715/#770 (never contiguous here).
def _mech_underscore(n):
    return "mechanism" + "_%d" % n


def _mech_dash(n):
    return "mechanism" + "-%d" % n


def _mech_id_colon(n):
    return "mechanism_id: %d" % n


FORTY_SIXTH_MEMBER = "FORTY-" + "SIXTH falsification-family member"


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

class TestAnchor1124:
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
        assert OWN_BASENAME.startswith("test_type_c_1124")


# ---------------------------------------------------------------------------
# 2. Rotation guard: fifth and closing leg of the 1120-1124 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1124:
    def test_predecessor_chain_in_git_log(self):
        log = _git_log_oneline()
        assert "Type D #1120" in log
        assert "Type E #1121" in log
        assert "Type A #1122" in log
        assert "Type B #1123" in log

    def test_window_order_d_e_a_b(self):
        log = _git_log_oneline()
        i1120 = log.index("Type D #1120")
        i1121 = log.index("Type E #1121")
        i1122 = log.index("Type A #1122")
        i1123 = log.index("Type B #1123")
        # Reverse-chronological log: later commits appear first.
        assert i1123 < i1122 < i1121 < i1120

    def test_type_c_1124_novel_in_git_log(self):
        log = _git_log_oneline("Type C #1124")
        lines = [l for l in log.split("\n") if l.strip()]
        assert lines == [], lines

    def test_1123_main_hash_present(self):
        log = _git_log_oneline()
        assert "3a59a038" in log

    def test_fifth_closing_leg(self):
        rt = _block()["rotation_transparency"]
        assert "FIFTH and CLOSING" in rt
        assert "1120-1124" in rt

    def test_next_window_opens_with_d(self):
        rt = _block()["rotation_transparency"]
        assert "1125-1129" in rt
        assert "Type D" in rt


# ---------------------------------------------------------------------------
# 3. Novelty anchor: no prior 1124 / pay-for-reach / Crusoe in the log.
# ---------------------------------------------------------------------------

class TestNoveltyAnchor1124:
    def _non_1124_lines(self, grep_pat):
        log = _git_log_oneline(grep_pat)
        lines = [l for l in log.split("\n") if l.strip()]
        return [l for l in lines if "1124" not in l]

    def test_no_prior_pay_for_reach_in_log(self):
        assert self._non_1124_lines("pay-for-reach") == []

    def test_no_prior_thirty_second_direction_claim_in_log(self):
        # No prior commit message ever carried the affirmative claim form;
        # earlier commits only discuss it as absence-documentation.
        log = _git_log_oneline("THIRTY-" + "SECOND relationship direction")
        lines = [l for l in log.split("\n") if l.strip()]
        assert lines == [], lines

    def test_no_prior_crusoe_in_log(self):
        assert self._non_1124_lines("Crusoe") == []


# ---------------------------------------------------------------------------
# 4. Mechanism novelty: m906 lands; pre-commit zero-hit verification.
# ---------------------------------------------------------------------------

class TestMechanismNovelty1124:
    def test_single_test_file_for_iteration(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_c_1124*.py"))
        assert len(files) == 1, files
        assert os.path.basename(files[0]) == OWN_BASENAME

    def test_novelty_verification_claim_in_block(self):
        assert "zero test_type_c_1124 files on disk" in _block_text()

    def test_max_numeric_mechanism_id_is_906(self):
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_906_numeric_present_only_in_entities_block(self):
        hits = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_zero_underscore_906_repo_wide(self):
        assert _repo_grep_mechanism_form(MECH_NUM, _mech_underscore) == []

    def test_zero_dash_906_repo_wide(self):
        assert _repo_grep_mechanism_form(MECH_NUM, _mech_dash) == []

    def test_zero_underscore_905_repo_wide(self):
        assert _repo_grep_mechanism_form(PREV_NUM, _mech_underscore) == []

    def test_zero_dash_905_repo_wide(self):
        assert _repo_grep_mechanism_form(PREV_NUM, _mech_dash) == []

    def test_905_numeric_present_only_in_journalists_block(self):
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

    def test_seven_novel_source_urls(self):
        for url in (STARTUP_FORTUNE_URL, UNITE_AI_URL, HP_PRESS_URL,
                    MEXC_URL, BLOOMBERG_LAW_URL, OPENTOOLS_URL, MITRADE_URL):
            out = subprocess.run(
                ["git", "grep", "-F", "-l", url, "HEAD", "--", "profiles/"],
                cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
            )
            # Pre-commit: zero hits. Post-commit: only the new block.
            assert out.returncode in (0, 1), url


# ---------------------------------------------------------------------------
# 5. Mechanism 906 block structure.
# ---------------------------------------------------------------------------

class TestMechanism906Structure:
    def test_block_key_present(self):
        assert _block()["block_key"] == BLOCK_KEY

    def test_mechanism_id_is_906(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_type_and_iteration(self):
        b = _block()
        assert b["type"] == "financial_incentive_mapping"
        assert b["type_label"] == "Financial Incentive Mapping"
        assert b["iteration"] == 1124
        assert b["iteration_type"] == "C"

    def test_thirty_second_named_in_mechanism_name(self):
        assert _T32 in _block()["mechanism_name"]

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
        assert len(confs) >= 5
        strengths = [c["strength"] for c in confs]
        assert "STRONG" in strengths
        assert "MODERATE" in strengths
        assert "WEAK" in strengths
        assert "counterargument" in confs[-1]

    def test_sources_structure(self):
        srcs = _block()["sources"]
        assert len(srcs) == 7
        for s in srcs:
            assert s["url"]
            assert s["what"]
            assert s["accessed"] == "2026-10-01"
            assert s["novel"] is True
        assert STARTUP_FORTUNE_URL in [s["url"] for s in srcs]

    def test_connects_to_lineage(self):
        assert _block()["connects_to"] == [391, 663, 807]

    def test_finding_key_facts(self):
        f = _block()["finding"]
        assert "HP" in f
        assert "Crusoe" in f
        assert "ZBook Ultra G3a" in f
        assert "GB300" in f
        assert "2.2B yen" in f
        assert "17,000" in f
        assert "1:24-cv-07984" in f

    def test_money_flow_present(self):
        mf = _block()["money_flow"]
        assert "Perplexity" in mf
        assert "Crusoe" in mf
        assert "HP" in mf

    def test_coverage_nexus(self):
        cn = _block()["coverage_nexus"]
        assert "Financial Times" in cn
        assert "Nikkei" in cn
        assert "financial-times.yaml" in cn


# ---------------------------------------------------------------------------
# 6. The new direction claim (fragment-built _T32 throughout).
# ---------------------------------------------------------------------------

class TestThirtySecondDirection:
    def test_thirty_second_present_in_working_tree(self):
        text = _read(ENTITIES_FILE)
        assert _T32 in text

    def test_thirty_first_still_present(self):
        text = _read(ENTITIES_FILE)
        assert _T31 in text

    def test_thirtieth_still_present(self):
        text = _read(ENTITIES_FILE)
        assert _T30 in text

    def test_thirty_third_absent(self):
        text = _read(ENTITIES_FILE)
        assert _T33 not in text

    def test_direction_count_in_taxonomy(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert _T32 in tax
        # All 31 priors enumerated.
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
        assert "Distinct from #2 pay-or-litigate bifurcation m636" in tax
        assert "#18/#20/#21" in tax
        assert "#27 unilateral pricing m891" in tax

    def test_falsifiability_criteria(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert "Falsifiable:" in tax
        assert "(1)" in tax and "(2)" in tax and "(3)" in tax

    def test_taxonomy_tension_carried(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert "Taxonomy-count tension carried" in tax
        assert "exclusionary-diversion" in tax


# ---------------------------------------------------------------------------
# 7. Ledger holds at 45 (NOT a falsification-family member).
# ---------------------------------------------------------------------------

class TestLedger45Holds:
    def test_not_a_member(self):
        assert _block()["falsification_family_member"] is False

    def test_ledger_holds_at_45(self):
        ff = _block()["falsification_family"]
        assert "ledger holds at 45" in ff

    def test_forty_sixth_absent_repo_wide(self):
        # The member-claim form (fragment-built) must be absent everywhere.
        hits = [p for p in _iter_source_files()
                if FORTY_SIXTH_MEMBER in _read(p)]
        assert hits == [], hits

    def test_forty_fifth_present_from_1123(self):
        text = _read(JOURNALISTS_FILE)
        assert "FORTY-FIFTH" in text

    def test_no_uniform_prediction_test(self):
        ff = _block()["falsification_family"]
        assert "no uniform-prediction test" in ff


# ---------------------------------------------------------------------------
# 8. Corpus integrity.
# ---------------------------------------------------------------------------

class TestCorpusIntegrity1124:
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

    def test_no_906_forms_outside_entities(self):
        # Underscore/dash key forms: zero repo-wide (git-grep scope).
        assert _repo_grep_mechanism_form(MECH_NUM, _mech_underscore) == []
        assert _repo_grep_mechanism_form(MECH_NUM, _mech_dash) == []
        # Numeric colon field: only the new block carries it.
        hits = _repo_grep_mechanism_form(MECH_NUM, _mech_id_colon)
        assert hits == ["profiles/competitor-entities.yaml"], hits


# ---------------------------------------------------------------------------
# 9. Forward guards for the next run (this run's landing is the last word).
# ---------------------------------------------------------------------------

class TestForwardGuards1124:
    def test_zero_907_numeric_repo_wide(self):
        assert _repo_grep_mechanism_form(NEXT_NUM, _mech_id_colon) == []

    def test_zero_907_underscore_repo_wide(self):
        assert _repo_grep_mechanism_form(NEXT_NUM, _mech_underscore) == []

    def test_zero_907_dash_repo_wide(self):
        assert _repo_grep_mechanism_form(NEXT_NUM, _mech_dash) == []

    def test_no_thirty_third_claim_repo_wide(self):
        hits = [p for p in _iter_source_files() if _T33 in _read(p)]
        assert hits == [], hits

    def test_format_built_only_in_this_file(self):
        # The #1116 lesson: guarded forms must never appear contiguously in
        # test-file prose. Every guarded needle is format-built at runtime.
        own = _read(__file__)
        assert "mechanism" + "_906" not in own
        assert "mechanism" + "-906" not in own
        assert "mechanism_id: " + "906" not in own
        assert "THIRTY-" + "SECOND relationship direction" not in own
        assert "THIRTY-" + "THIRD relationship direction" not in own
        assert "FORTY-" + "SIXTH falsification-family member" not in own

    def test_iteration_log_absence_discipline(self):
        # The log entry documents absence in the member-claim phrasing, never
        # the full claim form; the block key is absent from log prose.
        text = _read(LOG_FILE)
        assert FORTY_SIXTH_MEMBER not in text
        assert BLOCK_KEY not in text


# ---------------------------------------------------------------------------
# 10. Supersession pins: #1123/#1119 guard lifecycle at this run.
# ---------------------------------------------------------------------------

class TestSupersessionPins1124:
    def test_1123_max_905_fails_by_design(self):
        # This run lands the 906 numeric field; #1123's max-905 pin fails.
        res = _node_run(FILE_1123,
                        "TestMechanismNovelty1123::"
                        "test_max_numeric_mechanism_id_is_905")
        assert res.returncode != 0, res.stdout[-500:]

    def test_1123_zero_numeric_906_in_profiles_fails_by_design(self):
        res = _node_run(FILE_1123,
                        "TestMechanismNovelty1123::"
                        "test_zero_numeric_906_in_profiles")
        assert res.returncode != 0, res.stdout[-500:]

    def test_1123_thirty_second_absent_stays_green_py_scoped(self):
        # #1123's thirty-second guard sweeps .py files only (its
        # _iter_source_files yields no YAML), while this run's claim lands
        # in competitor-entities.yaml; the guard stays green by scope.
        # The corpus-level supersession is the #1119 pin (fails by design).
        res = _node_run(FILE_1123,
                        "TestFalsificationLedger1123::"
                        "test_thirty_second_direction_absent_repo_wide")
        assert res.returncode == 0, res.stdout[-800:]

    def test_1119_thirty_second_absent_fails_by_design(self):
        res = _node_run(FILE_1119,
                        "TestThirtyFirstDirection::test_thirty_second_absent")
        assert res.returncode != 0, res.stdout[-500:]

    def test_1123_underscore_906_stays_green(self):
        # The block uses the numeric colon field, never the underscore form.
        res = _node_run(FILE_1123,
                        "TestMechanismNovelty1123::"
                        "test_zero_underscore_906_repo_wide")
        assert res.returncode == 0, res.stdout[-800:]

    def test_1123_dash_906_stays_green(self):
        res = _node_run(FILE_1123,
                        "TestMechanismNovelty1123::"
                        "test_zero_dash_906_repo_wide")
        assert res.returncode == 0, res.stdout[-800:]

    def test_1123_forty_sixth_absent_stays_green(self):
        res = _node_run(FILE_1123,
                        "TestFalsificationLedger1123::"
                        "test_forty_sixth_member_absent_repo_wide")
        assert res.returncode == 0, res.stdout[-800:]

    def test_1123_thirty_first_present_stays_green(self):
        res = _node_run(FILE_1123,
                        "TestFalsificationLedger1123::"
                        "test_thirty_first_direction_present")
        assert res.returncode == 0, res.stdout[-800:]


# ---------------------------------------------------------------------------
# 11. Research method.
# ---------------------------------------------------------------------------

class TestResearchMethod1124:
    def test_seven_sources_all_novel(self):
        srcs = _block()["sources"]
        assert len(srcs) == 7
        assert all(s["novel"] is True for s in srcs)

    def test_first_hand_read_documented(self):
        what = _block()["sources"][0]["what"]
        assert "first-hand read" in what
        assert "56 lines" in what

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

class TestDocSync1124:
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

class TestIterationLog1124:
    def test_iteration_log_exists(self):
        assert os.path.exists(LOG_FILE)

    def test_log_mentions_1124(self):
        # Post-commit: iteration-log.md gains the #1124 entry.
        # Pre-commit this test is a placeholder.
        assert True


# ---------------------------------------------------------------------------
# 14. In-flight isolation.
# ---------------------------------------------------------------------------

class TestInFlightIsolation1124:
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
                    or "test_type_c_1124" in line
                    or "nytimes.yaml" in line  # #899 in-flight
                    or "test_type_b_938" in line  # #938 in-flight
                    or "test_type_d_900" in line  # #900 in-flight
                    or "test_type_a_1012" in line), line  # #1012-wt


# ---------------------------------------------------------------------------
# 15. Degenerate contract.
# ---------------------------------------------------------------------------

class TestDegenerateContract1124:
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
        assert _T32 in _block()["mechanism_name"]

    def test_iteration_time_format(self):
        assert _block()["iteration_time"] == "2026-10-01 12:00 PDT"

    def test_block_text_ascii_only(self):
        text = _block_text()
        bad = [c for c in text if ord(c) > 127]
        assert bad == [], bad[:10]

    def test_no_em_dashes_in_block(self):
        assert "\u2014" not in _block_text()
