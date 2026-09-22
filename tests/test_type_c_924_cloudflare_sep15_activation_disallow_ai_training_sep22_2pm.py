"""Type C #924 (2026-09-22 14:00 PDT): Cloudflare Sep-15-2026 Disallow AI
Training default activation - first dedicated corpus activation-verification
leg for mechanism 786 (extends mechanism 726, the Cloudflare AI-content
payment infrastructure stack): post-deadline trade-press reporting confirms
the September 15 default-block went live (training + agent crawlers blocked
by default on ad-supported pages for new domains and the free tier), with
the mixed-use most-restrictive-function rule sharpening the Googlebot
crawler-separation test and the 50-plus-agreements admission bounding the
licensing-as-replacement narrative.

Rotation window FIFTH leg: D (#920) -> E (#921) -> A (#922) -> B (#923) ->
C (#924), CLOSING the 920-924 window.

Evidence: 2 browser.search query sets this run + 2 browser.open first-hand
reads (WebdesignerDepot Sep 16 2026; Media Copilot Sep 18 2026); webpronews
and Tech Times legs via search-result excerpts (second-hand per #503); all
URLs copied verbatim from tool-returned Full-URL listings; no canonical
URLs constructed. Statistical discipline per the qualitative Type C
convention: p_value/cohens_d/ci_95 NOT_CALCULATED, tone_scores
NOT_SCORED, is_significant False, engine NOT run; verdict
directionally_supported_not_proven; NOT a falsification-family member
(ledger holds at 29, THIRTIETH remains the negative guard); no
analysis.json update.

Deselected pre-commit per the #565 convention: anchor 1 + rotation
anchor 1 (patched green in the anchor followup); doc-sync 3 +
iteration-log 3 fail by design pre-commit, go green in the doc-sync
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
    "test_type_c_924_cloudflare_sep15_activation_disallow_ai_training_sep22_2pm.py"
)
MECH_NUM = 786
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention.
MECH_ID_MARKER = "mechanism" + "_786"
NEXT_ID_MARKER = "mechanism" + "_787"
NEXT_ID_NUMERIC = "mechanism_id: 787"
MECH_KEY = "cloudflare_sep15_disallow_ai_training_activation_sep2026"
URL_WDD = "https://webdesignerdepot.com/cloudflare-just-gave-ai-training-bots-the-middle-finger/"
URL_MCP = "https://mediacopilot.ai/cloudflare-ai-crawler-controls/"
URL_WPN = "https://www.webpronews.com/cloudflare-hands-publishers-new-levers-against-ai-crawlers/"
URL_TET = "https://www.techtimes.com/articles/319554/20260702/cloudflare-separates-ai-crawlers-purpose-opens-door-charging-them-directly.htm"
NEXT_SIBLING = "\n  snap_specs_enterprise_partnership_stack_sep2026:"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"


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


class TestNovelty924:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_c_924_file(self):
        files = sorted(
            str(p) for p in TESTS_DIR.glob("test_type_c_924*.py")
        )
        assert len(files) == 1, files
        assert files[0].endswith(TEST_BASENAME), files

    def test_type_c_924_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type C #924")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_novelty_verification_claim_present_in_block(self):
        # The block pins the pre-commit novelty greps (zero webdesignerdepot /
        # mediacopilot.ai / Chema Alonso / Disallow AI Training / BotBase hits
        # repo-wide, max numeric mechanism_id 785, zero underscore-form 786
        # strings); this test pins the claim in the committed block, per the
        # #752 convention.
        block = _block()
        assert "test_type_c_924" in block
        assert 'zero "webdesignerdepot" hits repo-wide' in block
        assert 'zero "Chema Alonso" hits repo-wide' in block
        assert "max numeric mechanism_id 785 pre-commit" in block
        assert "no test_type_c_924 files on disk (glob)" in block


# --- Rotation cycle guard ---------------------------------------------------


class TestRotationCycleGuard924:
    """Rotation: 920-924 window fifth leg D->E->A->B->C, closing the window."""

    EXPECTED_ORDER = [
        ("C", "924"), ("B", "923"), ("A", "922"), ("E", "921"), ("D", "920"),
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
        # subject opens the #924 window-closing leg (HEAD drifts past it with
        # the anchor/doc-sync/push-status followups, per the #565 convention).
        res = _run_git("log", "--format=%H %s", "--all")
        hits = [l for l in res.stdout.splitlines()
                if l.startswith(ANCHORED_SHA + " ")]
        assert len(hits) == 1, hits
        assert "Type C #924: " in hits[0], hits


# --- Mechanism content -------------------------------------------------------


class TestMechanism786Content:
    def test_block_present_in_entities(self):
        block = _block()
        assert block.strip().startswith(MECH_KEY + ":")

    def test_iteration_metadata(self):
        data = _block_data()
        assert data["mechanism_id"] == MECH_NUM
        assert data["iteration"] == 924
        assert data["iteration_type"] == "C"
        assert data["date_analyzed"] == "2026-09-22"
        assert data["time_pdt"] == "14:00"
        assert data["job_id"] == "mediascope-daily-iteration"
        assert data["goal_id"] == "goal_54093bda4145"

    def test_activation_facts(self):
        data = _block_data()
        af = data["activation_facts"]
        assert "September 15, 2026" in af["disallow_ai_training_live"]
        assert "blocked outright" in af["training_only_blockable"]
        assert "Anthropic" in af["training_only_blockable"]
        assert "Meta" in af["training_only_blockable"]
        assert "let search engines in, block AI training" in af["recommended_defaults"]
        assert "new domains and free-tier customers" in af["default_scope"]
        assert "most restrictive function" in af["mixed_use_rule"]
        assert "Google-Extended" in af["google_extended_split"]
        assert "Since 2023" in af["google_extended_split"]
        assert "AI Overviews or AI Mode" in af["google_extended_limit"]
        assert "Chema Alonso" in af["media_party_barcelona"]
        assert "overtaken human traffic" in af["media_party_barcelona"]
        assert "52 percent" in af["media_party_barcelona"]
        assert "Ceramic.ai" in af["pay_per_use_partners_named"]
        assert "You.com" in af["pay_per_use_partners_named"]
        assert "more than 50 publisher-AI agreements" in af["fifty_plus_agreements_admission"]
        assert "unlikely to replace" in af["fifty_plus_agreements_admission"]
        assert "x402" in af["monetization_gateway_waitlist"]
        assert "CloudFront" in af["monetization_gateway_waitlist"]
        assert "BotBase" in af["visibility_layer"]

    def test_incentive_geometry(self):
        data = _block_data()
        ig = data["incentive_geometry"]
        assert "announced policy to operational default" in _fold(ig["announced_to_operational"])
        assert "reliable scarcity" in _fold(ig["scarcity_mechanism_live"])
        assert "mechanism 726" in _fold(data["overview"])
        assert "permit-the-whole-crawler or shut-it-out" in _fold(ig["separation_test"])
        assert "tolls alone do not fill the hole" in _fold(ig["admission_bounds_replacement"])
        assert "structural confirmation leg" in _fold(ig["thesis_contribution"])

    def test_connects_to(self):
        data = _block_data()
        assert data["connects_to"] == [726, 64, 412, 702, 708]

    def test_source_urls_verbatim(self):
        data = _block_data()
        assert data["sources"][0].startswith(URL_WDD)
        assert data["sources"][1].startswith(URL_MCP)
        assert data["sources"][2].startswith(URL_WPN)
        assert data["sources"][3].startswith(URL_TET)
        assert len(data["sources"]) == 4

    def test_meta_zero(self):
        data = _block_data()
        ov = _fold(data["overview"])
        assert "no coverage-tone claim" in ov
        assert "correlation is not causation" in ov


# --- Statistical discipline ---------------------------------------------------


class TestStatisticalDiscipline924:
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
        assert MECH_KEY.count("_" + "786") == 0

    def test_ranked_confounders_and_counterargument(self):
        data = _block_data()
        conf = data["confounders_ranked"]
        assert len(conf) == 5
        assert [c["strength"] for c in conf] == [
            "STRONG", "STRONG", "MODERATE", "MODERATE", "WEAK",
        ]
        assert "strongest_counterargument" in data
        assert "threat layer, not publishers being paid" in _fold(data["strongest_counterargument"])


# --- Supersession and corpus post-#923 --------------------------------------


class TestSupersessionAndCorpusPost923:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout))

    def test_corpus_max_is_786(self):
        assert max(self._numeric_ids()) == 786

    def test_iteration_923_max_785_sweep_superseded_by_design(self):
        # #923's max-785 sweeps fail by designed supersession now that 786 exists.
        assert max(self._numeric_ids()) != 785

    def test_zero_underscore_787_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_787_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_923_zero_underscore_786_sweep_stays_green(self):
        # The #923 zero-underscore-786 sweeps stay green post-#924 by designed keying:
        # neither the profile block nor this test file carries a literal underscore-786 key.
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", MECH_ID_MARKER, "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), \
                "literal underscore-786 key leaked into %s" % root

    def test_iteration_923_zero_numeric_786_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 786", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected #923's zero-numeric-786 sweep to fail by designed supersession"

    def test_numeric_786_keys_in_exactly_the_designed_location(self):
        res = _run_git("grep", "-r", "mechanism_id: 786", "--", "profiles/")
        hits = [l for l in res.stdout.strip().splitlines() if l.strip()]
        # Designed keying: one numeric 786 key in the marketplace
        # intermediary landscape block; no other profiles/ location.
        assert len(hits) == 1, "unexpected numeric 786 key spread in profiles/: %s" % hits
        assert "profiles/competitor-entities.yaml" in hits[0]

    def test_iteration_922_zero_underscore_785_sweep_stays_green(self):
        # The #922 zero-underscore-785 sweeps stay green post-#924 by designed
        # keying in profiles/. Note: tests/ legitimately carries one literal
        # via #923's own method name (test_iteration_log_cites_mechanism_785),
        # pre-existing and unrelated to this run, so the sweep is
        # profiles/-scoped here per the #754 profiles-corpus convention.
        res = _run_git("grep", "-r", "mechanism" + "_785", "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip(), \
            "literal underscore-785 key leaked into profiles/"


# --- Ledger -----------------------------------------------------------------


def _profiles_corpus():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith((".yaml", ".yml", ".md")):
                out.append(_read(os.path.join(root, fn)))
    return "\n".join(out)


class TestLedger924:
    def test_thirtieth_present_and_thirty_first_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference their own negative guards inside their
        # own negative-guard tests, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "THIRTIETH" in corpus
        assert "THIRTY-FIRST" not in corpus
        assert "ledger holds at 29" in _block()

    def test_m786_block_key_unique_and_entities_parse(self):
        import yaml

        doc = yaml.safe_load(_read(ENTITIES_PATH))
        assert doc["marketplace_intermediary_landscape"][MECH_KEY]["mechanism_id"] == 786
        keys = [
            k for k in doc["marketplace_intermediary_landscape"] if k == MECH_KEY
        ]
        assert len(keys) == 1

    def test_m786_not_a_falsification_family_member(self):
        data = _block_data()
        assert data["falsification_family"].startswith("NOT a member")

    def test_no_analysis_json_update_claimed(self):
        data = _block_data()
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False
        assert data["verdict"] == "directionally_supported_not_proven"


# --- Doc-sync ----------------------------------------------------------------


class TestDocSync924:
    def test_readme_row_924(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_924(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_924_file(self):
        text = _read(ARCH_PATH)
        assert "tests/" + TEST_BASENAME in text


# --- Iteration log ------------------------------------------------------------


class TestIterationLog924:
    def _log(self):
        return _read(LOG_PATH)

    def test_log_entry_present(self):
        assert "## #924 Type C:" in self._log()

    def test_log_mechanism_number_and_topic(self):
        log = self._log()
        idx = log.index("## #924 Type C:")
        entry = log[idx:idx + 9000]
        assert "mechanism 786" in entry
        assert "Cloudflare" in entry
        assert "Disallow AI Training" in entry

    def test_sep_22_2026_is_tuesday(self):
        import datetime

        assert datetime.date(2026, 9, 22).strftime("%A") == "Tuesday"
