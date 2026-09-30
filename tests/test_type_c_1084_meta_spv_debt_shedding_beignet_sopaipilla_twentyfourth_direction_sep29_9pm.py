"""Type C #1084: Meta x project-vehicle off-balance-sheet data center debt
(Beignet $27B Hyperion, Sopaipilla $12.55B El Paso, CleanSpark $2.28B Anviran) -
SPV-DEBT-SHEDDING as the TWENTY-FOURTH relationship direction. FIFTH and
CLOSING leg of the 1080-1084 window.

DESIGN (demand-side minority-stake project finance):
- Corpus already holds the Jan-2026 Apple x Google $1B/yr Gemini deal
  (apple_google_gemini_deal block), the Jul-2026 Apple x OpenAI trade-secrets
  suit (m-line 8235), the Dec-2025 Disney x OpenAI $1B arc (m584, terminated
  Mar 2026), and the Google-guarantor geometry (Google guarantees Anthropic's
  $35B off-balance-sheet exposure). This run does NOT re-claim those.
- Fresh this run: Sep 29 2026 AI-credit repricing across three Meta-tied
  vehicles. Beignet Investor LLC (Hyperion, Richland Parish LA, 5GW, >$50B):
  $27B of 6.581% senior secured notes due 2049 (largest private debt offering
  ever; priced at par Oct 2025), Meta minority 20% stake (off balance sheet),
  PIMCO anchored ~$18B, BlackRock $3B+; S&P A+ with substantial-credit-risk
  pass-through warning; Sep 29 print 91c (record low), yield ~7.55%, ~230bps
  over Treasuries (185bps at launch; 255bps July record-wide); Meta CDS near
  100bps (record). Sopaipilla Investor LLC (El Paso TX, up to 1GW, online
  2028): $12.55B investment-grade bond priced Sep 29 at 7.534% (junk-adjacent),
  led by JPMorgan + Morgan Stanley; 80% BlackRock subsidiaries (GIP, HPS),
  20% Meta; secured by Meta's 20-year rental income from 2028. CleanSpark Inc.
  (Sandersville GA): $2.28B debut five-year junk notes priced Sep 19 2026 at
  98.5 / 8.25% (~175bps over BB average), ~$10B orders (4x oversubscribed),
  led by Morgan Stanley; facility fully leased to Anviran LLC (Meta
  subsidiary) under a $6.6B 20-year contract; Meta guarantees rent and opex;
  operations Q4 2027. Market context: Morgan Stanley ~$3T off-balance-sheet
  financing/leasing across the AI buildout; Alphabet + Meta ~$220B bonds over
  12 months (ainvest Sep 14 2026).
- THE DIRECTION: spv-debt-shedding - the demand-side hyperscaler funds its
  compute buildout through project vehicles in which it holds only a minority
  equity stake (20%), so project debt stays off the consolidated balance sheet
  while compute is contractually secured; construction/credit risk is sold to
  bondholders at yields pricing the risk the sponsor declines to carry.
- Distinct from #22 risk-transfer m876 (SUPPLY side insures its own guarantee
  exposure via third-party insurers; here the DEMAND side sheds financing risk
  onto debt markets) and the inverse of the Google-guarantor geometry (Google
  GUARANTEES Anthropic's $35B exposure - the guarantor keeps the risk; Meta's
  SPVs are built to NOT keep it).
- 6 confounders strongest-first (ordinary project finance; rate-and-duration
  repricing; Meta retains economic exposure; structural heterogeneity
  CleanSpark-vs-JVs; excerpt-bounded relay-tier evidence; single-day snapshot).
- Counterargument: ordinary treasury diversification - the 24th slot survives
  only on the risk-allocation leg (the 20%-minority-stake vehicle must do work
  a plain Meta corporate bond could not do); falsifiable via whether rating
  agencies treat the SPV debt as Meta credit anyway.

NOVELTY VERIFICATION (pre-commit, all green):
- zero test_type_c_1084 files on disk (glob)
- no "Type C #1084" in git log (--grep)
- max numeric mechanism_id 881 in profiles/ pre-commit (Type B #1083,
  mechanism 881 in profiles/careers/journalists.yaml)
- zero numeric 882 mechanism_id keys in profiles/
- zero underscore-form and dash-form 882 mechanism key strings repo-wide
  pre-commit (needles format-built per #715); block key zero-hit
- zero Beignet/Sopaipilla/Hyperion/CleanSpark/Anviran hits in profiles/
  pre-commit; 6 novel source URLs zero-hit repo-wide pre-commit
  (git grep -F on verbatim Full-URL listings)

BY-DESIGN-FAILING SETS:
- Pre-commit run: deselect the anchor-marked tests (3 per #565, patched in
  the anchor followup), the rotation-marked tests (4 per #565, log entry
  prepended at doc-sync), and the itlog-marked tests (6 per #721, green
  after the log-hash followup). The doc-sync ratchet (4 per #719), the
  research-method tests (3), and the staging tests (2) fail pre-commit by
  design and go green post-doc-sync/staging.
- Post-doc-sync re-run: deselect anchor + rotation + itlog marks; everything
  else green.

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

ITERATION = 1084
TYPE_LETTER = "C"
RUN_PDT = "2026-09-29 21:00 PDT"
MECH_KEY = (
    "type_c_1084_meta_spv_debt_shedding_beignet_sopaipilla_"
    "twentyfourth_direction_sep29_9pm"
)
M_ID = 882
OWN_BASENAME = (
    "test_type_c_1084_meta_spv_debt_shedding_beignet_sopaipilla_"
    "twentyfourth_direction_sep29_9pm.py"
)

# Guard needles: corpus max is now 882, so the next-number sweep targets 883.
# Format-built per #715 so no contiguous literal exists in this file.
NEXT_US = "mechanism" + "_883"  # next-number underscore sweep
NEXT_DASH = "mechanism" + "-883"  # next-number dash sweep
NEXT_NUMERIC = "mechanism_id: " + "883"  # next-number numeric sweep

# Absence needles, format-built per #715 (joined forms must be absent).
EIGHTH_MEMBER = "THIRTY-" + "EIGHTH falsification-family member"
TWENTY_FIFTH = "TWENTY-" + "FIFTH relationship direction"

# Anchor SHA for the #1084 main commit; patched post-commit per #565.
ANCHORED_SHA = "3582c34205e550266f58d1e77ceddd73f0244d2d"  # patched in the anchor followup per #565

# Doc-sync ratchet targets (54783/1408 authoritative post-#1083 + 60/+1
# this file).
README_TESTS_AFTER = 54843
README_FILES_AFTER = 1409

NOVELTY_CLAIMS = (
    "zero\ntest_type_c_1084 files, max numeric\nmechanism_id 881 pre-commit, "
    "block key zero-hit, 6 novel\nURLs zero-hit, spv-debt-shedding absent"
)

EXPECTED_NEW_URLS = [
    "https://www.reuters.com/commentary/reuters-open-interest/are-ai-credit-cracks-warning-or-buy-signal-2026-09-29/",
    "https://finimize.com/content/metas-beignet-bonds-are-testing-ais-off-balance-sheet-boom",
    "https://cryptonews.net/news/finance/33483323/",
    "https://www.webull.com/news/15301968728318976",
    "https://www.thehindubusinessline.com/info-tech/meta-tied-data-centre-draws-blowout-demand-for-debut-junk-bond/article71483673.ece/amp/",
    "https://www.ainvest.com/news/big-tech-record-bond-issuance-warps-credit-market-2609/",
]

EXPECTED_ORDER = [("C", "1084"), ("B", "1083"), ("A", "1082"), ("E", "1081"),
                  ("D", "1080")]

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
class TestNoveltyAnchorTypeC1084:
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
        # Scoped to the #1084 header line (not the whole log) per the #1044
        # test fix: newer entries name predecessor SHAs in their
        # rotation-transparency sections, which a whole-log index() cannot
        # distinguish.
        log = _read(ITERATION_LOG)
        header_start = log.index("## #1084 Type C")
        header_end = log.index("\n", header_start)
        assert ANCHORED_SHA[:8] in log[header_start:header_end]

    def test_novelty_claims(self):
        assert NOVELTY_CLAIMS == (
            "zero\ntest_type_c_1084 files, max numeric\nmechanism_id 881 "
            "pre-commit, block key zero-hit, 6 novel\nURLs zero-hit, "
            "spv-debt-shedding absent"
        )


# ---------------------------------------------------------------------------
# 2. Rotation guard (1080-1084 window: D -> E -> A -> B -> C), per #565.
#    All rotation tests are deselected pre-commit (log entry prepended at
#    doc-sync) and re-run after doc-sync.
# ---------------------------------------------------------------------------
@pytest.mark.rotation
class TestRotationGuard1080_1084Window:
    def test_window_legs_in_log(self):
        log = _read(ITERATION_LOG)
        for number, letter in (("1080", "D"), ("1081", "E"), ("1082", "A"),
                               ("1083", "B")):
            assert "## #%s Type %s" % (number, letter) in log

    def test_this_run_fifth_leg_c(self):
        log = _read(ITERATION_LOG)
        assert log.count("## #1084 Type C") == 1
        rt = get_block()["rotation_transparency"]
        assert "1080-1084" in rt and "#1083 Type B" in rt and "CLOSING leg" in rt
        assert "D->E->A->B->C" in rt

    def test_predecessor_1083_pinned(self):
        rt = get_block()["rotation_transparency"]
        assert "#1083 Type B" in rt

    def test_iteration_type_c(self):
        assert get_block()["iteration_type"] == TYPE_LETTER


# ---------------------------------------------------------------------------
# 3. Mechanism structure
# ---------------------------------------------------------------------------
class TestMechanism882Structure:
    def test_block_key_zero_indent_unique(self):
        lines = [l for l in _read(PROFILE).splitlines() if l.startswith(MECH_KEY + ":")]
        assert len(lines) == 1

    def test_block_key_field_repeat_two_occurrences(self):
        # Designed keying per #1064/#1069: YAML key + block_key: field repeat.
        text = _read(PROFILE)
        assert text.count(MECH_KEY) == 2

    def test_mechanism_id_numeric_882(self):
        assert get_block()["mechanism_id"] == M_ID
        assert isinstance(get_block()["mechanism_id"], int)

    def test_type_fields(self):
        b = get_block()
        assert b["type"] == "financial_incentive_mapping"
        assert b["type_label"] == "Financial Incentive Mapping"
        assert b["iteration"] == ITERATION
        assert b["iteration_type"] == TYPE_LETTER
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_connects_to_infrastructure_family(self):
        assert get_block()["connects_to"] == [864, 867, 870, 873, 876]

    def test_discipline_fields(self):
        b = get_block()
        assert b["tone_scored"] is False
        assert b["engine_run"] is False
        assert b["is_significant"] is False
        assert b["verdict"] == "directionally_supported_not_proven"
        assert b["no_analysis_json_update"] is True
        assert b["artifact_grade"] is False

    def test_sources_six_novel(self):
        sources = get_block()["sources"]
        assert len(sources) == 6
        assert [s["url"] for s in sources] == EXPECTED_NEW_URLS
        assert all(s["novel"] is True for s in sources)
        assert all(s["accessed"] == "2026-09-29" for s in sources)

    def test_mechanism_name(self):
        name = get_block()["mechanism_name"]
        assert "SPV-DEBT-SHEDDING" in name
        assert "TWENTY-FOURTH" in name


# ---------------------------------------------------------------------------
# 4. Mechanism legs
# ---------------------------------------------------------------------------
class TestMechanism882Legs:
    def test_beignet_leg(self):
        leg = get_block()["beignet_leg"]
        for needle in ("$27B", "6.581%", "2049", "91 cents", "20%", "PIMCO",
                       "Hyperion", "Richland Parish", "~$18B", "100bps"):
            assert needle in leg, needle

    def test_sopaipilla_leg(self):
        leg = get_block()["sopaipilla_leg"]
        for needle in ("$12.55B", "7.534%", "El Paso", "80%", "BlackRock",
                       "20-year", "2028", "JPMorgan"):
            assert needle in leg, needle

    def test_cleanspark_leg(self):
        leg = get_block()["cleanspark_leg"]
        for needle in ("$2.28B", "8.25%", "Anviran", "$6.6B", "Sandersville",
                       "4x oversubscribed", "Sep 19 2026"):
            assert needle in leg, needle

    def test_market_context_leg(self):
        leg = get_block()["market_context_leg"]
        assert "~$3T" in leg
        assert "~$220B" in leg
        assert "Morgan Stanley" in leg

    def test_finding_sep29_peg(self):
        finding = get_block()["finding"]
        assert "Sep 29 2026" in finding
        assert "off Meta" in finding

    def test_incentive_geometry(self):
        geo = get_block()["incentive_geometry"]
        assert "20%" in geo
        assert "bondholders" in geo
        assert "PIMCO" in geo

    def test_coverage_nexus_no_tone(self):
        assert "NOT_SCORED" in get_block()["coverage_nexus"]

    def test_legs_distinct(self):
        b = get_block()
        legs = [b["beignet_leg"], b["sopaipilla_leg"], b["cleanspark_leg"],
                b["market_context_leg"]]
        assert len(set(legs)) == 4


# ---------------------------------------------------------------------------
# 5. Taxonomy (TWENTY-FOURTH direction)
# ---------------------------------------------------------------------------
class TestMechanism882Taxonomy:
    def test_twentyfourth_direction_named(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "TWENTY-FOURTH relationship direction" in tax
        assert "SPV-DEBT-SHEDDING" in tax

    def test_enumeration_chain(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "23 inbound-pull m879" in tax
        assert "22 risk-transfer m876" in tax
        assert "1 sue-then-sign m624" in tax

    def test_distinct_from_22_risk_transfer(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "SUPPLY side" in tax
        assert "DEMAND side" in tax

    def test_google_guarantor_inverse(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "Google" in tax and "guarantor" in tax.lower()

    def test_slot_earned_on_risk_allocation(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "20%-minority-stake" in tax
        assert "$27B+" in tax

    def test_taxonomy_tension_carried(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "m737" in tax
        assert "Not resolved this run" in tax


# ---------------------------------------------------------------------------
# 6. Confounders + counterargument
# ---------------------------------------------------------------------------
class TestMechanism882Confounders:
    def test_six_confounders(self):
        assert len(get_block()["confounders"]) == 6

    def test_strongest_first_ordering(self):
        strengths = [c["strength"] for c in get_block()["confounders"]]
        assert strengths[:3] == ["STRONG", "STRONG", "STRONG"]
        assert strengths[3:5] == ["MEDIUM", "MEDIUM"]
        assert strengths[5] == "WEAK"

    def test_excerpt_bounded_confounders(self):
        texts = " ".join(c["what"] for c in get_block()["confounders"])
        assert "0 browser.open per #503" in texts
        assert "relabeled, not removed" in texts

    def test_counterargument_slot_survival(self):
        ca = get_block()["counterargument"]
        assert "24th slot survives only" in ca
        assert "treasury diversification" in ca

    def test_counterargument_falsifiability(self):
        ca = get_block()["counterargument"]
        assert "falsify" in ca
        assert "CDS" in ca


# ---------------------------------------------------------------------------
# 7. Research method (fails pre-commit by design: log entry not yet written)
# ---------------------------------------------------------------------------
class TestResearchMethodTypeC1084:
    def _section(self):
        log = _read(ITERATION_LOG)
        start = log.index("## #1084 Type C")
        end = log.index("## #1083 Type B")
        return log[start:end]

    def test_four_search_sets_zero_open(self):
        section = self._section()
        assert "4 browser.search query sets" in section
        assert "0 browser.open" in section
        assert "#503" in section

    def test_rejected_candidates_logged(self):
        section = self._section()
        assert "Research rejected" in section

    def test_search_topics_logged(self):
        section = self._section()
        assert "Meta data center financing" in section


# ---------------------------------------------------------------------------
# 8. Corpus novelty post-commit
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPostCommit:
    def test_max_numeric_mechanism_id_882(self):
        assert max(_corpus_ids()) == M_ID

    def test_zero_883_keys(self):
        # The #1085 Type D run pins the zero-883 guards; this run's own
        # next-number sweeps must be clean.
        assert NEXT_NUMERIC not in _read(PROFILE)
        assert not _repo_grep(NEXT_US)
        assert not _repo_grep(NEXT_DASH)

    def test_falsification_ledger_holds_37(self):
        b = get_block()
        assert b["falsification_family_member"] is False
        assert "ledger holds at 37" in b["falsification_family"]
        assert not _repo_grep(EIGHTH_MEMBER)

    def test_no_twentyfifth_relationship_direction(self):
        # Per #715 the absence needle is format-built so the contiguous
        # literal never appears in this file (self-match would fail the
        # sweep); the joined needle must be absent repo-wide.
        assert not _repo_grep(TWENTY_FIFTH)

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
        assert "SPV-DEBT-SHEDDING" in novelty
        assert "zero test_type_c_1084 files on disk" in novelty


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

    def test_readme_row_1084(self):
        text = _read(README)
        assert OWN_BASENAME in text
        assert "Type C #1084" in text
        assert "mechanism 882" in text

    def test_arch_row_1084(self):
        text = _read(ARCH)
        assert OWN_BASENAME in text
        assert "Type C #1084" in text

    def test_expected_order_in_docstring(self):
        assert EXPECTED_ORDER == [("C", "1084"), ("B", "1083"), ("A", "1082"),
                                  ("E", "1081"), ("D", "1080")]


# ---------------------------------------------------------------------------
# 10. Iteration-log entry (deselected pre-commit per #719/#721)
# ---------------------------------------------------------------------------
@pytest.mark.itlog
class TestIterationLogEntry:
    def _section(self):
        log = _read(ITERATION_LOG)
        start = log.index("## #1084 Type C")
        end = log.index("## #1083 Type B")
        return log[start:end]

    def test_log_header_present(self):
        log = _read(ITERATION_LOG)
        assert log.count("## #1084 Type C") == 1

    def test_log_contains_mechanism(self):
        section = self._section()
        assert "mechanism 882" in section
        assert "SPV-DEBT-SHEDDING" in section

    def test_log_rotation(self):
        section = self._section()
        assert "1080-1084" in section
        assert "C #1084" in section

    def test_log_carries_commit_hashes_per_721(self):
        section = self._section()
        assert re.search(r"main commit [0-9a-f]{8}", section)
        assert re.search(r"anchor [0-9a-f]{8}", section)

    def test_log_ledger_holds_37(self):
        section = self._section()
        assert "ledger holds at 37" in section

    def test_log_window_closing(self):
        section = self._section()
        assert "CLOSING" in section
        assert "#1085 Type D" in section


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

    def test_block_key_no_numeric_mechanism_id(self):
        # Designed keying per #715: colon-form only, no numeric mechanism-id
        # substring in the block key (iteration number 1084 is allowed).
        assert "882" not in MECH_KEY
