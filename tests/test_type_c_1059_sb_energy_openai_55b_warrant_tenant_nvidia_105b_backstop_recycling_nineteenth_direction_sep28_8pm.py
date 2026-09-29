"""Type C #1059: SB Energy x OpenAI x Nvidia three-party financial architecture
(WSJ Aug 31 2026 exclusive, SB Energy S-1 filed Sep 1 2026) - BACKSTOP-RECYCLING
as the NINETEENTH relationship direction: the supplier's contingent guarantee
($105B cap, first 4.25GW of OpenAI's PORTS-Pike lease obligations, Nvidia's own
SEC filing) underwrites the customer's third-party capacity lease while the
landlord pays the tenant in equity (~4M warrants at $0.01, $3.6B Jan -> ~$5.5B
Jun 30, second demand-for-equity instance after m1009); tenant-investor-board
triple role. Mechanism 867 in profiles/competitor-entities.yaml (top-level).

FIFTH and CLOSING leg of the 1055-1059 window (D->E->A->B->C per #565).
Zero "SB Energy"/"sb-energy" hits repo-wide pre-commit; 7 novel source URLs
zero-hit pre-commit (git grep -F on verbatim Full-URL listings); max numeric
mechanism_id 866 pre-commit (Type B #1058). Excerpt-bounded per #503:
3 browser.search query sets, 0 browser.open. tone NOT_SCORED, engine NOT run,
falsification ledger holds at 35, NOT artifact-grade, verdict
directionally_supported_not_proven.
"""

import glob
import os
import re
import subprocess

import pytest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, "profiles", "competitor-entities.yaml")
ITERATION_LOG = os.path.join(REPO, "iteration-log.md")
README = os.path.join(REPO, "README.md")
ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")

TYPE_LETTER = "C"
ITERATION = 1059
M_ID = 868
MECH_KEY = (
    "type_c_1059_sb_energy_openai_55b_warrant_tenant_backstop_recycling_"
    "nineteenth_direction_sep28_8pm"
)
MECH_ID_MARKER = "mechanism" + "_" + "86" + "7"  # own-form underscore sweep marker
MECH_ID_DASH = "mechanism" + "-" + "86" + "7"
MECH_ID_NUMERIC = "mechanism_id" + ": " + "86" + "7"
NEXT_US = "mechanism" + "_" + "86" + "9"  # next-number underscore sweep
NEXT_DASH = "mechanism" + "-" + "86" + "9"  # next-number dash sweep
NEXT_NUMERIC = "mechanism_id" + ": " + "86" + "9"  # next-number numeric sweep
OWN_BASENAME = os.path.basename(__file__)
ANCHORED_SHA = "b7261ef57336f19c97da693e7deddf397bec87a3"  # patched in the anchor followup commit
NOVELTY_CLAIMS = (
    "zero\ntest_type_c_1059 files, max numeric\nmechanism_id 866 pre-commit, "
    "block key zero-hit, 7 novel\nURLs zero-hit, SB Energy absent"
)
EXPECTED_NEW_URLS = [
    "https://www.globaldatacenterhub.com/p/why-the-tenant-is-now-on-the-landlords",
    "https://www.europesays.com/people/217489/",
    "https://startupfortune.com/softbanks-sb-energy-files-for-ipo-while-admitting-it-needs-openai-to-pay-up/",
    "https://www.techrepublic.com/article/news-openai-sb-energy-warrants-ipo/",
    "https://www.ainvest.com/news/sb-energy-gave-openai-5-5b-warrants-move-nvidia-signed-loan-2609/",
    "https://dailyaibrief.com/news/openai-warrants-sb-energy-5-5-billion-liy4BmD3",
    "https://wwconemedia.com/openai-got-sb-energy-warrants-valued-at-5-5-billion-but-the-bigger-story-is-who-is-financing-the-ai-boom/",
]
CARRIED_URLS = []
EXPECTED_ORDER = [("C", "1059"), ("B", "1058"), ("A", "1057"), ("E", "1056"), ("D", "1055")]
README_TESTS_BEFORE = 54290
README_FILES_BEFORE = 1383
README_TESTS_AFTER = 54345
README_FILES_AFTER = 1384
INFLIGHT_FILES = [
    "profiles/nytimes.yaml",  # #899 Type C, modified in worktree
    "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",  # #938, modified
    "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",  # #900, untracked
    "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",  # #1012-wt, modified
]
STAGED_EXPECTED_BASENAMES = {
    "competitor-entities.yaml",
    OWN_BASENAME,
    "test_type_d_1055_m862_m863_m864_qualitative_corpus_integrity_sep28_4am.py",
    "test_type_e_1056_podcast_sentiment_134th_verification_sep28_5pm.py",
    "test_type_a_1057_gizmodo_openai_sep28_astra_cancellation_credit_vs_meta_scrapped_tool_sep28_6pm.py",
    "test_type_b_1058_lucas_ropek_techcrunch_sep28_openai_astra_inbrief_vs_sep16_meta_luna_inbrief_stigma_contrast_sep28_7pm.py",
    "README.md",
    "ARCHITECTURE.md",
    "iteration-log.md",
}


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _git(args):
    return subprocess.run(
        ["git", "-C", REPO] + args, capture_output=True, text=True, timeout=120
    )


def _load_profile():
    import yaml

    return yaml.safe_load(_read(PROFILE))


def get_block():
    return _load_profile()[MECH_KEY]


def _repo_grep(needle):
    hits = []
    for root in ("profiles", "tests"):
        base = os.path.join(REPO, root)
        for dirpath, _, files in os.walk(base):
            for fn in files:
                if fn.rsplit(".", 1)[-1] not in ("py", "yaml", "md", "json"):
                    continue
                p = os.path.join(dirpath, fn)
                if needle in open(p, errors="ignore").read():
                    hits.append(p)
    return hits


def _staged_paths():
    return _git(["diff", "--cached", "--name-only"]).stdout.splitlines()


# ---------------------------------------------------------------------------
# 1. Novelty anchor (anchor-marked tests deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestNoveltyAnchorTypeC1059:
    @pytest.mark.anchor
    def test_anchor_exists(self):
        assert ANCHORED_SHA not in (None, "PATCH_ME_IN_FOLLOWUP"), (
            "anchor NULL pre-commit (patched post-commit)"
        )

    @pytest.mark.anchor
    def test_anchor_shape(self):
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)

    @pytest.mark.anchor
    def test_anchor_in_log_header(self):
        # Corpus convention registers short hashes in the log header; the
        # anchor's first 8 chars are the main-commit short SHA. Scoped to
        # the #1059 header line (not the whole log) per the #1044 test fix:
        # newer entries name predecessor SHAs in their rotation-transparency
        # sections, which a whole-log index() cannot distinguish.
        log = _read(ITERATION_LOG)
        header_start = log.index("## #1059 Type C")
        header_end = log.index("\n", header_start)
        assert ANCHORED_SHA[:8] in log[header_start:header_end]

    def test_novelty_claims(self):
        assert NOVELTY_CLAIMS == (
            "zero\ntest_type_c_1059 files, max numeric\nmechanism_id 866 pre-commit, "
            "block key zero-hit, 7 novel\nURLs zero-hit, SB Energy absent"
        )


# ---------------------------------------------------------------------------
# 2. Rotation guard (1055-1059 window: D -> E -> A -> B -> C), per #565.
#    All rotation tests are deselected pre-commit (log entry prepended at
#    doc-sync) and re-run after doc-sync.
# ---------------------------------------------------------------------------
@pytest.mark.rotation
class TestRotationGuard1055_1059Window:
    def test_window_legs_in_log(self):
        log = _read(ITERATION_LOG)
        for number, letter in (("1055", "D"), ("1056", "E"), ("1057", "A"), ("1058", "B")):
            assert "## #%s Type %s" % (number, letter) in log

    def test_this_run_fifth_leg_c(self):
        log = _read(ITERATION_LOG)
        assert log.count("## #1059 Type C") == 1
        rt = get_block()["rotation_transparency"]
        assert "1055-1059" in rt and "C #1059" in rt and "CLOSING" in rt

    def test_predecessor_1058_pinned(self):
        rt = get_block()["rotation_transparency"]
        assert "#1058 Type B" in rt
        assert "103c871d" in rt and "57e08a7b" in rt and "e7ce1490" in rt

    def test_iteration_type_c(self):
        assert get_block()["iteration_type"] == TYPE_LETTER


# ---------------------------------------------------------------------------
# 3. Mechanism structure
# ---------------------------------------------------------------------------
class TestMechanism867Structure:
    def test_mechanism_id_and_type(self):
        block = get_block()
        assert block["mechanism_id"] == M_ID
        assert block["type"] == "financial_incentive_mapping"
        assert block["type_label"] == "Financial Incentive Mapping"

    def test_iteration_fields(self):
        block = get_block()
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == TYPE_LETTER
        assert block["iteration_time"] == "2026-09-28 20:00 PDT"
        assert block["scheduled_job_id"] == "mediascope-daily-iteration"
        assert block["goal_id"] == "goal_54093bda4145"

    def test_block_key_matches(self):
        block = get_block()
        assert block["block_key"] == MECH_KEY
        assert "866" not in MECH_KEY and "nineteenth_direction" in MECH_KEY

    def test_verdict_and_flags(self):
        block = get_block()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["tone_scored"] is False
        assert block["engine_run"] is False
        assert block["is_significant"] is False
        assert block["no_analysis_json_update"] is True
        assert block["artifact_grade"] is False
        assert block["falsification_family_member"] is False

    def test_falsification_ledger_35(self):
        assert get_block()["falsification_ledger_holds_at"] == 35

    def test_search_sets_browser_opens(self):
        block = get_block()
        assert block["search_sets"] == 3
        assert block["browser_opens"] == 0

    def test_connects_to(self):
        assert get_block()["connects_to"] == [864, 1009, 718, 754]

    def test_coverage_note_no_tone_claim(self):
        note = get_block()["coverage_note"]
        assert "tone NOT_SCORED" in note
        assert "No editorial-tone claim" in note
        assert "m519" in note


# ---------------------------------------------------------------------------
# 4. Mechanism finding (three legs + IPO + geometry)
# ---------------------------------------------------------------------------
class TestMechanism867Finding:
    def test_warrant_leg(self):
        finding = get_block()["finding"]
        assert "4.0 million stock warrants" in finding
        assert "$0.01 exercise price" in finding
        assert "3,991,809 warrant shares" in finding
        assert "$3.6B when issued in January 2026" in finding
        assert "$5.5B at June 30 2026" in finding
        assert "three planned data centers" in finding

    def test_tenant_leg(self):
        finding = get_block()["finding"]
        assert "17 individual lease agreements" in finding
        assert "about 8GW of computing capacity" in finding
        assert "PORTS-Pike" in finding
        assert "10GW of power infrastructure" in finding

    def test_backstop_leg(self):
        finding = get_block()["finding"]
        assert "capped at $105B" in finding
        assert "first 4.25GW" in finding
        assert "Nvidia's fiscal 2029" in finding
        assert "Nvidia's own SEC filing" in finding

    def test_ipo_leg(self):
        finding = get_block()["finding"]
        assert "September 1 2026" in finding
        assert "ticker SBE" in finding
        assert "$5-7B raise" in finding
        assert "$50B+ valuation" in finding

    def test_triple_role(self):
        finding = get_block()["finding"]
        assert "$500M into SB Energy in January 2026" in finding
        assert "board designation right" in finding
        assert "above 5%" in finding
        assert "low-single-digit percentage post-IPO" in finding

    def test_zero_operating_dcs(self):
        finding = get_block()["finding"]
        assert "operates ZERO data centers today" in finding
        assert "800MW under construction" in finding
        assert "$3.2B net loss" in finding
        assert "$140M of renewables-legacy revenue" in finding

    def test_geometry_summary(self):
        finding = get_block()["finding"]
        assert "the landlord pays the tenant in equity" in finding
        assert "the chip supplier backstops the tenant's rent" in finding
        assert "Nvidia backstops OpenAI's rent" in finding


# ---------------------------------------------------------------------------
# 5. Relationship-direction taxonomy (NINETEENTH)
# ---------------------------------------------------------------------------
class TestMechanism867Taxonomy:
    def test_nineteenth_direction(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "NINETEENTH relationship direction" in tax
        assert "BACKSTOP-RECYCLING" in tax

    def test_enumeration_carried(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "per the m807 enumeration" in tax
        assert "18 demand-recycling m864" in tax
        assert "13 demand-for-equity m1009" in tax

    def test_backstop_recycling_defined(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "contingent guarantee (not funded equity)" in tax
        assert "contingent-capital-out, chip-revenue-back" in tax

    def test_distinct_from_18_and_13(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "Distinct from #18 demand-recycling" in tax
        assert "from #13 demand-for-equity" in tax

    def test_warrant_leg_second_demand_for_equity(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "SECOND case after m1009" in tax
        wg = get_block()["warrant_geometry"]
        assert "Second demand-for-equity instance" in wg
        assert "m1009 Akamai-Anthropic" in wg


# ---------------------------------------------------------------------------
# 6. Confounders, counterevidence, strongest counterargument
# ---------------------------------------------------------------------------
class TestMechanism867Confounders:
    def test_six_confounders_ranked(self):
        confs = get_block()["confounders"]
        assert len(confs) == 6
        assert confs[0].startswith("STRONG: warrant valuation")
        assert confs[1].startswith("STRONG: deal-terms provenance")
        assert confs[2].startswith("STRONG: Reuters could not independently verify")
        assert confs[3].startswith("MEDIUM: the guarantee is phased")
        assert confs[4].startswith("MEDIUM: SB Energy's filing concedes two-way dependence")
        assert confs[5].startswith("WEAK: relay variance")

    def test_strongest_counterargument(self):
        sca = get_block()["strongest_counterargument"]
        assert "ordinary project finance" in sca
        assert "not a nineteenth direction" in sca
        assert "priced below market" in sca
        assert "directionally mapped, not proven" in sca

    def test_counterevidence(self):
        ce = get_block()["counterevidence"]
        assert "$90.7B investment portfolio" in ce
        assert "m864" in ce
        assert "no cash has moved" in ce

    def test_warrant_estimate_qualified(self):
        confs = get_block()["confounders"]
        assert "not cash transferred" in confs[0]
        assert "wwconemedia qualification" in confs[0]

    def test_relay_variance_nvidia_investment(self):
        gs = get_block()["guarantee_structure"]
        assert "$1.5B (dailyaibrief) vs ~$3B (startupfortune" in gs
        assert "unresolved this run" in gs


# ---------------------------------------------------------------------------
# 7. Research method (excerpt-bounded per #503)
# ---------------------------------------------------------------------------
class TestResearchMethodTypeC1059:
    def test_search_sets_and_open(self):
        rm = get_block()["certification_boundaries"]
        assert "3 browser.search query sets" in rm
        assert "0 browser.open this run" in rm
        assert "per #503" in rm

    def test_url_attestation(self):
        rm = get_block()["certification_boundaries"]
        assert "verbatim" in rm
        assert "no canonical URLs constructed" in rm

    def test_novelty_greps_documented(self):
        nov = get_block()["novelty"]
        assert "max numeric mechanism_id 866 pre-commit" in nov
        assert "block key zero-hit repo-wide pre-commit" in nov
        assert '"SB Energy"/"sb-energy" hits repo-wide pre-commit' in nov

    def test_rejected_and_selected_documented(self):
        rm = get_block()["certification_boundaries"]
        assert "REJECTED as a stale Jan/Feb 2026 story" in rm
        assert "SELECTED" in rm
        assert "NOTED but not selected this run" in rm


# ---------------------------------------------------------------------------
# 8. Corpus novelty post-commit
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPostCommit:
    def test_max_numeric_mechanism_id_is_868(self):
        ids = []
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(r"mechanism_id:\s*(\d+)", _read(f)):
                ids.append(int(m.group(1)))
        assert max(ids) == M_ID

    def test_zero_next_numeric_869_in_profiles(self):
        text = "\n".join(
            _read(os.path.join(root, fn))
            for root, _, files in os.walk(os.path.join(REPO, "profiles"))
            for fn in files
            if fn.endswith(".yaml")
        )
        assert NEXT_NUMERIC not in text

    def test_zero_next_underscore_dash_869_repo_wide(self):
        assert _repo_grep(NEXT_US) == []
        assert _repo_grep(NEXT_DASH) == []

    def test_own_underscore_dash_needles_zero_in_sources(self):
        # Format-built per #715: no literal own-number key string is
        # carried anywhere; the needles must be pure zero repo-wide.
        assert _repo_grep(MECH_ID_MARKER) == []
        assert _repo_grep(MECH_ID_DASH) == []

    def test_block_key_in_profile(self):
        assert MECH_KEY in _read(PROFILE)


# ---------------------------------------------------------------------------
# 9. Doc-sync ratchet per #719 (green post-doc-sync)
# ---------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_header_stats_bumped(self):
        line = next(
            l for l in _read(README).splitlines() if l.startswith("| Tests |")
        )
        assert str(README_TESTS_AFTER) in line
        assert str(README_FILES_AFTER) in line

    def test_readme_row_1059(self):
        text = _read(README)
        assert OWN_BASENAME in text
        assert "Type C #1059" in text
        assert "mechanism 867" in text

    def test_arch_row_1059(self):
        text = _read(ARCH)
        assert OWN_BASENAME in text
        assert "Type C #1059" in text

    def test_expected_order_in_docstring(self):
        assert EXPECTED_ORDER == [("C", "1059"), ("B", "1058"), ("A", "1057"), ("E", "1056"), ("D", "1055")]


# ---------------------------------------------------------------------------
# 10. Iteration-log entry (deselected pre-commit per #719/#721)
# ---------------------------------------------------------------------------
@pytest.mark.itlog
class TestIterationLogEntry:
    def _section(self):
        log = _read(ITERATION_LOG)
        start = log.index("## #1059 Type C")
        end = log.index("## #1058 Type B")
        return log[start:end]

    def test_log_header_present(self):
        log = _read(ITERATION_LOG)
        assert log.count("## #1059 Type C") == 1

    def test_log_contains_mechanism(self):
        section = self._section()
        assert "mechanism 867" in section
        assert "SB Energy" in section

    def test_log_rotation(self):
        section = self._section()
        assert "1055-1059" in section
        assert "C #1059" in section


# ---------------------------------------------------------------------------
# 11. In-flight concurrency isolation (#899, #938, #900, #1012-wt)
# ---------------------------------------------------------------------------
class TestInflightIsolation:
    def test_concurrent_inflight_files_not_in_this_commit_scope(self):
        # Fails pre-commit by design (nothing staged yet); green once the
        # run stages its own files. All four in-flight paths stay
        # uncommitted and unstaged.
        staged = _staged_paths()
        assert staged != [], "nothing staged yet (pre-commit)"
        for f in INFLIGHT_FILES:
            assert f not in staged, "in-flight file leaked into staging: %s" % f
        assert not any("test_type_b_938_" in l for l in staged)
        assert not any("test_type_d_900_" in l for l in staged)
        assert not any("test_type_a_1012_" in l for l in staged)

    def test_targeted_staging_only(self):
        # Fails pre-commit by design; green post-staging. The staged set
        # must be exactly this run's files - nothing more.
        staged = {os.path.basename(p) for p in _staged_paths()}
        assert staged == STAGED_EXPECTED_BASENAMES


# ---------------------------------------------------------------------------
# 12. Block hygiene
# ---------------------------------------------------------------------------
class TestBlockHygiene:
    def test_ascii_only(self):
        block = get_block()
        import json

        blob = json.dumps(block, ensure_ascii=False)
        assert "\u2014" not in blob  # no em dashes, repo prose rule
        blob.encode("ascii")  # raises on any other non-ASCII

    def test_urls_verbatim(self):
        for url in EXPECTED_NEW_URLS + CARRIED_URLS:
            assert url.startswith("https://") and " " not in url

    def test_test_file_ascii(self):
        blob = _read(os.path.join(REPO, "tests", OWN_BASENAME))
        assert "\u2014" not in blob
        blob.encode("ascii")

    def test_source_references_recorded(self):
        # Per the standing "keep references" rule: all 7 novel source URLs
        # are recorded verbatim in the block's sources list, all novel,
        # all accessed this run.
        urls = [s["url"] for s in get_block()["sources"]]
        assert len(urls) == 7
        for url in EXPECTED_NEW_URLS:
            assert url in urls
        assert all(s["novel"] is True for s in get_block()["sources"])
        assert all(s["accessed"] == "2026-09-28" for s in get_block()["sources"])
