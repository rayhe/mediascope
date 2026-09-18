"""Type C #829 (2026-09-18 08:00 PDT): Snap Specs Sep-16-2026 enterprise
partnership stack - first dedicated financial-incentive graph-expansion
mechanism for the launch (mechanism 729); four new Snap edges (Salesforce
Agentforce, Nvidia XR AI, AWS assistant, Verizon exclusive cellular) intersect
four pre-existing publisher orbits (Amazon licensing/ad orbit via the AWS leg,
Benioff-TIME owner-equity chain via the Salesforce leg, Verizon-retained-10pct
Yahoo-stake orbit via the Verizon leg, Nvidia null leg).

Rotation window fifth leg: D (#825) -> E (#826) -> A (#827) -> B (#828) ->
C (#829), CLOSING the 825-829 window.

Evidence: 3 browser.search query sets this run, 0 browser.open first-hand
reads; all facts via search-result excerpts (second-hand per #503); all
5 source URLs copied verbatim from search-result Full-URL listings; no
canonical URLs constructed. Statistical discipline per the qualitative Type C
convention: p_value/cohens_d/ci_95 NOT_CALCULATED, tone_scores NOT_SCORED,
is_significant False, engine NOT run; verdict directionally_supported_not_proven;
the TechCrunch-leg prediction failure (Ropek Sep 16 adversarial -0.45, m728) is
carried as a scope bound inside this new mechanism, NOT a falsification-family
member (ledger holds at 26); no analysis.json update.

Deselected pre-commit per the #565 convention: novelty anchor 1 + rotation
anchor 2 (test_window_closes_deabc, test_anchor_sha_matches_head - patched green
in the anchor followup); doc-sync 3 + iteration-log 2 fail by design pre-commit,
go green in the doc-sync followup.

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
    "test_type_c_829_snap_specs_enterprise_partnership_stack_sep18_8am.py"
)
MECH_NUM = 729
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention.
MECH_ID_MARKER = "mechanism" + "_729"
NEXT_ID_MARKER = "mechanism" + "_730"
NEXT_ID_NUMERIC = "mechanism_id: 730"
MECH_KEY = "snap_specs_enterprise_partnership_stack_sep2026"
URL_REUTERS = "https://www.reuters.com/business/snap-targets-enterprises-with-salesforce-nvidia-ai-tools-augmented-reality-2026-09-16/"
URL_TECHCRUNCH = "https://techcrunch.com/2026/09/16/snap-tries-to-make-the-case-again-for-its-2200-smart-glasses/"
URL_VERIZON = "https://www.verizon.com/about/news/verizon-specs-5g-ar-glasses-bundle"
URL_FOURWEEKMBA = "https://fourweekmba.com/ai-snap-specs-intelligence-enterprise-partners/"
URL_TIMES = "https://www.thetimes.com/business/companies-markets/article/evan-spiegel-specs-augmented-reality-glasses-7bmpm6sgl"
NEXT_SIBLING = "\nadvance_dual_asset_monetization:"
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


class TestNovelty829:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_c_829_file(self):
        files = sorted(
            str(p) for p in TESTS_DIR.glob("test_type_c_829*.py")
        )
        assert len(files) == 1, files
        assert files[0].endswith(TEST_BASENAME), files

    def test_type_c_829_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type C #829")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_novelty_verification_claim_present_in_block(self):
        # The block pins the pre-commit novelty greps (zero Trifork /
        # Hololight / Specs for Enterprise / Charging Case with Cellular /
        # Amazon Quick hits repo-wide; 3 of 5 source URLs zero-hit with the
        # Reuters Sep 16 and TechCrunch Sep 16 URLs already in corpus as
        # m727/m728 context; max numeric mechanism_id 728); this test pins
        # the claim in the committed block, per the #752 convention.
        block = _block()
        assert "test_type_c_829" in block
        assert "zero Trifork / Hololight / Specs for Enterprise" in block
        assert "max numeric mechanism_id 728 pre-commit" in block


# --- Rotation cycle guard ---------------------------------------------------


class TestRotationCycleGuard829:
    """Rotation: 825-829 window fifth leg D->E->A->B->C, closing the window."""

    EXPECTED_ORDER = [
        ("C", "829"), ("B", "828"), ("A", "827"), ("E", "826"), ("D", "825"),
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
        # Deselected pre-commit per the #565 convention: the #829 main commit
        # does not exist in history yet; patched green in the anchor followup.
        assert self._window() == self.EXPECTED_ORDER

    def test_window_cycle_edges_are_adjacent(self):
        window = self._window()
        for (t1, _), (t2, _) in zip(window, window[1:]):
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        # Deselected pre-commit per the #565 convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        )
        # Durable post-commit: the anchored main commit is in history and its
        # subject opens the #829 window-closing leg (HEAD drifts past it with
        # the anchor/doc-sync/push-status followups, per the #565 convention).
        res = _run_git("log", "--format=%H %s", "--all")
        hits = [l for l in res.stdout.splitlines()
                if l.startswith(ANCHORED_SHA + " ")]
        assert len(hits) == 1, hits
        assert "Type C #829: " in hits[0], hits


# --- Mechanism content -------------------------------------------------------


class TestMechanism729Content:
    def test_block_present_in_entities(self):
        block = _block()
        assert block.strip().startswith(MECH_KEY + ":")

    def test_iteration_metadata(self):
        data = _block_data()
        assert data["mechanism_id"] == MECH_NUM
        assert data["iteration"] == 829
        assert data["iteration_type"] == "C"
        assert data["date_analyzed"] == "2026-09-18"
        assert data["time_pdt"] == "08:00"
        assert data["job_id"] == "mediascope-daily-iteration"

    def test_partnership_facts(self):
        data = _block_data()
        pf = data["partnership_facts"]
        assert "September 16 2026" in pf["announced"]
        assert "Agentforce" in pf["salesforce_agentforce"]
        assert "XR AI platform" in pf["nvidia_xr_ai"]
        assert "voice commands" in pf["aws_assistant"]
        assert "Exclusive US partnership" in pf["verizon_exclusive"]
        assert "did not disclose the financial terms" in pf["terms"]
        assert "Trifork" in pf["terms"]
        assert "Hololight" in pf["terms"]
        assert "have not shipped" in pf["architecture_not_business"]
        assert "No revenue figure exists" in pf["architecture_not_business"]

    def test_orbit_intersections(self):
        data = _block_data()
        oi = data["orbit_intersections"]
        assert "$20-25M per year" in oi["aws_x_amazon_orbit"]
        assert "Rufus" in oi["aws_x_amazon_orbit"]
        assert "mechanism 36" in oi["salesforce_x_benioff_time"]
        assert "owns TIME outright" in oi["salesforce_x_benioff_time"]
        assert "10 percent" in oi["verizon_x_yahoo_stake"]
        assert "TechCrunch and Engadget" in oi["verizon_x_yahoo_stake"]
        assert "no incentive edge asserted" in oi["nvidia_null_leg"]

    def test_coverage_observations(self):
        data = _block_data()
        co = data["coverage_observations"]
        assert "zero standalone Sep 16 launch pieces (m727)" in co["wired_zero"]
        assert "bounded absence" in co["nyt_bounded_absence"]
        assert "mechanism 113" in co["engadget_consistent"]
        assert "-0.45" in co["techcrunch_prediction_failed"]
        assert "scope bound" in co["techcrunch_prediction_failed"]
        assert "Irenic Capital" in co["times_london_not_soft"]
        assert "$5.96" in co["times_london_not_soft"]

    def test_source_urls_verbatim(self):
        data = _block_data()
        assert data["sources"][0].startswith(URL_REUTERS)
        assert data["sources"][1].startswith(URL_TECHCRUNCH)
        assert data["sources"][2].startswith(URL_VERIZON)
        assert data["sources"][3].startswith(URL_FOURWEEKMBA)
        assert data["sources"][4].startswith(URL_TIMES)
        assert len(data["sources"]) == 5

    def test_meta_zero(self):
        data = _block_data()
        ov = _fold(data["overview"])
        assert "no coverage-tone claim is made" in ov
        assert "correlation is not causation" in ov


# --- Statistical discipline ---------------------------------------------------


class TestStatisticalDiscipline829:
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
        assert MECH_KEY.count("_" + "729") == 0

    def test_ranked_confounders_and_counterargument(self):
        data = _block_data()
        conf = data["confounders_ranked"]
        assert len(conf) == 6
        assert [c["strength"] for c in conf] == [
            "STRONG", "STRONG", "STRONG", "MODERATE", "MODERATE", "WEAK",
        ]
        assert "strongest_counterargument" in data
        assert "TechCrunch leg itself" in data["strongest_counterargument"]


# --- Supersession and corpus post-#828 --------------------------------------


class TestSupersessionAndCorpusPost828:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout))

    def test_corpus_max_is_729(self):
        assert max(self._numeric_ids()) == 729

    def test_iteration_828_max_728_sweep_superseded_by_design(self):
        # #828's max-728 sweeps fail by designed supersession now that 729 exists.
        assert max(self._numeric_ids()) != 728

    def test_zero_underscore_730_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_730_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_828_zero_underscore_729_sweep_stays_green(self):
        # The #828 zero-underscore-729 sweeps stay green post-#829 by designed keying:
        # neither the profile block nor this test file carries a literal underscore-729 key.
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", MECH_ID_MARKER, "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), \
                "literal underscore-729 key leaked into %s" % root

    def test_iteration_828_zero_numeric_729_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 729", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected #828's zero-numeric-729 sweep to fail by designed supersession"

    def test_numeric_729_keys_in_exactly_the_designed_location(self):
        res = _run_git("grep", "-r", "mechanism_id: 729", "--", "profiles/")
        hits = [l for l in res.stdout.strip().splitlines() if l.strip()]
        # Designed keying: one numeric 729 key in the marketplace
        # intermediary landscape block; no other profiles/ location.
        assert len(hits) == 1, "unexpected numeric 729 key spread in profiles/: %s" % hits
        assert "profiles/competitor-entities.yaml" in hits[0]

    def test_iteration_827_zero_underscore_728_sweep_stays_green(self):
        # The #827 zero-underscore-728 sweeps stay green post-#829 by designed keying:
        # profiles/ carries zero literal underscore-728 keys, and the only
        # tests/ carrier is the #828 file's own sweep needle (excluded as sweep
        # carrier per the #715 convention, as #828's own sweep does).
        res = _run_git("grep", "-r", "mechanism" + "_728", "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip(), \
            "literal underscore-728 key leaked into profiles/"
        res = _run_git("grep", "-rl", "mechanism" + "_728", "--", "tests/")
        carriers = [l for l in res.stdout.strip().splitlines() if l.strip()]
        assert carriers == [
            "tests/test_type_b_828_lucas_ropek_techcrunch_snap_jun16_sep16_register_shift_sep18_7am.py"
        ], "unexpected underscore-728 carriers in tests/: %s" % carriers


# --- Ledger -----------------------------------------------------------------


def _profiles_corpus():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith((".yaml", ".yml", ".md")):
                out.append(_read(os.path.join(root, fn)))
    return "\n".join(out)


class TestLedger829:
    def test_twenty_sixth_present_and_twenty_seventh_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference "TWENTY-SEVENTH" inside their own
        # negative guards, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus
        assert "ledger holds at 26" in _block()

    def test_m729_block_key_unique_and_entities_parse(self):
        import yaml

        doc = yaml.safe_load(_read(ENTITIES_PATH))
        assert doc["marketplace_intermediary_landscape"][MECH_KEY]["mechanism_id"] == 729
        keys = [
            k for k in doc["marketplace_intermediary_landscape"] if k == MECH_KEY
        ]
        assert len(keys) == 1

    def test_m729_not_a_falsification_family_member(self):
        data = _block_data()
        assert data["falsification_family"].startswith("NOT a member")

    def test_no_analysis_json_update_claimed(self):
        data = _block_data()
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False
        assert data["verdict"] == "directionally_supported_not_proven"


# --- Doc-sync ----------------------------------------------------------------


class TestDocSync829:
    def test_readme_row_829(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_829(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_829_file(self):
        text = _read(ARCH_PATH)
        assert "tests/" + TEST_BASENAME in text


# --- Iteration log ------------------------------------------------------------


class TestIterationLog829:
    def _log(self):
        return _read(LOG_PATH)

    def test_log_entry_present(self):
        assert "## #829 Type C:" in self._log()

    def test_log_mechanism_number_and_topic(self):
        log = self._log()
        idx = log.index("## #829 Type C:")
        entry = log[idx:idx + 8000]
        assert "mechanism 729" in entry
        assert "Snap" in entry
        assert "enterprise partnership" in entry

    def test_sep_18_2026_is_friday(self):
        import datetime

        assert datetime.date(2026, 9, 18).strftime("%A") == "Friday"
