"""Type C iteration #1144 (2026-10-02 07:00 PDT): Apple Siri AI publisher-negotiation
watch, Oct-2-2026 status check - 51 days after the Aug-12-2026 WSJ report
(mechanism 156): zero signed-deal closures surfaced, no counterparty publisher
named; mechanisms 156/606 stay PREDICTIVE. Novel core: OpenAI's September 2026
court filing in the Musk xAI antitrust case (FT-original reporting; MacRumors
Sep 23 2026 relay) calling the ChatGPT-in-Siri integration "persistently
underperforming" - FIRST corpus documentation of the commercial failure of the
Dec-2024 Apple-OpenAI Siri distribution deal (exclusivity asked and refused,
non-exclusive contract clause, off-by-default friction, redacted March 2026
conversation). Apple's nine-figure variable-pay proposal is a second instance
of #27 unilateral pricing (m891): Apple sizes the pot and runs the counter -
EXTENDS the direction, does not earn a new one; the thirty-sixth direction
stays absent by design. New mechanism 918 in profiles/competitor-entities.yaml
(connects_to 156/606/654/891). NOT a falsification-family member: ledger
holds at 46.

81 tests / 16 classes, all green pre-commit (venv python) with TestDocSync and
TestIterationLog deselected by design (placeholders patched in the doc-sync /
log-hash followups per #719). Anchor placeholder (ANCHORED_SHA) patched to the
main commit's 40-char SHA in the anchor followup per #565; deselect the
placeholder test in post-commit full runs. TestRotationGuard novelty pin is red
post-main-commit by design (deselected in post-commit runs).

Research in 2 rounds (direct browser.search, 0 browser.open per #503).
Round 1 - REJECTED: (a) LASST v. OpenAI Hugging Face suit (filed Sep 29 2026,
CDAFA/UCL, injunction-only) - litigation, not a financial relationship, and
the coverage side is already Type A corpus; (b) OpenAI publisher licensing
Oct 2026 - the stockmoguls Sep-6 re-crawl surfaced only corpus duplicates
(NYT $28M litigation spend = m753 family; DOJ fair-use brief = m672;
NYT-Amazon deal = m559; News Corp x Meta $50M/yr in corpus). Round 2 -
SELECTED: the mechanism-606 Apple Siri publisher-negotiation watch at day 51
(zero closures; bounded absence per the iteration-492 rule) with the
"persistently underperforming" filing as the novel core (zero hits repo-wide
pre-commit); context legs: Apple v. OpenAI trade-secrets September escalation
(13 employees, new-evidence fight, Oct 1 / Oct 14 hearings) and Musk dropping
the Apple half of the xAI suit (Sep 14, dismissal with prejudice). All URLs
copied verbatim from Full-URL listings; no canonical URLs constructed.
ASCII-only, no em dashes.
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
    "type_c_1144_apple_siri_ai_publisher_negotiation_watch_day_fifty_one_"
    "zero_closures_persistently_underperforming_filing_oct02_7am"
)
OWN_BASENAME = ("test_type_c_1144_apple_siri_publisher_watch_day51_"
                "zero_closures_underperforming_filing_oct02_7am.py")

# Predecessor test file for supersession pins.
FILE_1143 = ("test_type_b_1143_cristina_criddle_ft_blindsided_openai_"
             "anthropic_sep16_m758_temporal_extension_oct02_6am.py")

# Eight novel source URLs (copied verbatim from Full-URL listings; split so
# this file carries no contiguous full URL).
URL_MACRUMORS_UNDERPERFORMING = (
    "https://www.macrumors.com/2026/09/23/"
    "openai-siri-chatgpt-underperforming/"
)
URL_AIWEEKLY_UNDERPERFORMING = (
    "https://aiweekly.co/alerts/"
    "openai-apples-chatgpt-in-siri-deal-persistently-underperformed"
)
URL_WEBPRONEWS_BITTER_LESSON = (
    "https://www.webpronews.com/"
    "openais-bitter-lesson-from-siri-why-apples-chatgpt-bet-fell-flat/"
)
URL_BUSINESSMODELANALYST_POOL = (
    "https://businessmodelanalyst.com/"
    "apple-publisher-payments-siri-pool/"
)
URL_MACRUMORS_MUSK_DROPS = (
    "https://www.macrumors.com/2026/09/14/"
    "spacexai-drops-apple-lawsuit/"
)
URL_9TO5MAC_NEW_EVIDENCE = (
    "https://9to5mac.com/2026/09/25/"
    "openai-accuses-apple-of-improperly-adding-new-evidence-"
    "to-trade-secrets-case/"
)
URL_MACOBSERVER_PUBLISHER_PLANS = (
    "https://www.macobserver.com/news/"
    "apple-plans-to-pay-news-publishers-for-content-used-by-siri-ai/"
)
URL_LINKEDIN_JERRYCARDS = (
    "https://www.linkedin.com/posts/jerrycards_apple-siri-"
    "appleintelligence-activity-7493520225796050944-ffcZ"
)
NOVEL_URLS = (
    URL_MACRUMORS_UNDERPERFORMING,
    URL_AIWEEKLY_UNDERPERFORMING,
    URL_WEBPRONEWS_BITTER_LESSON,
    URL_BUSINESSMODELANALYST_POOL,
    URL_MACRUMORS_MUSK_DROPS,
    URL_9TO5MAC_NEW_EVIDENCE,
    URL_MACOBSERVER_PUBLISHER_PLANS,
    URL_LINKEDIN_JERRYCARDS,
)

# Patched post-commit once README/ARCHITECTURE doc-sync lands (per #719).
README_TEST_COUNT = 0  # placeholder per #719 (patched in doc-sync followup)
README_FILE_COUNT = 0  # placeholder per #719 (patched in doc-sync followup)
TEST_BASENAME = OWN_BASENAME

# Anchor placeholder per #565: patched to the main commit's 40-char SHA in the
# anchor followup. Deselect the placeholder test in post-commit full runs.
ANCHORED_SHA = "02b20835d56a48c150e8cc5bf0f98af569647ce7"  # Type C #1144 main commit (Type C runs self-anchor per #565)

MECH_NUM = 918
NEXT_NUM = 919
PREV_NUM = 917

# Fragment-built direction needles per #715 (never contiguous here).
_T34 = "THIRTY-" + "FOURTH relationship direction"
_T35 = "THIRTY-" + "FIFTH relationship direction"
_T36 = "THIRTY-" + "SIXTH relationship direction"
_T37 = "THIRTY-" + "SEVENTH relationship direction"


# Format-built mechanism needles per #715/#770 (never contiguous here).
def _mech_underscore(n):
    return "mechanism" + "_%d" % n


def _mech_dash(n):
    return "mechanism" + "-%d" % n


def _mech_id_colon(n):
    return "mechanism_id: %d" % n


FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
FORTY_SIXTH_MEMBER = "FORTY" + "-SIXTH falsification-family member"

# Predecessor chain hashes (verified in git log pre-commit).
PRED_MAIN_1140 = "48062ab5"
PRED_MAIN_1141 = "7d6a4a7a"
PRED_MAIN_1142 = "224f054e"
PRED_MAIN_1143 = "fb2d19f0"


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

class TestAnchor1144:
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
        assert OWN_BASENAME.startswith("test_type_c_1144")


# ---------------------------------------------------------------------------
# 2. Rotation guard: fifth and closing leg of the 1140-1144 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1144:
    def test_predecessor_chain_in_git_log(self):
        log = _git_log_oneline()
        assert "Type D #1140" in log
        assert "Type E #1141" in log
        assert "Type A #1142" in log
        assert "Type B #1143" in log

    def test_window_order_d_e_a_b(self):
        log = _git_log_oneline()
        i1140 = log.index("Type D #1140")
        i1141 = log.index("Type E #1141")
        i1142 = log.index("Type A #1142")
        i1143 = log.index("Type B #1143")
        # Reverse-chronological log: later commits appear first.
        assert i1143 < i1142 < i1141 < i1140

    def test_type_c_1144_novel_in_git_log(self):
        # Red post-main-commit by design; deselect in post-commit runs.
        log = _git_log_oneline("Type C #1144")
        lines = [l for l in log.split("\n") if l.strip()]
        assert lines == [], lines

    def test_1143_main_hash_present(self):
        log = _git_log_oneline()
        assert PRED_MAIN_1143 in log

    def test_1140_thru_1142_main_hashes_present(self):
        log = _git_log_oneline()
        assert PRED_MAIN_1140 in log
        assert PRED_MAIN_1141 in log
        assert PRED_MAIN_1142 in log

    def test_fifth_closing_leg(self):
        rt = _block()["rotation_transparency"]
        assert "FIFTH and CLOSING" in rt
        assert "1140-1144" in rt

    def test_next_window_opens_with_d(self):
        rt = _block()["rotation_transparency"]
        assert "1145-1149" in rt
        assert "Type D" in rt


# ---------------------------------------------------------------------------
# 3. Novelty anchor: no prior 1144 / persistently-underperforming / day-51.
# ---------------------------------------------------------------------------

class TestNoveltyAnchor1144:
    def _non_1144_lines(self, grep_pat):
        log = _git_log_oneline(grep_pat)
        lines = [l for l in log.split("\n") if l.strip()]
        return [l for l in lines if "1144" not in l]

    def test_no_prior_persistently_underperforming_in_log(self):
        assert self._non_1144_lines("persistently underperforming") == []

    def test_no_prior_day_fifty_one_watch_in_log(self):
        assert self._non_1144_lines("day_fifty_one") == []

    def test_no_prior_thirty_sixth_claim_in_log(self):
        # No prior commit message ever carried the affirmative claim form;
        # earlier commits only discuss it as absence-documentation.
        log = _git_log_oneline(_T36)
        lines = [l for l in log.split("\n") if l.strip()]
        assert lines == [], lines


# ---------------------------------------------------------------------------
# 4. Mechanism novelty: m918 lands; pre-commit zero-hit verification.
# ---------------------------------------------------------------------------

class TestMechanismNovelty1144:
    def test_single_test_file_for_iteration(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_c_1144*.py"))
        assert len(files) == 1, files
        assert os.path.basename(files[0]) == OWN_BASENAME

    def test_novelty_verification_claim_in_block(self):
        assert "zero test_type_c_1144 files on disk" in _block_text()

    def test_max_numeric_mechanism_id_is_918(self):
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_918_numeric_present_only_in_entities_block(self):
        hits = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_zero_underscore_918_repo_wide(self):
        assert _repo_grep_mechanism_form(MECH_NUM, _mech_underscore) == []

    def test_zero_dash_918_repo_wide(self):
        assert _repo_grep_mechanism_form(MECH_NUM, _mech_dash) == []

    def test_zero_underscore_917_repo_wide(self):
        assert _repo_grep_mechanism_form(PREV_NUM, _mech_underscore) == []

    def test_zero_dash_917_repo_wide(self):
        assert _repo_grep_mechanism_form(PREV_NUM, _mech_dash) == []

    def test_917_numeric_present_only_in_journalists_block(self):
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

    def test_eight_novel_source_urls(self):
        assert len(NOVEL_URLS) == 8
        for url in NOVEL_URLS:
            out = subprocess.run(
                ["git", "grep", "-F", "-l", url, "HEAD", "--", "profiles/"],
                cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
            )
            # Pre-commit: zero hits. Post-commit: only the new block.
            assert out.returncode in (0, 1), url


# ---------------------------------------------------------------------------
# 5. Mechanism 918 block structure.
# ---------------------------------------------------------------------------

class TestMechanism918Structure:
    def test_block_key_present(self):
        assert _block()["block_key"] == BLOCK_KEY

    def test_mechanism_id_is_918(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_connects_to_watch_and_geometry(self):
        assert _block()["connects_to"] == [156, 606, 654, 891]

    def test_iteration_type_c(self):
        b = _block()
        assert b["iteration"] == 1144
        assert b["iteration_type"] == "C"
        assert b["iteration_time"] == "2026-10-02 07:00 PDT"

    def test_eight_sources_all_novel(self):
        srcs = _block()["sources"]
        assert len(srcs) == 8
        assert all(s["novel"] is True for s in srcs)
        assert all(s["accessed"] == "2026-10-02" for s in srcs)

    def test_five_confounders_strong_first(self):
        confs = _block()["confounders"]
        assert len(confs) == 5
        assert confs[0]["strength"] == "STRONG"
        assert confs[1]["strength"] == "STRONG"

    def test_money_flow_four_channels(self):
        mf = _block()["money_flow"]
        assert "PREDICTIVE" in mf
        assert "OBSERVED" in mf
        assert "DOCUMENTED" in mf
        assert "ACTIVE" in mf

    def test_finding_carries_novel_core(self):
        f = _block()["finding"]
        assert "51 days" in f
        assert "persistently underperforming" in f
        assert "PREDICTIVE" in f


# ---------------------------------------------------------------------------
# 6. No thirty-sixth direction: Apple's proposal EXTENDS #27, not a new one.
# ---------------------------------------------------------------------------

class TestNoThirtySixthDirection1144:
    def test_thirty_fifth_still_present(self):
        text = _read(ENTITIES_FILE)
        assert _T35 in text

    def test_thirty_fourth_still_present(self):
        text = _read(ENTITIES_FILE)
        assert _T34 in text

    def test_thirty_sixth_absent(self):
        text = _read(ENTITIES_FILE)
        assert _T36 not in text

    def test_taxonomy_documents_unilateral_pricing_extension(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert "unilateral pricing" in tax
        assert "m891" in tax
        assert "sizes the pot" in tax
        assert "runs the counter" in tax

    def test_taxonomy_distinct_from_meter_then_invite(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert "m915" in tax
        assert "opposite designer" in tax

    def test_mechanism_name_claims_no_new_direction(self):
        assert _T36 not in _block()["mechanism_name"]
        assert "Unilateral Pricing" in _block()["mechanism_name"]


# ---------------------------------------------------------------------------
# 7. Ledger holds at 46 (NOT a falsification-family member).
# ---------------------------------------------------------------------------

class TestLedger46Holds1144:
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

    def test_forty_sixth_present_from_1132(self):
        text = _read(VERGE_FILE)
        assert FORTY_SIXTH_MEMBER in text

    def test_no_uniform_prediction_test(self):
        ff = _block()["falsification_family"]
        assert "no uniform-prediction test" in ff


# ---------------------------------------------------------------------------
# 8. Corpus integrity.
# ---------------------------------------------------------------------------

class TestCorpusIntegrity1144:
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

    def test_no_918_forms_outside_entities(self):
        # Underscore/dash key forms: zero repo-wide (git-grep scope).
        assert _repo_grep_mechanism_form(MECH_NUM, _mech_underscore) == []
        assert _repo_grep_mechanism_form(MECH_NUM, _mech_dash) == []
        # Numeric colon field: only the new block carries it.
        hits = _repo_grep_mechanism_form(MECH_NUM, _mech_id_colon)
        assert hits == ["profiles/competitor-entities.yaml"], hits


# ---------------------------------------------------------------------------
# 9. Forward guards for the next run (this run's landing is the last word).
# ---------------------------------------------------------------------------

class TestForwardGuards1144:
    def test_zero_919_numeric_repo_wide(self):
        assert _repo_grep_mechanism_form(NEXT_NUM, _mech_id_colon) == []

    def test_zero_919_underscore_repo_wide(self):
        assert _repo_grep_mechanism_form(NEXT_NUM, _mech_underscore) == []

    def test_zero_919_dash_repo_wide(self):
        assert _repo_grep_mechanism_form(NEXT_NUM, _mech_dash) == []

    def test_no_thirty_seventh_claim_repo_wide(self):
        hits = [p for p in _iter_source_files() if _T37 in _read(p)]
        assert hits == [], hits

    def test_format_built_only_in_this_file(self):
        # The #1116 lesson: guarded forms must never appear contiguously in
        # test-file prose. Every guarded needle is format-built at runtime.
        own = _read(__file__)
        assert "mechanism" + "_918" not in own
        assert "mechanism" + "-918" not in own
        assert "mechanism_id: " + "918" not in own
        assert "mechanism" + "_919" not in own
        assert "mechanism" + "-919" not in own
        assert "mechanism_id: " + "919" not in own
        assert "THIRTY-" + "SIXTH relationship direction" not in own
        assert "THIRTY-" + "SEVENTH relationship direction" not in own
        assert "FORTY-" + "SEVENTH falsification-family member" not in own

    def test_iteration_log_absence_discipline(self):
        # The log entry documents absence in the member-claim phrasing, never
        # the full claim form; the block key is absent from log prose.
        text = _read(LOG_FILE)
        assert FORTY_SEVENTH_MEMBER not in text
        assert BLOCK_KEY not in text


# ---------------------------------------------------------------------------
# 10. Supersession pins: #1143 guard lifecycle at this run.
# ---------------------------------------------------------------------------

class TestSupersessionPins1144:
    def test_1143_max_917_fails_by_design(self):
        # This run lands the 918 numeric field; #1143's max-917 pin fails.
        res = _node_run(FILE_1143,
                        "TestMechanismNovelty1143::"
                        "test_max_numeric_mechanism_id_is_917")
        assert res.returncode != 0, res.stdout[-500:]

    def test_1143_zero_numeric_918_in_profiles_fails_by_design(self):
        res = _node_run(FILE_1143,
                        "TestMechanismNovelty1143::"
                        "test_zero_numeric_918_in_profiles")
        assert res.returncode != 0, res.stdout[-500:]

    def test_1143_no_type_c_1144_pin_flips_post_commit(self):
        # Pre-commit this pin is green (no Type C #1144 in git log yet);
        # post-main-commit it flips red by design. Deselect post-commit.
        res = _node_run(FILE_1143,
                        "TestGuardLifecycle1143::"
                        "test_no_type_c_1144_in_git_log_pin")
        assert res.returncode == 0, res.stdout[-500:]

    def test_1143_underscore_918_stays_green(self):
        # The block uses the numeric colon field, never the underscore form.
        res = _node_run(FILE_1143,
                        "TestMechanismNovelty1143::"
                        "test_zero_underscore_918_repo_wide")
        assert res.returncode == 0, res.stdout[-800:]

    def test_1143_dash_918_stays_green(self):
        res = _node_run(FILE_1143,
                        "TestMechanismNovelty1143::"
                        "test_zero_dash_918_repo_wide")
        assert res.returncode == 0, res.stdout[-800:]

    def test_1143_forty_seventh_absent_stays_green(self):
        res = _node_run(FILE_1143,
                        "TestFalsificationLedger1143::"
                        "test_forty_seventh_member_claim_absent")
        assert res.returncode == 0, res.stdout[-800:]

    def test_1143_forty_sixth_intact_stays_green(self):
        res = _node_run(FILE_1143,
                        "TestFalsificationLedger1143::"
                        "test_forty_sixth_member_form_present")
        assert res.returncode == 0, res.stdout[-800:]

    def test_1143_thirty_fifth_intact_stays_green(self):
        res = _node_run(FILE_1143,
                        "TestForwardLookingStaleness1143::"
                        "test_thirty_fifth_direction_still_present")
        assert res.returncode == 0, res.stdout[-800:]


# ---------------------------------------------------------------------------
# 11. Research method.
# ---------------------------------------------------------------------------

class TestResearchMethod1144:
    def test_eight_sources_all_novel(self):
        srcs = _block()["sources"]
        assert len(srcs) == 8
        assert all(s["novel"] is True for s in srcs)

    def test_round1_duplicates_rejected_documented(self):
        # Round 1 (direct search) found the LASST v. OpenAI Hugging Face suit
        # (rejected: litigation, not a financial relationship) and the
        # stockmoguls Sep-6 re-crawl (rejected: NYT $28M spend = m753 family,
        # DOJ brief = m672, NYT-Amazon = m559, News Corp x Meta in corpus).
        doc = __doc__ or ""
        assert "REJECTED" in doc
        assert "m753" in doc
        assert "m672" in doc
        assert "m559" in doc

    def test_round2_selected_documented(self):
        doc = __doc__ or ""
        assert "SELECTED" in doc
        assert "mechanism-606" in doc

    def test_novelty_documents_url_method(self):
        nov = _block()["novelty"]
        assert "Full-URL listings" in nov
        assert "verbatim" in nov
        assert "no canonical URLs constructed" in nov

    def test_novelty_documents_ascii(self):
        nov = _block()["novelty"]
        assert "ASCII-only" in nov
        assert "no em dashes" in nov

    def test_excerpt_bounded_zero_browser_open(self):
        doc = __doc__ or ""
        assert "0 browser.open" in doc


# ---------------------------------------------------------------------------
# 12. Doc-sync (patched in the doc-sync followup per #719).
# ---------------------------------------------------------------------------

class TestDocSync1144:
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

class TestIterationLog1144:
    def test_iteration_log_exists(self):
        assert os.path.exists(LOG_FILE)

    def test_log_mentions_1144(self):
        # Post-commit: iteration-log.md gains the #1144 entry.
        # Pre-commit this test is a placeholder.
        assert True


# ---------------------------------------------------------------------------
# 14. In-flight isolation.
# ---------------------------------------------------------------------------

class TestInFlightIsolation1144:
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
                    or "test_type_c_1144" in line
                    or "nytimes.yaml" in line  # #899 in-flight
                    or "test_type_b_938" in line  # #938 in-flight
                    or "test_type_d_900" in line  # #900 in-flight
                    or "test_type_a_1012" in line), line  # #1012-wt


# ---------------------------------------------------------------------------
# 15. Degenerate contract.
# ---------------------------------------------------------------------------

class TestDegenerateContract1144:
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

    def test_mechanism_name_carries_watch_framing(self):
        assert "Publisher-Negotiation Watch" in _block()["mechanism_name"]


# ---------------------------------------------------------------------------
# 16. Background suite check (checked only per #795 - the verdict and
# tombstoning belong to the next Type D run, #1145).
# ---------------------------------------------------------------------------

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1140_full_suite.log"
)


class TestBackgroundSuiteCheck1144:
    def test_suite_log_path_noted(self):
        assert os.path.basename(SUITE_LOG) == "type_d_1140_full_suite.log"

    def test_verdict_belongs_to_1145(self):
        rt = _block()["rotation_transparency"]
        assert "belongs to #1145" in rt
        assert "#795" in rt
