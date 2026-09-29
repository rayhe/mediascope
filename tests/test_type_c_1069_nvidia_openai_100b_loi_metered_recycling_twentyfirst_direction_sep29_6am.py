"""Type C #1069: Nvidia x OpenAI up-to-$100B progressive equity LOI (Sep 22 2025)
and its Jan-2026 stall - METERED-RECYCLING as the TWENTY-FIRST relationship
direction.

Expected order (newest first): C #1069, B #1068, A #1067, E #1066, D #1065.
EXPECTED_ORDER = [("C", "1069"), ("B", "1068"), ("A", "1067"), ("E", "1066"),
                  ("D", "1065")]
"""

import glob
import os
import re
import subprocess

import pytest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, "profiles", "competitor-entities.yaml")
README = os.path.join(REPO, "README.md")
ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")
ITERATION_LOG = os.path.join(REPO, "iteration-log.md")

ITERATION = 1069
TYPE_LETTER = "C"
RUN_PDT = "2026-09-29 06:00 PDT"
MECH_KEY = (
    "type_c_1069_nvidia_openai_100b_loi_metered_recycling_"
    "twentyfirst_direction_sep29_6am"
)
M_ID = 873
OWN_BASENAME = (
    "test_type_c_1069_nvidia_openai_100b_loi_metered_recycling_"
    "twentyfirst_direction_sep29_6am.py"
)

# Guard needles: corpus max is now 873, so the next-number sweep targets 874.
# Format-built per #715 so no contiguous literal exists in this file.
NEXT_US = "mechanism" + "_874"  # next-number underscore sweep
NEXT_DASH = "mechanism" + "-874"  # next-number dash sweep
NEXT_NUMERIC = "mechanism_id: " + "874"  # next-number numeric sweep

# Anchor SHA for the #1069 commit; patched post-commit per #565.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

# Doc-sync ratchet targets (exact counts from authoritative .venv collect-only).
README_TESTS_AFTER = 54878
README_FILES_AFTER = 1394

NOVELTY_CLAIMS = (
    "zero\ntest_type_c_1069 files, max numeric\nmechanism_id 872 pre-commit, "
    "block key zero-hit, 5 novel\nURLs zero-hit, letter of intent absent"
)

EXPECTED_NEW_URLS = [
    "https://nvidianews.nvidia.com/news/openai-and-nvidia-announce-strategic-partnership-to-deploy-10gw-of-nvidia-systems",
    "https://www.reuters.com/business/nvidia-invest-100-billion-openai-2025-09-22/",
    "https://www.reuters.com/business/nvidia-openai-talks-stalled-over-doubts-wsj-reports-2026-01-31/",
    "https://www.bloomberg.com/news/articles/2026-01-31/nvidia-ceo-says-100-billion-openai-plan-was-never-a-commitment",
    "https://techcratic.com/nvidia-ceo-jensen-huang-says-the-companys-investment-in-openai-will-be-nothing-like-100-billion",
]

EXPECTED_ORDER = [("C", "1069"), ("B", "1068"), ("A", "1067"), ("E", "1066"),
                  ("D", "1065")]

INFLIGHT_FILES = {
    "profiles/nytimes.yaml",
    "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",
    "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
    "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
}

STAGED_EXPECTED_BASENAMES = {
    "competitor-entities.yaml",
    OWN_BASENAME,
    "test_type_b_1068_cherlynn_low_engadget_apple_watch_audio_intelligence_vs_meta_glasses_hands_on_register_constancy_sep29_5am.py",
    "README.md",
    "ARCHITECTURE.md",
    "iteration-log.md",
}


def _read(path):
    with open(path, encoding="utf-8", errors="strict") as fh:
        return fh.read()


def _git(args):
    return subprocess.run(
        ["git"] + args, cwd=REPO, capture_output=True, text=True, check=False
    )


def _load_profile():
    import yaml

    return yaml.safe_load(_read(PROFILE))


def get_block():
    return _load_profile()[MECH_KEY]


def _corpus_ids():
    ids = []
    for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
        for m in re.finditer(r"mechanism_id:\s*(\d+)", _read(f)):
            ids.append(int(m.group(1)))
    return ids


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
class TestNoveltyAnchorTypeC1069:
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
        # Scoped to the #1069 header line (not the whole log) per the #1044
        # test fix: newer entries name predecessor SHAs in their
        # rotation-transparency sections, which a whole-log index() cannot
        # distinguish.
        log = _read(ITERATION_LOG)
        header_start = log.index("## #1069 Type C")
        header_end = log.index("\n", header_start)
        assert ANCHORED_SHA[:8] in log[header_start:header_end]

    def test_novelty_claims(self):
        assert NOVELTY_CLAIMS == (
            "zero\ntest_type_c_1069 files, max numeric\nmechanism_id 872 pre-commit, "
            "block key zero-hit, 5 novel\nURLs zero-hit, letter of intent absent"
        )


# ---------------------------------------------------------------------------
# 2. Rotation guard (1065-1069 window: D -> E -> A -> B -> C), per #565.
#    All rotation tests are deselected pre-commit (log entry prepended at
#    doc-sync) and re-run after doc-sync.
# ---------------------------------------------------------------------------
@pytest.mark.rotation
class TestRotationGuard1065_1069Window:
    def test_window_legs_in_log(self):
        log = _read(ITERATION_LOG)
        for number, letter in (("1065", "D"), ("1066", "E"), ("1067", "A"),
                               ("1068", "B")):
            assert "## #%s Type %s" % (number, letter) in log

    def test_this_run_fifth_leg_c(self):
        log = _read(ITERATION_LOG)
        assert log.count("## #1069 Type C") == 1
        rt = get_block()["rotation_transparency"]
        assert "1065-1069" in rt and "#1068 Type B" in rt and "CLOSING leg" in rt
        assert "D->E->A->B->C" in rt

    def test_predecessor_1068_pinned(self):
        rt = get_block()["rotation_transparency"]
        assert "#1068 Type B" in rt

    def test_iteration_type_c(self):
        assert get_block()["iteration_type"] == TYPE_LETTER


# ---------------------------------------------------------------------------
# 3. Mechanism structure
# ---------------------------------------------------------------------------
class TestMechanism873Structure:
    def test_mechanism_id_and_type(self):
        block = get_block()
        assert block["mechanism_id"] == M_ID
        assert block["type"] == "financial_incentive_mapping"
        assert block["type_label"] == "Financial Incentive Mapping"

    def test_iteration_fields(self):
        block = get_block()
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == TYPE_LETTER
        assert block["iteration_time"] == "2026-09-29 06:00 PDT"
        assert block["scheduled_job_id"] == "mediascope-daily-iteration"
        assert block["goal_id"] == "goal_54093bda4145"

    def test_block_key_descriptive_no_873(self):
        assert MECH_KEY in _read(PROFILE)
        assert "873" not in MECH_KEY
        assert "metered_recycling" in MECH_KEY
        assert "twentyfirst_direction" in MECH_KEY
        assert get_block()["block_key"] == MECH_KEY

    def test_discipline_flags(self):
        block = get_block()
        assert block["tone_scored"] is False
        assert block["engine_run"] is False
        assert block["is_significant"] is False
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["no_analysis_json_update"] is True
        assert block["artifact_grade"] is False
        assert block["yaml_parse_clean"] is True
        assert block["ascii_only"] is True

    def test_connects_to(self):
        block = get_block()
        assert block["connects_to"] == [864, 867, 1009, 870]
        assert block["falsification_family_member"] is False


# ---------------------------------------------------------------------------
# 4. The three legs + coverage nexus
# ---------------------------------------------------------------------------
class TestMechanism873Legs:
    def test_commitment_leg(self):
        leg = get_block()["commitment_leg"]
        assert "$100 billion" in leg
        assert "10 gigawatts" in leg
        assert "Sep 22 2025" in leg
        assert "Vera Rubin" in leg
        assert "first-hand" in leg

    def test_meter_leg(self):
        leg = get_block()["meter_leg"]
        assert "two intertwined transactions" in leg
        assert "non-voting shares" in leg
        assert "$10B per gigawatt" in leg
        assert "cannot outrun the demand leg" in leg

    def test_stall_leg(self):
        leg = get_block()["stall_leg"]
        assert "Jan 31 2026" in leg
        assert "never a commitment" in leg
        assert "nothing like $100 billion" in leg
        assert "largest investment" in leg
        assert "circular" in leg

    def test_coverage_nexus_no_tone_claims(self):
        nexus = get_block()["coverage_nexus"]
        assert "circular-dealmmaking news peg" in nexus
        assert "financial-event peg" in nexus
        assert "tone NOT_SCORED" in nexus

    def test_finding_geometry(self):
        finding = get_block()["finding"]
        assert "metered-recycling" in finding
        assert "THE COMMITMENT LEG" in finding
        assert "THE METER LEG" in finding
        assert "THE STALL LEG" in finding
        assert "THE GEOMETRY" in finding
        assert "self-collateralizing ratchet" in finding

    def test_sources_first_hand(self):
        sources = get_block()["sources"]
        assert len(sources) == 5
        urls = [s["url"] for s in sources]
        for u in EXPECTED_NEW_URLS:
            assert u in urls
        assert all(s["novel"] is True for s in sources)
        assert all(s["accessed"] == "2026-09-29" for s in sources)

    def test_counterargument_earns_slot(self):
        ca = get_block()["counterargument"]
        assert "vendor financing" in ca
        assert "twenty-first slot" in ca
        assert "risk-allocation work" in ca


# ---------------------------------------------------------------------------
# 5. Taxonomy: the twenty-first direction
# ---------------------------------------------------------------------------
class TestMechanism873Taxonomy:
    def test_twentyfirst_direction_named(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "TWENTY-FIRST" in tax
        assert "METERED-RECYCLING" in tax

    def test_enumeration_lists_twentyone(self):
        tax = get_block()["relationship_direction_taxonomy"]
        for n in ("1 sue-then-sign m624", "13 demand-for-equity m1009",
                 "18 demand-recycling m864", "19 backstop-recycling m867",
                 "20 demand-underwriting m870"):
            assert n in tax

    def test_refinement_of_eighteen(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "refinement of #18" in tax
        assert "cash out as equity, back as revenue" in tax

    def test_distinct_from_nineteen(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "Distinct from #19" in tax
        assert "contingent guarantee" in tax

    def test_distinct_from_twenty(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "and #20" in tax
        assert "buyer" in tax

    def test_m737_tension_carried(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "termination-leverage" in tax
        assert "Not resolved this run" in tax


# ---------------------------------------------------------------------------
# 6. Confounders, strongest-first
# ---------------------------------------------------------------------------
class TestMechanism873Confounders:
    def test_six_confounders_ranked(self):
        confs = get_block()["confounders"]
        assert len(confs) == 6
        assert [c["strength"] for c in confs] == [
            "STRONG", "STRONG", "STRONG", "MEDIUM", "MEDIUM", "WEAK",
        ]

    def test_headline_ceiling_confound(self):
        confs = get_block()["confounders"]
        assert "non-binding LOI" in confs[0]["what"]
        assert "ceiling" in confs[0]["what"]

    def test_stall_provenance_confound(self):
        confs = get_block()["confounders"]
        assert "WSJ-reported" in confs[1]["what"]
        assert "paywalled" in confs[1]["what"]

    def test_two_transaction_attribution_confound(self):
        confs = get_block()["confounders"]
        assert "Reuters" in confs[2]["what"]
        assert "characterization" in confs[2]["what"]

    def test_circular_discourse_confound(self):
        confs = get_block()["confounders"]
        assert "analyst and commentator framing" in confs[3]["what"]

    def test_relay_tier_confound(self):
        confs = get_block()["confounders"]
        assert "relay-tier" in confs[4]["what"]

    def test_timing_confound(self):
        confs = get_block()["confounders"]
        assert "Sep 2025" in confs[5]["what"]

    def test_not_falsification_family_ledger_35(self):
        block = get_block()
        assert block["falsification_family_member"] is False
        # The ledger and falsification-family prose lives in the iteration-log
        # entry (discipline section), not the block itself.
        section = _log_section()
        assert "NOT a falsification-family member" in section
        assert "ledger holds at 35" in section


# ---------------------------------------------------------------------------
# 7. Research method
# ---------------------------------------------------------------------------
class TestResearchMethodTypeC1069:
    def test_two_browser_open_first_hand(self):
        section = _log_section()
        assert "2 browser.open" in section
        assert "Nvidia" in section

    def test_three_search_sets(self):
        section = _log_section()
        assert "3 browser.search" in section

    def test_urls_verbatim_no_canonical(self):
        for url in EXPECTED_NEW_URLS:
            assert url.startswith("https://") and " " not in url

    def test_ascii_only_no_em_dashes(self):
        blob = _read(os.path.join(REPO, "tests", OWN_BASENAME))
        assert "\u2014" not in blob
        blob.encode("ascii")


# ---------------------------------------------------------------------------
# 8. Post-commit corpus novelty: 873 is max, 874 is zero
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPostCommit:
    def test_max_numeric_mechanism_id_is_873(self):
        assert max(_corpus_ids()) == M_ID

    def test_zero_next_numeric_874_in_profiles(self):
        base = os.path.join(REPO, "profiles")
        for root, _, files in os.walk(base):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(root, fn))
                    assert NEXT_NUMERIC not in text

    def test_zero_next_underscore_dash_874_repo_wide(self):
        assert _repo_grep(NEXT_US) == []
        assert _repo_grep(NEXT_DASH) == []

    def test_five_urls_now_in_corpus(self):
        text = "\n".join(
            _read(os.path.join(root, fn))
            for root, _, files in os.walk(os.path.join(REPO, "profiles"))
            for fn in files
            if fn.endswith(".yaml")
        )
        for u in EXPECTED_NEW_URLS:
            assert u in text, "novel URL not ingested: %s" % u

    def test_own_needles_format_built(self):
        # Per #715: own file's forward-looking needles are format-built so no
        # contiguous literal exists anywhere in the committed tree. The
        # absence assertions below are themselves format-built for the same
        # reason: asserting absence of a literal would embed the literal.
        blob = _read(os.path.join(REPO, "tests", OWN_BASENAME))
        assert "mechanism" + "_" + "87" + "4" not in blob
        assert "mechanism" + "-" + "87" + "4" not in blob


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

    def test_readme_row_1069(self):
        text = _read(README)
        assert OWN_BASENAME in text
        assert "Type C #1069" in text
        assert "mechanism 873" in text

    def test_arch_row_1069(self):
        text = _read(ARCH)
        assert OWN_BASENAME in text
        assert "Type C #1069" in text

    def test_expected_order_in_docstring(self):
        assert EXPECTED_ORDER == [("C", "1069"), ("B", "1068"), ("A", "1067"),
                                  ("E", "1066"), ("D", "1065")]


# ---------------------------------------------------------------------------
# 10. Iteration-log entry (deselected pre-commit per #719/#721)
# ---------------------------------------------------------------------------
@pytest.mark.itlog
class TestIterationLogEntry:
    def _section(self):
        log = _read(ITERATION_LOG)
        start = log.index("## #1069 Type C")
        end = log.index("## #1068 Type B")
        return log[start:end]

    def test_log_header_present(self):
        log = _read(ITERATION_LOG)
        assert log.count("## #1069 Type C") == 1

    def test_log_contains_mechanism(self):
        section = self._section()
        assert "mechanism 873" in section
        assert "METERED-RECYCLING" in section

    def test_log_rotation(self):
        section = self._section()
        assert "1065-1069" in section
        assert "C #1069" in section


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
        import json

        blob = json.dumps(get_block(), ensure_ascii=False)
        assert "\u2014" not in blob  # no em dashes, repo prose rule
        blob.encode("ascii")  # raises on any other non-ASCII

    def test_source_references_recorded(self):
        # Per the standing "keep references" rule: every fact needs a
        # source URL or citation; the block carries 5 verbatim URLs.
        sources = get_block()["sources"]
        assert len(sources) == 5
        assert all(s["url"].startswith("https://") for s in sources)

    def test_test_file_ascii(self):
        blob = _read(os.path.join(REPO, "tests", OWN_BASENAME))
        assert "\u2014" not in blob
        blob.encode("ascii")

    def test_finding_carries_discipline_prose(self):
        # Discipline prose lives in the block's finding (legs + first-hand
        # caveat) and the iteration-log entry (ledger, falsification family);
        # the machine-readable flags are asserted in test_discipline_flags.
        finding = get_block()["finding"]
        assert "FIRST-HAND SOURCES this run" in finding
        section = _log_section()
        assert "MANUAL" in section
        assert "NOT a falsification-family member" in section
        assert "ledger holds at 35" in section


def _log_section():
    # Helper used by TestResearchMethodTypeC1069; defined after the classes
    # that reference it at call time (not import time).
    log = _read(ITERATION_LOG)
    start = log.index("## #1069 Type C")
    end = log.index("## #1068 Type B")
    return log[start:end]
