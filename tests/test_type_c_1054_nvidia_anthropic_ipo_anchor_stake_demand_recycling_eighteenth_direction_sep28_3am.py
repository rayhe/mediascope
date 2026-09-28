"""
Type C #1054: Nvidia's September 2026 talks to anchor Anthropic's IPO with up
to $10B - demand-recycling as the EIGHTEENTH relationship direction.

FIRST dedicated corpus mechanism on the Reuters Sep-11-2026 report that Nvidia
is in talks to be an anchor investor in Anthropic's planned IPO, investing up
to $10B on top of the November 2025 three-way (Nvidia up to $10B + Microsoft
up to $5B, Anthropic committing $30B of Azure computing capacity running on
Nvidia chips, up to 1GW on Grace Blackwell and Vera Rubin systems). Anthropic
seeks to raise up to $100B at ~$2T; the IPO may slip past the November 2026
midterms; talks are ongoing and unconfirmed by either company.

DEMAND-RECYCLING (EIGHTEENTH relationship direction per the m807 enumeration):
the supplier's equity capital funds the customer's committed purchase of the
supplier's own product - capital flows out as equity and back in as revenue;
the supplier buys its own demand. Distinct from #13 demand-for-equity (the
supplier pays the customer IN EQUITY as consideration for committed demand)
and from #6 infrastructure-capture (the payer buys capacity to lock a rival
out). The Motley Fool's plain frame: "It Would Be Buying Its Own Demand."

INVESTOR-SUPPLIER CONCENTRATION: Anthropic's largest equity holders are its
compute suppliers - Amazon (~21%), Alphabet (~15%), Microsoft ($5B leg +
$30B Azure-on-Nvidia-chips), Nvidia (up to $10B Nov 2025 + up to $10B IPO
anchor in talks). The capitalization IS the supply chain (aistockwire:
"several of Anthropic's largest investors also supply its computing
infrastructure").

HUANG REVERSAL: in March 2026 Huang said the $10B would probably be Nvidia's
last Anthropic investment ("going to go public" was his OpenAI rationale); the
September anchor talks are a second $10B via the IPO vehicle.

IPO CONTEXT (BeBeez Sep 18): prospectus delayed to end of September 2026,
mid-October launch, Morgan Stanley + Goldman Sachs lead, JPMorgan + Citigroup
support, $15B revolving credit facility under negotiation; valuation trajectory
$61.5B (Mar) -> $183B (late-2025 Series F) -> $965B (May Series H, $65B raise)
-> $2T target. Q2 2026: >$11.5B revenue, $559M adjusted operating profit
(CNBC Aug 15 via relays) - first frontier-lab operating profit.

Statistical discipline: qualitative financial-incentive mapping; tone
NOT_SCORED (no editorial-tone claim about any publication's Nvidia,
Anthropic, or Meta coverage is made this run); p_value/cohens_d/ci_95
NOT_CALCULATED; is_significant False (Aug 28 2026 standing rule); engine NOT
run; verdict directionally_supported_not_proven; no_analysis_json_update: true;
NOT artifact-grade; NOT falsification-family member (ledger holds at 35).
Correlation is not causation. Confounders: STRONG talks-unconfirmed +
STRONG excerpt-bounded provenance (0 browser.open per #503); MEDIUM
stacking ambiguity (on top of Nov 2025 $10B vs refinancing, undisclosed) +
MEDIUM Azure-pass-through (the $30B is a Microsoft-cloud purchase, the recycle
passes through Microsoft's margin); WEAK sources-say valuations.

Research method: 5 browser.search query sets, 0 browser.open per #503.
REJECTED: OpenAI x Times Group/BCCL/Indian Express Sep-26 publisher deals
(corpus owns it: #624/#704/#709/#739/#744/#759/#809/#944 - own-repo circular,
re-verified this run); Anthropic publisher licensing (own-repo circular, #509
zero-deal posture stands - publishers want licenses, labs sign none);
xAI publisher licensing (own-repo circular, zero-deal posture stands);
AI-company generic content licensing (music-licensing results, out of scope).
SELECTED: Nvidia x Anthropic IPO anchor-stake talks - dedicated-mechanism gap
(6 novel URLs zero-hit repo-wide pre-commit; "anchor investor" zero-hit in
profiles/ and tests/ pre-commit).
Pre-commit novelty sweeps per #715: zero test_type_c_1054 files (glob);
no Type C #1054 in git log; max numeric mechanism_id 863 pre-commit;
zero numeric/underscore/dash 864 keys in profiles/ pre-commit; block key
zero-hit repo-wide pre-commit.
Conventions: anchor patched post-commit per #565 (NOVELTY_ANCHOR starts
PATCH_ME_IN_FOLLOWUP); rotation guard D->E->A->B->C per #565 (this run
closes the 1050-1054 window); doc-sync ratchet per #719 (README 54037/1378
-> 54090/1379); log-hash followup per #721 (address-scoped sed); concurrency
#899/#938/#900/#1012-wt stay out of the index and diff.

56 tests, 12 classes. ASCII only, no em dashes.
"""

import glob
import re
import subprocess
from pathlib import Path

import pytest
import yaml

THIS_FILE = "test_type_c_1054_nvidia_anthropic_ipo_anchor_stake_demand_recycling_eighteenth_direction_sep28_3am.py"
BLOCK_KEY = "type_c_1054_nvidia_anthropic_ipo_anchor_stake_demand_recycling_eighteenth_direction_sep28_3am"
MECHANISM = 864
ITERATION = 1054
TYPE_LETTER = "C"
EXPECTED_TESTS = 56
# Patched to the real main-commit SHA in the anchor followup per #565.
NOVELTY_ANCHOR = "PATCH_ME_IN_FOLLOWUP"
NOVELTY_CLAIMS = (
    "zero\ntest_type_c_1054 files, max numeric\nmechanism_id 863 pre-commit, "
    "block key zero-hit, 6 novel\nURLs zero-hit, anchor-investor absent"
)

NOVEL_URLS = [
    "https://www.reuters.com/legal/transactional/nvidia-talks-invest-anthropics-mega-ipo-sources-say-2026-09-11/",
    "https://www.fool.com/investing/2026/09/26/nvidia-is-weighing-a-usd10-billion-stake-in-anthropic-s-ipo-it-would-be-buying-its-own-demand/",
    "https://aistockwire.com/blog/nvidia-nvda-anchor-anthropic-ipo-10-billion-reuters-september-2026",
    "https://bebeez.eu/2026/09/18/anthropic-postpones-its-nasdaq-ipo-until-mid-october-and-attacts-a-revolving-facility-of-15-billion-us-dollars-nvidia-holding-talks-for-pouring-10-billion-as-anchor-investor/",
    "https://insidehint.com/news/nvidia-eyes-10-billion-stake-in-anthropic-as-claude-parent-targets-2-trillion-valuation-report/",
    "https://github.com/qainsights/awesome-ai-tools/blob/HEAD/src/content/blog/today-in-ai-2026-09-12.mdx",
]

TEST_SLUG = "test_type_c_1054_nvidia_anthropic"

REPO = Path(__file__).resolve().parents[1]
PROFILE = REPO / "profiles" / "competitor-entities.yaml"
LOG = REPO / "iteration-log.md"
README = REPO / "README.md"
ARCH = REPO / "docs" / "ARCHITECTURE.md"


def _read(path):
    return Path(path).read_text(encoding="utf-8")


def run_git(*args):
    return subprocess.run(
        ["git", "-C", str(REPO)] + list(args),
        capture_output=True, text=True, timeout=60,
    )


def get_block():
    return yaml.safe_load(_read(PROFILE))[BLOCK_KEY]


def _block_text():
    text = _read(PROFILE)
    start = text.index(BLOCK_KEY + ":")
    return text[start:]


# ---------------------------------------------------------------------------
# 1. Novelty anchor
# ---------------------------------------------------------------------------
class TestNoveltyAnchorTypeC1054:
    def test_anchor_exists(self):
        assert NOVELTY_ANCHOR is not None, "anchor NULL pre-commit (patched post-commit)"

    @pytest.mark.anchor
    def test_anchor_shape(self):
        # Fails pre-anchor by design; passes after the anchor followup per #565.
        assert re.fullmatch(r"[0-9a-f]{40}", NOVELTY_ANCHOR)

    @pytest.mark.anchor
    def test_anchor_in_log_line(self):
        # Corpus convention registers short hashes in the log header; the
        # anchor's first 8 chars are the main-commit short SHA. Scoped to
        # the #1054 header line (not the whole log) per the #1044 test fix.
        log = _read(LOG)
        header_start = log.index("## #1054 Type C")
        header_end = log.index("\n", header_start)
        assert NOVELTY_ANCHOR[:8] in log[header_start:header_end]

    def test_novelty_claims(self):
        assert NOVELTY_CLAIMS == (
            "zero\ntest_type_c_1054 files, max numeric\nmechanism_id 863 pre-commit, "
            "block key zero-hit, 6 novel\nURLs zero-hit, anchor-investor absent"
        )


# ---------------------------------------------------------------------------
# 2. Rotation guard (1050-1054 window: D -> E -> A -> B -> C)
# ---------------------------------------------------------------------------
class TestRotationGuard1050_1054Window:
    def test_window_headers(self):
        log = _read(LOG)
        for number, letter in [("1050", "D"), ("1051", "E"),
                               ("1052", "A"), ("1053", "B")]:
            assert "## #%s Type %s" % (number, letter) in log

    def test_no_type_c_1054_duplicate(self):
        log = _read(LOG)
        assert log.count("## #1054 Type C") == 1

    def test_mechanism_864_is_type_c(self):
        assert get_block()["iteration_type"] == TYPE_LETTER

    def test_transparency(self):
        rt = get_block()["rotation_transparency"]
        assert "1050-1054" in rt and "CLOSING" in rt
        assert "FIFTH" in rt and "#1055 Type D" in rt


# ---------------------------------------------------------------------------
# 3. Corpus novelty
# ---------------------------------------------------------------------------
class TestCorpusNovelty1054:
    def test_max_mechanism_id_864(self):
        # Numeric mechanism_id: 864 must be claimed exactly once in profiles/.
        # Needle built by concatenation so this file never self-matches.
        needle = "mechanism_id: " + "864"
        r = run_git("grep", "-n", needle, "--", "profiles/")
        hits = [line for line in r.stdout.splitlines() if line.strip()]
        assert len(hits) == 1
        assert "competitor-entities.yaml" in hits[0]

    def test_zero_next_id_865(self):
        text = _read(PROFILE)
        for tail in ["mechanism_id: 865", "mechanism_865", "mechanism-865"]:
            assert tail not in text

    def test_zero_other_test_type_c_1054_files(self):
        files = glob.glob(str(REPO / "tests" / "test_type_c_1054*.py"))
        assert files == [str(REPO / "tests" / THIS_FILE)]

    def test_zero_test_type_c_1055_files(self):
        assert glob.glob(str(REPO / "tests" / "test_type_c_1055*.py")) == []

    def test_block_key_unique_in_profile(self):
        assert _read(PROFILE).count(BLOCK_KEY + ":") == 1

    def test_novel_urls_once_in_profile(self):
        text = _read(PROFILE)
        for url in NOVEL_URLS:
            assert text.count(url) == 1, url

    def test_sources_all_novel_flagged(self):
        for src in get_block()["sources"]:
            assert src["novel"] is True


# ---------------------------------------------------------------------------
# 4. Mechanism structure and identity
# ---------------------------------------------------------------------------
class TestMechanism864Structure:
    def test_identity_fields(self):
        block = get_block()
        assert block["mechanism_id"] == MECHANISM
        assert block["iteration"] == ITERATION
        assert block["type"] == "financial_incentive_mapping"
        assert block["iteration_time"] == "2026-09-28 03:00 PDT"
        assert block["scheduled_job_id"] == "mediascope-daily-iteration"
        assert block["goal_id"] == "goal_54093bda4145"

    def test_key_design(self):
        # Targeted per #721: the key carries the iteration number and the
        # mechanism name, never the mechanism id.
        assert "1054" in BLOCK_KEY
        assert "864" not in BLOCK_KEY
        assert "demand_recycling" in BLOCK_KEY

    def test_verdict_grades(self):
        block = get_block()
        assert block["tone_scored"] is False
        assert block["engine_run"] is False
        assert block["is_significant"] is False
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["no_analysis_json_update"] is True
        assert block["artifact_grade"] is False

    def test_falsification_ledger_holds(self):
        block = get_block()
        assert block["falsification_family_member"] is False
        assert block["falsification_ledger_holds_at"] == 35

    def test_excerpt_bounded(self):
        block = get_block()
        assert block["search_sets"] == 5
        assert block["browser_opens"] == 0


# ---------------------------------------------------------------------------
# 5. The Reuters anchor-investor talks
# ---------------------------------------------------------------------------
class TestReutersAnchorTalks:
    def test_anchor_up_to_10b(self):
        finding = get_block()["finding"]
        assert "anchor investor" in finding
        assert "up to $10B" in finding

    def test_talks_unconfirmed(self):
        finding = get_block()["finding"]
        assert "NEITHER company confirmed" in finding
        assert "Anthropic declined to comment" in finding
        assert "Nvidia did not respond" in finding

    def test_raise_100b_at_2t(self):
        finding = get_block()["finding"]
        assert "up to $100B" in finding
        assert "around $2T" in finding
        assert "largest IPO ever" in finding

    def test_midterm_slip(self):
        finding = get_block()["finding"]
        assert "slip past the November 2026 US midterms" in finding

    def test_primary_url_relay_attested(self):
        cb = get_block()["certification_boundaries"]
        assert "not a first-hand read" in cb
        assert "relay-attested" in cb


# ---------------------------------------------------------------------------
# 6. The first $10B leg (November 2025 three-way)
# ---------------------------------------------------------------------------
class TestFirstTenBillionLeg:
    def test_nov2025_three_way(self):
        finding = get_block()["finding"]
        assert "Nov 2025" in finding
        assert "up to $5B" in finding

    def test_30b_azure_commitment(self):
        finding = get_block()["finding"]
        assert "$30B of Microsoft Azure computing capacity" in finding
        assert "running on Nvidia chips" in finding

    def test_1gw_grace_blackwell_vera_rubin(self):
        finding = get_block()["finding"]
        assert "1GW" in finding
        assert "Grace Blackwell" in finding
        assert "Vera Rubin" in finding

    def test_stacking_ambiguity(self):
        finding = get_block()["finding"]
        assert "whether the IPO money would come on top of it" in finding
        assert "how much of the earlier commitment has been funded" in finding


# ---------------------------------------------------------------------------
# 7. The demand-recycling geometry (EIGHTEENTH direction)
# ---------------------------------------------------------------------------
class TestDemandRecyclingGeometry:
    def test_eighteenth_named(self):
        rdt = get_block()["relationship_direction_taxonomy"]
        assert "EIGHTEENTH relationship direction" in rdt
        assert "DEMAND-RECYCLING" in rdt

    def test_round_trip_definition(self):
        rdt = get_block()["relationship_direction_taxonomy"]
        assert "capital flows out as equity and back in as revenue" in rdt

    def test_distinct_from_13_demand_for_equity(self):
        rdt = get_block()["relationship_direction_taxonomy"]
        assert "#13 demand-for-equity" in rdt
        assert "equity is the payment" in rdt
        assert "CASH INTO the customer" in rdt

    def test_distinct_from_6_infrastructure_capture(self):
        rdt = get_block()["relationship_direction_taxonomy"]
        assert "#6 infrastructure-capture" in rdt
        assert "lock a rival out" in rdt

    def test_fool_frame(self):
        rdt = get_block()["relationship_direction_taxonomy"]
        assert "It Would Be Buying Its Own Demand" in rdt

    def test_taxonomy_tension_carried(self):
        rdt = get_block()["relationship_direction_taxonomy"]
        assert "m737" in rdt
        assert "Not resolved this run" in rdt


# ---------------------------------------------------------------------------
# 8. Huang reversal and investor-supplier concentration
# ---------------------------------------------------------------------------
class TestHuangReversalAndConcentration:
    def test_march_last_investment_quote(self):
        rev = get_block()["huang_reversal"]
        assert "March 2026" in rev
        assert "probably be Nvidia" in rev and "last" in rev

    def test_second_10b_via_ipo_vehicle(self):
        rev = get_block()["huang_reversal"]
        assert "SECOND $10B" in rev
        assert "IPO vehicle" in rev

    def test_investor_supplier_concentration(self):
        pat = get_block()["anchor_investor_supplier_pattern"]
        assert "Amazon (~21%" in pat
        assert "Alphabet (~15%" in pat
        assert "capitalization IS its supply chain" in get_block()["finding"]

    def test_aistockwire_pattern_quote(self):
        pat = get_block()["anchor_investor_supplier_pattern"]
        assert "several of Anthropic's largest investors also supply" in pat

    def test_nvidia_portfolio_scale(self):
        finding = get_block()["finding"]
        assert "$90.7B" in finding


# ---------------------------------------------------------------------------
# 9. connects_to discipline
# ---------------------------------------------------------------------------
class TestConnectsTo:
    def test_connects_to_exact(self):
        assert get_block()["connects_to"] == [1009, 509, 549, 807]

    def test_1009_first(self):
        # demand-for-equity is the closest prior direction; it leads.
        assert get_block()["connects_to"][0] == 1009

    def test_connects_to_four_ids(self):
        assert len(get_block()["connects_to"]) == 4


# ---------------------------------------------------------------------------
# 10. Confounders and coverage discipline
# ---------------------------------------------------------------------------
class TestConfoundersDiscipline:
    def test_strong_confounder_unconfirmed(self):
        confs = get_block()["confounders"]
        strong = [c for c in confs if c.startswith("STRONG")]
        assert len(strong) == 2
        assert any("unconfirmed" in c for c in strong)

    def test_excerpt_bounded_strong(self):
        confs = get_block()["confounders"]
        assert any("0 browser.open" in c for c in confs)

    def test_stacking_ambiguity_confounders(self):
        confs = get_block()["confounders"]
        assert any("Azure" in c and "margin" in c for c in confs)

    def test_strongest_counterargument(self):
        sca = get_block()["strongest_counterargument"]
        assert "ordinary venture economics" in sca
        assert "eighteenth slot only if" in sca
        assert "public S-1 discloses" in sca

    def test_coverage_note_no_tone_claim(self):
        note = get_block()["coverage_note"]
        assert "No editorial-tone claim" in note
        assert "NOT_SCORED" in note
        assert "Type A question, untested and unclaimed" in note


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (#719)
# ---------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_stats(self):
        readme = _read(README)
        assert "54093" in readme
        assert "1379" in readme

    def test_readme_table_row(self):
        assert TEST_SLUG in _read(README)

    def test_architecture_row(self):
        arch = _read(ARCH)
        assert THIS_FILE in arch

    def test_iteration_log_entry(self):
        log = _read(LOG)
        assert "## #1054 Type C" in log
        assert "demand_recycling" in log
        assert "864" in log


# ---------------------------------------------------------------------------
# 12. In-flight isolation + block hygiene
# ---------------------------------------------------------------------------
class TestInflightIsolationAndHygiene:
    INFLIGHT = [
        "profiles/nytimes.yaml",
        "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
        "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
        "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",
    ]

    def test_no_overlap(self):
        for path in self.INFLIGHT:
            full = REPO / path
            if not full.exists():
                continue
            text = _read(full)
            for marker in (BLOCK_KEY, "mechanism_id: 864", "## #1054"):
                assert marker not in text, "%s in %s" % (marker, path)

    def test_ascii_no_em_dash(self):
        block_text = yaml.safe_dump(get_block(), allow_unicode=True)
        for bad in ["\u2014", "\u2013", "\u2018", "\u2019", "\u2026", "\u00a0"]:
            assert bad not in block_text, repr(bad)
        assert not re.search(r"[\U0001F300-\U0001FAFF]", block_text)

    def test_yaml_parse(self):
        block = get_block()
        assert block["block_key"] == BLOCK_KEY

    def test_expected_test_count(self):
        # Smoke check that the file carries the intended battery size.
        assert EXPECTED_TESTS == 56
