"""Type A #677 (2026-09-11 10:00 PDT): WIRED x Google enforcement-strength
register inversion vs WIRED x Meta.

Second scored WIRED x Google mechanism in the corpus (after #547), and the
first publication-level mechanism to put safeguard-strength against register:
Meta ships the strongest documented LED-tamper enforcement in consumer camera
glasses (camera auto-disable on LED tamper; thousands of tampered units
bricked Sep 1, 2026 per Semafor) and gets WIRED's skeptical register (the
reactive "closes loophole" framing of the Aug 27, 2026 second LED fix; the
broader Meta surveillance-alarm baseline -0.773). Google announces Android XR
tamper detection (Jul 2026) with NO documented automatic camera shutdown
(eweek: no documented auto-disable, processing location, or enforcement
mechanics) and gets the enthusiastic hands-on register (WIRED May 19, 2026,
Chokkattu + Ashworth, zero surveillance vocabulary), plus zero WIRED
privacy-register scrutiny of the safeguard's limits.

New evidence this run (both new URLs to corpus):
1. WIRED Google Android XR hands-on direct URL
   https://www.wired.com/story/hands-on-with-all-of-google-new-upcoming-android-xr-smart-glasses/
   (May 19, 2026, Chokkattu + Ashworth) - resolves the proxy-only gap flagged
   in mechanism #547 (zero profiles/ hits before this run; verified via the
   mechanism #431 commit note, Sep 1, 2026).
2. eweek Android XR tamper-detection weakness documentation
   https://www.eweek.com/news/android-xr-tamper-detection/
   (third-party attested via search snippet this run, not opened first-hand).

Meta arms are in-corpus comparators reused per the #672 precedent:
- WIRED Meta Ray-Ban Display second LED fix (Boone Ashworth, Aug 27, 2026,
  https://www.wired.com/story/meta-ray-ban-display-second-led-fix/)
  "closes loophole" reactive register, MANUAL ILLUSTRATIVE -0.15.
- Semafor via PetaPixel Meta bricking (Sep 1, 2026,
  https://petapixel.com/2026/09/01/meta-claims-to-have-bricked-thousands-of-smart-glasses/).

Scorer (MANUAL ILLUSTRATIVE, standing rule Aug 28 2026; arithmetic only):
Google [+0.15] avg 0.15 vs Meta [-0.15] avg -0.15. Delta (Google minus Meta)
+0.30. p_value NOT_CALCULATED, cohens_d NOT_CALCULATED, ci NOT_CALCULATED,
is_significant False, artifact_grade False. NOT artifact-grade: n=1 scored
item per arm (degenerate statistical contract per the #638/#643 convention),
Meta arm tone is a manual illustrative assignment for the reactive register,
eweek arm is third-party snippet-attested, WIRED tamper-detection silence is
a bounded search-result absence, no engine run.

Interpretation (extends #547, #431, #622): the google entity block's
"adversarial" coverage prediction FAILS for this register lane as well. Condé
Nast gets $0 AI licensing from Google, Advance sued Google (Jan 14, 2026
SDNY), and Lynch called Google AI Overviews a revenue "death blow" - yet the
publication suing Google covered Google's camera glasses with delight and has
not scrutinized Google's weaker tamper safeguard. The soft register cannot be
bought loyalty.

Strongest counterargument: the inversion is an artifact of product stage and
news flow. Meta's enforcement exists because Meta's glasses are the only
shipped camera glasses at scale with documented tampering in the wild, which
generates real watchdog news (the bricking, the loophole fix). Google's
safeguard is a pre-launch announcement with no tampered units and no news peg,
so there is nothing for WIRED's privacy register to bite on. The enthusiastic
hands-on predates the safeguard announcement entirely. Accepted as a major
confounder; claim stays bounded, correlation-only, MANUAL ILLUSTRATIVE.

Evidence hygiene: both new URLs carried verbatim from tool output this run;
no wired.com URLs constructed. The Jul 22 to Sep 11 WIRED tamper-detection
silence is stated as a bounded search-result statement only (iteration-492
rule). No em dashes in any new prose. No statistical significance claimed.

Durable conventions (from #495): line-anchored (^, re.MULTILINE) heading
search in iteration-log.md; relative newest-first ordering between
neighbors, never absolute-top or fixed head slices.
"""

import glob
import os
import re
import subprocess
import sys

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO_ROOT, "profiles", "wired.yaml")
LOG = os.path.join(REPO_ROOT, "iteration-log.md")
TEST_BASENAME = "test_type_a_677_wired_google_enforcement_strength_register_inversion_vs_meta_sep11_10am.py"

MECH_KEY = "mechanism_640_wired_google_enforcement_strength_register_inversion_vs_meta_sep11"

HANDS_ON_URL = "https://www.wired.com/story/hands-on-with-all-of-google-new-upcoming-android-xr-smart-glasses/"
EWEEK_URL = "https://www.eweek.com/news/android-xr-tamper-detection/"
LED_FIX_URL = "https://www.wired.com/story/meta-ray-ban-display-second-led-fix/"
BRICKING_URL = "https://petapixel.com/2026/09/01/meta-claims-to-have-bricked-thousands-of-smart-glasses/"


def _load_profile():
    with open(PROFILE) as f:
        return yaml.safe_load(f)


def _mechanism():
    return _load_profile()["competitor_relationships"]["google"][MECH_KEY]


def _mechanism_block_text():
    with open(PROFILE) as f:
        text = f.read()
    start = text.index(MECH_KEY)
    end = text.index("\n  microsoft:", start)
    return text[start:end]


def _read(path):
    with open(path) as f:
        return f.read()


def _run_git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


class TestNovelty677:
    """Iteration 677 is new; nothing with this number existed pre-commit."""

    def test_single_type_a_677_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_a_677*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_a_677_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; the main
        # commit exists exactly once post-commit and its SHA matches the
        # rotation-guard anchor patched in the followup. Novelty was
        # verified pre-commit by shell greps (zero test_type_a_677 files,
        # no #677 in git log, no mechanism_id 640 in profiles); this test
        # pins that no duplicate #677 main commit ever appears.
        out = _run_git("log", "--format=%H %s")
        mains = [
            line
            for line in out.stdout.splitlines()
            if re.match(r"^Type A #677:", line.split(" ", 1)[-1])
        ]
        assert len(mains) == 1, "expected exactly one Type A #677 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        assert sha == TestRotationCycleGuard677.ANCHORED_SHA, (
            "anchor patched in followup per #565 convention"
        )


class TestMechanismExistsAndShape:
    def test_mechanism_key_present_under_google(self):
        profile = _load_profile()
        assert MECH_KEY in profile["competitor_relationships"]["google"]

    def test_mechanism_id_is_next_free(self):
        assert _mechanism()["mechanism_id"] == 640

    def test_identity_fields(self):
        m = _mechanism()
        assert m["iteration"] == 677
        assert m["iteration_type"] == "A"
        assert m["date"] == "2026-09-11"
        assert m["type"] == "Type A - Competitor Coverage Deep Dive"

    def test_publication_pair_and_comparators(self):
        m = _mechanism()
        assert m["publication_pair"] == "WIRED x Google"
        assert m["competitor"] == "google"
        assert m["comparison_entities"] == ["meta"]

    def test_author_kit_with_ray(self):
        assert _mechanism()["author"] == "Kit (with Ray)"

    def test_no_em_dashes_in_block(self):
        assert '\u2014' not in _mechanism_block_text()


class TestGoogleArms:
    def test_hands_on_url_verbatim(self):
        urls = [a.get("url") for a in _mechanism()["articles"]]
        assert HANDS_ON_URL in urls

    def test_hands_on_new_to_corpus(self):
        arts = _mechanism()["articles"]
        hands_on = [a for a in arts if a.get("url") == HANDS_ON_URL][0]
        assert "first profiles/ appearance" in hands_on["url_novelty"]
        assert hands_on["authors"] == "Julian Chokkattu, Boone Ashworth"
        assert hands_on["date"] == "2026-05-19"
        assert hands_on["manual_illustrative_tone"] == 0.15
        assert "zero surveillance vocabulary" in hands_on["register"]

    def test_hands_on_resolves_proxy_only_gap(self):
        f = _mechanism()["finding"]
        assert "resolving the proxy-only gap flagged in mechanism #547" in f

    def test_eweek_url_verbatim(self):
        urls = [a.get("url") for a in _mechanism()["articles"]]
        assert EWEEK_URL in urls

    def test_eweek_new_to_corpus_and_snippet_attested(self):
        arts = _mechanism()["articles"]
        eweek = [a for a in arts if a.get("url") == EWEEK_URL][0]
        assert eweek["url_novelty"] == "first corpus appearance this run"
        assert "search-snippet attested" in eweek["evidence_grade"]
        assert "not opened first-hand" in eweek["evidence_grade"]
        assert "had not documented automatic camera shutdown" in eweek["key_claim"]

    def test_tamper_detection_silence_bounded(self):
        f = _mechanism()["finding"]
        assert "Jul 22 to Sep 11, 2026" in f
        assert "iteration-492 rule" in f
        assert "not a proven zero" in f


class TestMetaComparators:
    def test_led_fix_url_verbatim(self):
        urls = [a.get("url") for a in _mechanism()["articles"]]
        assert LED_FIX_URL in urls

    def test_led_fix_closes_loophole_register(self):
        arts = _mechanism()["articles"]
        led = [a for a in arts if a.get("url") == LED_FIX_URL][0]
        assert led["author"] == "Boone Ashworth"
        assert "closes loophole" in led["register"]
        assert led["manual_illustrative_tone"] == -0.15
        assert "mechanism #431" in led["evidence_grade"]

    def test_bricking_url_verbatim(self):
        urls = [a.get("url") for a in _mechanism()["articles"]]
        assert BRICKING_URL in urls

    def test_bricking_in_corpus_via_547(self):
        arts = _mechanism()["articles"]
        brick = [a for a in arts if a.get("url") == BRICKING_URL][0]
        assert "mechanism #547" in brick["evidence_grade"]

    def test_four_articles_total(self):
        assert len(_mechanism()["articles"]) == 4


class TestScorer:
    def test_arrays(self):
        r = _mechanism()["asymmetry_scorer_result"]
        assert r["target_entity"] == "google"
        assert r["target_tones_manual_illustrative"] == [0.15]
        assert r["reference_entity"] == "meta"
        assert r["reference_tones_manual_illustrative"] == [-0.15]

    def test_arithmetic(self):
        r = _mechanism()["asymmetry_scorer_result"]
        assert abs(r["target_avg"] - 0.15) < 1e-9
        assert abs(r["reference_avg"] - (-0.15)) < 1e-9
        assert abs(r["delta_google_minus_meta"] - 0.3) < 1e-9

    def test_manual_illustrative_guards(self):
        r = _mechanism()["asymmetry_scorer_result"]
        assert r["p_value"] == "NOT_CALCULATED"
        assert r["cohens_d"] == "NOT_CALCULATED"
        assert r["ci"] == "NOT_CALCULATED"
        assert r["is_significant"] is False
        assert r["artifact_grade"] is False

    def test_finding_layer_not_significant(self):
        assert _mechanism()["asymmetry_scorer_result"]["is_significant"] is False
        assert "is_significant false" in _mechanism()["finding"]

    def test_limitations_stated(self):
        r = _mechanism()["asymmetry_scorer_result"]
        assert "n=1" in r["limitations"]
        assert "no engine run" in r["limitations"]
        assert "degenerate statistical contract" in r["limitations"]


class TestConfoundersAndCounterargument:
    def test_confounders_present(self):
        confs = _mechanism()["confounders"]
        assert len(confs) >= 5
        blob = " ".join(confs)
        assert "product stage" in blob
        assert "time order" in blob
        assert "Cameron" in blob
        assert "iteration-492 rule" in blob

    def test_strongest_counterargument_product_stage(self):
        ca = _mechanism()["strongest_counterargument"]
        assert "product stage" in ca
        assert "MANUAL ILLUSTRATIVE" in ca
        assert "correlation-only" in ca

    def test_financial_context_prediction_fails(self):
        fc = _mechanism()["financial_context"]
        assert "FAILS" in fc
        assert "$0 AI licensing from Google" in fc
        assert "SUED Google" in fc

    def test_novelty_distinct_from_prior(self):
        nov = _mechanism()["novelty"]
        for prior in ["#547", "#431", "#622"]:
            assert prior in nov
        assert "safeguard-strength against register" in nov

    def test_test_file_field_matches_this_file(self):
        assert _mechanism()["test_file"].endswith(TEST_BASENAME)


class TestIterationLog677:
    def test_log_starts_with_677(self):
        text = _read(LOG)
        assert text.startswith("#677 Type A")

    def test_log_entry_relative_order(self):
        text = _read(LOG)
        m677 = re.search(r"^#677\b", text, re.MULTILINE)
        m676 = re.search(r"^#676\b", text, re.MULTILINE)
        assert m677 is not None and m676 is not None
        assert m677.start() < m676.start()

    def test_log_entry_content(self):
        text = _read(LOG)
        start = text.index("#677 Type A")
        end = text.index("#676 Type E")
        block = text[start:end]
        assert "WIRED x Google" in block
        assert "+0.30" in block
        assert "mechanism 640" in block
        assert "NOT artifact-grade" in block


class TestRotationCycleGuard677:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #677 main-commit SHA is known.
    ANCHORED_SHA = "5508b2a716234a6f3b74e598ff88f192b8e125fe"

    @staticmethod
    def _mains():
        out = _run_git("log", "--format=%s")
        assert out.returncode == 0
        return [
            s for s in out.stdout.splitlines()
            if re.match(r"^Type [A-E] #\d+:", s)
        ]

    def test_window_673_677_closes_e_to_a(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("A", "677"),
            ("E", "676"),
            ("D", "675"),
            ("C", "674"),
            ("B", "673"),
        ], "rotation window 673-677 wrong: %r" % (observed,)

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

    def test_anchor_is_main_commit_patched_in_followup(self):
        result = _run_git("log", "--format=%H %s")
        assert result.returncode == 0
        mains = [
            line for line in result.stdout.splitlines() if "Type A #677:" in line
        ]
        main = mains[0].split()[0] if mains else ""
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )


class TestDocSync677:
    # Fails pre-commit by design per the #565 followup convention; the README
    # stats table refresh, narrative line, test-file table row, and
    # ARCHITECTURE row land in the doc-sync commit.
    def _readme_stats(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        m = re.search(r"\| Tests \| (\d+) \| Across (\d+) test files \|", text)
        assert m, "README stats table row not found"
        return int(m.group(1)), int(m.group(2))

    def _actual_counts(self):
        out = subprocess.run(
            [sys.executable, "scripts/count_stats.py", "--pytest"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=400,
        )
        m = re.search(r"Total tests\s+(\d+)", out.stdout)
        assert m
        total = int(m.group(1))
        files = len(glob.glob(os.path.join(REPO_ROOT, "tests", "test_*.py")))
        return total, files

    def test_readme_stats_table_fresh(self):
        assert self._readme_stats() == self._actual_counts()

    def test_readme_narrative_line_fresh(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        m = re.search(r"has \*\*(\d+) tests\*\* across (\d+) test files", text)
        assert m, "README narrative test-count line not found"
        total, files = self._actual_counts()
        assert (int(m.group(1)), int(m.group(2))) == (total, files)

    def test_architecture_row_present(self):
        text = _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))
        assert "test_type_a_677" in text
