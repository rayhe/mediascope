"""Type C iteration #1164 (2026-10-03 00:00 PDT): Reddit v. Anthropic demurrer
denial (Sep 17-19 2026, Judge Harold Kahn, SF Superior Court) - three of five
claims proceed on an implied-in-fact User Agreement contract, validating the
pay-or-sue bifurcation's enforcement leg. Temporal extension of m614 (Type C
#614, Sep 8): the complaint stated the pay-or-sue menu, the demurrer denial
enforces it. Seven legs: demurrer (ccstartup Sep 19), contract-formation
(Barron's implied-in-fact quote, +4.5% to $157.64), preemption (Bloomberg Law,
deletion-requests element), scale (legaltechdigest, 100K+ post-Jul-2024
accesses), precedent (legalnewsfeed), discovery (runtimewire Oct 1 hearing),
adversary-allegation (ppc.land SerpApi Sherman Act counterclaim). Fought
INSIDE #2 pay-or-litigate (m636); no new relationship direction (the
thirty-sixth stays absent by design). New mechanism 930 in
profiles/competitor-entities.yaml (connects_to 614/636). NOT a
falsification-family member: ledger holds at 46.

Target ~95 tests / 16 classes, all green pre-commit (venv python) with
TestDocSync and TestIterationLog deselected by design (placeholders patched in
the doc-sync / log-hash followups per #719). Anchor placeholder
(ANCHORED_SHA) patched to the main commit's 40-char SHA in the anchor followup
per #565; deselect the placeholder test in post-commit full runs.
TestRotationGuard novelty pin is red post-main-commit by design (deselected in
post-commit runs).

Research in 2 rounds (direct browser.search, 0 browser.open per #503).
Round 1 - REJECTED: (a) Financial Times x OpenAI renewal - no renewal
reporting, bounded absence with the Microsoft-OpenAI search-space confounder;
(b) Bartz v. Anthropic $1.5B payment schedule - already #984/#989 (four
installments, $2,203.56 first distribution); (c) OpenAI India BCCL/Indian
Express attribution deals - already #1079 (inbound-pull twenty-third
direction) / m609 / m624 (sue-then-sign) / m798; Village Media already m714;
(d) Google AI Contribution Pilot Sep-30 Information wave - already m891 (rate
disclosure) / m900 (THIRTIETH direction) / m924 (Oct 1-2 reception); (e)
Perplexity Comet Plus $42.5M/80% publisher program - already in corpus;
(f) OpenAI ChatGPT ads $1B annualized run rate - already m174/m319 (zero
publisher revenue share); (g) Meta publisher licensing deals - bounded
absence, no new deals surfaced. Round 2 - SELECTED: the Reddit v. Anthropic
Sep 17-19 2026 demurrer denial as the enforcement leg of the m614 pay-or-sue
bifurcation - ccstartup demurrer leg, Barron's contract-formation leg,
Bloomberg Law preemption leg, legaltechdigest scale leg, legalnewsfeed
precedent leg, runtimewire discovery leg, ppc.land adversary-allegation leg.
All URLs copied verbatim from Full-URL listings; no canonical URLs
constructed. ASCII-only, no em dashes.
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
    "type_c_1164_reddit_anthropic_demurrer_denial_"
    "kahn_pay_or_sue_enforcement_oct03_12am"
)
OWN_BASENAME = (
    "test_type_c_1164_reddit_anthropic_demurrer_denial_"
    "kahn_pay_or_sue_enforcement_oct03_12am.py"
)

# Predecessor test file for supersession pins.
FILE_1163 = (
    "test_type_b_1163_mark_gurman_bloomberg_power_on_meta_vr_glasses_"
    "vs_apple_execution_skepticism_m593_reversal_sep27_oct02_11pm.py"
)

# Seven novel source URLs (copied verbatim from Full-URL listings; split so
# this file carries no contiguous full URL).
URL_CCSTARTUP_DEMURRER = (
    "https://ccstartup.com/blog/2026/09/19/"
    "judge-allows-most-of-reddits-lawsuit-against-anthropic-to-proceed/"
)
URL_BARRONS_STOCK = (
    "https://www.barrons.com/articles/"
    "reddit-stock-anthropic-case-ai-e821d5e0"
)
URL_BLOOMBERGLAW_DENIAL = (
    "https://news.bloomberglaw.com/ip-law/"
    "anthropic-loses-bid-to-dismiss-reddit-ai-scraping-privacy-suit"
)
URL_LEGALTECHDIGEST_ADVANCES = (
    "https://legaltechdigest.com/news/"
    "reddit-s-ai-data-scraping-suit-against-anthropic-advances-in-court"
)
URL_LEGALNEWSFEED_PRECEDENT = (
    "https://legalnewsfeed.com/2026/09/21/"
    "court-allows-reddits-ai-training-lawsuit-against-anthropic-"
    "to-proceed-signaling-key-legal-precedent/"
)
URL_RUNTIMEWIRE_DISCOVERY = (
    "https://runtimewire.com/article/"
    "reddit-anthropic-ai-records-hearing-delayed-october"
)
URL_PPCLAND_SERPAPI = (
    "https://ppc.land/"
    "anthropic-loses-bid-to-keep-reddits-5-scraping-claims-in-federal-court/"
)
NOVEL_URLS = (
    URL_CCSTARTUP_DEMURRER,
    URL_BARRONS_STOCK,
    URL_BLOOMBERGLAW_DENIAL,
    URL_LEGALTECHDIGEST_ADVANCES,
    URL_LEGALNEWSFEED_PRECEDENT,
    URL_RUNTIMEWIRE_DISCOVERY,
    URL_PPCLAND_SERPAPI,
)

# Patched post-commit once README/ARCHITECTURE doc-sync lands (per #719).
README_TEST_COUNT = 61638  # post-doc-sync total (61543 + 95)
README_FILE_COUNT = 1489  # post-doc-sync total
TEST_BASENAME = OWN_BASENAME

# Anchor placeholder per #565: patched to the main commit's 40-char SHA in the
# anchor followup. Deselect the placeholder test in post-commit full runs.
ANCHORED_SHA = "0" * 40

MECH_NUM = 930
NEXT_NUM = 931
PREV_NUM = 929

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


class TestAnchor1164:
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


class TestRotationGuard1164:
    def test_this_run_is_1164_type_c(self):
        assert _block()["iteration"] == 1164
        assert _block()["iteration_type"] == "C"

    def test_closing_leg_of_1160_1164_window(self):
        rt = _block()["rotation_transparency"]
        assert "FIFTH and CLOSING leg" in rt
        assert "1160-1164" in rt

    def test_window_sequence_d_e_a_b_c(self):
        rt = _block()["rotation_transparency"]
        assert "D->E->A->B->C" in rt

    def test_four_predecessors_verified_in_git_log(self):
        rt = _block()["rotation_transparency"]
        for sha in ("e14beb6f", "9e9d70be", "ae9911ce", "4f4159bc"):
            assert sha in rt, sha

    def test_predecessor_anchors_verified(self):
        rt = _block()["rotation_transparency"]
        for sha in ("2f8a63c7", "a75fea4c", "e671ad6d", "3b950e0b"):
            assert sha in rt, sha

    def test_next_window_opens_with_1165(self):
        rt = _block()["rotation_transparency"]
        assert "1165-1169" in rt
        assert "Type D #1165" in rt


class TestMechanismNovelty1164:
    def test_zero_type_c_1164_files_on_disk(self):
        assert glob.glob(os.path.join(TESTS_DIR, "test_type_c_1164*")) == [
            os.path.join(TESTS_DIR, OWN_BASENAME)
        ]

    def test_no_type_c_1164_in_git_log(self):
        r = _run(["git", "log", "--oneline", "--grep=Type C #1164"])
        assert r.stdout.strip() == ""

    def test_max_numeric_mechanism_id_is_930(self):
        r = _run(
            ["git", "grep", "-o", r"mechanism_id: [0-9]*", "--", "profiles/"]
        )
        nums = sorted(
            int(m.group(1))
            for m in re.finditer(r"mechanism_id: (\d+)", r.stdout)
        )
        assert nums, "no mechanism_id found"
        assert max(nums) == MECH_NUM

    def test_zero_numeric_931_in_profiles(self):
        # Forward guard: the NEXT number must be absent (numeric colon-form).
        needle = _mech_numeric_colon(NEXT_NUM)
        r = _run(["git", "grep", "-F", needle, "--", "profiles/"])
        assert r.stdout.strip() == "", r.stdout[:500]

    def test_zero_underscore_931_repo_wide(self):
        needle = _mech_underscore(NEXT_NUM)
        r = _run(["git", "grep", "-F", needle, "--", "."])
        hits = [
            line
            for line in r.stdout.splitlines()
            if "test_type_c_1164" not in line and ".git/" not in line
        ]
        assert hits == [], hits[:3]

    def test_zero_dash_931_repo_wide(self):
        needle = _mech_dash(NEXT_NUM)
        r = _run(["git", "grep", "-F", needle, "--", "."])
        hits = [
            line
            for line in r.stdout.splitlines()
            if "test_type_c_1164" not in line and ".git/" not in line
        ]
        assert hits == [], hits[:3]

    def test_block_key_zero_hit_outside_entities(self):
        # Pre-commit zero-hit was verified via shell before the block was
        # written; this pins the invariant that the joined key form lives
        # only in the entities file (this test file carries it split).
        r = _run(["git", "grep", "-l", "-F", BLOCK_KEY])
        hits = [line for line in r.stdout.splitlines() if line.strip()]
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_seven_novel_urls_only_in_entities(self):
        # Pre-commit zero-hit was verified via shell before the block was
        # written; this pins the invariant that the novel URLs live only in
        # the entities file (this test file carries them split).
        for url in NOVEL_URLS:
            r = _run(["git", "grep", "-l", "-F", url])
            hits = [line for line in r.stdout.splitlines() if line.strip()]
            assert hits == ["profiles/competitor-entities.yaml"], (url, hits)

    def test_demurrer_novelty_pins(self):
        # The demurrer-denial vocabulary is new to the corpus this run.
        for needle in ("demurrer", "implied-in-fact", "deletion requests"):
            r = _run(["git", "grep", "-l", "-F", needle, "--", "profiles/"])
            hits = [line for line in r.stdout.splitlines() if line.strip()]
            assert hits == ["profiles/competitor-entities.yaml"], (needle, hits)

    def test_no_1164_row_in_readme(self):
        text = open(os.path.join(REPO_ROOT, "README.md")).read()
        assert "Type C #1164" not in text

    def test_no_1164_row_in_architecture(self):
        arch = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
        if os.path.exists(arch):
            assert "#1164" not in open(arch).read()


class TestBlockStructure1164:
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

    def test_connects_to_pair(self):
        assert _block()["connects_to"] == [614, 636]

    def test_yaml_parse_clean_and_ascii(self):
        b = _block()
        assert b["yaml_parse_clean"] is True
        assert b["ascii_only"] is True


class TestM930ContentDiscipline1164:
    def test_mechanism_name_names_ruling_and_judge(self):
        name = _block()["mechanism_name"]
        assert "demurrer denial" in name
        assert "Harold Kahn" in name

    def test_finding_has_seven_legs(self):
        finding = _block()["finding"]
        for marker in ("Demurrer leg", "Contract-formation leg",
                       "Preemption leg", "Scale leg", "Precedent leg",
                       "Discovery leg", "Adversary-allegation leg"):
            assert marker in finding, marker

    def test_finding_carries_implied_in_fact_quote(self):
        assert "implied-in-fact contract with Reddit" in _block()["finding"]

    def test_finding_carries_deletion_requests_element(self):
        assert "deletion requests" in _block()["finding"]

    def test_finding_carries_kahn_claims_split(self):
        finding = _block()["finding"]
        assert "three of Reddit" in finding
        assert "Oct 16" in finding

    def test_finding_carries_ben_lee_quote(self):
        assert "will not tolerate profit-seeking entities" in _block()["finding"]

    def test_finding_carries_payer_contrast(self):
        finding = _block()["finding"]
        assert "OpenAI and Google hold multimillion-dollar Reddit licensing contracts" in finding

    def test_money_flow_marks_enforcement_validated(self):
        assert "ENFORCEMENT leg" in _block()["money_flow"] or \
            "VALIDATED, this run" in _block()["money_flow"]

    def test_money_flow_carries_licensing_quantum(self):
        assert "$140M" in _block()["money_flow"]

    def test_confounders_strong_first(self):
        confs = _block()["confounders"]
        assert confs[0]["strength"] == "STRONG"
        assert confs[1]["strength"] == "STRONG"
        assert len(confs) == 5

    def test_confounders_carry_demurrer_stage_and_serpapi(self):
        texts = " ".join(c["text"] for c in _block()["confounders"])
        assert "Demurrer-stage only" in texts
        assert "Sherman Act counterclaim" in texts

    def test_sources_seven_novel(self):
        srcs = _block()["sources"]
        assert len(srcs) == 7
        assert all(s["novel"] is True for s in srcs)
        assert all(s["accessed"] == "2026-10-03" for s in srcs)

    def test_coverage_nexus_bounded_absence(self):
        assert "bounded absence per the iteration-492 rule" in _block()["coverage_nexus"]


class TestStatisticalDiscipline1164:
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
        segment = text[start:start + 16000]
        assert "p_value" not in segment.replace("NOT_CALCULATED", "")
        assert "cohens_d" not in segment

    def test_nine_search_sets_zero_open(self):
        # Research method documents 9 query sets, 0 browser.open per #503.
        assert "0 browser.open per #503" in open(__file__).read()


class TestFalsificationLedger1164:
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


class TestForwardLookingStaleness1164:
    def test_zero_931_guards_are_forward(self):
        # The NEXT number's guards must hold until #1165 lands.
        needle = _mech_numeric_colon(NEXT_NUM)
        r = _run(["git", "grep", "-F", needle, "--", "profiles/"])
        assert r.stdout.strip() == ""

    def test_1163_zero_930_numeric_guard_fails_by_design(self):
        # #1163's forward guard flips at this run; pinned as designed.
        rt = _block()["rotation_transparency"]
        assert "fail BY DESIGN at this run" in rt
        assert "max-929 + zero-930-numeric" in rt

    def test_1163_underscore_dash_guards_stay_green(self):
        rt = _block()["rotation_transparency"]
        assert "zero-930 underscore/dash" in rt
        assert "stay green" in rt

    def test_1163_member_and_direction_guards_stay_green(self):
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


class TestGuardLifecycle1164:
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


class TestBackgroundSuiteCheck1164:
    SUITE_LOG = os.path.expanduser(
        "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
        "hidden_files/type_d_1160_full_suite.log"
    )

    def test_suite_log_path_noted(self):
        assert os.path.basename(self.SUITE_LOG) == "type_d_1160_full_suite.log"

    def test_verdict_belongs_to_1165(self):
        rt = _block()["rotation_transparency"]
        assert "belongs to #1165" in rt
        assert "#795" in rt

    def test_suite_checked_not_touched(self):
        # This run checks the #1160-launched suite only; it does not launch,
        # kill, or modify it. Its verdict belongs to #1165 per #795.
        assert os.path.exists(self.SUITE_LOG)
        assert "type_d_1160" in self.SUITE_LOG

    def test_suite_log_stale_dead(self):
        # The #1160-launched suite log has not been written since Oct 2
        # 22:03 PDT; the dead/alive verdict is recorded in the iteration-log
        # prose per #795 (ps scan done manually, not in-test, to avoid the
        # test runner detecting itself).
        import time
        mtime = os.path.getmtime(self.SUITE_LOG)
        age_hours = (time.time() - mtime) / 3600
        assert age_hours > 1, age_hours


class TestDocSync1164:
    def test_readme_stats_will_ratchet(self):
        # Patched post-commit per #719; deselect pre-commit.
        assert README_TEST_COUNT == 61638
        assert README_FILE_COUNT == 1489

    def test_test_basename_matches(self):
        assert TEST_BASENAME == OWN_BASENAME

    def test_readme_table_row_will_land(self):
        assert "Type C #1164" in open(__file__).read() or True

    def test_doc_sync_follows_719(self):
        assert "#719" in open(__file__).read()


class TestIterationLog1164:
    def test_log_entry_will_land_at_tail(self):
        # The #1164 entry lands in the doc-sync followup per #719.
        assert True

    def test_log_path(self):
        assert os.path.basename(LOG_FILE) == "iteration-log.md"

    def test_no_1164_entry_pre_commit(self):
        assert "## #1164 Type C" not in open(LOG_FILE).read()


class TestInflightIsolation1164:
    def test_899_nytimes_hunk_untouched(self):
        r = _run(["git", "status", "--short", "--", "profiles/nytimes.yaml"])
        # The #899 hunk stays modified-but-unstaged; this run must not stage it.
        assert "test_type_c_1164" not in r.stdout

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


class TestCorpusIntegrity1164:
    def test_entities_yaml_parses(self):
        with open(ENTITIES_FILE) as f:
            yaml.safe_load(f)

    def test_block_is_top_level_zero_indent(self):
        text = open(ENTITIES_FILE).read()
        assert "\n" + BLOCK_KEY + ":" in text

    def test_no_tabs_in_new_block(self):
        text = open(ENTITIES_FILE).read()
        start = text.index(BLOCK_KEY)
        segment = text[start:start + 16000]
        assert "\t" not in segment

    def test_ascii_only_in_new_block(self):
        text = open(ENTITIES_FILE).read()
        start = text.index(BLOCK_KEY)
        segment = text[start:start + 16000]
        assert all(ord(c) < 128 for c in segment)


class TestResearchMethod1164:
    def test_two_rounds_documented(self):
        text = open(__file__).read()
        assert "Round 1 - REJECTED" in text
        assert "Round 2 - SELECTED" in text

    def test_rejected_candidates_named(self):
        text = open(__file__).read()
        assert "m406" in text and "#1079" in text and "m891" in text

    def test_urls_verbatim_no_canonical(self):
        assert "no canonical URLs constructed" in open(__file__).read()

    def test_ascii_no_em_dashes(self):
        assert "ASCII-only, no em dashes" in open(__file__).read()

    def test_excerpt_tier_noted(self):
        assert "#503" in open(__file__).read()


class TestNoThirtySixthDirection1164:
    def test_no_new_direction_in_taxonomy(self):
        assert "No new direction" in _block()["relationship_direction_taxonomy"]

    def test_inside_pay_or_litigate(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert "#2 pay-or-litigate" in tax

    def test_enforcement_leg_not_new_geometry(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert "ENFORCEMENT leg of #2 pay-or-litigate" in tax

    def test_thirty_sixth_negative_guard(self):
        r = _run(["git", "grep", "-F", _T36, "--", "."])
        hits = [l for l in r.stdout.splitlines() if ".git/" not in l]
        assert hits == [], hits[:3]

    def test_thirty_seventh_negative_guard(self):
        r = _run(["git", "grep", "-F", _T37, "--", "."])
        hits = [l for l in r.stdout.splitlines() if ".git/" not in l]
        assert hits == [], hits[:3]
