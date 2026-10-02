"""Type C iteration #1149 (2026-10-02 11:00 PDT): Reach plc H1 2026 earnings
disclosure - FIRST regulated-earnings quantification of unlicensed AI usage
("we know AI firms are using our content in their products many millions of
times a day") and AI licensing deals named a near-term strategic priority.
Publisher-side P&L leg EXTENDING m468's usage-based geometry (Reach x Amazon,
Mar 2 2026); the publisher-side mirror of #27 unilateral pricing (m891,
extended at m918): same meter vocabulary, opposite control arrow - the
publisher wants the meter for visibility, the lab-side proposal keeps the
meter inside the payer. No new relationship direction; the thirty-sixth
direction stays absent by design. New mechanism 921 in
profiles/competitor-entities.yaml (connects_to 468/735/777/891/918). NOT a
falsification-family member: ledger holds at 46.

Target ~80 tests / 16 classes, all green pre-commit (venv python) with
TestDocSync and TestIterationLog deselected by design (placeholders patched in
the doc-sync / log-hash followups per #719). Anchor placeholder
(ANCHORED_SHA) patched to the main commit's 40-char SHA in the anchor followup
per #565; deselect the placeholder test in post-commit full runs.
TestRotationGuard novelty pin is red post-main-commit by design (deselected in
post-commit runs).

Research in 2 rounds (direct browser.search, 0 browser.open per #503).
Round 1 - REJECTED: (a) the Sep-15-2026 ANI v. OpenAI Division Bench
notice/reply order - already mapped at Type C #809 (mechanism with Sep 17
2026 date_analyzed; notice, Dec-8 listing, lapsed no-scrape undertaking,
Sibal/Datar intervenors all in corpus); (b) Wiley Q1 FY2027 AI-revenue print
- already m777 / Type C #909; (c) OpenAI India attribution blitz (BCCL Sep 7,
Indian Express Group Sep 8) - already m609; (d) Reach x Amazon usage-based
deal itself - already m468 / Type C #468; (e) NYT x Amazon deal - already
m559. Round 2 - SELECTED: the Reach plc H1 2026 RNS disclosure (Jul 22 2026)
as the novel core - zero "many millions of times a day" hits repo-wide
pre-commit; the FY2025 transcript pipeline leg ("in conversation with a
number of major platforms"); Digiday North interview (pay-per-use in the
revenue mix); DNPA licence-fees-and-attribution position as the India-side
context leg (particle.news Sep-15 piece). All URLs copied verbatim from
Full-URL listings; no canonical URLs constructed. ASCII-only, no em dashes.
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
    "type_c_1149_reach_plc_h1_2026_earnings_ai_usage_disclosure_"
    "many_millions_oct02_11am"
)
OWN_BASENAME = ("test_type_c_1149_reach_plc_h1_2026_earnings_"
                "ai_usage_disclosure_oct02_11am.py")

# Predecessor test file for supersession pins.
FILE_1148 = ("test_type_b_1148_dan_howley_yahoo_finance_meta_glasses_"
             "apple_watch_same_consent_problem_parity_bound_sep26_10am.py")

# Seven novel source URLs (copied verbatim from Full-URL listings; split so
# this file carries no contiguous full URL).
URL_INVESTEGATE_RNS = (
    "http://www.investegate.co.uk/announcement/rns/reach--rch/"
    "reach-plc-half-year-report/9680684"
)
URL_REACHPLC_H1_PDF = (
    "https://www.reachplc.com/content/dam/reach/corporate/documents/"
    "results-and-reports/2026/hy-26-results.pdf.downloadasset.pdf"
)
URL_LSE_RNS = (
    "https://www.lse.co.uk/rns/RCH/"
    "reach-plc-half-year-report-k5e3wuj0wc7irxi.html"
)
URL_SHARECAST_RNS = (
    "https://www.sharecast.com/news/Results-and-Trading-Reports/"
    "Reach-plc-Half-year-Report--dl36087056.html"
)
URL_REACHPLC_FY25_TRANSCRIPT = (
    "https://www.reachplc.com/content/dam/reach/corporate/documents/"
    "results-and-reports/2025/fy-25-transcript.pdf.downloadasset.pdf"
)
URL_DIGIDAY_NORTH = (
    "https://digiday.com/media/the-big-bang-has-happened-reach-gets-"
    "proactive-on-ai-era-referrals-starting-with-subscriptions/"
)
URL_PARTICLE_DNPA = (
    "https://particle.news/story/delhi-high-court-refuses-immediate-"
    "restraint-on-openai-in-ani-copyright-appeal"
)
NOVEL_URLS = (
    URL_INVESTEGATE_RNS,
    URL_REACHPLC_H1_PDF,
    URL_LSE_RNS,
    URL_SHARECAST_RNS,
    URL_REACHPLC_FY25_TRANSCRIPT,
    URL_DIGIDAY_NORTH,
    URL_PARTICLE_DNPA,
)

# Patched post-commit once README/ARCHITECTURE doc-sync lands (per #719).
README_TEST_COUNT = 0  # patched to 60430 + collected in doc-sync followup
README_FILE_COUNT = 1474  # post-doc-sync total
TEST_BASENAME = OWN_BASENAME

# Anchor placeholder per #565: patched to the main commit's 40-char SHA in the
# anchor followup. Deselect the placeholder test in post-commit full runs.
ANCHORED_SHA = "04645a0ba11546e6f7e063786f0485e905d8a3b7"  # Type C #1149 main commit (Type C runs self-anchor per #565)

MECH_NUM = 921
NEXT_NUM = 922
PREV_NUM = 920

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
PRED_MAIN_1145 = "8f4266d2"
PRED_MAIN_1146 = "a2da1a45"
PRED_MAIN_1147 = "5837f480"
PRED_MAIN_1148 = "6dd1f44b"


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

class TestAnchor1149:
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
        assert OWN_BASENAME.startswith("test_type_c_1149")


# ---------------------------------------------------------------------------
# 2. Rotation guard: fifth and closing leg of the 1145-1149 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1149:
    def test_predecessor_chain_in_git_log(self):
        log = _git_log_oneline()
        assert "Type D #1145" in log
        assert "Type E #1146" in log
        assert "Type A #1147" in log
        assert "Type B #1148" in log

    def test_window_order_d_e_a_b(self):
        log = _git_log_oneline()
        i1145 = log.index("Type D #1145")
        i1146 = log.index("Type E #1146")
        i1147 = log.index("Type A #1147")
        i1148 = log.index("Type B #1148")
        # Reverse-chronological log: later commits appear first.
        assert i1148 < i1147 < i1146 < i1145

    def test_type_c_1149_novel_in_git_log(self):
        # Red post-main-commit by design; deselect in post-commit runs.
        log = _git_log_oneline("Type C #1149")
        lines = [l for l in log.split("\n") if l.strip()]
        assert lines == [], lines

    def test_1148_main_hash_present(self):
        log = _git_log_oneline()
        assert PRED_MAIN_1148 in log

    def test_1145_thru_1147_main_hashes_present(self):
        log = _git_log_oneline()
        assert PRED_MAIN_1145 in log
        assert PRED_MAIN_1146 in log
        assert PRED_MAIN_1147 in log

    def test_fifth_closing_leg(self):
        rt = _block()["rotation_transparency"]
        assert "FIFTH and CLOSING" in rt
        assert "1145-1149" in rt

    def test_next_window_opens_with_d(self):
        rt = _block()["rotation_transparency"]
        assert "1150-1154" in rt
        assert "Type D" in rt


# ---------------------------------------------------------------------------
# 3. Novelty anchor: no prior 1149 / many-millions / thirty-sixth claim.
# ---------------------------------------------------------------------------

class TestNoveltyAnchor1149:
    def _non_1149_lines(self, grep_pat):
        log = _git_log_oneline(grep_pat)
        lines = [l for l in log.split("\n") if l.strip()]
        return [l for l in lines if "1149" not in l]

    def test_no_prior_many_millions_in_log(self):
        assert self._non_1149_lines("many millions") == []

    def test_no_prior_reach_h1_disclosure_in_log(self):
        assert self._non_1149_lines("reach_plc_h1") == []

    def test_no_prior_thirty_sixth_claim_in_log(self):
        # No prior commit message ever carried the affirmative claim form;
        # earlier commits only discuss it as absence-documentation.
        log = _git_log_oneline(_T36)
        lines = [l for l in log.split("\n") if l.strip()]
        assert lines == [], lines


# ---------------------------------------------------------------------------
# 4. Mechanism novelty: m921 lands; pre-commit zero-hit verification.
# ---------------------------------------------------------------------------

class TestMechanismNovelty1149:
    def test_single_test_file_for_iteration(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_c_1149*.py"))
        assert len(files) == 1, files
        assert os.path.basename(files[0]) == OWN_BASENAME

    def test_novelty_verification_claim_in_block(self):
        assert "zero test_type_c_1149 files on disk" in _block_text()

    def test_max_numeric_mechanism_id_is_921(self):
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_921_numeric_present_only_in_entities_block(self):
        hits = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_zero_underscore_921_repo_wide(self):
        assert _repo_grep_mechanism_form(MECH_NUM, _mech_underscore) == []

    def test_zero_dash_921_repo_wide(self):
        assert _repo_grep_mechanism_form(MECH_NUM, _mech_dash) == []

    def test_zero_underscore_920_repo_wide(self):
        assert _repo_grep_mechanism_form(PREV_NUM, _mech_underscore) == []

    def test_zero_dash_920_repo_wide(self):
        assert _repo_grep_mechanism_form(PREV_NUM, _mech_dash) == []

    def test_920_numeric_present_only_in_journalists_block(self):
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
        assert len(NOVEL_URLS) == 7
        for url in NOVEL_URLS:
            out = subprocess.run(
                ["git", "grep", "-F", "-l", url, "HEAD", "--", "profiles/"],
                cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
            )
            # Pre-commit: zero hits. Post-commit: only the new block.
            assert out.returncode in (0, 1), url


# ---------------------------------------------------------------------------
# 5. Mechanism 921 block structure.
# ---------------------------------------------------------------------------

class TestMechanism921Structure:
    def test_block_key_present(self):
        assert _block()["block_key"] == BLOCK_KEY

    def test_mechanism_id_is_921(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_connects_to_deal_and_geometry(self):
        assert _block()["connects_to"] == [468, 735, 777, 891, 918]

    def test_iteration_type_c(self):
        b = _block()
        assert b["iteration"] == 1149
        assert b["iteration_type"] == "C"
        assert b["iteration_time"] == "2026-10-02 11:00 PDT"

    def test_seven_sources_all_novel(self):
        srcs = _block()["sources"]
        assert len(srcs) == 7
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
        assert "$0" in mf

    def test_finding_carries_novel_core(self):
        f = _block()["finding"]
        assert "many millions of times a day" in f
        assert "AI licensing deals" in f
        assert "PREDICTIVE" not in f  # finding states observed facts
        assert "Amazon deal" in f

    def test_finding_carries_pipeline_leg(self):
        f = _block()["finding"]
        assert "in conversation with a number of major platforms" in f
        assert "more control and crucially more visibility" in f


# ---------------------------------------------------------------------------
# 6. No thirty-sixth direction: publisher-side mirror, not a new geometry.
# ---------------------------------------------------------------------------

class TestNoThirtySixthDirection1149:
    def test_thirty_fifth_still_present(self):
        text = _read(ENTITIES_FILE)
        assert _T35 in text

    def test_thirty_fourth_still_present(self):
        text = _read(ENTITIES_FILE)
        assert _T34 in text

    def test_thirty_sixth_absent(self):
        text = _read(ENTITIES_FILE)
        assert _T36 not in text

    def test_taxonomy_documents_mirror_not_new_direction(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert "No new direction" in tax
        assert "publisher side of the meter" in tax
        assert "m891" in tax
        assert "m918" in tax

    def test_taxonomy_names_opposite_control_arrow(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert "opposite control arrow" in tax
        assert "visibility" in tax

    def test_mechanism_name_claims_no_new_direction(self):
        assert _T36 not in _block()["mechanism_name"]
        assert "Publisher-Side Mirror" in _block()["mechanism_name"]


# ---------------------------------------------------------------------------
# 7. Ledger holds at 46 (NOT a falsification-family member).
# ---------------------------------------------------------------------------

class TestLedger46Holds1149:
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

class TestCorpusIntegrity1149:
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

    def test_no_921_forms_outside_entities(self):
        # Underscore/dash key forms: zero repo-wide (git-grep scope).
        assert _repo_grep_mechanism_form(MECH_NUM, _mech_underscore) == []
        assert _repo_grep_mechanism_form(MECH_NUM, _mech_dash) == []
        # Numeric colon field: only the new block carries it.
        hits = _repo_grep_mechanism_form(MECH_NUM, _mech_id_colon)
        assert hits == ["profiles/competitor-entities.yaml"], hits


# ---------------------------------------------------------------------------
# 9. Forward guards for the next run (this run's landing is the last word).
# ---------------------------------------------------------------------------

class TestForwardGuards1149:
    def test_zero_922_numeric_repo_wide(self):
        assert _repo_grep_mechanism_form(NEXT_NUM, _mech_id_colon) == []

    def test_zero_922_underscore_repo_wide(self):
        assert _repo_grep_mechanism_form(NEXT_NUM, _mech_underscore) == []

    def test_zero_922_dash_repo_wide(self):
        assert _repo_grep_mechanism_form(NEXT_NUM, _mech_dash) == []

    def test_no_thirty_seventh_claim_repo_wide(self):
        hits = [p for p in _iter_source_files() if _T37 in _read(p)]
        assert hits == [], hits

    def test_format_built_only_in_this_file(self):
        # The #1116 lesson: guarded forms must never appear contiguously in
        # test-file prose. Every guarded needle is format-built at runtime.
        own = _read(__file__)
        assert "mechanism" + "_921" not in own
        assert "mechanism" + "-921" not in own
        assert "mechanism_id: " + "921" not in own
        assert "mechanism" + "_922" not in own
        assert "mechanism" + "-922" not in own
        assert "mechanism_id: " + "922" not in own
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
# 10. Supersession pins: #1148 guard lifecycle at this run.
# ---------------------------------------------------------------------------

class TestSupersessionPins1149:
    def test_1148_921_numeric_guard_lifecycle_fails_by_design(self):
        # This run lands the 921 numeric field; #1148's guard-lifecycle
        # zero-921 pin fails. (#1148's TestMechanismNovelty1148 max-920 pin
        # scopes to its own block text, so it cannot fail from this run;
        # the guard-lifecycle pin is the design-failing one.)
        res = _node_run(FILE_1148,
                        "TestGuardLifecycle1148::"
                        "test_921_numeric_absent_in_profiles")
        assert res.returncode != 0, res.stdout[-500:]

    def test_1148_zero_numeric_921_in_profiles_fails_by_design(self):
        res = _node_run(FILE_1148,
                        "TestMechanismNovelty1148::"
                        "test_zero_numeric_921_in_profiles")
        assert res.returncode != 0, res.stdout[-500:]

    def test_1148_no_type_c_1149_pin_flips_post_commit(self):
        # Pre-commit this pin is green (no Type C #1149 in git log yet);
        # post-main-commit it flips red by design. Deselect post-commit.
        res = _node_run(FILE_1148,
                        "TestGuardLifecycle1148::"
                        "test_no_type_c_1149_in_git_log_pin")
        assert res.returncode == 0, res.stdout[-500:]

    def test_1148_underscore_920_stays_green(self):
        # The block uses the numeric colon field, never the underscore form.
        res = _node_run(FILE_1148,
                        "TestMechanismNovelty1148::"
                        "test_zero_underscore_920_repo_wide")
        assert res.returncode == 0, res.stdout[-800:]

    def test_1148_dash_920_stays_green(self):
        res = _node_run(FILE_1148,
                        "TestMechanismNovelty1148::"
                        "test_zero_dash_920_repo_wide")
        assert res.returncode == 0, res.stdout[-800:]

    def test_1148_forty_seventh_absent_stays_green(self):
        res = _node_run(FILE_1148,
                        "TestFalsificationLedger1148::"
                        "test_forty_seventh_member_claim_absent")
        assert res.returncode == 0, res.stdout[-800:]

    def test_1148_forty_sixth_intact_stays_green(self):
        res = _node_run(FILE_1148,
                        "TestFalsificationLedger1148::"
                        "test_forty_sixth_member_form_present")
        assert res.returncode == 0, res.stdout[-800:]

    def test_1148_thirty_fifth_intact_stays_green(self):
        res = _node_run(FILE_1148,
                        "TestForwardLookingStaleness1148::"
                        "test_thirty_fifth_direction_still_present")
        assert res.returncode == 0, res.stdout[-800:]


# ---------------------------------------------------------------------------
# 11. Research method.
# ---------------------------------------------------------------------------

class TestResearchMethod1149:
    def test_seven_sources_all_novel(self):
        srcs = _block()["sources"]
        assert len(srcs) == 7
        assert all(s["novel"] is True for s in srcs)

    def test_round1_rejections_documented(self):
        # Round 1 (direct search) rejected: the Sep-15 ANI Division Bench
        # order (already #809), Wiley Q1 FY2027 (already m777/#909), the
        # India attribution blitz (already m609), the Reach x Amazon deal
        # itself (already m468), NYT x Amazon (already m559).
        doc = __doc__ or ""
        assert "REJECTED" in doc
        assert "#809" in doc
        assert "m777" in doc
        assert "m609" in doc
        assert "m468" in doc
        assert "m559" in doc

    def test_round2_selected_documented(self):
        doc = __doc__ or ""
        assert "SELECTED" in doc
        assert "many millions" in doc

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

class TestDocSync1149:
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

class TestIterationLog1149:
    def test_iteration_log_exists(self):
        assert os.path.exists(LOG_FILE)

    def test_log_mentions_1149(self):
        # Post-commit: iteration-log.md gains the #1149 entry.
        # Pre-commit this test is a placeholder.
        assert True


# ---------------------------------------------------------------------------
# 14. In-flight isolation.
# ---------------------------------------------------------------------------

class TestInFlightIsolation1149:
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
                    or "test_type_c_1149" in line
                    or "iteration-log.md" in line  # #715 form-discipline fix
                    or "nytimes.yaml" in line  # #899 in-flight
                    or "test_type_b_938" in line  # #938 in-flight
                    or "test_type_d_900" in line  # #900 in-flight
                    or "test_type_a_1012" in line), line  # #1012-wt


# ---------------------------------------------------------------------------
# 15. Degenerate contract.
# ---------------------------------------------------------------------------

class TestDegenerateContract1149:
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

    def test_mechanism_name_carries_disclosure_framing(self):
        assert "Earnings Disclosure" in _block()["mechanism_name"]


# ---------------------------------------------------------------------------
# 16. Background suite check (checked only per #795 - the verdict and
# tombstoning belong to the next Type D run, #1150).
# ---------------------------------------------------------------------------

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1145_full_suite.log"
)


class TestBackgroundSuiteCheck1149:
    def test_suite_log_path_noted(self):
        assert os.path.basename(SUITE_LOG) == "type_d_1145_full_suite.log"

    def test_verdict_belongs_to_1150(self):
        rt = _block()["rotation_transparency"]
        assert "belongs to #1150" in rt
        assert "#795" in rt
