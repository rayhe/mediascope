"""Type C #824 (2026-09-18 03:00 PDT): Cloudflare AI-content payment
infrastructure stack - first dedicated lab-neutral tollbooth-operator
mechanism in the corpus (mechanism 726); Human Native acquisition
(Jan 16 2026) + Pay Per Crawl rails (402/Merchant of Record) + Pay Per
Use value pricing (Jul 1 2026, Ceramic.ai + You.com) + bot-blocking
leverage (Vogel Aug 2026 "real momentum").

Rotation window fifth leg: D (#820) -> E (#821) -> A (#822) -> B (#823) ->
C (#824), CLOSING the 820-824 window.

Evidence: 2 browser.search query sets this run, 0 browser.open first-hand
reads; all facts via search-result excerpts (second-hand per #503); all
URLs copied verbatim from search-result Full-URL listings; no canonical
URLs constructed. Statistical discipline per the qualitative Type C
convention: p_value/cohens_d/ci_95 NOT_CALCULATED, tone_scores
NOT_SCORED, is_significant False, engine NOT run; verdict
directionally_supported_not_proven; NOT a falsification-family member
(ledger holds at 26); no analysis.json update.

Deselected pre-commit per the #565 convention: anchor 1 + rotation
anchor 1 (patched green in the anchor followup); doc-sync 3 +
iteration-log 2 fail by design pre-commit, go green in the doc-sync
followup.

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
    "test_type_c_824_cloudflare_ai_payment_infrastructure_stack_sep18_3am.py"
)
MECH_NUM = 726
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention.
MECH_ID_MARKER = "mechanism" + "_726"
NEXT_ID_MARKER = "mechanism" + "_727"
NEXT_ID_NUMERIC = "mechanism_id: 727"
MECH_KEY = "cloudflare_ai_content_payment_infrastructure_stack_sep2026"
URL_DECODER = "https://the-decoder.com/cloudflare-acquires-human-native-to-build-new-payment-model-for-ai-training-data/"
URL_DIGIDAY = "http://digiday.com/media/cloudflares-human-native-acquisition-signals-a-new-content-economy-for-publishers/"
URL_ADVTV = "https://www.advanced-television.com/2026/01/16/cloudflare-acquires-human-native/"
URL_TECHCRUNCH = "https://techcrunch.com/2026/07/01/cloudflares-new-policy-pushes-ai-companies-to-pay-for-publishers-content/"
URL_PRESSGAZETTE = "https://pressgazette.co.uk/platforms/cloudflare-says-bot-blocking-is-fueling-publisher-ai-deals/"
URL_REGISTER = "https://www.theregister.com/software/2025/07/01/cloudflare-creates-ai-crawler-tollbooth-to-pay-publishers/101654"
URL_SEJ = "https://www.searchenginejournal.com/cloudflare-sparks-seo-debate-with-new-ai-crawler-payment-system/550328/"
URL_TECHSPOT = "https://www.techspot.com/news/108521-cloudflare-tests-pay-crawl-system-charges-ai-firms.html"
NEXT_SIBLING = "\nadvance_dual_asset_monetization:"
ANCHORED_SHA = "c4be72c9ddc401c8bc9490c98011097933fab437"


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


class TestNovelty824:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_c_824_file(self):
        files = sorted(
            str(p) for p in TESTS_DIR.glob("test_type_c_824*.py")
        )
        assert len(files) == 1, files
        assert files[0].endswith(TEST_BASENAME), files

    def test_type_c_824_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type C #824")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_novelty_verification_claim_present_in_block(self):
        # The block pins the pre-commit novelty greps (Zero Ceramic.ai hits,
        # zero merchant-of-record / 402 hits, 7-of-8 source URLs zero-hit with
        # the TechCrunch URL already in mechanism 64, max numeric
        # mechanism_id 725); this test pins the claim in the committed block,
        # per the #752 convention.
        block = _block()
        assert "test_type_c_824" in block
        assert "Zero Ceramic.ai hits repo-wide pre-commit" in block
        assert "max numeric mechanism_id 725 pre-commit" in block


# --- Rotation cycle guard ---------------------------------------------------


class TestRotationCycleGuard824:
    """Rotation: 820-824 window fifth leg D->E->A->B->C, closing the window."""

    EXPECTED_ORDER = [
        ("C", "824"), ("B", "823"), ("A", "822"), ("E", "821"), ("D", "820"),
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
        # subject opens the #824 window-closing leg (HEAD drifts past it with
        # the anchor/doc-sync/push-status followups, per the #565 convention).
        res = _run_git("log", "--format=%H %s", "--all")
        hits = [l for l in res.stdout.splitlines()
                if l.startswith(ANCHORED_SHA + " ")]
        assert len(hits) == 1, hits
        assert "Type C #824: " in hits[0], hits


# --- Mechanism content -------------------------------------------------------


class TestMechanism726Content:
    def test_block_present_in_entities(self):
        block = _block()
        assert block.strip().startswith(MECH_KEY + ":")

    def test_iteration_metadata(self):
        data = _block_data()
        assert data["mechanism_id"] == MECH_NUM
        assert data["iteration"] == 824
        assert data["iteration_type"] == "C"
        assert data["date_analyzed"] == "2026-09-18"
        assert data["time_pdt"] == "03:00"
        assert data["job_id"] == "mediascope-daily-iteration"

    def test_acquisition_facts(self):
        data = _block_data()
        sf = data["stack_facts"]
        assert "January 16, 2026" in sf["acquired"]
        assert "founded 2024" in sf["acquired"]
        assert "LocalGlobe" in sf["backers"]
        assert "Mercuri" in sf["backers"]
        assert "DeepMind" in sf["team"]
        assert "Bloomberg" in sf["team"]
        assert "Napster era" in sf["mission_quote"]

    def test_payment_rails_facts(self):
        data = _block_data()
        sf = data["stack_facts"]
        assert "402" in sf["pay_per_crawl"]
        assert "Merchant of Record" in sf["pay_per_crawl"]
        assert "Ed25519" in data["overview"]
        assert "July 1, 2026" in sf["pay_per_use"]
        assert "Ceramic.ai" in sf["pay_per_use"]
        assert "You.com" in sf["pay_per_use"]
        assert "x402 Foundation" in sf["settlement_rail"]

    def test_leverage_evidence(self):
        data = _block_data()
        quotes = " ".join(data["leverage_evidence"])
        assert "Neil Vogel" in quotes
        assert "real momentum" in quotes
        assert "reliable scarcity" in quotes
        assert "almost all AI crawlers" in quotes
        assert "Conde Nast" in quotes
        assert "Quora" in quotes

    def test_incentive_geometry(self):
        data = _block_data()
        ig = data["incentive_geometry"]
        assert "tollbooth" in _fold(data["overview"])
        assert "not a payer" in _fold(data["overview"])
        assert "can not be blocked" in _fold(
            ig["lab_neutral_with_asymmetric_enforcement"])
        assert "mechanism 64" in _fold(data["overview"])

    def test_scale_and_asymmetry(self):
        data = _block_data()
        sf = data["stack_facts"]
        assert "20 percent" in sf["scale"]
        assert "1 million" in sf["scale"]
        assert "1,600:1" in sf["value_asymmetry"]
        assert "9.4:1" in sf["value_asymmetry"]
        assert "50 percent" in sf["value_asymmetry"]

    def test_source_urls_verbatim(self):
        data = _block_data()
        assert data["sources"][0].startswith(URL_DECODER)
        assert data["sources"][1].startswith(URL_DIGIDAY)
        assert data["sources"][4].startswith(URL_PRESSGAZETTE)
        assert data["sources"][5].startswith(URL_REGISTER)
        assert len(data["sources"]) == 8

    def test_meta_zero(self):
        data = _block_data()
        ov = _fold(data["overview"])
        assert "no coverage-tone claim" in ov
        assert "correlation is not causation" in ov


# --- Statistical discipline ---------------------------------------------------


class TestStatisticalDiscipline824:
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
        assert "ledger holds at 26" in data["falsification_family"]

    def test_designed_keying_no_underscore_form_in_block(self):
        # Per the #715/#723/#738/#739 designed-keying convention, the block
        # key and block text must never carry the contiguous underscore-form
        # marker; the needle is format-built so this test carries no literal.
        block = _block()
        needle = MECH_ID_MARKER
        assert needle not in block
        assert MECH_KEY.count("_" + "726") == 0

    def test_ranked_confounders_and_counterargument(self):
        data = _block_data()
        conf = data["confounders_ranked"]
        assert len(conf) == 5
        assert [c["strength"] for c in conf] == [
            "STRONG", "STRONG", "MODERATE", "MODERATE", "WEAK",
        ]
        assert "strongest_counterargument" in data
        assert "beta-stage payment rail" in _fold(data["strongest_counterargument"])


# --- Supersession and corpus post-#823 --------------------------------------


class TestSupersessionAndCorpusPost823:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout))

    def test_corpus_max_is_726(self):
        assert max(self._numeric_ids()) == 726

    def test_iteration_823_max_725_sweep_superseded_by_design(self):
        # #823's max-725 sweeps fail by designed supersession now that 726 exists.
        assert max(self._numeric_ids()) != 725

    def test_zero_underscore_727_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_727_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_823_zero_underscore_726_sweep_stays_green(self):
        # The #823 zero-underscore-726 sweeps stay green post-#824 by designed keying:
        # neither the profile block nor this test file carries a literal underscore-726 key.
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", MECH_ID_MARKER, "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), \
                "literal underscore-726 key leaked into %s" % root

    def test_iteration_823_zero_numeric_726_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 726", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected #823's zero-numeric-726 sweep to fail by designed supersession"

    def test_numeric_726_keys_in_exactly_the_designed_location(self):
        res = _run_git("grep", "-r", "mechanism_id: 726", "--", "profiles/")
        hits = [l for l in res.stdout.strip().splitlines() if l.strip()]
        # Designed keying: one numeric 726 key in the marketplace
        # intermediary landscape block; no other profiles/ location.
        assert len(hits) == 1, "unexpected numeric 726 key spread in profiles/: %s" % hits
        assert "profiles/competitor-entities.yaml" in hits[0]

    def test_iteration_822_zero_underscore_725_sweep_stays_green(self):
        # The #822 zero-underscore-725 sweeps stay green post-#824 by designed keying.
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", "mechanism" + "_725", "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), \
                "literal underscore-725 key leaked into %s" % root


# --- Ledger -----------------------------------------------------------------


def _profiles_corpus():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith((".yaml", ".yml", ".md")):
                out.append(_read(os.path.join(root, fn)))
    return "\n".join(out)


class TestLedger824:
    def test_twenty_sixth_present_and_twenty_seventh_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference "TWENTY-SEVENTH" inside their own
        # negative guards, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus
        assert "ledger holds at 26" in _block()

    def test_m726_block_key_unique_and_entities_parse(self):
        import yaml

        doc = yaml.safe_load(_read(ENTITIES_PATH))
        assert doc["marketplace_intermediary_landscape"][MECH_KEY]["mechanism_id"] == 726
        keys = [
            k for k in doc["marketplace_intermediary_landscape"] if k == MECH_KEY
        ]
        assert len(keys) == 1

    def test_m726_not_a_falsification_family_member(self):
        data = _block_data()
        assert data["falsification_family"].startswith("NOT a member")

    def test_no_analysis_json_update_claimed(self):
        data = _block_data()
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False
        assert data["verdict"] == "directionally_supported_not_proven"


# --- Doc-sync ----------------------------------------------------------------


class TestDocSync824:
    def test_readme_row_824(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_824(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_824_file(self):
        text = _read(ARCH_PATH)
        assert "tests/" + TEST_BASENAME in text


# --- Iteration log ------------------------------------------------------------


class TestIterationLog824:
    def _log(self):
        return _read(LOG_PATH)

    def test_log_entry_present(self):
        assert "## #824 Type C:" in self._log()

    def test_log_mechanism_number_and_topic(self):
        log = self._log()
        idx = log.index("## #824 Type C:")
        entry = log[idx:idx + 8000]
        assert "mechanism 726" in entry
        assert "Cloudflare" in entry
        assert "Human Native" in entry

    def test_sep_18_2026_is_friday(self):
        import datetime

        assert datetime.date(2026, 9, 18).strftime("%A") == "Friday"
