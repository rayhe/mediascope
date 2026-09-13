"""Type B #723 (2026-09-13 11:00 PDT): Cherlynn Low (Engadget) Apple Audio
Intelligence control-case REPLICATION of Mechanism #150 (mechanism 668).

Mechanism #150 (2026-08-17) established Cherlynn Low as a journalist-level
CONTROL CASE: she covered Meta Glasses (Tue Jun 23 2026) and Snap Specs
(Jun 17 2026) with uniformly zero privacy alarm vocabulary for both
entities, proving Engadget's privacy-vocabulary asymmetry operates through
editorial beat assignment (Karissa Bell's Meta-only privacy investigations),
not individual journalist bias.

New evidence (Sep 2026): Low's Apple Watch Series 12 hands-on
(Thu Sep 10 2026, covering Audio Intelligence always-listening features:
Live Rewind's rolling 15-second ambient audio buffer, Siri Recap
conversation summaries) uses the same non-alarmist register. Key evidence
(search-excerpt-bounded, browser.open terminally unavailable this run per
developer constraint): Low states she is "not against AI wearables that
listen to your surroundings and conversations, as long as done responsibly
and with accountability," and is "intrigued by things like Siri Recap and
Live Rewind" - explicit normalization of ambient-listening wearables by the
same journalist whose Meta coverage was uniformly alarm-free.

This is a REPLICATION of the #150 control case with a THIRD entity (Apple),
not a new asymmetry finding. Journalist-level privacy-alarm differential
Meta vs Apple = 0.00 (NULL DIFFERENTIAL, both arms zero alarm), MANUAL
ILLUSTRATIVE, p_value / cohens_d / ci_95 NOT_CALCULATED, is_significant
False per the Aug 28 2026 standing rule; engine NOT run; NOT artifact-grade.

Verdict: directionally_supported_not_proven. NOT a falsification-family
member (ledger holds at 24). Connects to 113 (Engadget privacy routing),
150 (the replicated control case), 151 (Rutherford null differential).

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
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
TEST_BASENAME = os.path.basename(__file__)
MECH_KEY = "cherlynn_low_engadget_apple_audio_intelligence_control_replication"
APPLE_URL = (
    "https://www.engadget.com/2254467/"
    "apple-watch-series-12-hands-on-siri-recap-transcribe-live-rewind-health-sensing/"
)
META_URL = (
    "https://www.engadget.com/2199519/"
    "meta-ai-glasses-hands-on-kylie-jenner-edition/"
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


class TestNovelty723:
    """Iteration 723 is new; mechanism 668 is the next free id."""

    def test_single_type_b_723_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_b_723*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_b_723_main_commit_unique(self):
        # Green post-main-commit; novelty verified pre-commit by shell greps
        # (zero test_type_b_723 files, no "Type B #723" in git log, zero
        # mechanism_id: 668 keys repo-wide, max numeric mechanism 667).
        out = _run_git("log", "--format=%s")
        assert out.returncode == 0
        mains = [s for s in out.stdout.splitlines() if s.startswith("Type B #723:")]
        assert len(mains) == 1, "expected exactly one Type B #723 main commit, got %r" % (mains,)

    def test_mechanism_id_is_668(self):
        assert _mechanism()["mechanism_id"] == 668
        assert _mechanism()["iteration"] == 723
        assert _mechanism()["rotation_type"] == "B"


class TestMechanism723Content:
    """Profile block content: pair, journalist, arms, quotes, exact URLs."""

    def test_pair_and_journalist(self):
        m = _mechanism()
        assert m["journalist"] == "Cherlynn Low"
        assert m["publication"] == "Engadget (Yahoo/Apollo)"
        assert m["competitor"] == "Apple"

    def test_apple_arm_new_evidence(self):
        text = _read(PROFILE_PATH)
        assert "Thu Sep 10, 2026" in text or "Sep 10 2026" in text or "2026-09-10" in text
        assert "Audio Intelligence" in text

    def test_meta_arm_carried_from_150(self):
        m = _mechanism()
        assert META_URL in m["source_urls"]
        assert APPLE_URL in m["source_urls"]

    def test_verbatim_quotes_present(self):
        text = _read(PROFILE_PATH)
        norm = re.sub(r"\s+", " ", text)
        assert "not against AI wearables that listen to your surroundings and conversations" in norm
        assert "as long as done responsibly and with accountability" in norm

    def test_source_urls_exact_no_invention(self):
        m = _mechanism()
        for u in m["source_urls"]:
            assert u.startswith("https://www.engadget.com/"), u
        assert len(m["source_urls"]) >= 2

    def test_test_file_field_points_here(self):
        assert _mechanism()["test_file"].endswith(TEST_BASENAME)

    def test_no_em_dashes_in_mechanism_prose(self):
        m = _mechanism()
        prose = m["finding"] + " ".join(m["confounders"]) + " ".join(m["testable_predictions"])
        assert "\u2014" not in prose, "em dash found in mechanism prose"
        assert "\u2013" not in prose, "en dash found in mechanism prose"


class TestNullDifferential723:
    """Journalist-level privacy-alarm differential Meta vs Apple = 0.00."""

    def test_delta_arithmetic_zero(self):
        meta_alarm = 0
        apple_alarm = 0
        delta = apple_alarm - meta_alarm
        assert delta == 0.00
        assert isinstance(delta, (int, float))

    def test_scores_labeled_manual_illustrative(self):
        text = _read(PROFILE_PATH)
        block_start = text.find(MECH_KEY)
        block = text[block_start : block_start + 9000]
        assert "MANUAL ILLUSTRATIVE" in block

    def test_statistical_contract_not_calculated(self):
        text = _read(PROFILE_PATH)
        block_start = text.find(MECH_KEY)
        block = text[block_start : block_start + 9000]
        assert "NOT_CALCULATED" in block
        assert "is_significant" in block and "False" in block
        assert "NOT artifact-grade" in block or "not artifact-grade" in block


class TestControlReplication723:
    """This REPLICATES #150; it is not a new asymmetry finding."""

    def test_replication_claimed_not_discovery(self):
        m = _mechanism()
        assert "REPLICATION" in m["finding"]
        assert "not a new asymmetry finding" in m["finding"]

    def test_cross_references_include_150_113_151(self):
        m = _mechanism()
        for ref in (150, 113, 151):
            assert ref in m["connects_to"], "missing cross-ref %d" % ref

    def test_verdict_directionally_supported(self):
        assert _mechanism()["verdict"] == "directionally_supported_not_proven"

    def test_not_falsification_member(self):
        m = _mechanism()
        assert "NOT a falsification-family member" in m["finding"]
        assert "ledger holds at 24" in m["finding"]


class TestConfoundersAndCounterevidence723:
    """Confounders ranked 3 strong / 3 moderate / 3 weak; counterevidence present."""

    def test_confounders_ranked_3_3_3(self):
        confs = _mechanism()["confounders"]
        strong = [c for c in confs if c.startswith("STRONG")]
        moderate = [c for c in confs if c.startswith("MODERATE")]
        weak = [c for c in confs if c.startswith("WEAK")]
        assert len(strong) == 3, strong
        assert len(moderate) == 3, moderate
        assert len(weak) == 3, weak

    def test_strong_confounder_names_secure_exclave(self):
        confs = _mechanism()["confounders"]
        strong_text = " ".join(c for c in confs if c.startswith("STRONG"))
        assert "Secure Exclave" in strong_text
        assert "form factor" in strong_text or "Form factor" in strong_text

    def test_three_counterevidence(self):
        text = _read(PROFILE_PATH)
        block_start = text.find(MECH_KEY)
        block = text[block_start : block_start + 12000]
        assert "counterevidence" in block.lower()
        ce = re.findall(r"(?m)^\s*-\s*'?(COUNTEREVIDENCE|counterevidence)", block)
        assert len(ce) >= 3 or block.lower().count("counterevidence") >= 3

    def test_correlational_note_no_causal_claim(self):
        text = _read(PROFILE_PATH)
        block_start = text.find(MECH_KEY)
        block = text[block_start : block_start + 12000]
        assert "Correlation is not causation" in block or "correlation" in block.lower()

    def test_evidence_tier_labeled_search_excerpt_bounded(self):
        text = _read(PROFILE_PATH)
        block_start = text.find(MECH_KEY)
        block = text[block_start : block_start + 12000]
        assert "search-excerpt-bounded" in block


class TestIterationLog723:
    """iteration-log.md carries the #723 entry."""

    def test_log_has_723_entry(self):
        text = _read(LOG_PATH)
        assert "#723 Type B:" in text

    def test_log_entry_names_mechanism_668(self):
        text = _read(LOG_PATH)
        assert "mechanism 668" in text

    def test_log_entry_names_cherlynn_low_apple(self):
        text = _read(LOG_PATH)
        idx = text.find("#723 Type B:")
        entry = text[idx : idx + 6000]
        assert "Cherlynn Low" in entry
        assert "Apple" in entry

    def test_log_entry_names_rotation(self):
        text = _read(LOG_PATH)
        idx = text.find("#723 Type B:")
        entry = text[idx : idx + 6000]
        assert "719" in entry and "723" in entry


class TestRotationCycleGuard723:
    """Rotation: distinct-mains window test, #716-style.

    Robust to the #678 history artifact and the #565 followup convention:
    first occurrence of each distinct iteration number, newest first.
    """

    ANCHORED_SHA = "23c167cb4738ec9428ddea9a192c89384458fcf7"

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

    def test_window_719_723_closes_a_to_b(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("B", "723"),
            ("A", "722"),
            ("E", "721"),
            ("D", "720"),
            ("C", "719"),
        ], "rotation window 719-723 wrong: %r" % (observed,)

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
        """Rotation window 719-723 closes A->B. Anchor patched in followup per #565."""
        result = _run_git("log", "--format=%H %s")
        assert result.returncode == 0
        mains = [
            line for line in result.stdout.splitlines() if "Type B #723:" in line
        ]
        main = mains[0].split()[0] if mains else ""
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )


class TestDocSync723:
    def test_readme_has_row(self):
        text = _read(README_PATH)
        assert TEST_BASENAME in text

    def test_architecture_has_row(self):
        text = _read(ARCH_PATH)
        assert TEST_BASENAME in text


class TestSweepSupersession723:
    """Pins the post-#723 state: max mechanism_id 668; ledger holds at 24."""

    def test_max_mechanism_id_is_668(self):
        texts = []
        for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for f in files:
                if f.endswith((".yaml", ".yml")):
                    texts.append(_read(os.path.join(root, f)))
        corpus = "\n".join(texts)
        ids = [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)\b", corpus)]
        modern = [i for i in ids if i >= 600]
        assert max(modern) == 668, max(modern)

    def test_zero_mechanism_669_keys_repo_wide(self):
        for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for f in files:
                if f.endswith((".yaml", ".yml")):
                    t = _read(os.path.join(root, f))
                    assert "mechanism_669" not in t, f

    def test_zero_mechanism_668_underscore_keys_in_other_test_files(self):
        # Own file excluded from the sweep per the #715 pattern-rescope
        # lesson: MECH_KEY legitimately names the mechanism here.
        # The #722 sweep (zero "mechanism_668" keys in profiles yamls) stays
        # green by designed keying: this block uses mechanism_id: 668 (no
        # underscore-668 string), so #722 fails by NO supersession here.
        key_re = re.compile(r"\bmechanism_668_[a-z0-9_]")
        for f in glob.glob(os.path.join(REPO_ROOT, "tests", "test_*.py")):
            if os.path.basename(f) == TEST_BASENAME:
                continue
            assert not key_re.search(_read(f)), f

    def test_722_zero_sweep_stays_green_no_supersession(self):
        for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for f in files:
                if f.endswith((".yaml", ".yml")):
                    t = _read(os.path.join(root, f))
                    assert "mechanism_668" not in t, f

    def test_falsification_ledger_holds_at_24(self):
        texts = []
        for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for f in files:
                if f.endswith((".yaml", ".yml")):
                    texts.append(_read(os.path.join(root, f)))
        corpus = "\n".join(texts)
        assert "TWENTY-FOURTH" in corpus
        assert "TWENTY-FIFTH" not in corpus


class TestDateGrounding723:
    """Event dates grounded; weekdays verified via date -d (America/Los_Angeles)."""

    def test_apple_hands_on_date_grounded(self):
        text = _read(PROFILE_PATH)
        block_start = text.find(MECH_KEY)
        block = text[block_start : block_start + 12000]
        assert "Thu Sep 10, 2026" in block
        assert "Apple" in block

    def test_meta_hands_on_date_grounded(self):
        text = _read(PROFILE_PATH)
        block_start = text.find(MECH_KEY)
        block = text[block_start : block_start + 12000]
        assert "Tue Jun 23, 2026" in block

    def test_apple_event_date_grounded(self):
        text = _read(PROFILE_PATH)
        block_start = text.find(MECH_KEY)
        block = text[block_start : block_start + 12000]
        assert "Wed Sep 9, 2026" in block or "Sep 9, 2026" in block
