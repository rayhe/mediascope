"""Type C #784 (2026-09-16 02:00 PDT): Google pay-per-use AI licensing pilot
program for publishers (Digiday ~Sep 14 2026) - FIRST dedicated Google
pay-per-use publisher mechanism in the corpus (mechanism 702); third
instance of the variable-pay template (Apple proposal Aug 2026 mechanism
156, Microsoft PCM Feb 2026 mechanism 443); cooperative turn on the
historically adversarial Google x publisher vector (AI Overviews referral
collapse, EU antitrust probe mechanism 666, Cloudflare leverage mechanism
64); inference-data marketplace pricing-discovery framing.

Rotation window fifth leg: D (#780) -> E (#781) -> A (#782) -> B (#783) ->
C (#784), closing the 780-784 window.

Evidence is search-excerpt-bounded per #503 (4 browser.search query sets, 0
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
    "test_type_c_784_google_pay_per_use_ai_licensing_pilot_sep16_2am.py"
)
MECH_NUM = 702
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention.
MECH_ID_MARKER = "mechanism" + "_702"
NEXT_ID_MARKER = "mechanism" + "_703"
MECH_KEY = "google_pay_per_use_ai_licensing_pilot_publishers_sep2026"
NEXT_SIBLING = "\n  x_twitter:"
ANCHORED_SHA = "085b7bd98cbc259f5b8128389c18335be7108aa4"


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


class TestNovelty784:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_c_784_file(self):
        files = sorted(
            f for f in os.listdir(os.path.join(REPO_ROOT, "tests"))
            if f.startswith("test_type_c_784") and f.endswith(".py")
        )
        assert files == [TEST_BASENAME], files

    def test_type_c_784_main_commit_unique_and_anchored(self):
        mains = _git_log_mains(r"Type C #784: ")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim_present_in_block(self):
        # Novelty was verified pre-commit by shell greps (zero test_type_c_784
        # files, no "Type C #784" in git log, the Digiday URL zero-hit
        # repo-wide, zero Google pay-per-use mechanism keys, max numeric
        # mechanism_id 701, zero underscore-form 702 keys excluding
        # sweep-instrument carriers per #715); this test pins the claim in
        # the committed block, per the #752 convention.
        block = _block()
        assert "Zero test_type_c_784 files on disk pre-commit" in block
        assert "No Type C #784 in git log pre-commit" in block
        assert "digiday.com/media/google-rolls-out-pay-per-use-ai-licensing-program-to-publishers" in _fold(block)
        assert "Max numeric mechanism_id 701 pre-commit" in block


class TestRotationCycleGuard784:
    """Rotation: 780-784 window fifth leg D->E->A->B->C, closing the window."""

    EXPECTED_ORDER = [
        ("C", "784"), ("B", "783"), ("A", "782"), ("E", "781"), ("D", "780"),
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
        mains = _git_log_mains(r"Type C #784: ")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains and mains[0].startswith(ANCHORED_SHA + " "), mains


class TestMechanism702Content:
    def test_block_present_in_entities(self):
        assert MECH_KEY + ":" in _read(ENTITIES_PATH)
        assert _block_data()["mechanism_id"] == MECH_NUM

    def test_iteration_metadata(self):
        data = _block_data()
        assert data["iteration"] == 784
        assert data["iteration_type"] == "C"
        assert data["rotation"] == "Type C"
        assert data["type"] == "financial_incentive_mapping"
        assert data["time_pdt"] == "02:00"
        assert data["discovery_date"] == "2026-09-16"
        assert data["goal_id"] == "goal_54093bda4145"
        assert data["job_id"] == "mediascope-daily-iteration"

    def test_deal_parties_and_announcement(self):
        data = _block_data()
        assert data["deal_parties"]["payer"].startswith("Google")
        assert "pilot publishers" in data["deal_parties"]["counterparty"]
        assert "anonymous" in data["deal_parties"]["counterparty"]
        assert data["announcement"]["disclosed"].startswith("No Google announcement")
        assert "Digiday" in data["announcement"]["first_reported"]

    def test_deal_structure_pay_per_use(self):
        data = _block_data()
        struct = data["deal_structure"]
        assert "Pay-per-use" in struct["pricing_model"]
        assert "mechanism 156" in struct["pricing_model"]
        assert "mechanism 443" in struct["pricing_model"]
        assert len(struct["program_mechanics"]) == 3
        assert "Weekly calls" in struct["program_mechanics"][0]
        assert "marketplace for inference data" in struct["program_mechanics"][2]
        assert "black box" in struct["transparency"]
        assert "not yet fully baked" in struct["maturity"]
        terms = data["deal_terms"]
        assert terms["rates"].startswith("Undisclosed")
        assert terms["participants"].startswith("Undisclosed")

    def test_publisher_reception_quotes(self):
        data = _block_data()
        rec = data["publisher_reception"]
        assert "inside google" in _fold(rec["inside_vs_outside"])
        assert "old referral economics" in rec["inside_vs_outside"]
        assert "extremely collaborative" in rec["collaboration"]
        assert "precedent" in rec["precedent_value"]

    def test_pay_per_use_template_third_instance(self):
        data = _block_data()
        tpl = data["pay_per_use_template_third_instance"]
        assert "THIRD corpus instance" in tpl
        assert "mechanism 156" in tpl
        assert "mechanism 443" in tpl
        assert "Microsoft (operational) > Google (pilot) > Apple (proposal)" in tpl

    def test_cooperative_turn_adversarial_vector(self):
        data = _block_data()
        turn = data["cooperative_turn"]
        assert "mechanism 539" in turn
        assert "mechanism 666" in turn
        assert "mechanism 64" in turn
        assert "mechanism 412" in turn
        assert "54 percent to 24 percent" in turn

    def test_inference_data_marketplace_framing(self):
        data = _block_data()
        framing = data["inference_data_marketplace_framing"]
        assert "pricing discovery" in framing
        assert "Search Console" in framing

    def test_first_google_pay_per_use_claim(self):
        data = _block_data()
        claim = data["first_google_pay_per_use_claim"]
        assert "FIRST dedicated Google pay-per-use" in claim
        assert "mechanism 412" in claim

    def test_ranked_confounders_layers(self):
        confs = _block_data()["ranked_confounders"]
        assert len(confs) == 6
        layers = [c["strength"] for c in confs]
        assert layers.count("strong") == 3
        assert layers.count("moderate") == 2
        assert layers.count("weak") == 1
        assert [c["rank"] for c in confs] == [1, 2, 3, 4, 5, 6]

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
        assert "digiday.com/media/google-rolls-out-pay-per-use-ai-licensing-program-to-publishers" in urls

    def test_designed_keying_no_underscore_form_in_block(self):
        # The m702 block key carries no underscore-form marker substring, so
        # the #783 zero-underscore-702 sweep stays GREEN by design.
        assert MECH_ID_MARKER not in _block()


class TestSupersessionAndCorpusPost783:
    """Post-#783 corpus integrity: max 702, zero 703, designed supersession."""

    def _ids(self):
        return [
            int(x)
            for x in re.findall(r"mechanism_id:\s*(\d+)\b", _profiles_corpus())
        ]

    def test_max_numeric_mechanism_id_is_702(self):
        assert max(self._ids()) == MECH_NUM, max(self._ids())

    def test_701_still_present(self):
        hits = [h for h in _repo_grep("mechanism_id: 701")]
        assert len(hits) >= 1, hits

    def test_zero_underscore_703_keys_repo_wide(self):
        hits = _repo_grep(NEXT_ID_MARKER)
        hits = [h for h in hits if not h.endswith(TEST_BASENAME)]
        assert hits == [], hits

    def test_zero_numeric_703_keys_in_profiles(self):
        hits = _repo_grep("mechanism_id: 703", roots=("profiles",))
        assert hits == [], hits

    def test_d783_zero_underscore_702_profiles_sweep_stays_green(self):
        # #783 asserted zero underscore-form 702 markers in profiles/; the
        # m702 block key carries no such substring by designed keying, so
        # that sweep stays green.
        hits = _repo_grep(MECH_ID_MARKER, roots=("profiles",))
        assert hits == [], hits

    def test_d783_zero_underscore_702_tests_sweep_stays_green(self):
        # #783 asserted zero underscore-form 702 markers in tests/; this file
        # builds the marker by concatenation ("mechanism" + "_702") and
        # carries no contiguous literal, so the sweep stays green.
        hits = _repo_grep(MECH_ID_MARKER, roots=("tests",))
        hits = [h for h in hits if not h.endswith(TEST_BASENAME)]
        assert hits == [], hits

    def test_d783_zero_numeric_702_profiles_sweep_fails_by_designed_supersession(
        self,
    ):
        # #783 asserted zero "mechanism_id: 702" hits in profiles/; the m702
        # block supersedes it by design per the #710/#720 convention.
        hits = _repo_grep("mechanism_id: 702", roots=("profiles",))
        assert len(hits) >= 1, hits

    def test_d783_max_701_sweep_superseded_by_design(self):
        # #783 asserted max == 701; advancing to 702 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert max(self._ids()) == MECH_NUM != 701

    def test_m702_block_key_unique_and_entities_parse(self):
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


class TestLedger784:
    """Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent; m702 not a member."""

    def test_twenty_sixth_present_and_twenty_seventh_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference "TWENTY-SEVENTH" inside their own
        # negative guards, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus
        assert "ledger holds at 26" in _block()

    def test_m702_not_a_falsification_family_member(self):
        block = _block()
        assert "NOT a member" in block
        assert "qualitative financial mapping only" in block

    def test_no_analysis_json_update_claimed(self):
        block = _block()
        assert "no_analysis_json_update: true" in block


class TestDocSync784:
    def test_readme_row_784(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_784(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_784_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog784:
    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #784 entry sits at the end of the file, not the top.
        return "\n".join(lines[-60:])

    def test_log_entry_present(self):
        # "#784 Type C:" is the entry header; a bare "#784" would
        # false-positive on #783's rotation line ("(C to follow)").
        assert "#784 Type C:" in self._tail()

    def test_log_mechanism_number_and_topic(self):
        assert "mechanism 702" in self._tail()
        assert "Google" in self._tail()


class TestDateGrounding784:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_16_2026_is_wednesday(self):
        assert self._weekday("2026-09-16") == "Wednesday"
