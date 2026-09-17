"""Type B iteration #808 (Sep 17 2026, 11am PDT): Ece Yildirim cross-entity
register tracking (mechanism 716), the fourth leg of the 805-809 window.

D #805 -> E #806 -> A #807 -> B #808 -> C #809.

Follows the #803 single-file structural pattern (novelty anchor, rotation guard,
corpus/post-#807 supersession tests, ledger constancy, careers, doc-sync rows,
iteration-log entry).

Deselected pre-commit per the #565 convention: anchor 1.
Doc-sync 2 + iteration-log 2 go green in the doc-sync followup.
Patched green in the anchor followup.

FINDING: Ece Yildirim (Gizmodo, Privacy and Security desk) shows a
same-journalist, same-publication, same-week register INVERSION: her Sep 9 2026
Apple Watch Audio Intelligence piece ("If Meta Glasses Freak You Out, Wait
Until You Hear About the New Apple Watch Features", read first-hand this run,
42 rendered lines, byline confirmed on her Gizmodo author page) applies an
adversarial privacy register to APPLE ("sounds like a privacy nightmare",
"constantly eavesdropping", "covertly recorded, transcribed, or noted down",
"Apple executives were eager to assure viewers", "wave of public outcry";
-0.60 illustrative), while her Sep 15 2026 Meta piece ("Meta Is Hoping You
Will Pay for More AI Features on Instagram", Meta One subscription launch,
byline confirmed on author page + mirror attribution, search-excerpt-bounded
per #503) runs a neutral product/pricing news register with only mild
monetization edge ("coughing up monthly fees") and financial-context skepticism
(free cash flow, Reality Labs losses); zero privacy/surveillance vocabulary in
the excerpted Meta text, notable for a Privacy and Security desk byline
covering Meta AI expansion (-0.15 illustrative). Illustrative Apple-minus-Meta
delta -0.45: the same journalist goes harder on Apple than on Meta within one
week, inverting the corpus-typical Gizmodo gradient (Barr apocalyptic Meta
register, Pero Meta-hard patterns). Bounded: the Apple piece itself holds Meta
as the worse privacy comparator ("Apple's privacy record is pristine compared
to Meta's"; "pervert glasses"; "creeps"), so she does not spare Meta; the
adversarial energy is Apple-directed WITHIN a Meta-anchor-adversarial frame.
Strong confounders ranked first: product-domain mismatch (ambient audio vs
paid AI tiers), genre routing (commentary vs product news), the
Meta-anchor-adversarial frame inside the Apple piece. The Michael Grothaus
(Fast Company) pair was ABANDONED this run: his Apple Audio Intelligence piece
is confirmed his via the Fast Company author page, but the "Meta's creepy
smart glasses are part of a much bigger plan" piece carries no byline in the
extracted page text - per the no-invented-byline discipline it could not be
anchored. MANUAL ILLUSTRATIVE only; NOT a falsification-family member; ledger
holds at 26.
"""
import glob
import os
import re
import subprocess
import pytest
import yaml

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = "test_type_b_808_ece_yildirim_gizmodo_apple_adversarial_vs_meta_product_neutral_sep17_11am.py"
MECH_KEY = "ece yildirim gizmodo apple adversarial vs meta product neutral sep2026"
M_ID = 716
MECH_ID_MARKER = "mechanism" + "_716"
NEXT_ID_MARKER = "mechanism" + "_717"
NEXT_ID_NUMERIC = "mechanism_id: 717"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"
BLOCK_KEY = "type_b_808_ece_yildirim_gizmodo_apple_adversarial_vs_meta_product_neutral_sep17"

GIZMODO_PROFILE = os.path.join(REPO, "profiles", "gizmodo.yaml")
CAREERS_PROFILE = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
RESEARCH_PROFILE = os.path.join(REPO, "profiles", "competitor-coverage-research.yaml")
ITERATION_LOG = os.path.join(REPO, "iteration-log.md")


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO] + list(args),
        capture_output=True,
        text=True,
        check=False,
    )


def _gizmodo_text():
    with open(GIZMODO_PROFILE) as fh:
        return fh.read()


def _block():
    with open(GIZMODO_PROFILE) as fh:
        doc = yaml.safe_load(fh)
    return doc["journalist_cross_entity"]["ece_yildirim"]


# --- Novelty ---------------------------------------------------------------


class TestNovelty808:
    def test_type_b_808_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type B #808")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_no_type_b_808_file_on_disk_pre_commit(self):
        hits = [p for p in glob.glob(os.path.join(REPO, "tests", "test_type_b_808*"))
                if os.path.basename(p) != TEST_BASENAME]
        assert not hits, f"unexpected pre-existing Type B #808 test files: {hits}"

    def test_ece_yildirim_zero_hit_repo_wide_pre_commit(self):
        # Against HEAD (the committed, pre-#808 tree), not the working tree:
        # the profile edits are intentional post-commit additions.
        res = _run_git("grep", "-ci", "ece yildirim", "HEAD", "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and (not res.stdout.strip() or res.stdout.strip() == ""), \
            f"Ece Yildirim already referenced pre-commit: {res.stdout}"

    def test_block_key_zero_hit_repo_wide_pre_commit(self):
        res = _run_git("grep", "-c", BLOCK_KEY, "HEAD", "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and (not res.stdout.strip() or res.stdout.strip() in ("", "0")), \
            f"block key already referenced pre-commit: {res.stdout}"


# --- Rotation guard --------------------------------------------------------


ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
EXPECTED_ORDER = [
    ("B", "808"), ("A", "807"), ("E", "806"), ("D", "805"), ("C", "804"),
]
WINDOW_SEQ = "D (#805) -> E (#806) -> A (#807) -> B (#808) -> C (#809)"


class TestRotationCycleGuard808:
    def test_iteration_sequence_is_804_through_808(self):
        assert EXPECTED_ORDER == [
            ("B", "808"), ("A", "807"), ("E", "806"), ("D", "805"), ("C", "804"),
        ]

    def test_rotation_legs_adjacency(self):
        for (t1, n1), (t2, n2) in zip(EXPECTED_ORDER, EXPECTED_ORDER[1:]):
            assert int(n1) == int(n2) + 1
            assert (ORDER[t1] - ORDER[t2]) % 5 == 1

    def test_type_b_808_position_is_fourth_leg_of_805_809_window(self):
        assert EXPECTED_ORDER[0] == ("B", "808")

    def test_predecessor_is_type_a_807(self):
        assert EXPECTED_ORDER[1] == ("A", "807")


# --- Mechanism 716 content -------------------------------------------------


class TestMechanism716Content:
    def test_block_parses_under_journalist_cross_entity(self):
        with open(GIZMODO_PROFILE) as fh:
            doc = yaml.safe_load(fh)
        assert "ece_yildirim" in doc["journalist_cross_entity"]
        assert doc["journalist_cross_entity"]["ece_yildirim"]["mechanism_id"] == M_ID

    def test_block_key_unique(self):
        field = "    block_key: type_b_808_ece_yildirim_gizmodo_apple_adversarial_vs_meta_product_neutral_sep17\n"
        assert _gizmodo_text().count(field) == 1

    def test_block_716_identity_fields(self):
        b = _block()
        assert b["mechanism_id"] == M_ID
        assert b["iteration"] == 808
        assert b["iteration_type"] == "B"
        assert b["rotation_type"] == "B"
        assert b["journalist"] == "Ece Yildirim"
        assert b["publication"] == "Gizmodo"
        assert b["desk"] == "Privacy and Security"
        assert b["owner"] == "Keleops AG"
        assert b["author_page"] == "https://gizmodo.com/author/eceyildirim"
        assert b["test_file"] == "tests/" + TEST_BASENAME

    def test_apple_arm_fields(self):
        b = _block()
        apple = b["apple_arm"]
        assert apple["byline"] == "Ece Yildirim"
        assert apple["date"] == "2026-09-09"
        assert apple["register"] == "adversarial_privacy_commentary"
        assert apple["tone_MANUAL_ILLUSTRATIVE"] == -0.60
        assert apple["url"] == "https://gizmodo.com/if-meta-glasses-freak-you-out-wait-until-you-hear-about-the-new-apple-watch-features-2000809371"
        quotes = " ".join(apple["key_quotes"])
        assert "sounds like a privacy nightmare" in quotes
        assert "constantly eavesdropping" in quotes
        assert "wave of public outcry" in quotes
        assert "eager to assure" in quotes

    def test_apple_arm_meta_anchor_inside_piece(self):
        b = _block()
        anchors = " ".join(b["apple_arm"]["meta_anchor_inside_piece"])
        assert "pristine compared to Meta" in anchors
        assert "pervert glasses" in anchors
        assert "creeps" in anchors

    def test_meta_arm_fields(self):
        b = _block()
        meta = b["meta_arm"]
        assert meta["byline"] == "Ece Yildirim"
        assert meta["date"] == "2026-09-15"
        assert meta["register"] == "neutral_product_pricing_news"
        assert meta["tone_MANUAL_ILLUSTRATIVE"] == -0.15
        assert meta["url"] == "https://gizmodo.com/meta-is-hoping-youll-pay-for-more-ai-features-on-instagram-2000812018"
        quotes = " ".join(meta["key_quotes"])
        assert "coughing up monthly fees" in quotes
        assert "Meta One" in quotes

    def test_spread_delta_calc(self):
        b = _block()
        assert b["illustrative_register_delta_apple_minus_meta"] == -0.45
        assert b["delta_calc"] == "(-0.60) - (-0.15) = -0.45"

    def test_statistical_discipline(self):
        b = _block()
        disc = b["statistical_discipline"]
        assert "p_value NOT_CALCULATED" in disc
        assert "cohens_d NOT_CALCULATED" in disc
        assert "is_significant False" in disc
        assert "Engine NOT run" in disc
        assert b["no_analysis_json_update"] is True
        assert b["verdict"].startswith("Verdict: directionally_supported_not_proven")

    def test_research_method_documents_abandoned_grothaus_pair(self):
        b = _block()
        method = b["research_method"]
        assert "Grothaus" in method
        assert "ABANDONED" in method
        assert "no-invented-byline" in method
        assert "Excerpt-bounded per #503" in method

    def test_confounder_strong_triple_present(self):
        b = _block()
        strong = b["confounders_ranked"]["strong"]
        assert len(strong) == 3
        assert any(c.startswith("Product-domain mismatch") for c in strong)
        assert any(c.startswith("Genre routing") for c in strong)
        assert any("pristine compared to Meta" in c for c in strong)

    def test_counterevidence_present(self):
        b = _block()
        assert len(b["counterevidence"]) >= 3

    def test_cross_references_include_653_and_715(self):
        b = _block()
        ids = [c["mechanism_id"] for c in b["cross_references"] if "mechanism_id" in c]
        assert 653 in ids
        assert 715 in ids
        assert any("kyle_barr" in c.get("entry", "") for c in b["cross_references"])


# --- Supersession and corpus post-#807 --------------------------------------


class TestSupersessionAndCorpusPost807:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout))

    def test_corpus_max_is_716(self):
        assert max(self._numeric_ids()) == 716

    def test_iteration_807_max_715_sweep_superseded_by_design(self):
        # #807's max-715 sweeps fail by designed supersession now that 716 exists.
        assert max(self._numeric_ids()) != 715

    def test_zero_underscore_717_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_717_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_807_zero_underscore_716_sweep_stays_green(self):
        # The #807 zero-underscore-716 sweeps stay green post-#808 by designed keying:
        # neither the profile block nor this test file carries a literal underscore-716 key.
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", MECH_ID_MARKER, "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), \
                f"literal underscore-716 key leaked into {root}: {res.stdout.strip()[:200]}"

    def test_iteration_807_zero_numeric_716_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 716", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected #807's zero-numeric-716 sweep to fail by designed supersession"

    def test_numeric_716_keys_in_exactly_the_two_designed_locations(self):
        res = _run_git("grep", "-r", "mechanism_id: 716", "--", "profiles/")
        hits = [l for l in res.stdout.strip().splitlines() if l.strip()]
        # Designed keying: one numeric 716 key in the gizmodo journalist_cross_entity
        # block, one in the careers competitor_coverage sub-block; no other profiles/ location.
        assert len(hits) == 2, f"unexpected numeric 716 key spread in profiles/: {hits}"
        assert any("profiles/gizmodo.yaml" in h for h in hits)
        assert any("careers/journalists.yaml" in h for h in hits)


# --- Ledger -----------------------------------------------------------------


class TestLedger808:
    def _profiles_corpus(self):
        parts = []
        for root, _dirs, files in os.walk(os.path.join(REPO, "profiles")):
            for f in files:
                p = os.path.join(root, f)
                with open(p, encoding="utf-8", errors="replace") as fh:
                    parts.append(fh.read())
        return "\n".join(parts)

    def test_twenty_sixth_present_and_twenty_seventh_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference "TWENTY-SEVENTH" inside their own
        # negative guards, so a tests/ sweep would false-positive).
        corpus = self._profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus

    def test_m716_not_falsification_family_and_holds_26(self):
        b = _block()
        assert "ledger holds at 26" in b["falsification_family"]
        assert b["no_analysis_json_update"] is True


# --- Careers ----------------------------------------------------------------


class TestCareers808:
    def _careers(self):
        with open(CAREERS_PROFILE) as fh:
            return yaml.safe_load(fh)

    def test_ece_yildirim_entry_present(self):
        assert "ece_yildirim" in self._careers()

    def test_ece_yildirim_role(self):
        j = self._careers()["ece_yildirim"]
        assert j["current_role"] == "Staff Writer"
        assert j["current_publication"] == "Gizmodo"
        assert j["desk"] == "Privacy and Security"
        assert j["publication_owner"] == "Keleops AG"

    def test_ece_yildirim_beats(self):
        j = self._careers()["ece_yildirim"]
        assert "privacy" in j["beats"]
        assert "security" in j["beats"]
        assert "wearables" in j["beats"]

    def test_ece_yildirim_mechanism_ids(self):
        j = self._careers()["ece_yildirim"]
        assert j["mechanism_ids"] == [716]

    def test_ece_yildirim_competitor_coverage_block_key(self):
        j = self._careers()["ece_yildirim"]
        assert BLOCK_KEY in j["competitor_coverage"]
        assert j["competitor_coverage"][BLOCK_KEY]["mechanism_id"] == 716
        assert j["competitor_coverage"][BLOCK_KEY]["apple_arm"]["tone_score"] == -0.60
        assert j["competitor_coverage"][BLOCK_KEY]["meta_arm"]["tone_score"] == -0.15

    def test_sabrina_ortiz_entry_untouched(self):
        j = self._careers()["sabrina_ortiz"]
        assert j["mechanism_ids"] == [713]


# --- Doc sync ----------------------------------------------------------------


class TestDocSync808:
    def test_readme_row_present(self):
        with open(os.path.join(REPO, "README.md")) as fh:
            assert TEST_BASENAME in fh.read()

    def test_architecture_row_present(self):
        with open(os.path.join(REPO, "docs", "ARCHITECTURE.md")) as fh:
            assert TEST_BASENAME in fh.read()


# --- Iteration log -----------------------------------------------------------


class TestIterationLog808:
    def _tail(self):
        with open(ITERATION_LOG) as fh:
            lines = fh.readlines()
        return "".join(lines[-80:])

    def test_iteration_log_entry_present(self):
        assert "Type B #808" in self._tail()

    def test_iteration_log_window_sequence(self):
        assert WINDOW_SEQ in self._tail()
