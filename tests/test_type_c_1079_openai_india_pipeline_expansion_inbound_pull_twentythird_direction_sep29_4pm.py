"""Type C #1079: OpenAI India publisher pipeline expansion (Sep 28 2026 e4m -
two more deals in the works beyond the Sep 7-8 BCCL/Indian Express signings) -
INBOUND-PULL as the TWENTY-THIRD relationship direction. FIFTH and CLOSING
leg of the 1075-1079 window.

DESIGN (deal-pipeline / buyer-side selection-gate extension):
- Corpus already holds mechanism 798 / Type C #944 (fee estimates ~$5M/yr
  BCCL, ~$3M/yr Indian Express; bandwagon leg: publishers approaching
  OpenAI). This run does NOT re-claim those as new.
- Fresh extension this run: exchange4media Sep 28 2026 (opened first-hand,
  109 rendered lines) reports two more India publisher partnerships
  "understood to be in the works" per industry sources - one media house
  "rooted in television and digital broadcasting," the other with "a strong
  legacy in print and digital publishing." Both unnamed; OpenAI declined to
  comment; nothing signed.
- THE DIRECTION: inbound-pull - the Sep 7-8 anchor signings (OpenAI's
  "first publicly disclosed publisher partnerships in India") flip the
  solicitation arrow, and the lab rations deal access among inbound demand:
  "some leading publishers have approached OpenAI, although they are yet
  to secure commercial arrangements" (approached-but-not-secured), and the
  piece asks whether OpenAI pursues "a broader publisher ecosystem in the
  country or ... a more selective approach to media partnerships."
- Distinct from #1 sue-then-sign (no suit drives the pipeline), #8
  vendor-embed (no product embedding is the mechanism), #17 bundled-leverage
  (the competed-for object is the deal slot itself).
- 6 confounders strongest-first (single-trade-source unnamed-sources tier;
  "in the works" is not signed; gatekeeper inference partly interpretive;
  India-market specificity; timing; carried $5M/$3M pricing).
- Counterargument: ordinary deal momentum - the 23rd slot survives only on
  the rationing leg; if the two deals close on the identical attribution
  template with no selection evidence, it collapses into a time-extension
  of m609's blitz, not a new direction.

NOVELTY VERIFICATION (pre-commit, all green):
- zero test_type_c_1079 files on disk (glob)
- no "Type C #1079" in git log (--grep)
- max numeric mechanism_id 878 in profiles/ pre-commit (Type B #1078,
  mechanism 878 in profiles/careers/journalists.yaml)
- zero numeric 879 mechanism_id keys in profiles/
- zero underscore-form and dash-form 879 mechanism key strings repo-wide
  pre-commit (needles format-built per #715); block key zero-hit
- the 158690 e4m URL zero-hit repo-wide pre-commit (git grep -F on the
  verbatim Full-URL listing); the 158488 URL and $5M/$3M estimates are
  corpus-carried via m798 (#944), not re-claimed

BY-DESIGN-FAILING SETS:
- Pre-commit run: deselect the anchor-marked tests (3 per #565, patched in
  the anchor followup), the rotation-marked tests (4 per #565, log entry
  prepended at doc-sync), and the itlog-marked tests (5 per #721, green
  after the log-hash followup). The doc-sync ratchet (4 per #719), the
  research-method tests (2), and the staging tests (2) fail pre-commit by
  design and go green post-doc-sync/staging.
- Post-doc-sync re-run: deselect anchor + rotation + itlog marks; the two
  pre-commit-only placeholder tests (test_anchor_sha_placeholder_precommit
  is covered by the anchor mark) - everything else green.

STATISTICAL DISCIPLINE: MANUAL / QUALITATIVE ONLY per the Aug 28 2026
standing rule. p_value/cohens_d/ci_95 NOT_CALCULATED. tone NOT_SCORED.
Engine NOT run. is_significant False. verdict
directionally_supported_not_proven. no_analysis_json_update True. NOT
artifact-grade. n=1 mechanism; hypothesis-generating only. Correlation is
not causation.

ASCII-only, no em dashes.
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

ITERATION = 1079
TYPE_LETTER = "C"
RUN_PDT = "2026-09-29 16:00 PDT"
MECH_KEY = (
    "type_c_1079_openai_india_pipeline_expansion_inbound_pull_"
    "twentythird_direction_sep29_4pm"
)
M_ID = 879
OWN_BASENAME = (
    "test_type_c_1079_openai_india_pipeline_expansion_inbound_pull_"
    "twentythird_direction_sep29_4pm.py"
)

# Guard needles: corpus max is now 879, so the next-number sweep targets 880.
# Format-built per #715 so no contiguous literal exists in this file.
NEXT_US = "mechanism" + "_880"  # next-number underscore sweep
NEXT_DASH = "mechanism" + "-880"  # next-number dash sweep
NEXT_NUMERIC = "mechanism_id: " + "880"  # next-number numeric sweep

# Anchor SHA for the #1079 main commit; patched post-commit per #565.
ANCHORED_SHA = "a04bf111825da7bf3d78f9c36a44ebd8cf70801f"  # patched in the anchor followup per #565

# Doc-sync ratchet targets (54468/1403 authoritative per count_stats.py
# --check at doc-sync time + 54/+1 this file).
README_TESTS_AFTER = 54522
README_FILES_AFTER = 1404

NOVELTY_CLAIMS = (
    "zero\ntest_type_c_1079 files, max numeric\nmechanism_id 878 pre-commit, "
    "block key zero-hit, 1 novel\nURL zero-hit, inbound-pull absent"
)

EXPECTED_NEW_URLS = [
    "https://www.exchange4media.com/digital-news/openais-india-publisher-pipeline-expands-two-more-deals-in-the-works-158690.html",
]

EXPECTED_ORDER = [("C", "1079"), ("B", "1078"), ("A", "1077"), ("E", "1076"),
                  ("D", "1075")]

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
class TestNoveltyAnchorTypeC1079:
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
        # Scoped to the #1079 header line (not the whole log) per the #1044
        # test fix: newer entries name predecessor SHAs in their
        # rotation-transparency sections, which a whole-log index() cannot
        # distinguish.
        log = _read(ITERATION_LOG)
        header_start = log.index("## #1079 Type C")
        header_end = log.index("\n", header_start)
        assert ANCHORED_SHA[:8] in log[header_start:header_end]

    def test_novelty_claims(self):
        assert NOVELTY_CLAIMS == (
            "zero\ntest_type_c_1079 files, max numeric\nmechanism_id 878 "
            "pre-commit, block key zero-hit, 1 novel\nURL zero-hit, "
            "inbound-pull absent"
        )


# ---------------------------------------------------------------------------
# 2. Rotation guard (1075-1079 window: D -> E -> A -> B -> C), per #565.
#    All rotation tests are deselected pre-commit (log entry prepended at
#    doc-sync) and re-run after doc-sync.
# ---------------------------------------------------------------------------
@pytest.mark.rotation
class TestRotationGuard1075_1079Window:
    def test_window_legs_in_log(self):
        log = _read(ITERATION_LOG)
        for number, letter in (("1075", "D"), ("1076", "E"), ("1077", "A"),
                               ("1078", "B")):
            assert "## #%s Type %s" % (number, letter) in log

    def test_this_run_fifth_leg_c(self):
        log = _read(ITERATION_LOG)
        assert log.count("## #1079 Type C") == 1
        rt = get_block()["rotation_transparency"]
        assert "1075-1079" in rt and "#1078 Type B" in rt and "CLOSING leg" in rt
        assert "D->E->A->B->C" in rt

    def test_predecessor_1078_pinned(self):
        rt = get_block()["rotation_transparency"]
        assert "#1078 Type B" in rt

    def test_iteration_type_c(self):
        assert get_block()["iteration_type"] == TYPE_LETTER


# ---------------------------------------------------------------------------
# 3. Mechanism structure
# ---------------------------------------------------------------------------
class TestMechanism879Structure:
    def test_block_key_zero_indent_unique(self):
        lines = [l for l in _read(PROFILE).splitlines() if l.startswith(MECH_KEY + ":")]
        assert len(lines) == 1

    def test_block_key_field_repeat_two_occurrences(self):
        # Designed keying per #1064/#1069: YAML key + block_key: field repeat.
        text = _read(PROFILE)
        assert text.count(MECH_KEY) == 2

    def test_mechanism_id_numeric_879(self):
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
        assert "INBOUND-PULL" in name
        assert "TWENTY-THIRD" in name

    def test_leg_fields_present(self):
        b = get_block()
        for leg in ("pipeline_leg", "inbound_leg", "pricing_context_leg",
                    "inventory_leg", "traffic_tension_leg", "coverage_nexus",
                    "finding"):
            assert b[leg] and len(b[leg]) > 100, "leg missing/short: %s" % leg


# ---------------------------------------------------------------------------
# 4. Mechanism legs (key facts)
# ---------------------------------------------------------------------------
class TestMechanism879Legs:
    def test_pipeline_leg_facts(self):
        leg = get_block()["pipeline_leg"]
        assert "two more" in leg
        assert "in the works" in leg
        assert "television and digital broadcasting" in leg
        assert "strong legacy in print and digital publishing" in leg
        assert "declined to comment" in leg
        assert "first publicly disclosed publisher partnerships in India" in leg

    def test_inbound_leg_facts(self):
        leg = get_block()["inbound_leg"]
        assert "approached OpenAI" in leg
        assert "yet to secure commercial arrangements" in leg
        assert "m798" in leg

    def test_pricing_context_leg_carried_not_new(self):
        leg = get_block()["pricing_context_leg"]
        assert "$5 million" in leg
        assert "$3 million" in leg
        assert "not re-claimed" in leg
        assert "$250M/5yr" in leg

    def test_inventory_leg_facts(self):
        leg = get_block()["inventory_leg"]
        assert "160+ outlets" in leg
        assert "Folha de S.Paulo" in leg
        assert "100M weekly" in leg

    def test_traffic_tension_leg_facts(self):
        leg = get_block()["traffic_tension_leg"]
        assert "discovery journey changes" in leg
        assert "25-30%" in leg

    def test_sources_all_novel_with_accessed(self):
        srcs = get_block()["sources"]
        assert len(srcs) == 1
        for s in srcs:
            assert s["accessed"] == "2026-09-29"
            assert s["novel"] is True
        urls = [s["url"] for s in srcs]
        assert urls == EXPECTED_NEW_URLS

    def test_first_hand_bounding(self):
        finding = get_block()["finding"]
        assert "opened first-hand this run" in finding
        assert "109 rendered lines" in finding
        assert "excerpt-bounded per #503" in finding


# ---------------------------------------------------------------------------
# 5. Taxonomy (TWENTY-THIRD per the m807 enumeration)
# ---------------------------------------------------------------------------
class TestMechanism879Taxonomy:
    def test_twentythird_ordinal(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert tax.startswith("TWENTY-THIRD relationship direction")

    def test_enumeration_1_to_22_intact(self):
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
            ("22", "risk-transfer m876"),
        ):
            assert "%s %s" % (n, label) in tax, "enumeration leg missing: %s" % label

    def test_inbound_pull_distinctness(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "INBOUND-PULL" in tax
        assert "23 inbound-pull m879" in tax
        # The rationing leg is the work sequential signing cannot do.
        assert "rationing leg" in tax
        assert "#1" in tax and "#8" in tax and "#17" in tax

    def test_slot_bar_stated(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "a bar future instances must clear" in tax
        assert "documented inbound solicitation" in tax

    def test_taxonomy_count_tension_carried(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "termination-leverage" in tax
        assert "Not resolved this run" in tax

    def test_connects_to(self):
        assert get_block()["connects_to"] == [609, 798]


# ---------------------------------------------------------------------------
# 6. Confounders + counterargument + discipline prose
# ---------------------------------------------------------------------------
class TestMechanism879Confounders:
    def test_six_confounders_strongest_first(self):
        confs = get_block()["confounders"]
        assert len(confs) == 6
        strengths = [c["strength"] for c in confs]
        assert strengths[:2] == ["STRONG", "STRONG"]
        assert strengths[2:4] == ["MEDIUM", "MEDIUM"]
        assert strengths[4:] == ["WEAK", "WEAK"]

    def test_confounder_source_tier_and_pipeline_limits(self):
        text = " ".join(c["what"] for c in get_block()["confounders"])
        assert "Single-trade-source tier" in text
        assert "declined to comment" in text
        assert "In the works" in text and "is not signed" in text
        assert "fails to convert" in text

    def test_counterargument_slot_bar(self):
        ca = get_block()["counterargument"]
        assert "Ordinary deal momentum" in ca
        assert "reference-customer dynamics" in ca
        assert "collapses into a time-extension of m609" in ca

    def test_coverage_nexus_no_tone_claim(self):
        assert "tone NOT_SCORED" in get_block()["coverage_nexus"]
        assert "traffic versus licensing revenue" in get_block()["coverage_nexus"]


# ---------------------------------------------------------------------------
# 7. Research method (doc-sync dependent: asserts the iteration-log entry)
# ---------------------------------------------------------------------------
class TestResearchMethodTypeC1079:
    def _section(self):
        log = _read(ITERATION_LOG)
        start = log.index("## #1079 Type C")
        end = log.index("## #1078 Type B")
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
    def test_max_numeric_mechanism_id_879(self):
        assert max(_corpus_ids()) == M_ID

    def test_zero_880_keys(self):
        # The #1078 file's zero-879 forward guards fail BY DESIGN with this
        # landing (pinned as forward-looking staleness per #1060); the
        # #1080 Type D run pins the zero-880 guards.
        assert NEXT_NUMERIC not in _read(PROFILE)
        assert not _repo_grep(NEXT_US)
        assert not _repo_grep(NEXT_DASH)

    def test_falsification_ledger_holds_36(self):
        b = get_block()
        assert b["falsification_family_member"] is False
        assert "ledger holds at 36" in b["falsification_family"]
        assert "THIRTY-SEVENTH" not in _read(PROFILE)

    def test_no_twentyfourth_relationship_direction(self):
        # Per #715 the absence needle is format-built so the contiguous
        # literal never appears in this file (self-match would fail the
        # sweep); the joined needle must be absent repo-wide.
        needle = "TWENTY-" + "FOURTH relationship direction"
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
        assert "INBOUND-PULL" in novelty
        assert "zero test_type_c_1079 files on disk" in novelty


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

    def test_readme_row_1079(self):
        text = _read(README)
        assert OWN_BASENAME in text
        assert "Type C #1079" in text
        assert "mechanism 879" in text

    def test_arch_row_1079(self):
        text = _read(ARCH)
        assert OWN_BASENAME in text
        assert "Type C #1079" in text

    def test_expected_order_in_docstring(self):
        assert EXPECTED_ORDER == [("C", "1079"), ("B", "1078"), ("A", "1077"),
                                  ("E", "1076"), ("D", "1075")]


# ---------------------------------------------------------------------------
# 10. Iteration-log entry (deselected pre-commit per #719/#721)
# ---------------------------------------------------------------------------
@pytest.mark.itlog
class TestIterationLogEntry:
    def _section(self):
        log = _read(ITERATION_LOG)
        start = log.index("## #1079 Type C")
        end = log.index("## #1078 Type B")
        return log[start:end]

    def test_log_header_present(self):
        log = _read(ITERATION_LOG)
        assert log.count("## #1079 Type C") == 1

    def test_log_contains_mechanism(self):
        section = self._section()
        assert "mechanism 879" in section
        assert "INBOUND-PULL" in section

    def test_log_rotation(self):
        section = self._section()
        assert "1075-1079" in section
        assert "C #1079" in section

    def test_log_carries_commit_hashes_per_721(self):
        section = self._section()
        assert re.search(r"main commit [0-9a-f]{8}", section)
        assert re.search(r"anchor [0-9a-f]{8}", section)

    def test_log_ledger_holds_36(self):
        section = self._section()
        assert "ledger holds at 36" in section


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
        assert " " not in text[start:]

    def test_yaml_file_parses_clean(self):
        import yaml

        yaml.safe_load(_read(PROFILE))
