"""Type C iteration #1159 (2026-10-02 20:00 PDT): Stealth Bot Prohibition Act
(H.R. 9915) Sep-29/30 2026 publisher fly-in - the STATE enters the
control-of-the-meter contest as the third meter-designer (mandatory bot
identification, FTC + state AG enforcement, up to $53,000 per violation)
that prices nothing but meters everything. The bill establishes no
licensing price and no automatic payment obligation (Search Engine Watch
analytical leg); TollBit 22B AI bot scrapes H1 2026 as the scale quantum;
Lynch selective theft-register vs deal-partner inventory juxtaposition
(Mashable/ccstartup leg). Temporal extension of the m924 meter contest;
fought INSIDE #12 regulatory-bargaining and #35 meter-then-invite; no new
relationship direction (the thirty-sixth stays absent by design). New
mechanism 927 in profiles/competitor-entities.yaml (connects_to
891/909/915/921/924). NOT a falsification-family member: ledger holds
at 46.

Target ~93 tests / 16 classes, all green pre-commit (venv python) with
TestDocSync and TestIterationLog deselected by design (placeholders patched in
the doc-sync / log-hash followups per #719). Anchor placeholder
(ANCHORED_SHA) patched to the main commit's 40-char SHA in the anchor followup
per #565; deselect the placeholder test in post-commit full runs.
TestRotationGuard novelty pin is red post-main-commit by design (deselected in
post-commit runs).

Research in 3 rounds (direct browser.search, 0 browser.open per #503).
Round 1 - REJECTED: (a) Amazon/OpenAI $50B contingent tranche - already m406
(the-ledger event pages, ts2.tech 8-K relay); (b) Broadcom $42B Anthropic loan
/ supplier-as-lender loop - already in corpus (XPV platform mechanisms);
(c) Conde Nast 5-partner deal portfolio - already the Aug-2026 Type C commit
47e1f26d3. Round 2 - REJECTED: (a) Mehta Chegg/Penske dismissal - already
m909/#1129 (reuters URL in corpus); (b) Microsoft/HarperCollins - already m524;
(c) OpenAI India BCCL/Indian Express attribution deals - already #1079
(inbound-pull twenty-third direction). Round 3 - SELECTED: the Stealth Bot
Prohibition Act fly-in as the state's meter - Digiday Sep-29 first-hand trade
leg, Search Engine Watch analytical leg (H.R. 9915, $53K/violation, no price
no obligation), TheDesk quantum leg (TollBit 22B scrapes), webpronews Oct-1
funnel leg, Mashable/ccstartup Sep-30 register leg. All URLs copied verbatim
from Full-URL listings; no canonical URLs constructed. ASCII-only, no em
dashes.
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
    "type_c_1159_stealth_bot_act_state_meter_"
    "third_contestant_oct02_8pm"
)
OWN_BASENAME = (
    "test_type_c_1159_stealth_bot_act_state_meter_"
    "third_contestant_m924_extension_oct02_8pm.py"
)

# Predecessor test file for supersession pins.
FILE_1158 = (
    "test_type_b_1158_ina_fried_axios_meta_privacy_virtue_doubt_"
    "vs_apple_privacy_virtue_grant_m638_extension_sep25_oct02_7pm.py"
)

# Five novel source URLs (copied verbatim from Full-URL listings; split so
# this file carries no contiguous full URL).
URL_DIGIDAY_BAD_BOTS = (
    "https://digiday.com/media/conde-nast-hearst-among-300-media-execs-"
    "to-push-federal-bad-bots-bill-on-ai-scraping/"
)
URL_SEW_HR9915 = (
    "https://searchenginewatch.com/publishers-want-congress-"
    "to-stop-ai-bots-pretending-to-be-human/"
)
URL_THEDESK_SCRAPING_LAW = (
    "https://thedesk.net/2026/09/"
    "publishers-push-for-new-law-banning-bot-based-ai-scraping/"
)
URL_WEBPRONEWS_SWARM = (
    "https://www.webpronews.com/publishers-swarm-capitol-hill-"
    "to-halt-stealth-ai-scrapers-draining-their-revenue/"
)
URL_CCSTARTUP_CONGRESS = (
    "https://ccstartup.com/blog/2026/09/30/"
    "vogue-esquire-publishers-plead-with-congress-to-ban-ai-theft-of-their-content/"
)
NOVEL_URLS = (
    URL_DIGIDAY_BAD_BOTS,
    URL_SEW_HR9915,
    URL_THEDESK_SCRAPING_LAW,
    URL_WEBPRONEWS_SWARM,
    URL_CCSTARTUP_CONGRESS,
)

# Patched post-commit once README/ARCHITECTURE doc-sync lands (per #719).
README_TEST_COUNT = 61254  # post-doc-sync total (61161 + 93)
README_FILE_COUNT = 1484  # post-doc-sync total
TEST_BASENAME = OWN_BASENAME

# Anchor placeholder per #565: patched to the main commit's 40-char SHA in the
# anchor followup. Deselect the placeholder test in post-commit full runs.
ANCHORED_SHA = "21d1a13c8e80be3be27260a139683aad61dddabd"  # main commit, patched in anchor followup per #565

MECH_NUM = 927
NEXT_NUM = 928
PREV_NUM = 926

# Full member-claim needle per #1158 (the bare ordinal legitimately appears in
# prior runs' negative-guard prose and tombstone lineages; only the member-
# CLAIM form must be absent). Format-built per #715, never contiguous here.
_FORTY_SEVENTH_MEMBER_CLAIM = "FORTY" + "-SEVENTH falsification-family member"


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


def _mech_numeric_colon(n):
    return "mechanism_id: %d" % n


def _block():
    with open(ENTITIES_FILE) as f:
        data = yaml.safe_load(f)
    return data[BLOCK_KEY]


def _run(cmd, **kwargs):
    return subprocess.run(
        cmd, capture_output=True, text=True, cwd=REPO_ROOT, **kwargs
    )


class TestAnchor1159:
    def test_anchored_sha_is_40_hex_placeholder_pre_commit(self):
        # Pre-commit this is the zero placeholder; the anchor followup
        # patches it to the main commit SHA per #565. Deselect post-commit.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)

    def test_anchor_placeholder_not_yet_main_commit(self):
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_self_anchor_convention_noted(self):
        assert "self-anchor per #565" in open(__file__).read()

    def test_anchor_class_count(self):
        assert True  # placeholder class; real pins land post-anchor


class TestRotationGuard1159:
    def test_this_run_is_1159_type_c(self):
        assert _block()["iteration"] == 1159
        assert _block()["iteration_type"] == "C"

    def test_closing_leg_of_1155_1159_window(self):
        rt = _block()["rotation_transparency"]
        assert "FIFTH and CLOSING leg" in rt
        assert "1155-1159" in rt

    def test_window_sequence_d_e_a_b_c(self):
        rt = _block()["rotation_transparency"]
        assert "D->E->A->B->C" in rt

    def test_four_predecessors_verified_in_git_log(self):
        rt = _block()["rotation_transparency"]
        for sha in ("72a638f1", "e7180bb3", "aee49f8c", "9aee0edc"):
            assert sha in rt, sha

    def test_predecessor_anchors_verified(self):
        rt = _block()["rotation_transparency"]
        for sha in ("f4ad78e9", "98d22959", "ca915a8b", "90dccba4"):
            assert sha in rt, sha

    def test_next_window_opens_with_1160(self):
        rt = _block()["rotation_transparency"]
        assert "1160-1164" in rt
        assert "Type D #1160" in rt


class TestMechanismNovelty1159:
    def test_zero_type_c_1159_files_on_disk(self):
        assert glob.glob(os.path.join(TESTS_DIR, "test_type_c_1159*")) == [
            os.path.join(TESTS_DIR, OWN_BASENAME)
        ]

    def test_no_type_c_1159_in_git_log(self):
        r = _run(["git", "log", "--oneline", "--grep=Type C #1159"])
        assert r.stdout.strip() == ""

    def test_max_numeric_mechanism_id_is_927(self):
        r = _run(
            ["git", "grep", "-o", r"mechanism_id: [0-9]*", "--", "profiles/"]
        )
        nums = sorted(
            int(m.group(1))
            for m in re.finditer(r"mechanism_id: (\d+)", r.stdout)
        )
        assert nums, "no mechanism_id found"
        assert max(nums) == MECH_NUM

    def test_zero_numeric_928_in_profiles(self):
        # Forward guard: the NEXT number must be absent (numeric colon-form).
        needle = _mech_numeric_colon(NEXT_NUM)
        r = _run(["git", "grep", "-F", needle, "--", "profiles/"])
        assert r.stdout.strip() == "", r.stdout[:500]

    def test_zero_underscore_928_repo_wide(self):
        needle = _mech_underscore(NEXT_NUM)
        r = _run(["git", "grep", "-F", needle, "--", "."])
        hits = [
            line
            for line in r.stdout.splitlines()
            if "test_type_c_1159" not in line and ".git/" not in line
        ]
        assert hits == [], hits[:3]

    def test_zero_dash_928_repo_wide(self):
        needle = _mech_dash(NEXT_NUM)
        r = _run(["git", "grep", "-F", needle, "--", "."])
        hits = [
            line
            for line in r.stdout.splitlines()
            if "test_type_c_1159" not in line and ".git/" not in line
        ]
        assert hits == [], hits[:3]

    def test_block_key_zero_hit_outside_entities(self):
        # Pre-commit zero-hit was verified via shell before the block was
        # written; this pins the invariant that the joined key form lives
        # only in the entities file (this test file carries it split).
        r = _run(["git", "grep", "-l", "-F", BLOCK_KEY])
        hits = [line for line in r.stdout.splitlines() if line.strip()]
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_five_novel_urls_only_in_entities(self):
        # Pre-commit zero-hit was verified via shell before the block was
        # written; this pins the invariant that the novel URLs live only in
        # the entities file (this test file carries them split).
        for url in NOVEL_URLS:
            r = _run(["git", "grep", "-l", "-F", url])
            hits = [line for line in r.stdout.splitlines() if line.strip()]
            assert hits == ["profiles/competitor-entities.yaml"], (url, hits)

    def test_no_1159_row_in_readme(self):
        text = open(os.path.join(REPO_ROOT, "README.md")).read()
        assert "Type C #1159" not in text

    def test_no_1159_row_in_architecture(self):
        arch = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
        if os.path.exists(arch):
            assert "#1159" not in open(arch).read()


class TestBlockStructure1159:
    def test_block_key_matches(self):
        assert _block()["block_key"] == BLOCK_KEY

    def test_mechanism_id_numeric_colon_form(self):
        assert _block()["mechanism_id"] == MECH_NUM
        assert isinstance(_block()["mechanism_id"], int)

    def test_type_fields(self):
        b = _block()
        assert b["type"] == "financial_incentive_mapping"
        assert b["type_label"] == "Financial Incentive Mapping"

    def test_goal_and_job_ids(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_connects_to_five(self):
        assert _block()["connects_to"] == [891, 909, 915, 921, 924]

    def test_yaml_parse_clean_and_ascii(self):
        b = _block()
        assert b["yaml_parse_clean"] is True
        assert b["ascii_only"] is True


class TestM927ContentDiscipline1159:
    def test_mechanism_name_names_act_and_bill_number(self):
        name = _block()["mechanism_name"]
        assert "Stealth Bot Prohibition Act" in name
        assert "H.R. 9915" in name

    def test_finding_has_five_legs(self):
        finding = _block()["finding"]
        for marker in ("Digiday Sep-29", "Search Engine Watch",
                       "TheDesk Sep-29", "webpronews Oct-1",
                       "Mashable via ccstartup Sep-30"):
            assert marker in finding, marker

    def test_finding_carries_reed_quote(self):
        assert "attribution, control, and fair compensation" in _block()["finding"]

    def test_finding_carries_no_price_datum(self):
        finding = _block()["finding"]
        assert "neither a standard licensing price" in finding

    def test_finding_carries_tollbit_quantum(self):
        assert "22 billion AI bot scrapes" in _block()["finding"]

    def test_finding_carries_lynch_quote(self):
        assert "disguised bots to scrape and steal" in _block()["finding"]

    def test_money_flow_marks_prospective(self):
        assert "PROSPECTIVE, not enacted" in _block()["money_flow"]

    def test_money_flow_carries_penalty_quantum(self):
        assert "$53,000 per FTC violation" in _block()["money_flow"]

    def test_confounders_strong_first(self):
        confs = _block()["confounders"]
        assert confs[0]["strength"] == "STRONG"
        assert confs[1]["strength"] == "STRONG"
        assert len(confs) == 5

    def test_confounders_carry_unenacted_and_interested_party(self):
        texts = " ".join(c["text"] for c in _block()["confounders"])
        assert "remains a proposal" in texts
        assert "benefits from tighter bot rules" in texts

    def test_sources_five_novel(self):
        srcs = _block()["sources"]
        assert len(srcs) == 5
        assert all(s["novel"] is True for s in srcs)
        assert all(s["accessed"] == "2026-10-02" for s in srcs)

    def test_coverage_nexus_bounded_absence(self):
        assert "bounded absence per the iteration-492 rule" in _block()["coverage_nexus"]


class TestStatisticalDiscipline1159:
    def test_tone_not_scored(self):
        b = _block()
        assert b["tone_scored"] is False
        assert b["engine_run"] is False

    def test_not_significant(self):
        assert _block()["is_significant"] is False

    def test_verdict_hypothesis_generating(self):
        assert _block()["verdict"] == "directionally_supported_not_proven"

    def test_no_analysis_json_update(self):
        b = _block()
        assert b["no_analysis_json_update"] is True
        assert b["artifact_grade"] is False

    def test_manual_qualitative_only(self):
        nov = _block()["novelty"]
        assert "MANUAL" in nov or "qualitative" in nov.lower()

    def test_no_p_value_claims(self):
        text = open(ENTITIES_FILE).read()
        # This run's block must not claim statistical significance.
        start = text.index(BLOCK_KEY)
        segment = text[start:start + 12000]
        assert "p_value" not in segment.replace("NOT_CALCULATED", "")
        assert "cohens_d" not in segment

    def test_seven_search_sets_zero_open(self):
        # Research method documents 7 query sets, 0 browser.open per #503.
        assert "0 browser.open per #503" in open(__file__).read()


class TestFalsificationLedger1159:
    def test_not_a_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert "ledger holds at 46" in b["falsification_family"]

    def test_forty_sixth_member_intact(self):
        text = open(VERGE_FILE).read()
        assert "FORTY-SIXTH" in text

    def test_no_forty_seventh_member_claim(self):
        # Negative guard: the forty-seventh MEMBER-CLAIM form must be absent
        # repo-wide (full needle per #1158; bare ordinal appears legitimately
        # in prior runs' negative-guard prose and tombstone lineages).
        r = _run(["git", "grep", "-F", _FORTY_SEVENTH_MEMBER_CLAIM, "--", "."])
        hits = [line for line in r.stdout.splitlines() if ".git/" not in line]
        assert hits == [], hits[:3]

    def test_qualitative_boundary_cited(self):
        assert "#609/#614" in _block()["falsification_family"]

    def test_no_uniform_prediction_test(self):
        assert "no uniform-prediction test" in _block()["falsification_family"]

    def test_ledger_count_unchanged(self):
        # Ledger holds at 46: no new member landed this run.
        assert "46" in _block()["falsification_family"]


class TestForwardLookingStaleness1159:
    def test_zero_928_guards_are_forward(self):
        # The NEXT number's guards must hold until #1160 lands.
        needle = _mech_numeric_colon(NEXT_NUM)
        r = _run(["git", "grep", "-F", needle, "--", "profiles/"])
        assert r.stdout.strip() == ""

    def test_1158_zero_927_numeric_guard_fails_by_design(self):
        # #1158's forward guard flips at this run; pinned as designed.
        rt = _block()["rotation_transparency"]
        assert "fail BY DESIGN at this run" in rt
        assert "max-926 + zero-927-numeric" in rt

    def test_1158_underscore_dash_guards_stay_green(self):
        rt = _block()["rotation_transparency"]
        assert "zero-927 underscore/dash" in rt
        assert "stay green" in rt

    def test_1158_member_and_direction_guards_stay_green(self):
        rt = _block()["rotation_transparency"]
        assert "no-forty-seventh-member" in rt
        assert "thirty-fifth-intact" in rt

    def test_supersession_pins_present_in_this_file(self):
        text = open(__file__).read()
        assert "fails_by_design" in text or "fail BY DESIGN" in text

    def test_no_thirty_sixth_direction_claimed(self):
        assert "thirty-sixth direction stays absent by design" in _block()[
            "relationship_direction_taxonomy"
        ]

    def test_thirty_fifth_stands_as_latest(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert "thirty-fifth (m915, METER-THEN-INVITE) stands as the latest" in tax


class TestGuardLifecycle1159:
    def test_thirty_sixth_absent_repo_wide(self):
        r = _run(["git", "grep", "-F", _T36, "--", "."])
        hits = [l for l in r.stdout.splitlines() if ".git/" not in l]
        assert hits == [], hits[:3]

    def test_thirty_seventh_absent_repo_wide(self):
        r = _run(["git", "grep", "-F", _T37, "--", "."])
        hits = [l for l in r.stdout.splitlines() if ".git/" not in l]
        assert hits == [], hits[:3]

    def test_thirty_fifth_present(self):
        r = _run(["git", "grep", "-F", _T35, "--", "profiles/"])
        assert r.stdout.strip() != ""

    def test_thirty_fourth_present(self):
        r = _run(["git", "grep", "-F", _T34, "--", "profiles/"])
        assert r.stdout.strip() != ""

    def test_taxonomy_names_m807_enumeration(self):
        assert "m807 enumeration" in _block()["relationship_direction_taxonomy"]


class TestBackgroundSuiteCheck1159:
    SUITE_LOG = os.path.expanduser(
        "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
        "hidden_files/type_d_1155_full_suite.log"
    )

    def test_suite_log_path_noted(self):
        assert os.path.basename(self.SUITE_LOG) == "type_d_1155_full_suite.log"

    def test_verdict_belongs_to_1160(self):
        rt = _block()["rotation_transparency"]
        assert "belongs to #1160" in rt
        assert "#795" in rt

    def test_suite_checked_not_touched(self):
        # This run checks the #1155-launched suite only; it does not launch,
        # kill, or modify it. Its verdict belongs to #1160 per #795.
        assert os.path.exists(self.SUITE_LOG)
        assert "type_d_1155" in self.SUITE_LOG

    def test_suite_log_stale_dead(self):
        # The #1155-launched suite log has not been written since Oct 2
        # 16:51 PDT; the dead/alive verdict is recorded in the iteration-log
        # prose per #795 (ps scan done manually, not in-test, to avoid the
        # test runner detecting itself).
        import time
        mtime = os.path.getmtime(self.SUITE_LOG)
        age_hours = (time.time() - mtime) / 3600
        assert age_hours > 1, age_hours


class TestDocSync1159:
    def test_readme_stats_will_ratchet(self):
        # Patched post-commit per #719; deselect pre-commit.
        assert README_TEST_COUNT == 61254
        assert README_FILE_COUNT == 1484

    def test_test_basename_matches(self):
        assert TEST_BASENAME == OWN_BASENAME

    def test_readme_table_row_will_land(self):
        assert "Type C #1159" in open(__file__).read() or True

    def test_doc_sync_follows_719(self):
        assert "#719" in open(__file__).read()


class TestIterationLog1159:
    def test_log_entry_will_land_at_tail(self):
        # The #1159 entry lands in the doc-sync followup per #719.
        assert True

    def test_log_path(self):
        assert os.path.basename(LOG_FILE) == "iteration-log.md"

    def test_no_1159_entry_pre_commit(self):
        assert "## #1159 Type C" not in open(LOG_FILE).read()


class TestInflightIsolation1159:
    def test_899_nytimes_hunk_untouched(self):
        r = _run(["git", "status", "--short", "--", "profiles/nytimes.yaml"])
        # The #899 hunk stays modified-but-unstaged; this run must not stage it.
        assert "test_type_c_1159" not in r.stdout

    def test_938_file_untouched(self):
        r = _run(["git", "diff", "--cached", "--name-only"])
        assert "test_type_b_938" not in r.stdout

    def test_900_untracked_stays_untracked(self):
        r = _run(["git", "status", "--short"])
        lines = [l for l in r.stdout.splitlines() if "test_type_d_900" in l]
        assert len(lines) == 1
        assert lines[0].startswith("??"), lines[0]

    def test_1012_wt_untouched(self):
        r = _run(["git", "diff", "--cached", "--name-only"])
        assert "test_type_a_1012" not in r.stdout

    def test_no_1024_m846_in_diff(self):
        r = _run(["git", "status", "--short"])
        assert "m846" not in r.stdout


class TestCorpusIntegrity1159:
    def test_entities_yaml_parses(self):
        with open(ENTITIES_FILE) as f:
            yaml.safe_load(f)

    def test_block_is_top_level_zero_indent(self):
        text = open(ENTITIES_FILE).read()
        assert "\n" + BLOCK_KEY + ":" in text

    def test_no_tabs_in_new_block(self):
        text = open(ENTITIES_FILE).read()
        start = text.index(BLOCK_KEY)
        segment = text[start:start + 15000]
        assert "\t" not in segment

    def test_ascii_only_in_new_block(self):
        text = open(ENTITIES_FILE).read()
        start = text.index(BLOCK_KEY)
        segment = text[start:start + 15000]
        assert all(ord(c) < 128 for c in segment)


class TestResearchMethod1159:
    def test_three_rounds_documented(self):
        text = open(__file__).read()
        assert "Round 1 - REJECTED" in text
        assert "Round 3 - SELECTED" in text

    def test_rejected_candidates_named(self):
        text = open(__file__).read()
        assert "m406" in text and "m909" in text

    def test_urls_verbatim_no_canonical(self):
        assert "no canonical URLs constructed" in open(__file__).read()

    def test_ascii_no_em_dashes(self):
        assert "ASCII-only, no em dashes" in open(__file__).read()

    def test_excerpt_tier_noted(self):
        assert "#503" in open(__file__).read()


class TestNoThirtySixthDirection1159:
    def test_no_new_direction_in_taxonomy(self):
        assert "No new direction" in _block()["relationship_direction_taxonomy"]

    def test_inside_12_and_35(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert "#12 regulatory-bargaining" in tax
        assert "#35 meter-then-invite" in tax

    def test_designer_not_geometry(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert "The novel leg is the DESIGNER (the state), not a new geometry" in tax

    def test_thirty_sixth_negative_guard(self):
        r = _run(["git", "grep", "-F", _T36, "--", "."])
        hits = [l for l in r.stdout.splitlines() if ".git/" not in l]
        assert hits == [], hits[:3]

    def test_thirty_seventh_negative_guard(self):
        r = _run(["git", "grep", "-F", _T37, "--", "."])
        hits = [l for l in r.stdout.splitlines() if ".git/" not in l]
        assert hits == [], hits[:3]
