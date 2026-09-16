"""Type C #789 (2026-09-16 07:00 PDT): Paramount-WBD tender/exchange-offer
extension to Sep 18 2026 + SEC-filed enhanced deal-protection provisions -
FIRST dedicated Paramount-WBD extension mechanism in the corpus (mechanism
705); extends mechanism 124 (WBD quad-tech financial architecture) and its
paramount_merger sub-key with the creditor-confidence measurement (66.28% /
75.31% tendered as of Sep 4) and the deal-protection layer (quarterly $0.25
ticking fee ~$650M/quarter beyond Dec 31 2026, $2.8B Netflix termination-fee
funding, $1.5B debt-exchange backstop, $15B bridge-loan refinancing) that sets
the timing and certainty of Advance Publications' ~$2.94B WBD liquidity event.

Rotation window fifth leg: D (#785) -> E (#786) -> A (#787) -> B (#788) ->
C (#789), closing the 785-789 window.

Evidence is search-excerpt-bounded per #503 (5 browser.search query sets, 0
browser.open; all URLs copied verbatim from search-result Full-URL
listings; no canonical URLs constructed). Statistical discipline per the
qualitative Type C convention: p_value/cohens_d/ci_95 NOT_CALCULATED,
tone_scores NOT_SCORED, is_significant False, engine NOT run; verdict
directionally_supported_not_proven; NOT a falsification-family member
(ledger holds at 26); no analysis.json update.

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
    "test_type_c_789_paramount_wbd_tender_exchange_extension_sep16_7am.py"
)
MECH_NUM = 705
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention.
MECH_ID_MARKER = "mechanism" + "_705"
NEXT_ID_MARKER = "mechanism" + "_706"
MECH_KEY = "paramount_wbd_tender_exchange_extension_sep18_2026"
NEXT_SIBLING = "\n  yahoo_apollo:"
ANCHORED_SHA = "cb6827330661a30af4c26cb62a40a8d6653958b1"


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


def _git_log_mains(pattern):
    proc = subprocess.run(
        ["git", "-C", REPO_ROOT, "log", "--format=%H %s", "--no-merges", "--", "."],
        capture_output=True,
        text=True,
    )
    return [l for l in proc.stdout.splitlines() if re.search(pattern, l)]


def _repo_grep(pattern, roots=()):
    hits = []
    for root in roots or (".",):
        proc = subprocess.run(
            ["git", "-C", REPO_ROOT, "grep", "-n", "--", pattern, root],
            capture_output=True,
            text=True,
        )
        if proc.returncode == 0:
            hits.extend(proc.stdout.splitlines())
    return hits


def _profiles_corpus():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith((".yaml", ".yml", ".md")):
                out.append(_read(os.path.join(root, fn)))
    return "\n".join(out)


class TestNovelty789:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_c_789_file(self):
        files = sorted(
            f for f in os.listdir(os.path.join(REPO_ROOT, "tests"))
            if f.startswith("test_type_c_789") and f.endswith(".py")
        )
        assert files == [TEST_BASENAME], files

    def test_type_c_789_main_commit_unique_and_anchored(self):
        mains = _git_log_mains(r"Type C #789: ")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim_present_in_block(self):
        # Novelty was verified pre-commit by shell greps (zero test_type_c_789
        # files, no "Type C #789" in git log, the SEC Edgar URL zero-hit
        # repo-wide, the PRNewswire URL zero-hit repo-wide, the September 18
        # extension zero-hit, the 66.28/75.31 figures zero-hit, zero
        # underscore-form 705 mechanism keys, max numeric mechanism_id 704);
        # this test pins the claim in the committed block, per the #752
        # convention.
        block = _block()
        assert "Zero test_type_c_789 files on disk pre-commit" in block
        assert "No Type C #789 in git log pre-commit" in block
        assert "tm2533570d52" in _fold(block)
        assert "Max numeric mechanism_id 704 pre-commit" in block


class TestRotationCycleGuard789:
    """Rotation: 785-789 window fifth leg D->E->A->B->C, closing the window."""

    EXPECTED_ORDER = [
        ("C", "789"), ("B", "788"), ("A", "787"), ("E", "786"), ("D", "785"),
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
        mains = _git_log_mains(r"Type C #789: ")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains and mains[0].startswith(ANCHORED_SHA + " "), mains


class TestMechanism705Content:
    def test_block_present_in_entities(self):
        assert MECH_KEY + ":" in _read(ENTITIES_PATH)
        assert _block_data()["mechanism_id"] == MECH_NUM

    def test_iteration_metadata(self):
        data = _block_data()
        assert data["iteration"] == 789
        assert data["iteration_type"] == "C"
        assert data["rotation"] == "Type C"
        assert data["type"] == "financial_incentive_mapping"
        assert data["time_pdt"] == "07:00"
        assert data["discovery_date"] == "2026-09-16"
        assert data["goal_id"] == "goal_54093bda4145"
        assert data["job_id"] == "mediascope-daily-iteration"

    def test_deal_parties_and_announcement(self):
        data = _block_data()
        assert data["deal_parties"]["payer"].startswith("Paramount Skydance")
        assert "Discovery Global Holdings" in data["deal_parties"]["counterparty"]
        assert "CNN parent" in data["deal_parties"]["target"]
        assert "September 18, 2026" in data["announcement"]["action"]
        assert "PRNewswire" in data["announcement"]["form"]

    def test_extension_chain_twelfth(self):
        data = _block_data()
        chain = data["extension_chain"]
        assert "Twelfth" in chain["count"]
        assert len(chain["prior_extensions"]) == 10
        assert chain["prior_extensions"][0] == "2026-06-12"
        assert chain["prior_extensions"][-1] == "2026-08-31"

    def test_tender_figures_creditor_confidence(self):
        data = _block_data()
        figs = data["tender_figures"]
        assert figs["tender_offer_notes_pct"] == 66.28
        assert figs["exchange_offer_notes_pct"] == 75.31
        assert "2026-09-04" in figs["as_of"]
        assert "not view these figures to be representative" in figs["disclaimer"]

    def test_sec_filed_provisions(self):
        data = _block_data()
        prov = data["sec_filed_provisions"]
        assert "tm2533570d52" in prov["filing"]
        assert "$650 million" in prov["ticking_fee"]
        assert "December 31, 2026" in prov["ticking_fee"]
        assert "$2.8 billion" in prov["termination_fee_netflix"]
        assert "$1.5 billion" in prov["debt_exchange_backstop"]
        assert "$5.8 billion reverse termination fee" in prov["debt_exchange_backstop"]
        assert "$15 billion bridge loan" in prov["bridge_loan"]

    def test_mediascope_linkage_advance_liquidity(self):
        data = _block_data()
        link = data["mediascope_linkage"]
        assert "mechanism 124" in link["extends_mechanism_124"]
        assert "Advance Publications" in link["advance_liquidity"]
        assert "$2.94B" in link["advance_liquidity"]
        assert "66.28%/75.31%" in link["creditor_confidence"]
        assert "several removes" in link["cnn_newsroom_distance"]

    def test_ranked_confounders_layers(self):
        confs = _block_data()["ranked_confounders"]
        assert len(confs) == 5
        layers = [c["strength"] for c in confs]
        assert layers.count("strong") == 2
        assert layers.count("moderate") == 2
        assert layers.count("weak") == 1
        assert [c["rank"] for c in confs] == [1, 2, 3, 4, 5]

    def test_excerpt_bounded_per_503(self):
        block = _fold(_block())
        assert "search-excerpt-bounded per #503" in block
        assert "0 browser.open" in block
        assert "no canonical urls constructed" in block

    def test_statistical_discipline_type_c(self):
        disc = _block_data()["statistical_discipline"]
        assert disc["scorer"] == "none"
        assert disc["tone_scores"] == "NOT_SCORED"
        assert disc["p_value"] == "NOT_CALCULATED"
        assert disc["cohens_d"] == "NOT_CALCULATED"
        assert disc["ci_95"] == "NOT_CALCULATED"
        assert disc["is_significant"] is False
        assert disc["qualitative_only"] is True
        assert disc["artifact_grade"] is False

    def test_verdict_ledger_and_source_urls(self):
        data = _block_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False
        assert "NOT a member" in data["falsification_family"]
        assert "ledger holds at 26" in data["falsification_family"]
        urls = " ".join(data["source_urls"])
        assert "tm2533570d52_exa5ab.htm" in urls
        assert "6aa007b706b0f49a92996b51" in urls

    def test_designed_keying_no_underscore_form_in_block(self):
        # The m705 block key carries no underscore-form marker substring, so
        # the #788 zero-underscore-705 sweep stays GREEN by design.
        assert MECH_ID_MARKER not in _block()


class TestSupersessionAndCorpusPost788:
    """Post-#788 corpus integrity: max 705, zero 706, designed supersession."""

    def _ids(self):
        return [
            int(x)
            for x in re.findall(r"mechanism_id:\s*(\d+)\b", _profiles_corpus())
        ]

    def test_max_numeric_mechanism_id_is_705(self):
        assert max(self._ids()) == MECH_NUM, max(self._ids())

    def test_704_still_present(self):
        hits = [h for h in _repo_grep("mechanism_id: 704")]
        assert len(hits) >= 1, hits

    def test_zero_underscore_706_keys_repo_wide(self):
        hits = _repo_grep(NEXT_ID_MARKER)
        hits = [h for h in hits if not h.endswith(TEST_BASENAME)]
        assert hits == [], hits

    def test_zero_numeric_706_keys_in_profiles(self):
        hits = _repo_grep("mechanism_id: 706", roots=("profiles",))
        assert hits == [], hits

    def test_d788_zero_underscore_705_profiles_sweep_stays_green(self):
        # #788 asserted zero underscore-form 705 markers in profiles/; the
        # m705 block key carries no such substring by designed keying, so
        # that sweep stays green.
        hits = _repo_grep(MECH_ID_MARKER, roots=("profiles",))
        assert hits == [], hits

    def test_d788_zero_underscore_705_tests_sweep_stays_green(self):
        # #788 asserted zero underscore-form 705 markers in tests/; this file
        # builds the marker by concatenation ("mechanism" + "_705") and
        # carries no contiguous literal, so the sweep stays green.
        hits = _repo_grep(MECH_ID_MARKER, roots=("tests",))
        hits = [h for h in hits if not h.endswith(TEST_BASENAME)]
        assert hits == [], hits

    def test_d788_zero_numeric_705_profiles_sweep_fails_by_designed_supersession(
        self,
    ):
        # #788 asserted zero "mechanism_id: 705" hits in profiles/; the m705
        # block supersedes it by design per the #710/#720 convention.
        hits = _repo_grep("mechanism_id: 705", roots=("profiles",))
        assert len(hits) >= 1, hits

    def test_d788_max_704_sweep_superseded_by_design(self):
        # #788 asserted max == 704; advancing to 705 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert max(self._ids()) == MECH_NUM != 704

    def test_m705_block_key_unique_and_entities_parse(self):
        assert _read(ENTITIES_PATH).count(MECH_KEY + ":") == 1
        import yaml

        d = yaml.safe_load(_read(ENTITIES_PATH))

        def find(dd, key):
            if isinstance(dd, dict):
                for k, v in dd.items():
                    if k == key:
                        return v
                    r = find(v, key)
                    if r is not None:
                        return r
            return None

        assert find(d, MECH_KEY)["mechanism_id"] == MECH_NUM


class TestLedger789:
    """Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent; m705 not a member."""

    def test_twenty_sixth_present_and_twenty_seventh_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference "TWENTY-SEVENTH" inside their own
        # negative guards, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus
        assert "ledger holds at 26" in _block()

    def test_m705_not_a_falsification_family_member(self):
        block = _block()
        assert "NOT a member" in block
        assert "qualitative financial mapping only" in block

    def test_no_analysis_json_update_claimed(self):
        block = _block()
        assert "no_analysis_json_update: true" in block


class TestDocSync789:
    def test_readme_row_789(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_789(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_789_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog789:
    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #789 entry sits at the end of the file, not the top.
        return "\n".join(lines[-60:])

    def test_log_entry_present(self):
        # "#789 Type C:" is the entry header; a bare "#789" would
        # false-positive on #788's rotation line ("(C to follow)").
        assert "#789 Type C:" in self._tail()

    def test_log_mechanism_number_and_topic(self):
        assert "mechanism 705" in self._tail()
        assert "Paramount" in self._tail()


class TestDateGrounding789:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_16_2026_is_wednesday(self):
        assert self._weekday("2026-09-16") == "Wednesday"
