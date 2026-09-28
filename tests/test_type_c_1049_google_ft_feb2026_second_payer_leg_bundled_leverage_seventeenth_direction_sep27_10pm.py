"""
Type C #1049: Google x FT February 2026 AI licensing deal - the second-payer
leg term audit of the FT dual-AI-payer portfolio (m437: OpenAI Apr 2024 +
Google Feb 2026, Meta $0).

FIRST dedicated corpus mechanism on the BUNDLED-LEVERAGE geometry (the
Showcase-mutation): Google re-platformed pre-existing News Showcase revenue
lines (hundreds of thousands to millions of pounds per year, built into
publishers' annual plans) into AI licensing deals, so declining the new
terms risks the legacy Showcase check at the framework's sunset - the
publisher BATNA is the scheduled loss of an existing revenue check, not
litigation. SEVENTEENTH relationship direction per the m807 enumeration.

FIRST AI Contribution Pilot disambiguation in the corpus: the usage-based,
no-upfront-fee, invitation-only pilot (Search Console widget payouts, "peanuts"
per participants) is a SEPARATE track from the FT/Guardian/WaPo focused cash
deals - the second-payer leg is the focused deal, not the pilot.

FIRST dual-leg restraint-template replication: the OpenAI leg (Apr 2024,
$5-10M/yr secondary estimate) and the Google leg (Feb 2026, single-figure
millions/yr) carry the SAME restraint template (NDA + no-sue + 90-day exit +
publisher kill-switch); combined $10-20M/yr MANUAL ILLUSTRATIVE, consistent
with the #1044 denominator narrowing (~1.3-2.6% of the GBP566m FY2025 base).

FINANCIAL MAP (verified Sep 27 2026, excerpt-bounded, 0 browser.open per #503):
  Announcement: FT CEO Jon Slade announced at the FT Strategies "News in the
  Digital Age" conference (Feb 11 2026) that Google and FT signed a deal
  licensing FT journalism into AI pilot projects (Talking Biz News relay of
  Press Gazette's Charlotte Tobitt, carried from m437; re-attested via the
  archynewsy Press Gazette mirror, NOVEL URL).
  Terms (Press Gazette Aug 4 2026, carried from m437): two-year term;
  Guardian and FT signed, earning single-figure millions per year;
  take-it-or-leave-it terms; NDAs and no-sue clauses; 90-day exit;
  believed cash payments + extended display rights + API delivery.
  Bundled leverage (Press Gazette newsletter Aug 4 2026, NOVEL): Showcase
  revenue mutated into AI deals; declining means the binary choice of
  signing or losing the Showcase check at the legacy framework sunset
  (androidheadlines Jul 2026, carried); publishers sign away AI opt-out
  rights plus agree not to sue or talk publicly (except jointly agreed
  release); the CMA opt-out ruling is mooted by the mutation.
  Pilot track (Remote Work Europe Sep 2026, NOVEL; LinkedIn analysis, NOVEL):
  usage-based, no upfront fee, exitable anytime, invitation-only; Search
  Console AI-earnings widget; "peanuts" and "quite black box" per
  participants; NOT the FT focused deal.
  Slade Sep 17 2026 (carried via #904/m774): both deals carry the big red
  button, quote-amount controls, clear source references; FT in no legal
  actions against AI companies; Ask FT engine.

Statistical discipline: qualitative financial-incentive mapping; tone
NOT_SCORED; p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant False
(Aug 28 2026 standing rule); engine NOT run; verdict
directionally_supported_not_proven; no_analysis_json_update: true; NOT
artifact-grade; NOT falsification-family member (ledger holds at 35).
Correlation is not causation. Confounders: STRONG single-outlet Press
Gazette dependence + STRONG excerpt-bounded provenance; MEDIUM
Showcase-bundling inference + MEDIUM temporal (Aug-2026 reporting of Feb-2026
deals); WEAK LinkedIn newsletter provenance.

Research method: 4 browser.search query sets, 0 browser.open per #503.
REJECTED: Anthropic IPO underwriter/research-conflict mapping (strong Type C
material, but off the FT dual-payer portfolio this run - deferred); Companies
House direct filing read (not accessed; figures carried via trade-press
relays); Google official aboutamazon-style announcement read (not fetched,
excerpt-bounded per #503).
SELECTED: Google x FT second-payer leg term audit - dedicated-mechanism gap
(4 novel + 4 carried URLs; m437 held only the focused-deal facts, not the
bundled-leverage geometry, the pilot disambiguation, or the restraint
replication).
Pre-commit novelty sweeps per #715: zero test_type_c_1049 files (glob);
no Type C #1049 in git log; max numeric mechanism_id 860 pre-commit;
zero numeric/underscore/dash 861 keys in profiles/ pre-commit; block key
zero-hit; 4 novel URLs zero-hit repo-wide pre-commit (format-built needles);
4 carried URLs already in corpus via m437/#904.
Conventions: anchor patched post-commit per #565 (NOVELTY_ANCHOR starts
PATCH_ME_IN_FOLLOWUP); rotation guard D->E->A->B->C per #565 (this run
closes the 1045-1049 window); doc-sync ratchet per #719 (README 53780/1373
-> 53826/1374); log-hash followup per #721 (address-scoped sed); concurrency
#899/#938/#900/#1012-wt stay out of the index and diff.

46 tests, 12 classes. ASCII only, no em dashes.
"""

import glob
import re
import subprocess
from pathlib import Path

import pytest
import yaml

THIS_FILE = "test_type_c_1049_google_ft_feb2026_second_payer_leg_bundled_leverage_seventeenth_direction_sep27_10pm.py"
BLOCK_KEY = "type_c_1049_google_ft_feb2026_second_payer_leg_bundled_leverage_seventeenth_direction_sep27_10pm"
MECHANISM = 861
ITERATION = 1049
TYPE_LETTER = "C"
EXPECTED_TESTS = 46
# Patched to the real main-commit SHA in the anchor followup per #565.
NOVELTY_ANCHOR = "PATCH_ME_IN_FOLLOWUP"
NOVELTY_CLAIMS = (
    "zero\ntest_type_c_1049 files, max numeric\nmechanism_id 860 pre-commit, "
    "block key zero-hit, 4 novel\nURLs zero-hit, 4 carried"
)

NOVEL_URLS = [
    "https://www.archynewsy.com/google-ai-news-publishers-can-opt-out-more-deals-planned-press-gazette/",
    "https://pressgazette.substack.com/p/the-prisoners-dilemma-why-uk-publishers",
    "https://remoteworkeurope.eu/news/2026/google-pay-per-use-ai-licensing-publishers/",
    "https://www.linkedin.com/pulse/google-quietly-paying-publishers-ai-content-heres-why-mg6ef",
]
CARRIED_URLS = [
    "https://talkingbiznews.com/media-news/ft-signs-ai-deal-with-google/",
    "https://pressgazette.co.uk/news/google-ai-deals-uk-publishers/",
    "https://pressgazette.co.uk/publishers/nationals/ft-chief-jon-slade-on-how-business-brand-became-a-hit-with-gen-z/",
    "https://www.androidheadlines.com/2026/07/google-forces-publishers-ai-training-rights-news-showcase.html",
]

TEST_SLUG = "test_type_c_1049_google_ft"

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
class TestNoveltyAnchorTypeC1049:
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
        # the #1049 header line (not the whole log) per the #1044 test fix.
        log = _read(LOG)
        header_start = log.index("## #1049 Type C")
        header_end = log.index("\n", header_start)
        assert NOVELTY_ANCHOR[:8] in log[header_start:header_end]

    def test_novelty_claims(self):
        assert NOVELTY_CLAIMS == (
            "zero\ntest_type_c_1049 files, max numeric\nmechanism_id 860 pre-commit, "
            "block key zero-hit, 4 novel\nURLs zero-hit, 4 carried"
        )


# ---------------------------------------------------------------------------
# 2. Rotation guard (1045-1049 window: D -> E -> A -> B -> C)
# ---------------------------------------------------------------------------
class TestRotationGuard1045_1049Window:
    def test_window_headers(self):
        log = _read(LOG)
        for number, letter in [("1045", "D"), ("1046", "E"),
                               ("1047", "A"), ("1048", "B")]:
            assert "## #%s Type %s" % (number, letter) in log

    def test_no_type_c_1049_duplicate(self):
        log = _read(LOG)
        assert log.count("## #1049 Type C") == 1

    def test_mechanism_861_is_type_c(self):
        assert get_block()["iteration_type"] == TYPE_LETTER

    def test_transparency(self):
        rt = get_block()["rotation_transparency"]
        assert "1045-1049" in rt and "C #1049" in rt
        assert "FIFTH and CLOSING" in rt and "#1050 Type D" in rt


# ---------------------------------------------------------------------------
# 3. Corpus novelty
# ---------------------------------------------------------------------------
class TestCorpusNovelty1049:
    def test_max_mechanism_id_861(self):
        # Numeric mechanism_id: 861 must be claimed exactly once in profiles/.
        # Needle built by concatenation so this file never self-matches.
        needle = "mechanism_id: " + "861"
        r = run_git("grep", "-n", needle, "--", "profiles/")
        hits = [line for line in r.stdout.splitlines() if line.strip()]
        assert len(hits) == 1
        assert "competitor-entities.yaml" in hits[0]

    def test_zero_next_id_862(self):
        text = _read(PROFILE)
        for tail in ["mechanism_id: 862", "mechanism_862", "mechanism-862"]:
            assert tail not in text

    def test_zero_test_type_c_1050_files(self):
        assert glob.glob(str(REPO / "tests" / "test_type_c_1050*.py")) == []

    def test_block_key_unique_in_profile(self):
        assert _read(PROFILE).count(BLOCK_KEY + ":") == 1

    def test_novel_urls_once_in_profile(self):
        text = _read(PROFILE)
        for url in NOVEL_URLS:
            assert text.count(url) == 1, url

    def test_carried_urls_in_block_sources(self):
        block_text = _block_text()
        for url in CARRIED_URLS:
            assert url in block_text, url


# ---------------------------------------------------------------------------
# 4. Mechanism structure and identity
# ---------------------------------------------------------------------------
class TestMechanism861Structure:
    def test_identity_fields(self):
        b = get_block()
        assert b["mechanism_id"] == MECHANISM
        assert b["iteration"] == ITERATION
        assert b["iteration_type"] == TYPE_LETTER
        assert b["date_analyzed"] == "2026-09-27"
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["researcher"] == "Kit (with Ray)"

    def test_key_design(self):
        b = get_block()
        assert b["block_key"] == BLOCK_KEY
        # No numeric mechanism-id substring in the key per #715.
        assert "861" not in BLOCK_KEY

    def test_verdict_grades(self):
        b = get_block()
        assert b["verdict"] == "directionally_supported_not_proven"
        assert b["tone_scores"] == "NOT_SCORED"
        assert b["engine_run"] is False
        assert b["no_analysis_json_update"] is True
        assert b["artifact_grade"] is False

    def test_falsification_ledger(self):
        b = get_block()
        assert b["falsification_ledger"] == 35
        assert b["falsification_family_member"] is False

    def test_excerpt_bounded(self):
        b = get_block()
        assert b["excerpt_bounded"] is True
        assert b["browser_opens"] == 0
        assert len(b["sources"]) == 8


# ---------------------------------------------------------------------------
# 5. Bundled-leverage geometry (SEVENTEENTH direction)
# ---------------------------------------------------------------------------
class TestBundledLeverageGeometry:
    def test_seventeenth_named(self):
        tax = get_block()["relationship_direction_taxonomy"]
        assert "SEVENTEENTH" in tax
        assert "BUNDLED-LEVERAGE" in tax

    def test_showcase_annual_plans(self):
        f = get_block()["finding"]
        assert "annual plans" in f
        assert "hundreds of thousands to millions of pounds" in f

    def test_binary_choice_sunset(self):
        f = get_block()["finding"]
        assert "binary choice" in f
        assert "sunsets" in f

    def test_no_sue_nda_90day(self):
        f = get_block()["finding"]
        assert "no-sue" in f
        assert "non-disclosure agreements" in f
        assert "90 days notice" in f

    def test_cma_moot(self):
        f = get_block()["finding"]
        assert "Competition and Markets Authority" in f
        assert "mooted" in f


# ---------------------------------------------------------------------------
# 6. AI Contribution Pilot disambiguation
# ---------------------------------------------------------------------------
class TestContributionPilotDisambiguation:
    def test_pilot_separate_track(self):
        f = get_block()["finding"]
        assert "AI Contribution Pilot is a SEPARATE track" in f

    def test_usage_based_no_upfront(self):
        d = get_block()["contribution_pilot_disambiguation"]
        assert "no upfront fee" in d
        assert "invitation" in d

    def test_peanuts_blackbox(self):
        f = get_block()["finding"]
        assert "peanuts" in f
        assert "black box" in f

    def test_not_focused_deal(self):
        f = get_block()["finding"]
        assert "the second-payer leg is the focused deal, not the pilot" in f


# ---------------------------------------------------------------------------
# 7. Dual-leg restraint-template replication
# ---------------------------------------------------------------------------
class TestDualLegRestraintReplication:
    def test_openai_leg_carried(self):
        f = get_block()["finding"]
        assert "$5 to $10 million per year" in f

    def test_google_leg_single_figure(self):
        f = get_block()["finding"]
        assert "single-figure millions" in f

    def test_combined_illustrative(self):
        f = get_block()["finding"]
        assert "$10 to $20 million per year MANUAL ILLUSTRATIVE" in f
        assert "1.3 to 2.6 percent" in f

    def test_meta_zero(self):
        f = get_block()["finding"]
        assert "Meta $0" in f

    def test_red_button_both_legs(self):
        f = get_block()["finding"]
        assert "big red button" in f
        assert "both deals" in f


# ---------------------------------------------------------------------------
# 8. Connects-to
# ---------------------------------------------------------------------------
class TestConnectsTo:
    def test_connects_to_expected(self):
        c = get_block()["connects_to"]
        for mid in (437, 774, 859):
            assert mid in c

    def test_437_first(self):
        assert get_block()["connects_to"][0] == 437


# ---------------------------------------------------------------------------
# 9. Confounders and statistical discipline
# ---------------------------------------------------------------------------
class TestConfoundersDiscipline:
    def test_confounder_tiers(self):
        confs = get_block()["confounders"]
        assert any(c.startswith("STRONG:") for c in confs)
        assert any(c.startswith("MEDIUM:") for c in confs)
        assert any(c.startswith("WEAK:") for c in confs)

    def test_single_outlet_strong(self):
        confs = " ".join(get_block()["confounders"])
        assert "single-outlet dependence" in confs
        assert "Press Gazette" in confs

    def test_counterargument(self):
        sc = get_block()["strongest_counterargument"]
        assert "ordinary bundle economics" in sc
        assert "90-day exit" in sc

    def test_coverage_note(self):
        assert "tone NOT_SCORED" in get_block()["coverage_note"]

    def test_no_engine_stats(self):
        b = get_block()
        assert b["engine_run"] is False
        assert "p_value" not in str(b["finding"])


# ---------------------------------------------------------------------------
# 10. Doc sync ratchet
# ---------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_stats(self):
        readme = _read(README)
        assert "53826" in readme
        assert "1374" in readme

    def test_readme_table_row(self):
        assert TEST_SLUG in _read(README)

    def test_architecture_row(self):
        arch = _read(ARCH)
        assert THIS_FILE in arch

    def test_iteration_log_entry(self):
        log = _read(LOG)
        assert "## #1049 Type C" in log
        assert "bundled_leverage" in log
        assert "861" in log


# ---------------------------------------------------------------------------
# 11. In-flight isolation (#899 #938 #900 #1012-wt do not carry our edit)
# ---------------------------------------------------------------------------
class TestInflightIsolation:
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
            for marker in (BLOCK_KEY, "mechanism_id: 861", "## #1049"):
                assert marker not in text, "%s in %s" % (marker, path)


# ---------------------------------------------------------------------------
# 12. Block hygiene
# ---------------------------------------------------------------------------
class TestBlockHygiene:
    def test_ascii_no_em_dash(self):
        block_text = yaml.safe_dump(get_block(), allow_unicode=True)
        for bad in ["\u2014", "\u2013", "\u2018", "\u2019", "\u2026", "\u00a0"]:
            assert bad not in block_text, repr(bad)
        assert not re.search(r"[\U0001F300-\U0001FAFF]", block_text)
