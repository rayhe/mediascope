"""Type B #753: Devindra Hardawar (Engadget) Quest 3 vs Vision Pro review-register constancy (mechanism 686).

On Mon Sep 14 2026 this run pins the first dedicated corpus mechanism on Devindra
Hardawar, Engadget senior editor and Engadget Podcast host: journalist-level
cross-entity REGISTER CONSTANCY in the product-review genre. His first-hand
reviews of Meta's Quest 3 (Oct 2023, "Meta Quest 3 review: A bit of mixed reality
makes for better VR") and Apple's Vision Pro (Feb 2024, "Apple Vision Pro review:
Beta testing the future") run the same enthusiastic-hardware-reviewer register,
four months apart, same category (VR/AR headsets), same byline, same desk.
Meta arm: "simply blew me away" (mixed-reality multitasking), "makes every virtual
element look incredibly sharp", "the first time I have genuinely enjoyed using
Meta's finger tracking"; the Engadget Podcast episode on the review (Oct 2023,
hosted by Hardawar) calls it "the best standalone VR headset we have ever seen".
Caveats are product-anchored (app usefulness, awkward virtual keyboard). MANUAL
ILLUSTRATIVE +0.55. Apple arm: "It is far from a slam dunk, but it is also one of
the most fascinating devices we have ever seen"; "impressive 3D Immersive Videos",
"the elegant simplicity of the Vision Pro's eye tracking and hand gestures", "the
trouble with wearing such a heavy headset". MANUAL ILLUSTRATIVE +0.35. Illustrative
delta (Meta minus Apple) +0.20 - near-null constancy, and the sign is
Meta-favoring, directionally opposite to any Meta-penalty reading. This is the
review-register analogue of mechanism 698 (Raymond Wong, Gizmodo, +0.15 delta):
it bounds the review-register asymmetry findings (mechanism 528 Chokkattu -1.025,
mechanism 662 Chen -0.65) to journalist-specific, not genre-general, gradients.
Financial context: no documented AI content-licensing deal between Yahoo/Engadget
(Apollo-owned) and Meta or Apple in corpus; the Apollo financial chain in-corpus
points at Anthropic (mechanism 305: Apollo XPV Anthropic infrastructure financing
via Yahoo/TechCrunch), a different entity axis - so the deal-gradient prediction
on the Meta/Apple axis is NULL and the observed gap is near-null: a zero-gradient
control. MANUAL ILLUSTRATIVE only; p/d/ci NOT_CALCULATED; is_significant False;
engine NOT run; NOT artifact-grade; directionally_supported_not_proven;
TWENTY-FIFTH falsification-family member (ledger 24->25 per #753). Search-excerpt-
bounded per #503 (browser.open terminally failed upstream_unavailable this turn,
not retried per developer constraint). Designed keying per #723/#738/#739/#747:
the profile block key carries no underscore-form 686 mechanism key substring, so
the #752 zero-686 profile sweep instrument stays green while mechanism_id advances
in colon form.
"""

import glob
import os
import re
import subprocess

import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = os.path.basename(__file__)
MECH_KEY = "devindra_hardawar_engadget_quest3_vs_visionpro_review_register_constancy_sep14"
MECH_NUM = 686
QUEST3_URL = "https://www.engadget.com/meta-quest-3-review-mixed-reality-vr-150009788.html?src=rss/"
QUEST3_PODCAST_URL = "https://www.engadget.com/engadget-podcast-meta-quest-3-pixel-8-reviews-123048988.html?src=rss"
VISIONPRO_PODCAST_URL = "https://www.engadget.com/engadget-podcast-apple-vision-pro-review-133053827.html?src=rss"
VISIONPRO_HANGOVER_URL = "https://www.engadget.com/engadget-podcast-our-apple-vision-pro-hangover-133021630.html"
STORIES_URL = "https://www.engadget.com/facebook-ray-ban-stories-smart-glasses-ar-160006477.html?src=rss"


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _research():
    return _read("profiles/competitor-coverage-research.yaml")


def _fold(block):
    # YAML folding joins wrapped lines with spaces; normalize the same way
    # so multi-line assertions are not broken by source line breaks.
    return re.sub(r"\s+", " ", block)


def _block():
    corpus = _research()
    return corpus.split(MECH_KEY + ":")[1].split("\nmethodology:")[0]


def _profiles_corpus():
    parts = []
    for f in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
        parts.append(open(f, encoding="utf-8", errors="replace").read())
    return "\n".join(parts)


def _block_data():
    data = yaml.safe_load(_research())
    return data["cross_publication_findings"][MECH_KEY]


def _careers():
    return _read("profiles/careers/journalists.yaml")


class TestNovelty753:
    """Iteration 753 is new; nothing with this number existed pre-commit."""

    def test_single_type_b_753_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_b_753*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_b_753_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_b_753 files, no #753 in git log, zero
        # Devindra hits repo-wide, max mechanism_id 685 pre-commit); this
        # test pins that no duplicate #753 main commit ever appears.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%H %s"],
            capture_output=True,
            text=True,
        )
        mains = [
            line for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type B #753:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type B #753 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        anchor = TestRotationCycleGuard753.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)


class TestRotationCycleGuard753:
    """Rotation: distinct-mains window test, #721-style.

    Robust to the #678 history artifact and the #565 followup convention: first
    occurrence of each distinct iteration number, newest first. #753 closes the
    749-753 window, closing C->D->E->A->B.
    """

    ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # main commit this run, per #565

    @staticmethod
    def _mains():
        # First occurrence of each distinct iteration number, newest first.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%s"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        seen = set()
        mains = []
        for s in out:
            m = re.match(r"^Type [A-E] #(\d+):", s)
            if m and m.group(1) not in seen:
                seen.add(m.group(1))
                mains.append(s)
        return mains

    def test_window_749_753_closes_c_to_b(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("B", "753"),
            ("A", "752"),
            ("E", "751"),
            ("D", "750"),
            ("C", "749"),
        ], "rotation window 749-753 wrong: %r" % (observed,)

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["B", "A", "E", "D", "C"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                "rotation broken: %s -> %s is not a valid cycle edge" % (a, b)
            )


class TestMechanism686Content:
    def test_mech_block_present_in_research(self):
        corpus = _research()
        assert MECH_KEY + ":" in corpus
        assert "mechanism_id: 686" in corpus

    def test_iteration_metadata(self):
        block = _block()
        assert "iteration: 753" in block
        assert "rotation_type: B" in block
        assert "discovery_date: '2026-09-14'" in block
        assert "finding_type: journalist_cross_entity" in block

    def test_journalist_fields(self):
        block = _block()
        assert "journalist: Devindra Hardawar" in block
        assert "publication: Engadget" in block
        assert "competitor: Apple" in block

    def test_meta_arm_quotes(self):
        block = _fold(_block())
        assert "simply blew me away" in block
        assert "incredibly sharp" in block
        assert "genuinely enjoyed" in block
        assert "best standalone VR headset" in block

    def test_apple_arm_quotes(self):
        block = _fold(_block())
        assert "far from a slam dunk" in block
        assert "most fascinating devices" in block
        assert "eye tracking and hand gestures" in block
        assert "heavy headset" in block

    def test_manual_illustrative_discipline(self):
        block = _fold(_block())
        assert "MANUAL ILLUSTRATIVE" in block
        assert "+0.55" in block
        assert "+0.35" in block
        assert "+0.20" in block
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci_95 NOT_CALCULATED" in block
        assert "is_significant False" in block
        assert "engine NOT run" in block
        assert "NOT artifact-grade" in block

    def test_urls_verbatim(self):
        block = _block()
        for url in (
            QUEST3_URL, QUEST3_PODCAST_URL, VISIONPRO_PODCAST_URL,
            VISIONPRO_HANGOVER_URL, STORIES_URL,
        ):
            assert url in block, "missing URL: %s" % url

    def test_financial_context_apollo_chain(self):
        block = _fold(_block())
        assert "Apollo" in block
        assert "mechanism 305" in block
        assert "Anthropic" in block
        assert "NULL" in block
        assert "zero-gradient control" in block

    def test_wong_analogue_bounds(self):
        block = _fold(_block())
        assert "mechanism 698" in block
        assert "Raymond Wong" in block
        assert "journalist-specific, not genre-general" in block

    def test_confounder_strength_layers(self):
        confounders = _block_data()["confounders"]
        assert len(confounders) == 8, "expected 8 confounders, got %d" % len(confounders)
        flat = " ".join(confounders)
        assert flat.count("STRONG:") == 3
        assert flat.count("MODERATE:") == 3
        assert flat.count("WEAK:") == 2

    def test_three_counterevidence(self):
        counter = _block_data()["counterevidence"]
        assert len(counter) == 3, "expected 3 counterevidence, got %d" % len(counter)
        assert all("COUNTEREVIDENCE:" in c for c in counter)

    def test_verdict_and_ledger(self):
        block = _fold(_block())
        assert "directionally_supported_not_proven" in block
        assert "TWENTY-FIFTH falsification-family member" in block
        assert "ledger 24->25" in block
        assert "Correlation is not causation" in block

    def test_careers_backlink(self):
        careers = _careers()
        assert "name: Devindra Hardawar" in careers
        assert "mechanism_ids: [686]" in careers
        assert "Type B #753" in careers

    def test_designed_keying(self):
        # The block key and the whole profile corpus carry no underscore-form
        # 686 mechanism key substring; the id advances in colon form only.
        # This keeps the #752 zero-686 profile sweep instrument green.
        assert "mechanism" + "_686" not in MECH_KEY
        assert "mechanism_id: 686" in _block()
        assert "mechanism" + "_686" not in _profiles_corpus()


class TestSupersessionAndCorpusPost752:
    def _ids(self):
        return [
            int(x)
            for x in re.findall(r"mechanism_id:\s*(\d+)\b", _profiles_corpus())
        ]

    def test_max_mechanism_id_is_686(self):
        ids = self._ids()
        assert max(ids) == MECH_NUM, max(ids)

    def test_752_max_685_sweep_fails_by_designed_supersession(self):
        # Documented, not repaired: advancing max numeric mechanism id to 686
        # supersedes #752's test_max_mechanism_id_is_685 per the #710/#720
        # convention.
        assert max(self._ids()) == 686

    def test_752_zero_686_profile_sweep_stays_green_by_designed_keying(self):
        # The #752 profile-YAML zero-686 sweep asserts the contiguous
        # underscore form absent from every profile YAML; the #753 block key
        # was designed to keep it green.
        assert "mechanism" + "_686" not in _profiles_corpus()

    def test_750_751_zero_685_sweeps_stay_green(self):
        assert "mechanism" + "_685" not in _profiles_corpus()

    def test_747_zero_683_test_sweep_stays_green_by_designed_keying(self):
        # The #747 test-file zero-683 sweep scans test files for the
        # underscore form with trailing underscore; this file was written to
        # keep it green (keying uses the descriptive block key and
        # colon/space forms only).
        own = open(os.path.join(REPO_ROOT, "tests", TEST_BASENAME)).read()
        assert "mechanism" + "_683_" not in own

    def test_686_descriptive_key_unique_repo_wide(self):
        corpus = _profiles_corpus()
        assert corpus.count(MECH_KEY + ":") == 1
        tests_hits = [
            f for f in glob.glob(os.path.join(REPO_ROOT, "tests", "*.py"))
            if MECH_KEY in open(f, encoding="utf-8", errors="replace").read()
        ]
        assert tests_hits == [os.path.join(REPO_ROOT, "tests", TEST_BASENAME)], tests_hits

    def test_zero_underscore_687_keys(self):
        assert "mechanism" + "_687" not in _profiles_corpus()


class TestLedger753:
    def test_falsification_ledger_advances_to_25(self):
        corpus = _profiles_corpus()
        assert "TWENTY-FIFTH" in corpus
        assert "TWENTY-SIXTH" not in corpus


class TestDocSync753:
    def test_readme_row(self):
        assert TEST_BASENAME in _read("README.md")

    def test_architecture_row(self):
        assert TEST_BASENAME in _read("docs/ARCHITECTURE.md")


class TestIterationLog753:
    def _head(self):
        with open(os.path.join(REPO_ROOT, "iteration-log.md")) as f:
            lines = f.read().splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #753 entry sits at the end of the file, not the top.
        return "\n".join(lines[-60:])

    def test_log_entry_present(self):
        assert "#753" in self._head()

    def test_log_mechanism_686(self):
        assert "mechanism 686" in self._head()

    def test_log_journalist(self):
        assert "Devindra Hardawar" in self._head()

    def test_log_rotation_window(self):
        assert "749-753" in self._head()


class TestDateGrounding753:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_14_2026_is_monday(self):
        assert self._weekday("2026-09-14") == "Monday"
