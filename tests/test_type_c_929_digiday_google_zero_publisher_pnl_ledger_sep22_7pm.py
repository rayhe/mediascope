"""Type C #929 (2026-09-22 19:00 PDT): Digiday Publishing Summit Sep-2026
Google Zero publisher P&L ledger - first dedicated corpus mechanism pairing
the revenue-side buyer map (TV News Check "Content Sells, But Who's Buying?",
first-hand read) with the cost-side summit ledger (Digiday "Google Zero"
edition, first-hand read): licensing revenue opaque/concentrated with buyers
avoiding price discovery, newsroom cuts at deal-signers (Reach 160 jobs,
McClatchy 30% of unionized staff), publishers buying traffic back from Google
(paid search +274% / ~$113M July), ~1% AI Overview CTR. Corroborates the m786
admission (licensing will not replace lost revenue) from the publisher side.

Rotation window FIFTH leg: D (#925) -> E (#926) -> A (#927) -> B (#928) ->
C (#929), CLOSING the 925-929 window.

Evidence: 2 browser.search query sets this run + 2 browser.open first-hand
reads (TV News Check 126 lines; Digiday 184 lines); rejected candidates logged
(India blitz m609-family, UMG/ElevenLabs music-vertical, TechCrunch Sep 6
settlement fight m629, Roundtable/Paradium m738, Press Ranger/OtterlyAI m249,
stockmoguls/DOJ-brief m672, Press Gazette tracker m714/m734, Google pilot
m702/m708). Statistical discipline per the qualitative Type C convention:
p_value/cohens_d/ci_95 NOT_CALCULATED, tone_scores NOT_SCORED, is_significant
False, engine NOT run; verdict directionally_supported_not_proven; NOT a
falsification-family member (ledger holds at 29, THIRTIETH remains the
negative guard); no analysis.json update.

Deselected pre-commit per the #565 convention: anchor 1 + rotation guard 3
(patched green in the anchor followup); doc-sync 3 + iteration-log 3 fail by
design pre-commit, go green in the doc-sync followup.

Anchor placeholder: patched to the main commit SHA in the #565 follow-up.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TESTS_DIR = Path(REPO_ROOT) / "tests"
REPO = Path(REPO_ROOT)
ENTITIES_PATH = "profiles/competitor-entities.yaml"
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
TEST_BASENAME = (
    "test_type_c_929_digiday_google_zero_publisher_pnl_ledger_sep22_7pm.py"
)
MECH_NUM = 789
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention.
MECH_ID_MARKER = "mechanism" + "_789"
NEXT_ID_MARKER = "mechanism" + "_790"
NEXT_ID_NUMERIC = "mechanism_id: 790"
MECH_KEY = "digiday_publishing_summit_google_zero_publisher_pnl_ledger_sep2026"
URL_TVN = "https://tvnewscheck.com/ai/article/content-sells-but-whos-buying/"
URL_DIG = "https://digiday.com/media/media-briefing-overheard-at-the-digiday-publishing-summit-sept-26-google-zero-edition/"
NEXT_SIBLING = "\n  snap_specs_enterprise_partnership_stack_sep2026:"
ANCHORED_SHA = "2fbf4f6f06ef82bb08eb858925d676c951904b08"


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _block():
    doc = _read(ENTITIES_PATH)
    start = doc.index(MECH_KEY + ":")
    end = doc.index(NEXT_SIBLING, start)
    return doc[start:end]


def _block_data():
    import yaml

    return yaml.safe_load(_block())[MECH_KEY]


def _fold(s):
    return re.sub(r"\s+", " ", s.lower())


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT] + list(args),
        capture_output=True,
        text=True,
    )


# --- Novelty ---------------------------------------------------------------


class TestNovelty929:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_c_929_file(self):
        files = sorted(
            str(p) for p in TESTS_DIR.glob("test_type_c_929*.py")
        )
        assert len(files) == 1, files
        assert files[0].endswith(TEST_BASENAME), files

    def test_type_c_929_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type C #929")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_novelty_verification_claim_present_in_block(self):
        # The block pins the pre-commit novelty greps (zero tvnewscheck
        # content-sells URL / digiday summit URL / "Esther Cohen" /
        # "MonetizationOS" / "AI Content Trading Platform" hits repo-wide,
        # max numeric mechanism_id 788, zero underscore-form 789 strings);
        # this test pins the claim in the committed block, per the
        # #752 convention.
        data = _block_data()
        rm = _fold(data["research_method"])
        assert "zero test_type_c_929 files on disk" in rm
        assert 'no "type c #929" in git log' in rm
        assert "max numeric mechanism_id 788 pre-commit" in rm
        assert "zero underscore-form 789" in rm
        assert "both evidence urls zero-hit repo-wide pre-commit" in rm


# --- Rotation guard ---------------------------------------------------------


class TestRotationCycleGuard929:
    """Rotation: 925-929 window fifth leg D->E->A->B->C, closing the window."""

    EXPECTED_ORDER = [
        ("C", "929"), ("B", "928"), ("A", "927"), ("E", "926"), ("D", "925"),
    ]
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def _window(self):
        # First occurrence of each distinct iteration number, newest first
        # (robust to the #756-style followup commits that repeat the same
        # "Type X #N" wording without the colon, per the #752 convention;
        # hardened per the #783 repair to dedupe by iteration number).
        mains = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%s", "--no-merges",
             "-n", "40", "--", "."],
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        seen_nums = set()
        out = []
        for s in mains:
            m = re.match(r"Type ([A-E]) #(\d+):", s)
            if m and m.group(2) not in seen_nums:
                seen_nums.add(m.group(2))
                out.append(m.groups())
        return out[:5]

    def test_window_closes_deabc(self):
        assert self._window() == self.EXPECTED_ORDER

    def test_window_cycle_edges_are_adjacent(self):
        window = self._window()
        for (t1, _), (t2, _) in zip(window, window[1:]):
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        )
        # Durable post-commit: the anchored main commit is in history and its
        # subject opens the #929 window-closing leg (HEAD drifts past it with
        # the anchor/doc-sync/push-status followups, per the #565 convention).
        res = _run_git("log", "--format=%H %s", "--all")
        hits = [l for l in res.stdout.splitlines()
                if l.startswith(ANCHORED_SHA + " ")]
        assert len(hits) == 1, hits
        assert "Type C #929: " in hits[0], hits


# --- Mechanism content -------------------------------------------------------


class TestMechanism789Content:
    def test_block_present_in_entities(self):
        block = _block()
        assert block.strip().startswith(MECH_KEY + ":")

    def test_iteration_metadata(self):
        data = _block_data()
        assert data["mechanism_id"] == MECH_NUM
        assert data["iteration"] == 929
        assert data["iteration_type"] == "C"
        assert data["date_analyzed"] == "2026-09-22"
        assert data["time_pdt"] == "19:00"
        assert data["job_id"] == "mediascope-daily-iteration"
        assert data["goal_id"] == "goal_54093bda4145"

    def test_revenue_side_facts(self):
        data = _block_data()
        rf = data["revenue_side_facts"]
        assert "revenue share" in rf["perplexity_no_outright_buy"]
        assert "$20 million a year" in rf["amazon_portfolio"]
        assert "AI Content Trading Platform" in rf["amazon_portfolio"]
        assert "not broad licensing" in rf["meta_limited_deals"]
        assert "USA Today" in rf["meta_limited_deals"]
        assert "more than 20 disclosed" in rf["openai_partnerships"]
        assert "pay-per-use grounding" in rf["microsoft_marketplace"]
        assert "black box" in rf["google_catching_up"]
        assert "never signed a news publisher deal" in rf["anthropic_zero_deals"]
        assert "$1.5 billion" in rf["anthropic_zero_deals"]
        assert "Tavily" in rf["scraper_pipeline_layer"]
        assert "layer most publishers never see" in rf["scraper_pipeline_layer"]
        assert "7,000 enrolled" in rf["tollbit_scale"]
        assert "default to closed" in rf["monetization_os_prescription"]
        assert "price to zero" in rf["skok_price_to_zero"]
        assert "accurately cite and compensate" in rf["linkup_pays_claim"]

    def test_cost_side_facts(self):
        data = _block_data()
        cf = data["cost_side_facts"]
        assert "not coming back" in cf["google_zero_acceptance"]
        assert "closed-door town hall" in cf["google_zero_acceptance"]
        assert "picked off one by one" in cf["opacity_quotes"]
        assert "largely concentrated in the very biggest players" in cf["opacity_quotes"]
        assert "160 editorial jobs" in cf["reach_160_cuts"]
        assert "AI-generated summaries" in cf["reach_160_cuts"]
        assert "30 percent of all unionized" in cf["mcclatchy_30pct_cuts"]
        assert "Sacramento Bee" in cf["mcclatchy_30pct_cuts"]
        assert "274 percent" in cf["paid_search_inversion"]
        assert "$113 million" in cf["paid_search_inversion"]
        assert "about 1 percent" in cf["ai_overview_ctr_one_pct"]
        assert "126 million pounds" in cf["guardian_reader_revenue"]
        assert "1.4 million paying digital supporters" in cf["guardian_reader_revenue"]
        assert "traffic now as extra" in cf["esther_cohen_verge"]
        assert "dynamic paywall" in cf["reuters_dynamic_paywall"]

    def test_incentive_geometry(self):
        data = _block_data()
        ig = data["incentive_geometry"]
        assert "opacity as buyer strategy" in _fold(ig["opacity_as_strategy"])
        assert "mechanism 636" in _fold(ig["opacity_as_strategy"])
        assert "big publishers, negotiating one at a time" in _fold(ig["concentration_confirmed"])
        assert "mechanism 468" in _fold(ig["deal_signer_still_cuts"])
        assert "160 editorial jobs" in _fold(ig["deal_signer_still_cuts"])
        assert "mechanisms 702/708" in _fold(ig["flow_inversion"])
        assert "publisher-to-platform" in _fold(ig["flow_inversion"])
        assert "redundant by design" in _fold(ig["scarcity_pricing_thesis"])
        assert "toll booth" in _fold(ig["tollbooth_corroboration"])
        assert "mechanism 726" in _fold(ig["tollbooth_corroboration"])

    def test_connects_to(self):
        data = _block_data()
        assert data["connects_to"] == [726, 786, 468, 702, 708, 509, 636, 519]

    def test_source_urls_verbatim(self):
        data = _block_data()
        assert data["sources"][0].startswith(URL_TVN)
        assert data["sources"][1].startswith(URL_DIG)
        assert len(data["sources"]) == 2

    def test_no_tone_claim(self):
        data = _block_data()
        ov = _fold(data["overview"])
        assert "no coverage-tone claim" in ov
        assert "correlation is not causation" in ov


# --- Statistical discipline ---------------------------------------------------


class TestStatisticalDiscipline929:
    def test_statistical_discipline_type_c(self):
        data = _block_data()
        sd = data["statistical_discipline"]
        assert sd["scorer"] == "none"
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["qualitative_only"] is True
        assert sd["correlation_not_causation"] is True
        assert sd["artifact_grade"] is False

    def test_verdict_ledger_and_source_urls(self):
        data = _block_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False
        assert "ledger holds at 29" in data["falsification_family"]
        assert "THIRTIETH" in data["falsification_family"]

    def test_designed_keying_no_underscore_form_in_block(self):
        # Per the #715/#723/#738/#739 designed-keying convention, the block
        # key and block text must never carry the contiguous underscore-form
        # marker; the needle is format-built so this test carries no literal.
        block = _block()
        needle = MECH_ID_MARKER
        assert needle not in block
        assert MECH_KEY.count("_" + "789") == 0

    def test_ranked_confounders_and_counterargument(self):
        data = _block_data()
        conf = data["confounders_ranked"]
        assert len(conf) == 5
        assert [c["strength"] for c in conf] == [
            "STRONG", "STRONG", "MODERATE", "MODERATE", "WEAK",
        ]
        assert "strongest_counterargument" in data
        assert "document publishers describing a bad bargain" in _fold(data["strongest_counterargument"])


# --- Supersession and corpus post-#928 --------------------------------------


class TestSupersessionAndCorpusPost928:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout))

    def test_corpus_max_is_789(self):
        assert max(self._numeric_ids()) == 789

    def test_iteration_928_max_788_sweep_superseded_by_design(self):
        # #928's max-788 sweeps fail by designed supersession now that 789 exists.
        assert max(self._numeric_ids()) != 788

    def test_zero_underscore_790_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_790_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_928_zero_underscore_789_sweep_stays_green(self):
        # The #928 zero-underscore-789 sweeps stay green post-#929 by designed keying:
        # neither the profile block nor this test file carries a literal underscore-789 key.
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", MECH_ID_MARKER, "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), \
                "literal underscore-789 key leaked into %s" % root

    def test_iteration_928_zero_numeric_789_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 789", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected #928's zero-numeric-789 sweep to fail by designed supersession"

    def test_numeric_789_keys_in_exactly_the_designed_location(self):
        res = _run_git("grep", "-r", "mechanism_id: 789", "--", "profiles/")
        hits = [l for l in res.stdout.strip().splitlines() if l.strip()]
        # Designed keying: one numeric 789 key in the marketplace
        # intermediary landscape block; no other profiles/ location.
        assert len(hits) == 1, "unexpected numeric 789 key spread in profiles/: %s" % hits
        assert "profiles/competitor-entities.yaml" in hits[0]

    def test_iteration_927_zero_underscore_788_sweep_stays_green(self):
        # The #927 zero-underscore-788 sweeps stay green post-#929 by designed
        # keying in profiles/. Note: tests/ legitimately carries literals via
        # prior runs' own method names, pre-existing and unrelated to this
        # run, so the sweep is profiles/-scoped here per the #754
        # profiles-corpus convention.
        res = _run_git("grep", "-r", "mechanism" + "_788", "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip(), \
            "literal underscore-788 key leaked into profiles/"


# --- Ledger -----------------------------------------------------------------


def _profiles_corpus():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith((".yaml", ".yml", ".md")):
                out.append(_read(os.path.join(root, fn)))
    return "\n".join(out)


class TestLedger929:
    def test_thirtieth_present_and_thirty_first_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference their own negative guards inside their
        # own negative-guard tests, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "THIRTIETH" in corpus
        assert "THIRTY-FIRST" not in corpus
        assert "ledger holds at 29" in _block()

    def test_m789_block_key_unique_and_entities_parse(self):
        import yaml

        doc = yaml.safe_load(_read(ENTITIES_PATH))
        assert doc["marketplace_intermediary_landscape"][MECH_KEY]["mechanism_id"] == 789
        keys = [
            k for k in doc["marketplace_intermediary_landscape"] if k == MECH_KEY
        ]
        assert len(keys) == 1

    def test_m789_not_a_falsification_family_member(self):
        data = _block_data()
        assert data["falsification_family"].startswith("NOT a member")

    def test_no_analysis_json_update_claimed(self):
        data = _block_data()
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False
        assert data["verdict"] == "directionally_supported_not_proven"


# --- Doc-sync ----------------------------------------------------------------


class TestDocSync929:
    def test_readme_row_929(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_929(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_929_file(self):
        text = _read(ARCH_PATH)
        assert "tests/" + TEST_BASENAME in text


# --- Iteration log ------------------------------------------------------------


class TestIterationLog929:
    def _log(self):
        return _read(LOG_PATH)

    def test_log_entry_present(self):
        assert "## #929 Type C:" in self._log()

    def test_log_mechanism_number_and_topic(self):
        log = self._log()
        idx = log.index("## #929 Type C:")
        entry = log[idx:idx + 9000]
        assert "mechanism 789" in entry
        assert "Google Zero" in entry
        assert "publisher P" in entry

    def test_sep_22_2026_is_tuesday(self):
        import datetime

        assert datetime.date(2026, 9, 22).strftime("%A") == "Tuesday"
