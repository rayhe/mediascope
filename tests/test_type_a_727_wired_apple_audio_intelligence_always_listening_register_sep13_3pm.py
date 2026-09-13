"""Type A #727: WIRED x Apple Audio Intelligence always-listening register test (Sep 13 2026, 15:00 PDT).

THIRD leg of the Apple-always-listening corpus strand after m207/m446
(camera AirPods silence, visual sensor) and m668 (Engadget Cherlynn Low
control case, Type B journalist-level): WIRED covered Apple's Sep 9 2026
Audio Intelligence suite (Series 12/Ultra 4, S11 Secure Exclave) via Apple's
own 11-page technical privacy paper shared with WIRED, per aiweekly.co's
writeup of WIRED's original reporting. Register observed: pitch-carrying,
zero privacy-alarm (MANUAL ILLUSTRATIVE 0.0). The same publication carries
adversarial register (-0.55 to -0.62 MANUAL ILLUSTRATIVE) for Meta's
single-camera user-initiated glasses. Asymmetry (Apple minus Meta) MANUAL
ILLUSTRATIVE +0.55; p_value/cohens_d/ci NOT_CALCULATED; is_significant False
per the Aug 28 2026 standing rule. NOT artifact-grade. n=1-vs-3; WIRED Apple
arm is second-hand-excerpt-bounded (exact wired.com URL unverified this run
per #503/iteration-492, not asserted). NOT a falsification-family member
(ledger holds at 24); naive payer-softening does NOT fail on this leg (unlike
m633 Reuters/Meta, m648 El Pais/Meta, m552 FT x Anthropic). Correlation is not
causation.

6 browser.search query sets this run; all URLs verbatim from search-result
Full-URL listings; no wired.com URL reconstructed.
"""

import glob
import os
import re
import subprocess

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = os.path.basename(__file__)
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
MECH_KEY = "mechanism_670_wired_apple_audio_intelligence_always_listening_register_asymmetry_sep13"
MECH_NUM = 670


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _wired():
    return _read("profiles/wired.yaml")


def _fold(block):
    # YAML `>` folding joins wrapped lines with spaces; normalize the same way
    # so multi-line assertions are not broken by source line breaks.
    return re.sub(r"\s+", " ", block)


class TestNovelty727:
    """Iteration 727 is new; nothing with this number existed pre-commit."""

    def test_single_type_a_727_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_a_727*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_a_727_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_a_727 files, no #727 in git log); this test
        # pins that no duplicate #727 main commit ever appears.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%H %s"],
            capture_output=True,
            text=True,
        )
        mains = [
            line for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type A #727:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type A #727 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        anchor = TestRotationCycleGuard727.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)


class TestRotationCycleGuard727:
    """Rotation: distinct-mains window test, #721-style.

    Robust to the #678 history artifact and the #565 followup convention: first
    occurrence of each distinct iteration number, newest first.
    """

    ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

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

    def test_window_723_727_closes_e_to_a(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("A", "727"),
            ("E", "726"),
            ("D", "725"),
            ("C", "724"),
            ("B", "723"),
        ], "rotation window 723-727 wrong: %r" % (observed,)

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["A", "E", "D", "C", "B"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                "rotation broken: %s -> %s is not a valid cycle edge" % (a, b)
            )


class TestMechanism670Content:
    def test_mech_670_block_present_in_wired_apple(self):
        corpus = _wired()
        assert MECH_KEY + ":" in corpus
        assert "mechanism_id: 670" in corpus

    def test_iteration_metadata(self):
        corpus = _wired()
        block = corpus.split(MECH_KEY + ":")[1].split("\n  google:")[0]
        assert "iteration: 727" in block
        assert "iteration_type: A" in block
        assert 'iteration_time: "2026-09-13 15:00 PDT"' in block
        assert 'pair: "WIRED x Apple (vs Meta) - Audio Intelligence always-listening register test"' in block

    def test_finding_states_third_leg_and_direction(self):
        corpus = _wired()
        block = corpus.split(MECH_KEY + ":")[1].split("\n  google:")[0]
        assert "THIRD leg of the Apple-always-listening corpus strand" in block
        assert "NOT a falsification-family member" in block
        assert "ledger holds at 24" in block

    def test_manual_illustrative_discipline(self):
        corpus = _wired()
        block = corpus.split(MECH_KEY + ":")[1].split("\n  google:")[0]
        assert "MANUAL ILLUSTRATIVE" in block
        assert "NOT_CALCULATED" in block
        assert "is_significant: false" in block
        assert "NOT artifact-grade" in block

    def test_novelty_vs_existing_names_207_446_668(self):
        corpus = _wired()
        block = corpus.split(MECH_KEY + ":")[1].split("\n  google:")[0]
        assert "mechanism_207:" in block
        assert "mechanism_446:" in block
        assert "mechanism_668:" in block
        assert "mechanism_670_distinct:" in block

    def test_bystander_consent_gradient_noted(self):
        corpus = _wired()
        block = _fold(corpus.split(MECH_KEY + ":")[1].split("\n  google:")[0])
        assert "no practical means to consent or decline" in block
        assert "raised BY WIRED ITSELF for Meta glasses" in block

    def test_wiretap_states_and_eff_cited(self):
        corpus = _wired()
        block = corpus.split(MECH_KEY + ":")[1].split("\n  google:")[0]
        assert "wiretap laws in 11 US states" in block
        assert "unacceptable burden" in block

    def test_source_urls_all_verbatim_from_this_run(self):
        corpus = _wired()
        block = corpus.split(MECH_KEY + ":")[1].split("\n  google:")[0]
        for url in [
            "https://aiweekly.co/alerts/apple-defends-new-apple-watchs-always-listening-features",
            "https://www.fastcompany.com/91603935/new-apple-watch-ai-features-hint-at-how-apple-plans-to-address-privacy-concerns-in-future-smart-glasses-audio-intelligence",
            "https://www.macrumors.com/2026/09/10/apple-watch-live-rewind/",
            "https://Www.engadget.com/2254031/apple-watch-series-12-will-listen-to-your-conversations/",
            "https://www.theregister.com/security/2026/09/10/watch-out-apple-timepiece-can-grab-snippets-of-conversation-without-both-speakers-consent/5295666",
            "https://www.androidpure.com/apple-watch-audio-intelligence-wiretap-laws/",
            "https://www.digitaltrends.com/wearables/siri-is-about-to-hear-everything-you-say-but-apples-privacy-approach-has-me-cautiously-on-board/",
            "https://www.techspot.com/community/topics/apples-new-audio-intelligence-turns-the-watch-into-a-listening-device-privacy-is-part-of-the-pitch.298759/",
            "https://9to5mac.com/2026/09/09/apple-details-how-apple-watchs-new-audio-intelligence-features-work-in-privacy-paper/",
        ]:
            assert url in block, url

    def test_no_reconstructed_wired_url(self):
        corpus = _wired()
        block = _fold(corpus.split(MECH_KEY + ":")[1].split("\n  google:")[0])
        assert "no wired.com URL reconstructed" in block
        assert "not asserted" in block

    def test_financial_predictor_carried_and_consistent(self):
        corpus = _wired()
        block = corpus.split(MECH_KEY + ":")[1].split("\n  google:")[0]
        assert "potential $50M+ multi-year" in block
        assert "vs $0 Meta" in block
        assert "does NOT fail on this leg" in block


class TestSupersessionAndCorpusPost726:
    def _profiles_corpus(self):
        parts = []
        for f in glob.glob(os.path.join(REPO_ROOT, "profiles", "*.yaml")):
            parts.append(open(f, encoding="utf-8", errors="replace").read())
        return "\n".join(parts)

    def test_max_mechanism_id_is_670(self):
        ids = [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)\b", self._profiles_corpus())]
        modern = [i for i in ids if i >= 600]
        assert max(modern) == 670, max(modern)

    def test_725_zero_670_sweeps_fail_by_designed_supersession(self):
        # Documented, not repaired: advancing max numeric mechanism id to
        # 670 supersedes #725's zero-670 profiles/tests sweeps per the
        # #710/#720 convention.
        corpus = self._profiles_corpus()
        assert "mechanism_670_" in corpus
        ids = [int(x) for x in re.findall(r"mechanism_id:\s*['\"]?(\d+)", corpus)]
        assert 670 in ids

    def test_670_key_unique_repo_wide(self):
        corpus = self._profiles_corpus()
        keys = re.findall(r"\bmechanism_670_[a-z0-9_]+\b", corpus)
        # The block key plus the designed distinct-naming key in
        # novelty_vs_existing (mechanism_670_distinct) are the only two.
        assert set(keys) == {MECH_KEY, "mechanism_670_distinct"}, keys

    def test_zero_underscore_671_keys(self):
        assert "mechanism_671_" not in self._profiles_corpus()


class TestLedger727:
    def test_falsification_ledger_holds_at_24(self):
        parts = []
        for f in glob.glob(os.path.join(REPO_ROOT, "profiles", "*.yaml")):
            parts.append(open(f, encoding="utf-8", errors="replace").read())
        corpus = "\n".join(parts)
        assert "TWENTY-FOURTH" in corpus
        assert "TWENTY-FIFTH" not in corpus

    def test_670_not_a_falsification_member(self):
        corpus = _wired()
        block = corpus.split(MECH_KEY + ":")[1].split("\n  google:")[0]
        assert "NOT a falsification-family member" in block
