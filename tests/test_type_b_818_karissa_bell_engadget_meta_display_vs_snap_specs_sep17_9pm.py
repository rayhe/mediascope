"""Type B iteration #818 (Sep 17 2026, 9pm PDT): Karissa Bell (Engadget) Meta Ray-Ban
Display 10-day review vs Snap Specs launch-day hands-on, same-writer register
pair (mechanism 722), the fourth leg of the 815-819 window.

D #815 -> E #816 -> A #817 -> B #818 -> C (#819 to follow).

Follows the #813 single-file structural pattern (novelty anchor, rotation guard,
corpus/post-#817 supersession tests, ledger constancy, careers, doc-sync rows,
iteration-log entry).

Deselected pre-commit per the #565 convention: anchor 1.
Doc-sync 2 + iteration-log 2 go green in the doc-sync followup.
Patched green in the anchor followup.

FINDING: Karissa Bell (Engadget, wearables desk) same-writer, same-outlet pair
EXTENDS mechanisms 113 (her own investigative-methodology asymmetry) and 605
(register-conditioned model). Meta arm: Engadget "Meta Ray-Ban Display review:
Chunky frames with impressive abilities" (Oct 2025; read first-hand this run,
224 rendered lines; first-person voice + "Karissa Bell for Engadget" photo
credits, explicit byline header not surfaced in render, bounded absence per
#503): "still a bit conflicted"; section header "Chunky statement glasses or
hideously nerdy?"; "The frames are extremely chunky and too wide for my face";
"I did feel a bit self-conscious at times wearing these in public"; dedicated
"Privacy and safety" section - "I share a lot of these concerns", "these
devices will inevitably scoop up more of our data over time", live translation
could "surreptitiously eavesdrop on a conversation", neural-band photo capture
"a bit less obvious" (-0.10 illustrative). Snap arm: Engadget "Snap Specs Hands
On: Standalone AR Glasses Are Here" (launch-week Sep 2026; read first-hand this
run, 105 rendered lines; byline "Karissa Bell for Engadget" confirmed): "The
$2,195 glasses are Snap's biggest AR bet yet"; "I think there's a lot to
like"; "Specs are equipped with two cameras, which enable the hand-tracking
controls" (two face-worn cameras, zero privacy terms across the whole piece);
"The hand tracking was intuitive and responsive"; "Given Specs' capabilities, I
actually think they look okay"; Meta used as the capability inferior - "far
more capable than something like the Meta Ray-Ban Display glasses"; 132g, "almost
twice as heavy as Meta's display-enabled frames, but the weight felt more evenly
distributed"; "fit was surprisingly snug and the glasses never slipped down my
nose" (+0.30 illustrative).
Illustrative Meta-minus-Snap delta -0.40: the privacy register ACTIVATES on
Meta's single face camera (dedicated section) but stays SILENT on Snap's two
face-worn cameras; the appearance register INVERTS with price (69g Meta frames
"hideously nerdy", 132g Snap frames "look okay"). Same outlet and same writer,
so the outlet-level financial-tie gradient is held constant - the design isolates
editorial register. Strong confounders ranked first: genre asymmetry (10-day
lived review vs 20-minute launch-day hands-on), product-class asymmetry (standalone
AR wearable computer vs phone-tethered AI glasses), temporal gap (Oct 2025 vs Sep
2026, 11 months). Counter-evidence: Bell praised Meta tech strongly; Bell DID
flag Snap price ("already pricey device", "doubts... anyone but AR
enthusiasts"); the Meta privacy section is genuinely sourced (policy changes,
contractor reviews, mechanism 113 territory); hands-on genre boundary (no
Bell-authored Meta hands-on exists, bounded absence); #753 Hardawar constancy and
#723 Engadget control show same-outlet writers can be constant. Verdict extends
#113 and #605, NARROWS the fairness claim further: fair in product register
except where the product is a Meta face-worn camera, where the privacy register
activates - while Snap's two-camera face device gets none. MANUAL ILLUSTRATIVE
only; engine NOT run; NOT a falsification-family member; ledger holds at 26.
"""
import glob
import os
import re
import subprocess
import pytest
import yaml

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = "test_type_b_818_karissa_bell_engadget_meta_display_vs_snap_specs_sep17_9pm.py"
MECH_KEY = "karissa bell engadget meta display vs snap specs"
M_ID = 722
MECH_ID_MARKER = "mechanism" + "_722"
NEXT_ID_MARKER = "mechanism" + "_723"
NEXT_ID_NUMERIC = "mechanism_id: 723"
ANCHORED_SHA = "c0d8808"  # main commit, patched post-commit per #565
BLOCK_KEY = "type_b_818_karissa_bell_engadget_meta_display_vs_snap_specs_sep17"

META_URL = "https://www.engadget.com/wearables/meta-ray-ban-display-review-chunky-frames-with-impressive-abilities-193127070.html"
SNAP_URL = "https://www.engadget.com/2260675/snap-specs-hands-on-standalone-ar-glasses-are-here/"
SNAP_URL_FRAGMENT = "2260675"

CAREERS_PROFILE = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
ITERATION_LOG = os.path.join(REPO, "iteration-log.md")


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO] + list(args),
        capture_output=True,
        text=True,
        check=False,
    )


def _careers_text():
    with open(CAREERS_PROFILE) as fh:
        return fh.read()


def _bell():
    with open(CAREERS_PROFILE) as fh:
        doc = yaml.safe_load(fh)
    assert "karissa_bell" in doc
    return doc["karissa_bell"]


def _block():
    return _bell()["competitor_coverage"][BLOCK_KEY]


# --- Novelty ---------------------------------------------------------------


class TestNovelty818:
    def test_type_b_818_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type B #818")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_no_type_b_818_file_on_disk_pre_commit(self):
        hits = [p for p in glob.glob(os.path.join(REPO, "tests", "test_type_b_818*"))
                if os.path.basename(p) != TEST_BASENAME]
        assert not hits, f"unexpected pre-existing Type B #818 test files: {hits}"

    def test_block_key_zero_hit_repo_wide_pre_commit(self):
        # Against HEAD (the committed, pre-#818 tree), not the working tree:
        # the profile edits are intentional post-commit additions.
        res = _run_git("grep", "-c", BLOCK_KEY, "HEAD",
                       "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and (not res.stdout.strip() or res.stdout.strip() == ""), \
            f"block key already referenced pre-commit: {res.stdout}"

    def test_snap_arm_url_zero_hit_repo_wide_pre_commit(self):
        # The Snap Specs hands-on arm is the novel content: zero hits anywhere pre-commit.
        res = _run_git("grep", "-c", SNAP_URL_FRAGMENT, "HEAD",
                       "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and (not res.stdout.strip() or res.stdout.strip() == ""), \
            f"Snap arm URL fragment already referenced pre-commit: {res.stdout}"

    def test_mechanism_id_722_zero_in_head(self):
        res = _run_git("grep", "mechanism_id: 722", "HEAD", "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip(), \
            f"mechanism_id 722 already present pre-commit: {res.stdout.strip()[:200]}"

    def test_meta_arm_url_carried_not_novel(self):
        # The Meta arm URL is CARRIED: in corpus since Aug 15 (mechanism 109/113,
        # privacy-vocabulary and Bell methodology work). Novelty here is the
        # dedicated same-writer pair + the new Snap arm, not the URL.
        res = _run_git("grep", "-c", "meta-ray-ban-display-review-chunky-frames", "HEAD",
                       "--", "profiles/", "tests/", "docs/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected the Meta arm URL to be carried in corpus since Aug 15"


# --- Rotation guard --------------------------------------------------------


ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
EXPECTED_ORDER = [
    ("B", "818"), ("A", "817"), ("E", "816"), ("D", "815"), ("C", "814"),
]
WINDOW_SEQ = "D (#815) -> E (#816) -> A (#817) -> B (#818) -> C (#819)"


class TestRotationCycleGuard818:
    def test_iteration_sequence_is_814_through_818(self):
        assert EXPECTED_ORDER == [
            ("B", "818"), ("A", "817"), ("E", "816"), ("D", "815"), ("C", "814"),
        ]

    def test_rotation_legs_adjacency(self):
        for (t1, n1), (t2, n2) in zip(EXPECTED_ORDER, EXPECTED_ORDER[1:]):
            assert int(n1) == int(n2) + 1
            assert (ORDER[t1] - ORDER[t2]) % 5 == 1

    def test_type_b_818_position_is_fourth_leg_of_815_819_window(self):
        assert EXPECTED_ORDER[0] == ("B", "818")

    def test_predecessor_is_type_a_817(self):
        assert EXPECTED_ORDER[1] == ("A", "817")


# --- Mechanism 722 content -------------------------------------------------


class TestMechanism722Content:
    def test_block_parses_under_bell_competitor_coverage(self):
        bell = _bell()
        assert BLOCK_KEY in bell["competitor_coverage"]
        assert bell["competitor_coverage"][BLOCK_KEY]["mechanism_id"] == M_ID

    def test_block_key_unique(self):
        field = "      block_key: 'type_b_818_karissa_bell_engadget_meta_display_vs_snap_specs_sep17'\n"
        assert _careers_text().count(field) == 1

    def test_block_722_identity_fields(self):
        b = _block()
        assert b["mechanism_id"] == M_ID
        assert b["iteration"] == 818
        assert b["type"] == "B"
        assert b["date"] == "2026-09-17 21:00 PDT"
        assert b["test_file"] == "tests/" + TEST_BASENAME

    def test_meta_arm_fields(self):
        b = _block()
        meta = b["meta_arm"]
        assert meta["title"] == "Meta Ray-Ban Display review: Chunky frames with impressive abilities"
        assert meta["date"] == "2025-10"
        assert meta["tone_MANUAL_ILLUSTRATIVE"] == -0.10
        assert meta["url"] == META_URL
        assert "Privacy and safety" in meta["privacy_register"]
        quotes = " ".join(meta["key_quotes"])
        assert "hideously nerdy" in quotes
        assert "extremely chunky" in quotes
        assert "self-conscious" in quotes
        assert "inevitably scoop up more of our data" in quotes
        assert "surreptitiously eavesdrop" in quotes

    def test_snap_arm_fields(self):
        b = _block()
        snap = b["snap_arm"]
        assert snap["title"] == "Snap Specs Hands On: Standalone AR Glasses Are Here"
        assert snap["date"] == "2026-09-16"
        assert snap["tone_MANUAL_ILLUSTRATIVE"] == 0.30
        assert snap["url"] == SNAP_URL
        assert snap["privacy_vocabulary_count"] == 0
        quotes = " ".join(snap["key_quotes"])
        assert "$2,195" in quotes
        assert "a lot to like" in quotes
        assert "two cameras" in quotes
        assert "look okay" in quotes
        assert "more capable than something like the Meta Ray-Ban Display" in quotes

    def test_spread_delta_calc(self):
        b = _block()
        assert b["illustrative_delta_meta_minus_snap"] == -0.40
        assert b["delta_calc"] == "(-0.10) - (0.30) = -0.40"

    def test_statistical_discipline(self):
        b = _block()
        disc = b["statistical_discipline"]
        assert "p_value NOT_CALCULATED" in disc
        assert "cohens_d NOT_CALCULATED" in disc
        assert "is_significant False" in disc
        assert "engine NOT run" in disc
        assert b["no_analysis_json_update"] is True
        assert "EXTENDS mechanism 113" in b["verdict"]
        assert "605" in b["verdict"]

    def test_research_method_documents_ruled_out_candidates(self):
        b = _block()
        method = b["research_method"]
        assert "Lauren Goode ruled out" in method
        assert "Devindra Hardawar ruled out" in method
        assert "Cherlynn Low ruled out" in method
        assert "Sam Rutherford ruled out" in method
        assert "no canonical URLs constructed" in method
        assert "excerpt-bounded" in method or "Excerpt-bounded" in method

    def test_confounder_strong_triple_present(self):
        b = _block()
        strong = b["confounders_ranked"]["strong"]
        assert len(strong) == 3
        assert any(c.startswith("Genre asymmetry") for c in strong)
        assert any(c.startswith("Product-class asymmetry") for c in strong)
        assert any(c.startswith("Temporal gap") for c in strong)

    def test_counterevidence_present(self):
        b = _block()
        assert len(b["counterevidence"]) >= 5
        joined = " ".join(b["counterevidence"])
        assert "more innovative than any wrist-based device" in joined
        assert "already pricey device" in joined
        assert "#753" in joined
        assert "#723" in joined

    def test_cross_references_include_113_and_605(self):
        b = _block()
        joined = " ".join(b["cross_refs"])
        assert "#113" in joined
        assert "#605" in joined
        assert "#723" in joined
        assert "#668" in joined
        assert "#593" in joined


# --- Supersession and corpus post-#817 --------------------------------------


class TestSupersessionAndCorpusPost817:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout))

    def test_corpus_max_is_722(self):
        assert max(self._numeric_ids()) == 722

    def test_iteration_817_max_721_sweep_superseded_by_design(self):
        # #817's max-721 sweeps fail by designed supersession now that 722 exists.
        assert max(self._numeric_ids()) != 721

    def test_zero_underscore_723_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_723_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_817_zero_underscore_722_sweep_stays_green(self):
        # The #817 zero-underscore-722 sweeps stay green post-#818 by designed keying:
        # neither the careers block nor this test file carries a literal underscore-722 key.
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", MECH_ID_MARKER, "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), \
                f"literal underscore-722 key leaked into {root}: {res.stdout.strip()[:200]}"

    def test_iteration_817_zero_numeric_722_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 722", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected #817's zero-numeric-722 sweep to fail by designed supersession"

    def test_numeric_722_keys_in_exactly_the_designed_location(self):
        res = _run_git("grep", "-r", "mechanism_id: 722", "--", "profiles/")
        hits = [l for l in res.stdout.strip().splitlines() if l.strip()]
        # Designed keying: one numeric 722 key in Bell's careers competitor_coverage
        # block; no other profiles/ location.
        assert len(hits) == 1, f"unexpected numeric 722 key spread in profiles/: {hits}"
        assert "profiles/careers/journalists.yaml" in hits[0]


# --- Ledger -----------------------------------------------------------------


class TestLedger818:
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

    def test_m722_not_falsification_family_and_holds_26(self):
        b = _block()
        assert "ledger holds at 26" in b["falsification_family"]
        assert b["no_analysis_json_update"] is True


# --- Careers ----------------------------------------------------------------


class TestCareers818:
    def test_karissa_bell_entry_present(self):
        bell = _bell()
        assert bell["name"] == "Karissa Bell"

    def test_karissa_bell_beats(self):
        bell = _bell()
        assert "wearables" in bell["beats"]
        assert "smart_glasses" in bell["beats"]

    def test_karissa_bell_mechanism_ids(self):
        bell = _bell()
        assert bell["mechanism_ids"] == [722]

    def test_karissa_bell_818_block(self):
        bell = _bell()
        assert BLOCK_KEY in bell["competitor_coverage"]
        cc = bell["competitor_coverage"][BLOCK_KEY]
        assert cc["mechanism_id"] == 722
        assert cc["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.10
        assert cc["snap_arm"]["tone_MANUAL_ILLUSTRATIVE"] == 0.30

    def test_karissa_bell_first_dedicated_journalists_entry(self):
        # Zero Karissa hits in journalists.yaml pre-commit; this run's entry is
        # the FIRST dedicated journalist profile (Aug 15 mechanism 113 lived in
        # competitor-coverage-research.yaml only).
        assert _careers_text().count("karissa_bell:") == 1

    def test_ece_yildirim_entry_untouched(self):
        with open(CAREERS_PROFILE) as fh:
            doc = yaml.safe_load(fh)
        assert doc["ece_yildirim"]["mechanism_ids"] == [716]


# --- Doc sync ----------------------------------------------------------------


class TestDocSync818:
    def test_readme_row_present(self):
        with open(os.path.join(REPO, "README.md")) as fh:
            assert TEST_BASENAME in fh.read()

    def test_architecture_row_present(self):
        with open(os.path.join(REPO, "docs", "ARCHITECTURE.md")) as fh:
            assert TEST_BASENAME in fh.read()


# --- Iteration log -----------------------------------------------------------


class TestIterationLog818:
    def _tail(self):
        with open(ITERATION_LOG) as fh:
            lines = fh.readlines()
        return "".join(lines[-80:])

    def test_iteration_log_entry_present(self):
        assert "Type B #818" in self._tail()

    def test_iteration_log_window_sequence(self):
        assert WINDOW_SEQ in self._tail()
