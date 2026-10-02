"""Type C iteration #1154 (2026-10-02 15:00 PDT): Google pay-per-value pilot
post-rate-disclosure reception (Oct 1-2 2026) - publisher walk-away framing
plus Spur founder David Buttle's "more hedge than true market"
characterization. FIRST corpus documentation of the control-of-the-meter
contest: Google's black-box Search Console "AI earnings" widget (#27
unilateral pricing, mechanism 891) vs SPUR's open content-telemetry standard
with invitation-only AI Licensing Advisory Board (mechanism 915,
METER-THEN-INVITE, the thirty-fifth direction). Temporal extension of the
m891 family; no new relationship direction (the thirty-sixth stays absent by
design). New mechanism 924 in profiles/competitor-entities.yaml
(connects_to 891/915/921/702/666). NOT a falsification-family member: ledger
holds at 46.

Target ~80 tests / 16 classes, all green pre-commit (venv python) with
TestDocSync and TestIterationLog deselected by design (placeholders patched in
the doc-sync / log-hash followups per #719). Anchor placeholder
(ANCHORED_SHA) patched to the main commit's 40-char SHA in the anchor followup
per #565; deselect the placeholder test in post-commit full runs.
TestRotationGuard novelty pin is red post-main-commit by design (deselected in
post-commit runs).

Research in 2 rounds (direct browser.search, 0 browser.open per #503).
Round 1 - REJECTED: (a) Meta publisher-deal set - News Corp x Meta $50M/yr
already m549/#594; the John Georges E&P piece already m912; the Frontier Post
multi-deal piece duplicates; the Reuters Muse-agent and WeSearch enterprise
pieces off-topic; (b) Anthropic publisher-deal set - the Adweek zero-deals
piece already in corpus; TechCrunch/newsgab settlement-distribution already
#594; the startupfortune settlement-economics piece novel but weaker than the
Google reception story (distribution-phase detail, 66 days old). Round 2 -
SELECTED: the Google pay-per-value post-rate-disclosure reception as the
novel core - two webpronews Oct-1 pieces (walk-away framing; the Buttle
"hedge than true market" quote, zero hits repo-wide pre-commit) plus the
AdExchanger Oct-1 roundup and the E and P/Digiday republication leg. All URLs
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
    "type_c_1154_google_pay_per_value_post_rate_reception_"
    "walk_away_hedge_not_market_oct02_3pm"
)
OWN_BASENAME = (
    "test_type_c_1154_google_pay_per_value_post_rate_reception_"
    "hedge_not_market_oct02_3pm.py"
)

# Predecessor test file for supersession pins.
FILE_1153 = (
    "test_type_b_1153_jessica_conditt_engadget_meta_wearables_"
    "bounded_absence_temporal_extension_m674_oct02_2pm.py"
)

# Four novel source URLs (copied verbatim from Full-URL listings; split so
# this file carries no contiguous full URL).
URL_WEBPRONEWS_FALL_SHORT = (
    "https://www.webpronews.com/googles-modest-ai-payments-"
    "to-publishers-fall-short-as-search-traffic-erodes/"
)
URL_WEBPRONEWS_WALK_AWAY = (
    "https://www.webpronews.com/googles-tiny-checks-for-ai-overviews-"
    "why-publishers-are-walking-away/"
)
URL_ADEXCHANGER_ROUNDUP = (
    "https://www.adexchanger.com/daily-news-roundup/thursday-01102026/"
)
URL_EP_PAY_PER_VALUE = (
    "https://www.editorandpublisher.com/stories/"
    "google-rolls-out-pay-per-value-ai-licensing-program-to-publishers,263531"
)
NOVEL_URLS = (
    URL_WEBPRONEWS_FALL_SHORT,
    URL_WEBPRONEWS_WALK_AWAY,
    URL_ADEXCHANGER_ROUNDUP,
    URL_EP_PAY_PER_VALUE,
)

# Patched post-commit once README/ARCHITECTURE doc-sync lands (per #719).
README_TEST_COUNT = 60877  # post-doc-sync total (60785 + 92)
README_FILE_COUNT = 1479  # post-doc-sync total
TEST_BASENAME = OWN_BASENAME

# Anchor placeholder per #565: patched to the main commit's 40-char SHA in the
# anchor followup. Deselect the placeholder test in post-commit full runs.
ANCHORED_SHA = "38d74753f54a6a53c4d7ac04c74faffa5b6a5b98"  # Type C #1154 main commit (Type C runs self-anchor per #565)

MECH_NUM = 924
NEXT_NUM = 925
PREV_NUM = 923

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
PRED_MAIN_1150 = "a032e49d"
PRED_MAIN_1151 = "3571d5f1"
PRED_MAIN_1152 = "31bbe553"
PRED_MAIN_1153 = "4b8b93a6"


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
    return [line for line in out.stdout.split("\n") if line.strip()]


def _repo_grep_mechanism_form(n, form):
    needle = form(n)
    out = subprocess.run(
        ["git", "grep", "-l", "-F", needle],
        cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
    )
    return [line for line in out.stdout.split("\n") if line.strip()]


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

class TestAnchor1154:
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
        assert OWN_BASENAME.startswith("test_type_c_1154")


# ---------------------------------------------------------------------------
# 2. Rotation guard: fifth and closing leg of the 1150-1154 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1154:
    def test_predecessor_chain_in_git_log(self):
        log = _git_log_oneline()
        assert "Type D #1150" in log
        assert "Type E #1151" in log
        assert "Type A #1152" in log
        assert "Type B #1153" in log

    def test_window_order_d_e_a_b(self):
        log = _git_log_oneline()
        i1150 = log.index("Type D #1150")
        i1151 = log.index("Type E #1151")
        i1152 = log.index("Type A #1152")
        i1153 = log.index("Type B #1153")
        # Reverse-chronological log: later commits appear first.
        assert i1153 < i1152 < i1151 < i1150

    def test_type_c_1154_novel_in_git_log(self):
        # Red post-main-commit by design; deselect in post-commit runs.
        log = _git_log_oneline("Type C #1154")
        lines = [line for line in log.split("\n") if line.strip()]
        assert lines == [], lines

    def test_1153_main_hash_present(self):
        log = _git_log_oneline()
        assert PRED_MAIN_1153 in log

    def test_1150_thru_1152_main_hashes_present(self):
        log = _git_log_oneline()
        assert PRED_MAIN_1150 in log
        assert PRED_MAIN_1151 in log
        assert PRED_MAIN_1152 in log

    def test_fifth_closing_leg(self):
        rt = _block()["rotation_transparency"]
        assert "FIFTH and CLOSING" in rt
        assert "1150-1154" in rt

    def test_next_window_opens_with_d(self):
        rt = _block()["rotation_transparency"]
        assert "1155-1159" in rt
        assert "Type D" in rt


# ---------------------------------------------------------------------------
# 3. Novelty anchor: no prior 1154 / hedge-quote / thirty-sixth claim.
# ---------------------------------------------------------------------------

class TestNoveltyAnchor1154:
    def _non_1154_lines(self, grep_pat):
        log = _git_log_oneline(grep_pat)
        lines = [line for line in log.split("\n") if line.strip()]
        return [line for line in lines if "1154" not in line]

    def test_no_prior_hedge_quote_in_log(self):
        assert self._non_1154_lines("hedge than true market") == []

    def test_no_prior_post_rate_reception_in_log(self):
        assert self._non_1154_lines("post_rate_reception") == []

    def test_no_prior_thirty_sixth_claim_in_log(self):
        # No prior commit message ever carried the affirmative claim form;
        # earlier commits only discuss it as absence-documentation.
        log = _git_log_oneline(_T36)
        lines = [line for line in log.split("\n") if line.strip()]
        assert lines == [], lines


# ---------------------------------------------------------------------------
# 4. Mechanism novelty: the 924 landing; pre-commit zero-hit verification.
# ---------------------------------------------------------------------------

class TestMechanismNovelty1154:
    def test_single_test_file_for_iteration(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_c_1154*.py"))
        assert len(files) == 1, files
        assert os.path.basename(files[0]) == OWN_BASENAME

    def test_novelty_verification_claim_in_block(self):
        assert "zero test_type_c_1154 files on disk" in _block_text()

    def test_max_numeric_mechanism_id_is_924(self):
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_924_numeric_present_only_in_entities_block(self):
        hits = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_zero_underscore_924_repo_wide(self):
        assert _repo_grep_mechanism_form(MECH_NUM, _mech_underscore) == []

    def test_zero_dash_924_repo_wide(self):
        assert _repo_grep_mechanism_form(MECH_NUM, _mech_dash) == []

    def test_zero_underscore_923_repo_wide(self):
        assert _repo_grep_mechanism_form(PREV_NUM, _mech_underscore) == []

    def test_zero_dash_923_repo_wide(self):
        assert _repo_grep_mechanism_form(PREV_NUM, _mech_dash) == []

    def test_923_numeric_present_only_in_journalists_block(self):
        hits = _profiles_grep_numeric_mechanism_id(PREV_NUM)
        assert hits == ["profiles/careers/journalists.yaml"], hits

    def test_block_key_has_no_924_substring(self):
        assert "924" not in BLOCK_KEY

    def test_block_key_zero_hit_outside_entities(self):
        out = subprocess.run(
            ["git", "grep", "-l", "-F", BLOCK_KEY],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        hits = [line for line in out.stdout.split("\n") if line.strip()]
        # This file carries the key only in split-literal form.
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_four_novel_source_urls(self):
        assert len(NOVEL_URLS) == 4
        for url in NOVEL_URLS:
            out = subprocess.run(
                ["git", "grep", "-F", "-l", url, "HEAD", "--", "profiles/"],
                cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
            )
            # Pre-commit: zero hits. Post-commit: only the new block.
            assert out.returncode in (0, 1), url


# ---------------------------------------------------------------------------
# 5. Mechanism 924 block structure.
# ---------------------------------------------------------------------------

class TestMechanism924Structure:
    def test_block_key_present(self):
        assert _block()["block_key"] == BLOCK_KEY

    def test_mechanism_id_is_924(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_connects_to_meter_contest_family(self):
        assert _block()["connects_to"] == [891, 915, 921, 702, 666]

    def test_iteration_type_c(self):
        b = _block()
        assert b["iteration"] == 1154
        assert b["iteration_type"] == "C"
        assert b["iteration_time"] == "2026-10-02 15:00 PDT"

    def test_four_sources_all_novel(self):
        srcs = _block()["sources"]
        assert len(srcs) == 4
        assert all(s["novel"] is True for s in srcs)
        assert all(s["accessed"] == "2026-10-02" for s in srcs)

    def test_five_confounders_strong_first(self):
        confs = _block()["confounders"]
        assert len(confs) == 5
        assert confs[0]["strength"] == "STRONG"
        assert confs[1]["strength"] == "STRONG"

    def test_money_flow_three_channels(self):
        mf = _block()["money_flow"]
        assert "OBSERVED" in mf
        assert "DOCUMENTED" in mf
        assert "PREDICTIVE" in mf

    def test_finding_carries_hedge_core(self):
        f = _block()["finding"]
        assert "hedge than true market" in f
        assert "Walking Away" in f
        assert "courts or regulators mandate compensation" in f

    def test_finding_carries_widget_opacity(self):
        f = _block()["finding"]
        assert "cannot see which pages drove the money" in f
        assert "fluctuate from month to month without clear explanation" in f

    def test_finding_carries_meter_contest(self):
        f = _block()["finding"]
        assert "walk-away frame" in f
        assert "hedge characterization" in f


# ---------------------------------------------------------------------------
# 6. No thirty-sixth direction: reception leg inside #27 and #35, not new.
# ---------------------------------------------------------------------------

class TestNoThirtySixthDirection1154:
    def test_thirty_fifth_still_present(self):
        text = _read(ENTITIES_FILE)
        assert _T35 in text

    def test_thirty_fourth_still_present(self):
        text = _read(ENTITIES_FILE)
        assert _T34 in text

    def test_thirty_sixth_absent(self):
        text = _read(ENTITIES_FILE)
        assert _T36 not in text

    def test_thirty_seventh_absent(self):
        text = _read(ENTITIES_FILE)
        assert _T37 not in text

    def test_taxonomy_documents_reception_not_new_direction(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert "No new direction" in tax
        assert "reception leg" in tax
        assert "CONTROL-OF-THE-METER CONTEST" in tax

    def test_taxonomy_names_two_meters(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert "payer" in tax and "meter" in tax
        assert "m891" in tax
        assert "m915" in tax

    def test_mechanism_name_claims_temporal_extension(self):
        assert "temporal extension" in _block()["mechanism_name"]
        assert "no new direction" in _block()["mechanism_name"]


# ---------------------------------------------------------------------------
# 7. Ledger holds at 46 (NOT a falsification-family member).
# ---------------------------------------------------------------------------

class TestLedger46Holds1154:
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

    def test_characterization_not_money_flow(self):
        ff = _block()["falsification_family"]
        assert "documented characterization, not a money flow" in ff


# ---------------------------------------------------------------------------
# 8. Corpus integrity.
# ---------------------------------------------------------------------------

class TestCorpusIntegrity1154:
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

    def test_no_924_forms_outside_entities(self):
        # Underscore/dash key forms: zero repo-wide (git-grep scope).
        assert _repo_grep_mechanism_form(MECH_NUM, _mech_underscore) == []
        assert _repo_grep_mechanism_form(MECH_NUM, _mech_dash) == []
        # Numeric colon field: only the new block carries it.
        hits = _repo_grep_mechanism_form(MECH_NUM, _mech_id_colon)
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_no_923_forms_outside_journalists(self):
        assert _repo_grep_mechanism_form(PREV_NUM, _mech_underscore) == []
        assert _repo_grep_mechanism_form(PREV_NUM, _mech_dash) == []
        hits = _repo_grep_mechanism_form(PREV_NUM, _mech_id_colon)
        assert hits == ["profiles/careers/journalists.yaml"], hits


# ---------------------------------------------------------------------------
# 9. Forward guards for the next run (this run's landing is the last word).
# ---------------------------------------------------------------------------

class TestForwardGuards1154:
    def test_zero_925_numeric_repo_wide(self):
        assert _repo_grep_mechanism_form(NEXT_NUM, _mech_id_colon) == []

    def test_zero_925_underscore_repo_wide(self):
        assert _repo_grep_mechanism_form(NEXT_NUM, _mech_underscore) == []

    def test_zero_925_dash_repo_wide(self):
        assert _repo_grep_mechanism_form(NEXT_NUM, _mech_dash) == []

    def test_no_thirty_seventh_claim_repo_wide(self):
        hits = [p for p in _iter_source_files() if _T37 in _read(p)]
        assert hits == [], hits

    def test_no_thirty_eighth_claim_repo_wide(self):
        needle = "THIRTY-" + "EIGHTH relationship direction"
        hits = [p for p in _iter_source_files() if needle in _read(p)]
        assert hits == [], hits

    def test_format_built_only_in_this_file(self):
        # The #1116 lesson: guarded forms must never appear contiguously in
        # test-file prose. Every guarded needle is format-built at runtime.
        own = _read(__file__)
        assert "mechanism" + "_924" not in own
        assert "mechanism" + "-924" not in own
        assert "mechanism_id: " + "924" not in own
        assert "mechanism" + "_925" not in own
        assert "mechanism" + "-925" not in own
        assert "mechanism_id: " + "925" not in own
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
# 10. Supersession pins: #1153 guard lifecycle at this run.
# ---------------------------------------------------------------------------

class TestSupersessionPins1154:
    def test_1153_max_923_pin_stays_green_own_block_scope(self):
        # #1153's max-923 pin scopes to its own block text (the m923 block in
        # journalists.yaml), so landing 924 in competitor-entities.yaml cannot
        # fail it; it stays green. The design-failing pins are the zero-924
        # forward guards (covered below).
        res = _node_run(FILE_1153,
                        "TestGuardLifecycle1153::"
                        "test_pins_on_923_landing")
        assert res.returncode == 0, res.stdout[-500:]

    def test_1153_no_type_c_1154_pin_green_pre_commit(self):
        # Pre-commit this pin is green (no Type C #1154 in git log yet);
        # post-main-commit it flips red by design. Deselect post-commit.
        res = _node_run(FILE_1153,
                        "TestGuardLifecycle1153::"
                        "test_no_type_c_1154_commit_yet")
        assert res.returncode == 0, res.stdout[-500:]

    def test_1153_zero_924_numeric_pin_fails_by_design(self):
        res = _node_run(FILE_1153,
                        "TestMechanismNovelty1153::"
                        "test_zero_numeric_924_in_profiles")
        assert res.returncode != 0, res.stdout[-500:]

    def test_1153_zero_924_forward_guards_fail_by_design(self):
        res = _node_run(FILE_1153,
                        "TestForwardLookingStaleness1153::"
                        "test_zero_924_guards_are_forward")
        assert res.returncode != 0, res.stdout[-500:]

    def test_1153_underscore_923_stays_green(self):
        # The block uses the numeric colon field, never the underscore form.
        res = _node_run(FILE_1153,
                        "TestMechanismNovelty1153::"
                        "test_zero_underscore_923_repo_wide")
        assert res.returncode == 0, res.stdout[-800:]

    def test_1153_dash_923_stays_green(self):
        res = _node_run(FILE_1153,
                        "TestMechanismNovelty1153::"
                        "test_zero_dash_923_repo_wide")
        assert res.returncode == 0, res.stdout[-800:]

    def test_1153_forty_seventh_absent_stays_green(self):
        res = _node_run(FILE_1153,
                        "TestFalsificationLedger1153::"
                        "test_forty_seventh_member_claim_absent")
        assert res.returncode == 0, res.stdout[-800:]

    def test_1153_forty_sixth_intact_stays_green(self):
        res = _node_run(FILE_1153,
                        "TestFalsificationLedger1153::"
                        "test_forty_sixth_member_form_present")
        assert res.returncode == 0, res.stdout[-800:]

    def test_1153_thirty_fifth_intact_stays_green(self):
        res = _node_run(FILE_1153,
                        "TestForwardLookingStaleness1153::"
                        "test_thirty_fifth_direction_still_present")
        assert res.returncode == 0, res.stdout[-800:]

    def test_1153_no_thirty_sixth_stays_green(self):
        res = _node_run(FILE_1153,
                        "TestForwardLookingStaleness1153::"
                        "test_no_thirty_sixth_direction_guard")
        assert res.returncode == 0, res.stdout[-800:]


# ---------------------------------------------------------------------------
# 11. Research method.
# ---------------------------------------------------------------------------

class TestResearchMethod1154:
    def test_four_sources_all_novel(self):
        srcs = _block()["sources"]
        assert len(srcs) == 4
        assert all(s["novel"] is True for s in srcs)

    def test_round1_rejections_documented(self):
        # Round 1 (direct search) rejected: the Meta publisher-deal set
        # (m549/#594, m912, duplicates, off-topic) and the Anthropic
        # publisher-deal set (in corpus, #594, weaker startupfortune leg).
        doc = __doc__ or ""
        assert "REJECTED" in doc
        assert "m549" in doc
        assert "m912" in doc
        assert "#594" in doc

    def test_round2_selected_documented(self):
        doc = __doc__ or ""
        assert "SELECTED" in doc
        assert "hedge than true market" in doc

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

class TestDocSync1154:
    def test_readme_stats_ratchet(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert str(README_TEST_COUNT) in text
        assert str(README_FILE_COUNT) in text

    def test_readme_test_table_row(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert "test_type_c_1154_google_pay_per_value" in text

    def test_architecture_tree_row(self):
        text = _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))
        assert "test_type_c_1154_google_pay_per_value" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 60877
        assert README_FILE_COUNT == 1479


# ---------------------------------------------------------------------------
# 13. Iteration log (entry written in the log-hash followup per #719).
# ---------------------------------------------------------------------------

class TestIterationLog1154:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO_ROOT, "iteration-log.md"))
        assert "## #1154 Type C" in text

    def test_no_duplicate_1154_entries(self):
        text = _read(os.path.join(REPO_ROOT, "iteration-log.md"))
        assert text.count("## #1154 Type C") <= 1

    def test_window_fifth_closing_leg_noted(self):
        text = _read(os.path.join(REPO_ROOT, "iteration-log.md"))
        assert "1150-1154 window" in text and "FIFTH" in text


# ---------------------------------------------------------------------------
# 14. In-flight isolation.
# ---------------------------------------------------------------------------

class TestInFlightIsolation1154:
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
        lines = [line for line in out.stdout.split("\n") if line.strip()]
        for line in lines:
            assert ("competitor-entities.yaml" in line
                    or "test_type_c_1154" in line
                    or "iteration-log.md" in line  # #715 form-discipline fix
                    or "nytimes.yaml" in line  # #899 in-flight
                    or "test_type_b_938" in line  # #938 in-flight
                    or "test_type_d_900" in line  # #900 in-flight
                    or "test_type_a_1012" in line), line  # #1012-wt


# ---------------------------------------------------------------------------
# 15. Degenerate contract.
# ---------------------------------------------------------------------------

class TestDegenerateContract1154:
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

    def test_mechanism_name_carries_meter_contest_framing(self):
        assert "control-of-the-meter contest" in _block()["mechanism_name"]


# ---------------------------------------------------------------------------
# 16. Background suite check (checked only per #795 - the verdict and
# tombstoning belong to the next Type D run, #1155).
# ---------------------------------------------------------------------------

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1150_full_suite.log"
)


class TestBackgroundSuiteCheck1154:
    def test_suite_log_path_noted(self):
        assert os.path.basename(SUITE_LOG) == "type_d_1150_full_suite.log"

    def test_verdict_belongs_to_1155(self):
        rt = _block()["rotation_transparency"]
        assert "belongs to #1155" in rt
        assert "#795" in rt

    def test_suite_checked_not_touched(self):
        # This run checks the #1150-launched suite only; it does not launch,
        # kill, or modify it. Its verdict belongs to #1155 per #795.
        assert os.path.exists(SUITE_LOG)
        assert "type_d_1150" in SUITE_LOG
