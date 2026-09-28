"""
Type C #1044: FT Group FY2025 record revenue (GBP566m) - the financial-outcome
leg of the dual-AI-payer portfolio (mechanism 437: OpenAI Apr 2024 + Google
Feb 2026, Meta $0).

FIRST dedicated corpus mechanism on the FY2025 outcome as the financial leg of
the dual-payer portfolio; FIRST denominator audit narrowing the corpus's
"material commercial value" FT wording to contract/relationship materiality
(illustrative ~1.3-2.6% revenue share); FIRST corpus capture of the three-layer
opacity (owner/deal/accounts) that keeps AI-licensing materiality unquantified.

FINANCIAL MAP (verified Sep 27 2026, excerpt-bounded, 0 browser.open per #503):
  Outcome leg: FT Group 2025 revenue GBP566m (+5%), operating profit GBP51.8m
  (+23%), revenue growth every year since 2017 except 2020 (Press Gazette, Sep
  24 2026). Figures: consolidated, UNAUDITED, shared internally, seen by Press
  Gazette. Tenth anniversary of wholly-owned Nikkei ownership (Dec 2015);
  Nikkei publishes no global FT figures. Global paying audience ~3.5M
  (subscribers + 17 specialist brands + FT Live); 3M-by-2028 target already
  passed. Filed UK accounts (FT Ltd, Companies House): revenue GBP477.3m (+5%),
  operating profit GBP18.3m (+151%). Main FT newsbrand 1.62M paying readers
  (1.47M digital), both +9%; FT says now 1.9M. Slade: FT.com >700K habitual
  users, >1M recognised users. A Media Operator (independent relay): paying
  digital AND paying print each +9% YoY; double-digit digital-advertising and
  events growth. Growth path: GBP540m (2024, Slade Sep 10) -> GBP566m (+4.8%).
  Payer legs carried: OpenAI Apr 29 2024 (m54, active throughout FY2025);
  Google Feb 2026 (single-figure GBP M/yr, NDA, no-sue, 90-day exit, m774;
  ZERO months inside FY2025); Meta $0. Combined estimate $10-20M/yr MANUAL
  ILLUSTRATIVE (financial-times.yaml:4373). Geometry: PROSPEROUS-CAPTIVE - the
  restraints bind hardest where the publisher is least pressured; the Google
  leg was added on top of record scale, not rescue. The opacity triad
  (owner/deal/accounts) keeps materiality unquantified from any primary
  document. Temporal precision: FY2025 is a single-payer outcome year; the
  dual overlap only begins FY2026.

Statistical discipline: qualitative financial-incentive mapping; tone
NOT_SCORED; p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant False
(Aug 28 2026 standing rule); engine NOT run; verdict
directionally_supported_not_proven; no_analysis_json_update: true; NOT
artifact-grade; NOT falsification-family member (ledger holds at 34).
Correlation is not causation. Confounders: STRONG excerpt-bounded unaudited
provenance + STRONG subscription/ads/events-driven record + STRONG temporal
mismatch (Google leg signed Feb 2026, zero months in FY2025); MEDIUM
currency-conversion fragility + MEDIUM company-claimed figures; WEAK n=1
outcome year + WEAK seven-year-old opacity-recurrence leg.

Research method: 5 browser.search query sets, 0 browser.open per #503.
REJECTED: Sep-10 Slade Gen-Z interview URL (in corpus via #904/m774,
carried not novel); Guardian GBP282m record (different publisher, no new
mechanism); Nikkei acquisition-anniversary retrospective (no new URL found,
left for a future pass); Companies House direct filing read (not accessed;
figures carried via trade-press relays, stated in certification boundaries).
SELECTED: FT Group FY2025 record-revenue outcome + denominator audit -
dedicated-mechanism gap, 6 zero-hit source URLs, denominator correction of
an existing corpus wording.
Pre-commit novelty sweeps per #715: zero test_type_c_1044 files (glob);
no Type C #1044 in git log; max numeric mechanism_id 857 pre-commit;
zero numeric/underscore/dash 858 keys in profiles/ pre-commit; block key
zero-hit; all 6 source URLs zero-hit repo-wide pre-commit.

Doc-sync post-run: 53539/1368 -> 53585/1369 (+46/+1, venv authoritative).
Concurrency: #899 (nytimes.yaml m771 hunk), #938 (Type B test file anchor
edit), #900 (untracked test), #1012 working-tree edit on the committed
Type A file all stay out of this run's index and diff.

Novelty anchor, rotation-guard, and doc-sync tests fail pre-commit per the
#565/#715/#719/#721 conventions; all green post-doc-sync; anchor patched
in the followup; iteration-log newest-entry green.
46 tests, 11 classes. ASCII only, no em dashes.
"""

import re
import subprocess
from pathlib import Path

import pytest
import yaml

THIS_FILE = "test_type_c_1044_ft_group_fy2025_record_revenue_dual_payer_outcome_leg_sep27_5pm.py"
BLOCK_KEY = "type_c_1044_ft_group_fy2025_record_revenue_dual_payer_outcome_leg_sep27_5pm"
MECHANISM = 858
ITERATION = 1044
ITERATION_TYPE = "C"
EXPECTED_TESTS = 46
# Patched to the real main-commit SHA in the anchor followup per #565.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"
PREDECESSOR_SHAS = {
    "c2c5222c33a545ddc2974fedd962be15ffb6cac6",  # #1043 main
    "dc82a82dfe52e90f5a71b1e24f748f06773fc248",  # #1043 anchor
    "21d11bea28b43e6a75a8ef50bdfd613e4c807947",  # #1043 log-hash
}
NEW_URLS = [
    "https://pressgazette.co.uk/media_business/financial-times-revenue-2025/",
    "https://www.amediaoperator.com/news/financial-times-2025-accounts-print-growth/",
    "https://pressgazette.substack.com/p/future-of-media-awards-2026-winners",
    "https://www.digitalcontentnext.org/blog/executive-officer/jon-slade/",
    "https://pressgazette.co.uk/ft-financial-times-two-thirds-profit-growth-digital-subscription-success/",
    "http://mypresstoday.com/gb/en/post/3181/354402999/who-s-suing-ai-and-who-s-signing-latest-village-media-works-with-openai-but-seattle-times-newsday-but-editorial-perfil-sue.html",
]

REPO = Path(__file__).resolve().parents[1]
TESTS_DIR = REPO / "tests"
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


def _block():
    text = _read(PROFILE)
    start = text.index(BLOCK_KEY + ":")
    return yaml.safe_load(text[start:])[BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1044:
    def test_single_new_test_file_on_disk(self):
        matches = list(TESTS_DIR.glob("test_type_c_1044*"))
        assert len(matches) == 1
        assert matches[0].name == THIS_FILE

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # Fails pre-anchor by design; passes after the anchor followup per
        # #565: the committed test must carry the real main-commit SHA.
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP"
        r = run_git("cat-file", "-t", ANCHORED_SHA)
        assert r.stdout.strip() == "commit"
        r2 = run_git("log", "--format=%s", "-1", ANCHORED_SHA)
        assert "Type C #1044" in r2.stdout

    def test_novelty_first_claim_present(self):
        block = _block()
        novelty = block["novelty"]
        assert "FIRST" in novelty
        assert "denominator audit" in novelty
        assert "opacity" in novelty

    def test_zero_mechanism_id_858_except_this_block(self):
        # Numeric mechanism_id: 858 must be claimed only by this run's block.
        # Needle built by concatenation so this file never self-matches.
        needle = "mechanism_id: " + "858"
        r = run_git("grep", "-n", needle, "--", "profiles/")
        hits = [line for line in r.stdout.splitlines() if line.strip()]
        assert len(hits) == 1
        assert "competitor-entities.yaml" in hits[0]

    def test_no_858_block_keys_repo_wide(self):
        # No zero-indent block key may contain 858 as a mechanism id.
        # Needle built by concatenation so this file never self-matches.
        needle = "^[a-z_0-9]*" + "858" + "[a-z_0-9_]*:"
        r = run_git("grep", "-nE", needle, "--", "profiles/")
        hits = [line for line in r.stdout.splitlines()
                if "mechanism_id" not in line and line.strip()]
        assert hits == []

    def test_new_urls_zero_hit_pre_commit_except_block(self):
        # Each of the 6 new source URLs appears exactly once repo-wide
        # (inside this block). Pre-commit greps per #715 verified zero.
        text = _read(PROFILE)
        for url in NEW_URLS:
            assert text.count(url) == 1, url


# ---------------------------------------------------------------------------
# 2. Rotation guard (1040-1044 window: D -> E -> A -> B -> C)
# ---------------------------------------------------------------------------
class TestRotationGuard1040_1044Window:
    def test_window_legs_in_iteration_log(self):
        log = _read(LOG)
        for leg, itype in [("1040", "D"), ("1041", "E"), ("1042", "A"),
                           ("1043", "B"), ("1044", "C")]:
            assert f"Type {itype} #{leg}" in log, (leg, itype)

    def test_predecessor_shas_in_git_log(self):
        for sha in PREDECESSOR_SHAS:
            r = run_git("cat-file", "-t", sha)
            assert r.stdout.strip() == "commit", sha

    def test_no_type_c_1044_pre_commit(self):
        r = run_git("log", "--oneline", "--grep=Type C #1044")
        # Exactly one hit is this run's main commit; more than one is a dup.
        lines = [l for l in r.stdout.splitlines() if l.strip()]
        assert len(lines) <= 1

    def test_rotation_transparency_names_1040_1044_window(self):
        block = _block()
        rt = block["rotation_transparency"]
        assert "1040-1044 window" in rt
        assert "FIFTH and CLOSING leg" in rt
        assert "next run is #1045 Type D" in rt


# ---------------------------------------------------------------------------
# 3. Mechanism content and identity
# ---------------------------------------------------------------------------
class TestMechanism858Content:
    def test_identity_fields(self):
        block = _block()
        assert block["mechanism_id"] == MECHANISM
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == ITERATION_TYPE
        assert block["type"] == "financial_incentive_mapping"
        assert block["block_key"] == BLOCK_KEY

    def test_key_design_no_numeric_id_substring(self):
        block = _block()
        assert "858" not in block["block_key"]
        assert "no 858 string per #715" in block["key_design_note"]

    def test_verdict_and_grades(self):
        block = _block()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["no_analysis_json_update"] is True
        assert block["artifact_grade"] is False
        assert block["tone_scores"] == "NOT_SCORED"
        assert block["engine_run"] is False

    def test_falsification_ledger_holds_at_34(self):
        block = _block()
        assert block["falsification_ledger"] == 34
        assert block["falsification_family_member"] is False
        assert "THIRTY-FOURTH" in block["falsification_note"]

    def test_excerpt_bounded(self):
        block = _block()
        assert block["excerpt_bounded"] is True
        assert block["browser_opens"] == 0

    def test_six_sources_present(self):
        block = _block()
        assert len(block["sources"]) == 6
        for src in block["sources"]:
            assert src["url"] in NEW_URLS


# ---------------------------------------------------------------------------
# 4. Outcome leg
# ---------------------------------------------------------------------------
class TestOutcomeLeg:
    def test_group_2025_figures(self):
        block = _block()
        leg = block["outcome_leg"]
        assert "GBP566m" in leg["group_2025"]
        assert "GBP51.8m" in leg["group_2025"]
        assert "unaudited" in leg["group_2025"].lower()

    def test_filed_uk_accounts(self):
        block = _block()
        leg = block["outcome_leg"]
        assert "GBP477.3m" in leg["filed_uk_2025"]
        assert "GBP18.3m" in leg["filed_uk_2025"]
        assert "Companies House" in leg["filed_uk_2025"]

    def test_readers_growth(self):
        block = _block()
        leg = block["outcome_leg"]
        assert "1.62M" in leg["readers"]
        assert "1.47M" in leg["readers"]
        assert "+9%" in leg["readers"]

    def test_global_audience_and_growth_path(self):
        block = _block()
        leg = block["outcome_leg"]
        assert "3.5M" in leg["global_audience"]
        assert "GBP540m" in leg["growth_path"]
        assert "GBP566m" in leg["growth_path"]

    def test_owner_opacity(self):
        block = _block()
        leg = block["outcome_leg"]
        assert "Nikkei" in leg["owner"]
        assert "no global" in leg["owner"]

    def test_finding_states_unaudited_provenance(self):
        block = _block()
        assert "UNAUDITED" in block["finding"]
        assert "seen by Press Gazette" in block["finding"]


# ---------------------------------------------------------------------------
# 5. Payer legs carried
# ---------------------------------------------------------------------------
class TestPayerLegsCarried:
    def test_openai_leg_active_throughout_fy2025(self):
        block = _block()
        payer = block["payer_legs_carried"]
        assert "Apr 29 2024" in payer["openai"]
        assert "active throughout FY2025" in payer["openai"]

    def test_google_leg_zero_months_in_fy2025(self):
        block = _block()
        payer = block["payer_legs_carried"]
        assert "Feb 2026" in payer["google"]
        assert "ZERO months inside FY2025" in payer["google"]

    def test_meta_zero(self):
        block = _block()
        payer = block["payer_legs_carried"]
        assert "$0" in payer["meta"]

    def test_combined_estimate_illustrative(self):
        block = _block()
        payer = block["payer_legs_carried"]
        assert "$10-20M/yr" in payer["combined_estimate"]
        assert "ILLUSTRATIVE" in payer["combined_estimate"]

    def test_temporal_precision_in_finding(self):
        block = _block()
        assert "single-payer outcome year" in block["finding"]
        assert "dual overlap only begins FY2026" in block["finding"]


# ---------------------------------------------------------------------------
# 6. Denominator audit geometry
# ---------------------------------------------------------------------------
class TestDenominatorAuditGeometry:
    def test_prosperous_captive_geometry(self):
        block = _block()
        assert "PROSPEROUS-CAPTIVE" in block["geometry"]

    def test_opacity_triad_three_layers(self):
        block = _block()
        geo = block["geometry"]
        assert "owner-level" in geo
        assert "deal-level" in geo
        assert "accounts-level" in geo

    def test_denominator_correction_ratio(self):
        block = _block()
        assert "1.3-2.6%" in block["geometry"]
        assert "contract/relationship materiality" in block["geometry"]

    def test_google_leg_added_on_record_scale(self):
        block = _block()
        assert "on top of record scale" in block["geometry"]

    def test_mechanism_name_states_correction(self):
        block = _block()
        assert "denominator audit" in block["mechanism_name"]


# ---------------------------------------------------------------------------
# 7. Connections
# ---------------------------------------------------------------------------
class TestConnectsTo:
    def test_connects_to_expected(self):
        block = _block()
        assert block["connects_to"] == [437, 774, 54, 487]

    def test_437_is_first_connection(self):
        block = _block()
        assert block["connects_to"][0] == 437


# ---------------------------------------------------------------------------
# 8. Confounders and counterevidence
# ---------------------------------------------------------------------------
class TestConfoundersCounterevidence:
    def test_confounder_strength_tiers(self):
        block = _block()
        strengths = [c["strength"] for c in block["confounders"]]
        assert strengths.count("strong") == 3
        assert strengths.count("medium") == 2
        assert strengths.count("weak") == 2

    def test_temporal_mismatch_confounder(self):
        block = _block()
        texts = " ".join(c["text"] for c in block["confounders"])
        assert "ZERO months of the Google deal" in texts

    def test_strongest_counterargument(self):
        block = _block()
        sca = block["strongest_counterargument"]
        assert "Rorschach" in sca
        assert "Correlation, not causation" in sca

    def test_certification_boundaries(self):
        block = _block()
        assert "Excerpt-bounded per #503" in block["certification_boundaries"]
        assert "zero months of the Google deal" in block["certification_boundaries"]

    def test_coverage_note_no_tone_claim(self):
        block = _block()
        assert "tone NOT_SCORED" in block["coverage_note"]


# ---------------------------------------------------------------------------
# 9. Statistical discipline
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline:
    def test_no_engine_statistics(self):
        block = _block()
        assert block["engine_run"] is False
        assert block["tone_scores"] == "NOT_SCORED"
        assert block["no_analysis_json_update"] is True
        v = block["verification"]
        assert v["max_numeric_mechanism_id_pre_commit"] == 857
        assert v["mechanism_id_claimed"] == 858
        assert v["source_urls_first_appearance"] == 6
        assert v["search_sets"] == 5
        assert v["falsification_ledger_holds_at"] == 34

    def test_expected_test_count(self):
        # Self-count: this file must carry exactly EXPECTED_TESTS tests.
        import ast
        tree = ast.parse(_read(TESTS_DIR / THIS_FILE))
        count = sum(isinstance(n, ast.FunctionDef) and n.name.startswith("test_")
                    for n in ast.walk(tree))
        assert count == EXPECTED_TESTS, count


# ---------------------------------------------------------------------------
# 10. Doc-sync
# ---------------------------------------------------------------------------
class TestDocSync1044:
    def test_readme_stats_updated(self):
        readme = _read(README)
        assert "53585" in readme and "1369" in readme

    def test_readme_table_row(self):
        readme = _read(README)
        assert THIS_FILE in readme

    def test_arch_tree_row(self):
        arch = _read(ARCH)
        assert THIS_FILE in arch

    def test_iteration_log_newest_entry(self):
        log = _read(LOG)
        assert log.lstrip().startswith("## #1044 Type C")


# ---------------------------------------------------------------------------
# 11. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation:
    INFLIGHT = {
        "profiles/nytimes.yaml",
        "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
        "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
        "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",
    }

    def test_staged_set_excludes_inflight(self):
        r = run_git("diff", "--cached", "--name-only")
        staged = {l.strip() for l in r.stdout.splitlines() if l.strip()}
        assert not (staged & self.INFLIGHT), staged & self.INFLIGHT
