"""Type C #1074: Nvidia x insurer risk-transfer architecture (Aug 10 2026 Wall
Street MOUs; ~$12.9B insurance coverage Sep 2026) - RISK-TRANSFER as the
TWENTY-SECOND relationship direction.

Expected order (newest first): C #1074, B #1073, A #1072, E #1071, D #1070.
EXPECTED_ORDER = [("C", "1074"), ("B", "1073"), ("A", "1072"), ("E", "1071"),
                  ("D", "1070")]
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

ITERATION = 1074
TYPE_LETTER = "C"
RUN_PDT = "2026-09-29 11:00 PDT"
MECH_KEY = (
    "type_c_1074_nvidia_insurer_risk_transfer_"
    "twentysecond_direction_sep29_11am"
)
M_ID = 876
OWN_BASENAME = (
    "test_type_c_1074_nvidia_insurer_risk_transfer_"
    "twentysecond_direction_sep29_11am.py"
)

# Guard needles: corpus max is now 876, so the next-number sweep targets 877.
# Format-built per #715 so no contiguous literal exists in this file.
NEXT_US = "mechanism" + "_877"  # next-number underscore sweep
NEXT_DASH = "mechanism" + "-877"  # next-number dash sweep
NEXT_NUMERIC = "mechanism_id: " + "877"  # next-number numeric sweep

# Anchor SHA for the #1074 main commit; patched post-commit per #565.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

# Doc-sync ratchet targets (55110/1398 pre-commit + 52/+1 this file).
README_TESTS_AFTER = 55163
README_FILES_AFTER = 1399

NOVELTY_CLAIMS = (
    "zero\ntest_type_c_1074 files, max numeric\nmechanism_id 875 pre-commit, "
    "block key zero-hit, 6 novel\nURLs zero-hit, Pike County absent"
)

EXPECTED_NEW_URLS = [
    "https://startupfortune.com/nvidia-is-quietly-pushing-ai-data-center-risk-onto-insurance-companies/",
    "https://www.tradingview.com/news/cryptobriefing:9e10f05d0094b:0-nvidia-partners-with-insurers-to-mitigate-ai-expansion-risks/",
    "https://cryptobriefing.com/nvidia-500b-chip-financing-private-credit/",
    "https://www.computeleap.com/blog/nvidia-central-bank-of-ai/",
    "https://aistockwire.com/blog/oracle-orcl-data-center-loans-18-billion-89-cents-ai-debt-stress-september-2026",
    "https://wsnext.com/907be76-AI-Financing-Risk-Mitigation/",
]

EXPECTED_ORDER = [("C", "1074"), ("B", "1073"), ("A", "1072"), ("E", "1071"),
                  ("D", "1070")]

INFLIGHT_FILES = {
    "profiles/nytimes.yaml",
    "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",
    "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
    "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
}

STAGED_EXPECTED_BASENAMES = {
    "competitor-entities.yaml",
    OWN_BASENAME,
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
class TestNoveltyAnchorTypeC1074:
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
        # Scoped to the #1074 header line (not the whole log) per the #1044
        # test fix: newer entries name predecessor SHAs in their
        # rotation-transparency sections, which a whole-log index() cannot
        # distinguish.
        log = _read(ITERATION_LOG)
        header_start = log.index("## #1074 Type C")
        header_end = log.index("\n", header_start)
        assert ANCHORED_SHA[:8] in log[header_start:header_end]

    def test_novelty_claims(self):
        assert NOVELTY_CLAIMS == (
            "zero\ntest_type_c_1074 files, max numeric\nmechanism_id 875 pre-commit, "
            "block key zero-hit, 6 novel\nURLs zero-hit, Pike County absent"
        )


# ---------------------------------------------------------------------------
# 2. Rotation guard (1070-1074 window: D -> E -> A -> B -> C), per #565.
#    All rotation tests are deselected pre-commit (log entry prepended at
#    doc-sync) and re-run after doc-sync.
# ---------------------------------------------------------------------------
@pytest.mark.rotation
class TestRotationGuard1070_1074Window:
    def test_window_legs_in_log(self):
        log = _read(ITERATION_LOG)
        for number, letter in (("1070", "D"), ("1071", "E"), ("1072", "A"),
                               ("1073", "B")):
            assert "## #%s Type %s" % (number, letter) in log

    def test_this_run_fifth_leg_c(self):
        log = _read(ITERATION_LOG)
        assert log.count("## #1074 Type C") == 1
        rt = get_block()["rotation_transparency"]
        assert "1070-1074" in rt and "#1073 Type B" in rt and "CLOSING leg" in rt
        assert "D->E->A->B->C" in rt

    def test_predecessor_1073_pinned(self):
        rt = get_block()["rotation_transparency"]
        assert "#1073 Type B" in rt

    def test_iteration_type_c(self):
        assert get_block()["iteration_type"] == TYPE_LETTER


# ---------------------------------------------------------------------------
# 3. Mechanism structure
# ---------------------------------------------------------------------------
class TestMechanism876Structure:
    def test_block_key_zero_indent_unique(self):
        lines = [l for l in _read(PROFILE).splitlines() if l.startswith(MECH_KEY + ":")]
        assert len(lines) == 1

    def test_block_key_field_repeat_two_occurrences(self):
        # Designed keying per #1064/#1069: YAML key + block_key: field repeat.
        text = _read(PROFILE)
        assert text.count(MECH_KEY) == 2

    def test_mechanism_id_numeric_876(self):
        assert get_block()["mechanism_id"] == M_ID
        assert isinstance(get_block()["mechanism_id"], int)

    def test_type_fields(self):
        b = get_block()
        assert b["type"] == "financial_incentive_mapping"
        assert b["type_label"] == "Financial Incentive Mapping"
        assert b["iteration"] == ITERATION
        assert b["iteration_time"] == RUN_PDT
        assert b["scheduled_job_id"] == "mediascope-daily-iteration"
        assert b["goal_id"] == "goal_54093bda4145"

    def test_statistical_discipline_fields(self):
        b = get_block()
        assert b["tone_scored"] is False
        assert b["engine_run"] is False
        assert b["is_significant"] is False
        assert b["verdict"] == "directionally_supported_not_proven"
        assert b["no_analysis_json_update"] is True
        assert b["artifact_grade"] is False
        assert b["falsification_family_member"] is False

    def test_mechanism_name_first_dedicated(self):
        name = get_block()["mechanism_name"]
        assert name.startswith("FIRST dedicated corpus mechanism")
        assert "RISK-TRANSFER" in name
        assert "TWENTY-SECOND" in name

    def test_leg_fields_present(self):
        b = get_block()
        for leg in ("mou_leg", "insurance_leg", "cds_leg", "mismatch_leg",
                    "coverage_nexus", "finding"):
            assert b[leg] and len(b[leg]) > 100, "leg missing/short: %s" % leg


# ---------------------------------------------------------------------------
# 4. Mechanism legs (key facts)
# ---------------------------------------------------------------------------
class TestMechanism876Legs:
    def test_mou_leg_facts(self):
        leg = get_block()["mou_leg"]
        assert "Aug 10 2026" in leg
        assert "$500B" in leg
        assert "25%" in leg
        assert "Apollo" in leg and "KKR" in leg

    def test_insurance_leg_facts(self):
        leg = get_block()["insurance_leg"]
        assert "$12.9B" in leg
        assert "$105B" in leg
        assert "Pike County" in leg

    def test_cds_leg_facts(self):
        leg = get_block()["cds_leg"]
        assert "82 bps" in leg
        assert "Jul 27 2026" in leg

    def test_mismatch_leg_facts(self):
        leg = get_block()["mismatch_leg"]
        assert "GPU debt treadmill" in leg
        assert "$182B" in leg

    def test_sources_all_novel_with_accessed(self):
        srcs = get_block()["sources"]
        assert len(srcs) == 6
        for s in srcs:
            assert s["accessed"] == "2026-09-29"
            assert s["novel"] is True
        urls = [s["url"] for s in srcs]
        assert urls == EXPECTED_NEW_URLS

    def test_first_hand_vs_relay_bounding(self):
        finding = get_block()["finding"]
        assert "opened first-hand this run" in finding
        assert "excerpt-bounded relay per #503" in finding


# ---------------------------------------------------------------------------
# 5. Taxonomy (TWENTY-SECOND per the m807 enumeration)
# ---------------------------------------------------------------------------
class TestMechanism876Taxonomy:
    def test_twentysecond_ordinal(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert tax.startswith("TWENTY-SECOND relationship direction")

    def test_enumeration_1_to_21_intact(self):
        tax = get_block()["relationship_direction_taxonomy"]
        for n, label in (
            ("1", "sue-then-sign m624"), ("2", "pay-or-litigate bifurcation m636"),
            ("3", "grant-then-sue m675"), ("4", "license-over-authors m699"),
            ("5", "pool-and-license m720"), ("6", "infrastructure-capture m738"),
            ("7", "publisher-as-feed-operator m741"), ("8", "vendor-embed m807"),
            ("9", "litigation-pooling m810"), ("10", "publisher-traffic-gate m828"),
            ("11", "commerce-conversion licensing m831"),
            ("12", "regulatory-bargaining m1004"), ("13", "demand-for-equity m1009"),
            ("14", "exclusionary-diversion m1024"), ("15", "ecosystem-grant m1029"),
            ("16", "commerce-gatekeeping m1039"), ("17", "bundled-leverage m1049"),
            ("18", "demand-recycling m864"), ("19", "backstop-recycling m867"),
            ("20", "demand-underwriting m870"),
            ("21", "metered-recycling m873"),
        ):
            assert "%s %s" % (n, label) in tax, "enumeration leg missing: %s" % label

    def test_risk_transfer_distinctness(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "RISK-TRANSFER" in tax
        # The second hop (guarantee itself insured) is the work #19 cannot do.
        assert "second hop" in tax
        assert "#19" in tax and "#21" in tax and "#13" in tax and "#20" in tax

    def test_slot_bar_stated(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "a bar future instances must clear" in tax
        assert "82 bps" in tax

    def test_taxonomy_count_tension_carried(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "termination-leverage" in tax
        assert "Not resolved this run" in tax

    def test_connects_to(self):
        assert get_block()["connects_to"] == [864, 867, 870, 873]


# ---------------------------------------------------------------------------
# 6. Confounders + counterargument + discipline prose
# ---------------------------------------------------------------------------
class TestMechanism876Confounders:
    def test_six_confounders_strongest_first(self):
        confs = get_block()["confounders"]
        assert len(confs) == 6
        strengths = [c["strength"] for c in confs]
        assert strengths[:2] == ["STRONG", "STRONG"]
        assert strengths[2:4] == ["MEDIUM", "MEDIUM"]
        assert strengths[4:] == ["WEAK", "WEAK"]

    def test_confounder_source_tier_and_mou_limits(self):
        text = " ".join(c["what"] for c in get_block()["confounders"])
        assert "not a single dollar of it is confirmed as spent" in text
        assert "single secondary relay" in text

    def test_counterargument_slot_bar(self):
        ca = get_block()["counterargument"]
        assert "Ordinary structured finance" in ca
        assert "aircraft" in ca
        assert "collapses back into #19 with a reinsurance rider" in ca

    def test_coverage_nexus_no_tone_claim(self):
        assert "tone NOT_SCORED" in get_block()["coverage_nexus"]
        assert "89-91 cents on the dollar" in get_block()["coverage_nexus"]


# ---------------------------------------------------------------------------
# 7. Research method (doc-sync dependent: asserts the iteration-log entry)
# ---------------------------------------------------------------------------
class TestResearchMethodTypeC1074:
    def _section(self):
        log = _read(ITERATION_LOG)
        start = log.index("## #1074 Type C")
        end = log.index("## #1073 Type B")
        return log[start:end]

    def test_two_search_sets_one_open(self):
        section = self._section()
        assert "2 browser.search query sets" in section
        assert "1 browser.open" in section
        assert "#503" in section

    def test_rejected_candidates_logged(self):
        section = self._section()
        assert "Research rejected" in section


# ---------------------------------------------------------------------------
# 8. Corpus novelty post-commit
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPostCommit:
    def test_max_numeric_mechanism_id_876(self):
        assert max(_corpus_ids()) == M_ID

    def test_zero_877_keys(self):
        assert NEXT_NUMERIC not in _read(PROFILE)
        assert not _repo_grep(NEXT_US)
        assert not _repo_grep(NEXT_DASH)

    def test_falsification_ledger_holds_35(self):
        b = get_block()
        assert b["falsification_family_member"] is False
        assert "ledger holds at 35" in b["falsification_family"]
        assert "THIRTY-SIXTH" not in _read(PROFILE)

    def test_no_twentythird_relationship_direction(self):
        # Per #715 the absence needle is format-built so the contiguous
        # literal never appears in this file (self-match would fail the
        # sweep); the joined needle must be absent repo-wide.
        needle = "TWENTY-" + "THIRD relationship direction"
        assert not _repo_grep(needle)

    def test_new_urls_novel_repo_wide(self):
        for url in EXPECTED_NEW_URLS:
            hits = [h for h in _repo_grep(url) if "competitor-entities.yaml" in h
                    or OWN_BASENAME in h]
            # Each URL lives exactly in the block and in this file's constant.
            assert len(hits) == 2, (url, hits)

    def test_discipline_prose(self):
        b = get_block()
        assert b["yaml_parse_clean"] is True
        assert b["ascii_only"] is True
        novelty = b["novelty"]
        assert "FIRST dedicated corpus mechanism" in novelty
        assert "zero \"Pike County\" hits" in novelty


# ---------------------------------------------------------------------------
# 9. Doc-sync ratchet
# ---------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_header_stats_bumped(self):
        line = next(
            l for l in _read(README).splitlines() if l.startswith("| Tests |")
        )
        assert str(README_TESTS_AFTER) in line
        assert str(README_FILES_AFTER) in line

    def test_readme_row_1074(self):
        text = _read(README)
        assert OWN_BASENAME in text
        assert "Type C #1074" in text
        assert "mechanism 876" in text

    def test_arch_row_1074(self):
        text = _read(ARCH)
        assert OWN_BASENAME in text
        assert "Type C #1074" in text

    def test_expected_order_in_docstring(self):
        assert EXPECTED_ORDER == [("C", "1074"), ("B", "1073"), ("A", "1072"),
                                  ("E", "1071"), ("D", "1070")]


# ---------------------------------------------------------------------------
# 10. Iteration-log entry (deselected pre-commit per #719/#721)
# ---------------------------------------------------------------------------
@pytest.mark.itlog
class TestIterationLogEntry:
    def _section(self):
        log = _read(ITERATION_LOG)
        start = log.index("## #1074 Type C")
        end = log.index("## #1073 Type B")
        return log[start:end]

    def test_log_header_present(self):
        log = _read(ITERATION_LOG)
        assert log.count("## #1074 Type C") == 1

    def test_log_contains_mechanism(self):
        section = self._section()
        assert "mechanism 876" in section
        assert "RISK-TRANSFER" in section

    def test_log_rotation(self):
        section = self._section()
        assert "1070-1074" in section
        assert "C #1074" in section

    def test_log_carries_commit_hashes_per_721(self):
        section = self._section()
        assert re.search(r"main commit [0-9a-f]{8}", section)
        assert re.search(r"anchor [0-9a-f]{8}", section)

    def test_log_ledger_holds_35(self):
        section = self._section()
        assert "ledger holds at 35" in section


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
    def test_block_region_ascii_only(self):
        text = _read(PROFILE)
        start = text.index(MECH_KEY + ":")
        region = text[start:]
        bad = [c for c in region if ord(c) > 127]
        assert not bad, "non-ascii in block region: %r" % (bad[:5],)

    def test_no_em_dashes_in_block(self):
        text = _read(PROFILE)
        start = text.index(MECH_KEY + ":")
        assert "\u2014" not in text[start:]

    def test_yaml_file_parses_clean(self):
        import yaml

        yaml.safe_load(_read(PROFILE))
