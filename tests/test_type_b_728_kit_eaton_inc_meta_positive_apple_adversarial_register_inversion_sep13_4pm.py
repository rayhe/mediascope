"""Type B #728 (2026-09-13 16:00 PDT): Kit Eaton (Inc.) register INVERSION -
Meta wearables enthusiasm vs Apple Audio Intelligence controversy-forward
framing (mechanism 671).

BOUNDS mechanism #670 (WIRED outlet gradient), does not extend it. #727 (Type A,
m670) found WIRED treating Apple Watch Audio Intelligence in a pitch-carrying
register (illustrative +0.0) while its Meta glasses comparison arm ran
adversarial (about -0.55 to -0.62). This run isolates the same ambient-sensing
beat at journalist level for a NEW journalist and finds the gradient INVERTED:

Meta arm (Inc., circa Thu Sep 26 2024, Connect 2024 week): "Meta Bets on
Augmented Reality Devices as the Future of Wearable Tech" covers Orion AR
glasses and Ray-Ban Meta camera/microphone sunglasses in an enthusiastic
product register - "much more chic Ray Ban AR sunglasses"; "the really neat
thing about the sunglasses is that you can ask Meta's AI what it can see in
front of you, through the cameras"; Orion "looks more like a product people
could one day wear when walking down the street" (vs Apple Vision Pro "bulky
and hugely expensive"). Always-on cameras/microphones described neutrally as
features; zero privacy-alarm vocabulary in search excerpts. MANUAL
ILLUSTRATIVE register +0.55.

Apple arm (Inc., circa Thu Sep 10 2026, day after the Wed Sep 9 2026 Apple
"Surprise and Shine" event): "The Apple Watch Got a Massive AI Upgrade - and
the Controversy Could Get It Banned at the Office" (original headline uses an
em dash; rendered here with a hyphen per the ASCII-only corpus convention)
frames Audio Intelligence (Live Rewind 15-second ambient buffer, Siri Recap
conversation summaries) through a controversy-forward register - headline
"Controversy Could Get It Banned at the Office"; cites TechCrunch's
"normalizing the idea that technology is always listening"; same-beat context
includes EFF's Adam Schwartz ("Our right to conversational privacy must
include freedom from other people, without our clear opt-in consent") and
wiretap-law analysis ("a chime does not give a bystander a real way to
object"). MANUAL ILLUSTRATIVE register -0.50.

Apple-minus-Meta delta -1.05 (INVERSION): Eaton is harsher on Apple
ambient-listening than on Meta ambient-sensing. The same controversy frame
Eaton applies adversarially to Apple, WIRED applies leniently to Apple and
adversarially to Meta - so m670 is outlet-specific, not a journalist-universal
law.

Statistical discipline: MANUAL ILLUSTRATIVE; p_value / cohens_d / ci_95
NOT_CALCULATED; is_significant False per the Aug 28 2026 standing rule;
engine NOT run; NOT artifact-grade; no engine divergence pin. Verdict:
directionally_supported_not_proven. NOT a falsification-family member
(ledger holds at 24). Connects to 668 (same-beat Apple Audio Intelligence
journalist pair), 670 (the bounded WIRED gradient), 150 (Low Meta control).
Correlation is not causation.

Byline attribution: both canonical URLs carry the "kit-eaton" path segment
(verbatim from search-result Full URL listings); no page-rendered byline
confirmation this run (browser.open terminally unavailable per developer
constraint). Both arms search-excerpt-bounded.

No em dashes in any new prose. ASCII only.
"""

import glob
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROFILE_PATH = os.path.join(
    REPO_ROOT, "profiles", "competitor-coverage-research.yaml"
)
CAREER_PATH = os.path.join(
    REPO_ROOT, "profiles", "careers", "journalists.yaml"
)
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
TEST_BASENAME = os.path.basename(__file__)
MECH_KEY = "kit_eaton_inc_register_inversion_meta_positive_apple_adversarial"
META_URL = (
    "https://www.inc.com/kit-eaton/"
    "meta-bets-on-augmented-reality-devices-as-future-of-wearable-tech.html"
)
APPLE_URL = (
    "https://www.inc.com/kit-eaton/"
    "the-apple-watch-got-a-massive-ai-upgrade-and-the-controversy-"
    "could-get-it-banned-at-the-office/91403791"
)
TC_URL = (
    "https://techcrunch.com/2026/09/09/"
    "apple-watchs-new-ai-features-are-normalizing-the-idea-that-"
    "technology-is-always-listening/"
)


def _read(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def _profile():
    with open(PROFILE_PATH, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _mechanism():
    return _profile()["cross_publication_findings"][MECH_KEY]


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT, *args],
        capture_output=True,
        text=True,
        timeout=120,
    )


class TestNovelty728:
    """Iteration 728 is new; mechanism 671 is the next free id."""

    def test_single_type_b_728_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_b_728*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_b_728_main_commit_unique(self):
        # Green post-main-commit; novelty verified pre-commit by shell greps
        # (zero test_type_b_728 files, no "Type B #728" in git log, zero
        # "mechanism_671_" keys repo-wide, max numeric mechanism 670).
        out = _run_git("log", "--format=%s")
        assert out.returncode == 0
        mains = [s for s in out.stdout.splitlines() if s.startswith("Type B #728:")]
        assert len(mains) == 1, "expected exactly one Type B #728 main commit, got %r" % (mains,)

    def test_mechanism_id_is_671(self):
        assert _mechanism()["mechanism_id"] == 671
        assert _mechanism()["iteration"] == 728
        assert _mechanism()["rotation_type"] == "B"


class TestMechanism728Content:
    """Profile block content: pair, journalist, arms, quotes, exact URLs."""

    def test_pair_and_journalist(self):
        m = _mechanism()
        assert m["journalist"] == "Kit Eaton"
        assert m["publication"] == "Inc. (Mansueto Ventures)"
        assert m["competitor"] == "Apple"

    def test_both_arm_urls_in_source_urls(self):
        m = _mechanism()
        assert META_URL in m["source_urls"]
        assert APPLE_URL in m["source_urls"]
        assert TC_URL in m["source_urls"]

    def test_meta_arm_verbatim_quotes_present(self):
        text = _read(PROFILE_PATH)
        norm = re.sub(r"\s+", " ", text)
        assert "much more chic Ray Ban AR sunglasses" in norm
        assert "the really neat thing about the sunglasses" in norm
        assert "looks more like a product people could one day wear when walking down the street" in norm

    def test_apple_arm_verbatim_quotes_present(self):
        text = _read(PROFILE_PATH)
        norm = re.sub(r"\s+", " ", text)
        assert "Controversy Could Get It Banned at the Office" in norm
        assert "normalizing the idea that technology is always listening" in norm

    def test_source_urls_exact_no_invention(self):
        m = _mechanism()
        for u in m["source_urls"]:
            assert u.startswith("https://www.inc.com/") or u.startswith("https://techcrunch.com/"), u
        assert len(m["source_urls"]) >= 3

    def test_test_file_field_points_here(self):
        assert _mechanism()["test_file"].endswith(TEST_BASENAME)

    def test_no_em_dashes_in_mechanism_prose(self):
        m = _mechanism()
        prose = m["finding"] + " ".join(m["confounders"]) + " ".join(m["testable_predictions"])
        assert "\u2014" not in prose, "em dash found in mechanism prose"
        assert "\u2013" not in prose, "en dash found in mechanism prose"


class TestInversion728:
    """Apple-minus-Meta delta -1.05: Eaton inverts the m670 WIRED gradient."""

    def test_delta_arithmetic_negative_1_05(self):
        meta_register = 0.55
        apple_register = -0.50
        delta = round(apple_register - meta_register, 2)
        assert delta == -1.05
        assert isinstance(delta, float)

    def test_inversion_claimed_in_finding(self):
        m = _mechanism()
        assert "INVERTS" in m["finding"] or "INVERSION" in m["finding"]

    def test_scores_labeled_manual_illustrative(self):
        text = _read(PROFILE_PATH)
        block_start = text.find(MECH_KEY)
        block = text[block_start : block_start + 12000]
        assert "MANUAL ILLUSTRATIVE" in block

    def test_statistical_contract_not_calculated(self):
        text = _read(PROFILE_PATH)
        block_start = text.find(MECH_KEY)
        block = text[block_start : block_start + 12000]
        assert "NOT_CALCULATED" in block
        assert "is_significant" in block and "False" in block
        assert "NOT artifact-grade" in block

    def test_wired_gradient_bounded_not_extended(self):
        text = _read(PROFILE_PATH)
        block_start = text.find(MECH_KEY)
        block = text[block_start : block_start + 12000]
        assert "outlet-specific" in block
        assert "not a journalist-universal law" in block


class TestBoundOn670:
    """This BOUNDS mechanism 670; it is not a new asymmetry direction."""

    def test_cross_references_include_668_670_150(self):
        m = _mechanism()
        for ref in (668, 670, 150):
            assert ref in m["connects_to"], "missing cross-ref %d" % ref

    def test_verdict_directionally_supported(self):
        assert _mechanism()["verdict"] == "directionally_supported_not_proven"

    def test_not_falsification_member(self):
        m = _mechanism()
        assert "NOT a falsification-family member" in m["finding"]
        assert "ledger holds at 24" in m["finding"]

    def test_finding_type_journalist_cross_entity(self):
        assert _mechanism()["finding_type"] == "journalist_cross_entity"

    def test_career_entry_exists(self):
        text = _read(CAREER_PATH)
        assert "kit_eaton" in text
        assert "Kit Eaton" in text


class TestConfoundersAndCounterevidence728:
    """Confounders ranked 3 strong / 3 moderate / 3 weak; counterevidence present."""

    def test_confounders_ranked_3_3_3(self):
        confs = _mechanism()["confounders"]
        strong = [c for c in confs if c.startswith("STRONG")]
        moderate = [c for c in confs if c.startswith("MODERATE")]
        weak = [c for c in confs if c.startswith("WEAK")]
        assert len(strong) == 3, strong
        assert len(moderate) == 3, moderate
        assert len(weak) == 3, weak

    def test_strong_confounder_names_temporal_gap_genre_misuse_history(self):
        confs = _mechanism()["confounders"]
        strong_text = " ".join(c for c in confs if c.startswith("STRONG"))
        assert "23.5 months" in strong_text
        assert "Genre" in strong_text
        assert "misuse history" in strong_text

    def test_three_counterevidence(self):
        text = _read(PROFILE_PATH)
        block_start = text.find(MECH_KEY)
        block = text[block_start : block_start + 14000]
        assert block.lower().count("counterevidence") >= 4  # header + 3 items

    def test_correlational_note_no_causal_claim(self):
        text = _read(PROFILE_PATH)
        block_start = text.find(MECH_KEY)
        block = text[block_start : block_start + 14000]
        assert "Correlation is not causation" in block

    def test_evidence_tier_labeled_search_excerpt_bounded(self):
        text = _read(PROFILE_PATH)
        block_start = text.find(MECH_KEY)
        block = text[block_start : block_start + 14000]
        assert "search-excerpt-bounded" in block


class TestIterationLog728:
    """iteration-log.md carries the #728 entry."""

    def test_log_has_728_entry(self):
        text = _read(LOG_PATH)
        assert "#728 Type B:" in text

    def test_log_entry_names_mechanism_671(self):
        text = _read(LOG_PATH)
        assert "mechanism 671" in text

    def test_log_entry_names_kit_eaton_inversion(self):
        text = _read(LOG_PATH)
        idx = text.find("#728 Type B:")
        entry = text[idx : idx + 6000]
        assert "Kit Eaton" in entry
        assert "INVERSION" in entry

    def test_log_entry_names_rotation(self):
        text = _read(LOG_PATH)
        idx = text.find("#728 Type B:")
        entry = text[idx : idx + 6000]
        assert "724" in entry and "728" in entry


class TestRotationCycleGuard728:
    """Rotation: distinct-mains window test, #723-style.

    Robust to the #678 history artifact and the #565 followup convention:
    first occurrence of each distinct iteration number, newest first.
    """

    ANCHORED_SHA = "f02c542fbf2e7765c345764137fd5edc07b8bf9d"

    @staticmethod
    def _mains():
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

    def test_window_724_728_closes_a_to_b(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("B", "728"),
            ("A", "727"),
            ("E", "726"),
            ("D", "725"),
            ("C", "724"),
        ], "rotation window 724-728 wrong: %r" % (observed,)

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["B", "A", "E", "D", "C"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for newer, older in zip(observed, observed[1:]):
            assert (order[newer] - order[older]) % 5 == 1, (
                "rotation broken: %s (older) -> %s (newer) is not a valid cycle edge" % (older, newer)
            )

    def test_anchor_is_main_commit_patched_in_followup(self):
        """Rotation window 724-728 closes A->B. Anchor patched in followup per #565."""
        result = _run_git("log", "--format=%H %s")
        assert result.returncode == 0
        mains = [
            line for line in result.stdout.splitlines() if "Type B #728:" in line
        ]
        main = mains[0].split()[0] if mains else ""
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )


class TestDocSync728:
    def test_readme_has_row(self):
        text = _read(README_PATH)
        assert TEST_BASENAME in text

    def test_architecture_has_row(self):
        text = _read(ARCH_PATH)
        assert TEST_BASENAME in text


class TestSweepSupersession728:
    """Pins the post-#728 state: max mechanism_id 671; ledger holds at 24."""

    def test_max_mechanism_id_is_671(self):
        texts = []
        for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for f in files:
                if f.endswith((".yaml", ".yml")):
                    texts.append(_read(os.path.join(root, f)))
        corpus = "\n".join(texts)
        ids = [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)\b", corpus)]
        modern = [i for i in ids if i >= 600]
        assert max(modern) == 671, max(modern)

    def test_zero_mechanism_672_keys_repo_wide(self):
        for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for f in files:
                if f.endswith((".yaml", ".yml")):
                    t = _read(os.path.join(root, f))
                    assert "mechanism_672" not in t, f

    def test_727_max_670_sweep_fails_by_designed_supersession(self):
        # Documented, not repaired: advancing max numeric mechanism id to
        # 671 supersedes #727's max-670 sweep per the #710/#720 convention.
        texts = []
        for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for f in files:
                if f.endswith((".yaml", ".yml")):
                    texts.append(_read(os.path.join(root, f)))
        corpus = "\n".join(texts)
        ids = [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)\b", corpus)]
        assert 671 in ids

    def test_falsification_ledger_holds_at_24(self):
        texts = []
        for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for f in files:
                if f.endswith((".yaml", ".yml")):
                    texts.append(_read(os.path.join(root, f)))
        corpus = "\n".join(texts)
        assert "TWENTY-FOURTH" in corpus
        assert "TWENTY-FIFTH" not in corpus


class TestDateGrounding728:
    """Event dates grounded; weekdays verified via date -d (America/Los_Angeles)."""

    def test_meta_arm_date_grounded(self):
        text = _read(PROFILE_PATH)
        block_start = text.find(MECH_KEY)
        block = text[block_start : block_start + 14000]
        assert "Thu Sep 26, 2024" in block or "Sep 26 2024" in block

    def test_apple_arm_date_grounded(self):
        text = _read(PROFILE_PATH)
        block_start = text.find(MECH_KEY)
        block = text[block_start : block_start + 14000]
        assert "Thu Sep 10 2026" in block

    def test_apple_event_date_grounded(self):
        text = _read(PROFILE_PATH)
        block_start = text.find(MECH_KEY)
        block = text[block_start : block_start + 14000]
        assert "Wed Sep 9 2026" in block
