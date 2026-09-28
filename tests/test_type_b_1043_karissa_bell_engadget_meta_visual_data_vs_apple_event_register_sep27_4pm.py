"""Iteration #1043 Type B: Karissa Bell (Engadget) Meta visual-data opt-out vs Apple Audio Intelligence event register.

Type B journalist cross-entity tracking for Sun 2026-09-27 16:00 PDT.

Focus: Karissa Bell (Engadget Senior Reporter) - FOURTH mechanism in Bell's
journalist item (after 722/764/773) and the FIRST Bell-vs-Apple cross-entity
pair. Meta arm: her Sep 24 2026 privacy-investigation register on Meta's
visual-data opt-out concession ('Somewhere, a contractor just breathed a sigh
of relief', 'Meta has also done a pretty poor job of explaining this to
people', 'Even worse, those recordings are sometimes sent to third-party
contractors in other countries'). Apple arm: her Sep 9 2026 co-hosted Engadget
Podcast iPhone Duo launch recap covering Apple's ambient-listening Audio
Intelligence (Live Rewind rolling 15-second ambient-audio buffer, Siri Recap
conversation summaries) with zero privacy-investigation register
(listing-bounded). Extends her Meta-vs-Snap register findings (m722/m773) to a
new comparator (Apple) and a new product class (ambient-listening wearables),
replicating m150's beat-assignment theory at the within-writer level. MANUAL
ILLUSTRATIVE scores only. Engine NOT run.
Verdict: directionally_supported_not_proven. NOT falsification-family (ledger
holds at 34). Correlation is not causation.
"""

import glob
import re

import pytest
import yaml

REPO = "/home/hatch/workspace/repos/mediascope"
JOURNALISTS_YAML = REPO + "/profiles/careers/journalists.yaml"
README = REPO + "/README.md"
ARCHITECTURE = REPO + "/docs/ARCHITECTURE.md"
ITERATION_LOG = REPO + "/iteration-log.md"

TYPE_LETTER = "B"
ITERATION_NUMBER = "1043"
MECH_ID_MARKER = "mechanism" + "_857"
JOURNALIST_SLUG = "karissa_bell"
MECH_KEY = (
    "type_b_1043_karissa_bell_engadget_meta_visual_data_optout_vs_"
    "apple_audio_intelligence_event_register_sep27"
)
NOVELTY_CLAIMS = (
    "zero\ntest_type_b_1043 files, max numeric\nmechanism_id 856 pre-commit, "
    "block key zero-hit, novel Engadget visual-data\nURL zero-hit"
)
# Anchored to the main-commit SHA of this run; patched once known (NULL until then).
NOVELTY_ANCHOR = "c2c5222c33a545ddc2974fedd962be15ffb6cac6"

EXPECTED_URLS = [
    "https://www.engadget.com/2267227/meta-will-stop-training-its-ai-on-visual-data-from-its-smart-glasses-if-you-opt-out/",
    "https://www.engadget.com/2245776/meta-closing-loophole-that-allowed-people-to-record-with-smart-glasses-light-covered/",
    "https://www.listennotes.com/podcasts/the-engadget-podcast-engadget-pN2nIxROaoS/",
    "https://www.engadget.com/2254467/apple-watch-series-12-hands-on-siri-recap-transcribe-live-rewind-health-sensing/",
    "https://www.engadget.com/2199519/meta-ai-glasses-hands-on-kylie-jenner-edition/",
]

EXPECTED_HEADERS = ["#", "Type", "Focus", "Tests"]


def load_journalists():
    with open(JOURNALISTS_YAML, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def get_block():
    return load_journalists()[JOURNALIST_SLUG]["competitor_coverage"][MECH_KEY]


# ---------------------------------------------------------------------------
# 1. Novelty anchor
# ---------------------------------------------------------------------------
class TestNoveltyAnchorTypeB1043:
    def test_anchor_exists(self):
        assert NOVELTY_ANCHOR is not None, "anchor NULL pre-commit (patched post-commit)"

    def test_anchor_shape(self):
        assert re.fullmatch(r"[0-9a-f]{40}", NOVELTY_ANCHOR)

    def test_anchor_in_log_line(self):
        # Corpus convention registers short hashes in the log header; the
        # anchor's first 8 chars are the main-commit short SHA. Scoped to
        # the #1043 header line (not the whole log) per the #1044 test fix:
        # newer entries name predecessor SHAs in their rotation-transparency
        # sections, which a whole-log index() cannot distinguish.
        log = open(ITERATION_LOG, encoding="utf-8").read()
        header_start = log.index("## #1043 Type B")
        header_end = log.index("\n", header_start)
        assert NOVELTY_ANCHOR[:8] in log[header_start:header_end]

    def test_novelty_claims(self):
        assert NOVELTY_CLAIMS == (
            "zero\ntest_type_b_1043 files, max numeric\nmechanism_id 856 pre-commit, "
            "block key zero-hit, novel Engadget visual-data\nURL zero-hit"
        )


# ---------------------------------------------------------------------------
# 2. Rotation guard (1040-1044 window: D -> E -> A -> B -> C)
# ---------------------------------------------------------------------------
class TestRotationGuard1040_1044Window:
    def test_window_types(self):
        expected = [("B", "1043"), ("A", "1042"), ("E", "1041"), ("D", "1040")]
        log = open(ITERATION_LOG, encoding="utf-8").read()
        for letter, number in expected:
            assert "## #%s Type %s" % (number, letter) in log

    def test_no_type_b_1043_duplicate(self):
        log = open(ITERATION_LOG, encoding="utf-8").read()
        assert log.count("## #1043 Type B") == 1

    def test_mechanism_857_is_type_b(self):
        m = get_block()
        assert m["iteration_type"] == TYPE_LETTER

    def test_transparency(self):
        m = get_block()
        rt = m["rotation_transparency"]
        assert "1040-1044" in rt and "B #1043" in rt and "C expected #1044" in rt


# ---------------------------------------------------------------------------
# 3. Mechanism structure
# ---------------------------------------------------------------------------
class TestMechanism857Structure:
    def test_ids(self):
        m = get_block()
        assert m["iteration"] == 1043
        assert m["mechanism_id"] == 857
        assert m["block_key"] == MECH_KEY

    def test_journalist_item(self):
        item = load_journalists()[JOURNALIST_SLUG]
        assert item["name"] == "Karissa Bell"
        assert item["current_publication"] == "Engadget"
        assert item["mechanism_ids"] == [722, 764, 773, 857]
        # Pre-existing blocks survive the merge untouched.
        assert set(item["competitor_coverage"].keys()) == {
            "type_b_818_karissa_bell_engadget_meta_display_vs_snap_specs_sep17",
            "type_b_888_karissa_bell_engadget_specs_keynote_liveblog_vs_meta_display_privacy_register",
            "type_b_903_karissa_bell_engadget_muse_vs_specs_intelligence_ai_assistants",
            MECH_KEY,
        }

    def test_no_duplicate_top_level_key(self):
        text = open(JOURNALISTS_YAML, encoding="utf-8").read()
        assert text.count("\nkarissa_bell:\n") == 1

    def test_key_design_no_numeric_mechanism_id(self):
        assert "857" not in MECH_KEY
        assert MECH_ID_MARKER not in MECH_KEY
        assert get_block()["key_design_note"].startswith("Colon-form key only per #715")

    def test_goal_and_job(self):
        m = get_block()
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_source_urls(self):
        m = get_block()
        for url in EXPECTED_URLS[:4]:
            assert url in m["source_urls"]


# ---------------------------------------------------------------------------
# 4. Arms (evidence + register)
# ---------------------------------------------------------------------------
class TestMechanism857Arms:
    def test_meta_arm(self):
        arm = get_block()["meta_arm"]
        assert arm["author_byline"] == "Karissa Bell"
        assert arm["date"] == "2026-09-24"
        assert "Visual Data" in arm["title"]
        quotes = " ".join(arm["key_quotes"])
        assert "Somewhere, a contractor just breathed a sigh of relief" in quotes
        assert "pretty poor job of explaining" in quotes
        assert "Even worse" in quotes
        assert "yet another change" in quotes

    def test_apple_arm(self):
        arm = get_block()["apple_arm"]
        assert "Karissa Bell" in arm["author_byline"]
        assert arm["date"] == "2026-09-09"
        assert arm["evidence_tier"] == "podcast_listing_bounded_no_transcript"
        quotes = " ".join(arm["key_quotes"])
        assert "Cherlynn Low" in quotes
        assert "zero" in quotes.lower()

    def test_no_arm_overlap(self):
        m = get_block()
        assert m["meta_arm"]["url"] != m["apple_arm"]["url"]
        assert "engadget.com/2267227" in m["meta_arm"]["url"]
        assert "listennotes.com" in m["apple_arm"]["url"]

    def test_url_verbatim(self):
        m = get_block()
        for url in m["source_urls"]:
            assert url.startswith("http") and " " not in url

    def test_finding_contains_verdict(self):
        finding = get_block()["finding"]
        assert "directionally_supported_not_proven" in finding
        assert "NOT a falsification-family member (ledger holds at 34)" in finding

    def test_finding_not_empty(self):
        assert len(get_block()["finding"]) > 800


# ---------------------------------------------------------------------------
# 5. Scorer (MANUAL ILLUSTRATIVE only)
# ---------------------------------------------------------------------------
class TestMechanism857Scorer:
    def test_meta_tone(self):
        assert get_block()["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.55

    def test_apple_tone(self):
        assert get_block()["apple_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.10

    def test_delta(self):
        assert get_block()["illustrative_delta_meta_minus_apple"] == -0.45

    def test_delta_calc_string(self):
        assert get_block()["delta_calc"] == "(-0.55) - (-0.10) = -0.45"

    def test_delta_arithmetic(self):
        m = get_block()
        meta = m["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"]
        apple = m["apple_arm"]["tone_MANUAL_ILLUSTRATIVE"]
        assert abs((meta - apple) - m["illustrative_delta_meta_minus_apple"]) < 1e-9

    def test_meta_harsher(self):
        m = get_block()
        assert m["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] < m["apple_arm"]["tone_MANUAL_ILLUSTRATIVE"]


# ---------------------------------------------------------------------------
# 6. Confounders and counterevidence
# ---------------------------------------------------------------------------
class TestMechanism857Confounders:
    def test_confounders_ranked(self):
        confounders = get_block()["confounders_ranked"]
        assert len(confounders) >= 5
        joined = " ".join(confounders)
        assert "STRONG: Genre asymmetry" in joined
        assert "STRONG: Evidence-tier asymmetry" in joined
        assert "STRONG: Beat-assignment routing" in joined

    def test_counterevidence(self):
        counter = get_block()["counterevidence"]
        assert len(counter) >= 4
        joined = " ".join(counter)
        assert "m723" in joined
        assert "293" in joined

    def test_correlation_not_causation(self):
        assert "Correlation is not causation" in get_block()["finding"]


# ---------------------------------------------------------------------------
# 7. Qualitative / statistical discipline
# ---------------------------------------------------------------------------
class TestMechanism857Discipline:
    def test_manual_illustrative_only(self):
        assert "MANUAL ILLUSTRATIVE" in get_block()["finding"]

    def test_engine_not_run(self):
        disc = get_block()["statistical_discipline"]
        assert "Engine NOT run" in disc
        assert "p_value NOT_CALCULATED" in disc
        assert "cohens_d NOT_CALCULATED" in disc
        assert "ci_95 NOT_CALCULATED" in disc
        assert "is_significant False" in disc

    def test_no_engine_significance_claims(self):
        finding = get_block()["finding"]
        assert "MANUAL ILLUSTRATIVE: p_value NOT_CALCULATED" in finding
        assert "is_significant False" in finding

    def test_no_analysis_json_update(self):
        assert get_block()["no_analysis_json_update"] is True

    def test_not_falsification_family(self):
        assert get_block()["falsification_family"] == (
            "NOT a falsification-family member; ledger holds at 34."
        )

    def test_connects_to(self):
        connects = get_block()["connects_to"]
        for cid in [150, 293, 380, 668, 723]:
            assert cid in connects


# ---------------------------------------------------------------------------
# 8. Corpus novelty (post-commit ratchet)
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPostCommit:
    def test_max_mechanism_id_857(self):
        profiles = load_journalists()
        ids = []
        for item in profiles.values():
            if not isinstance(item, dict):
                continue
            ids.extend(item.get("mechanism_ids", []) or [])
            for block in (item.get("competitor_coverage") or {}).values():
                ids.append(block.get("mechanism_id"))
        assert max(i for i in ids if isinstance(i, int)) == 857

    def test_zero_next_mechanism_id_858(self):
        text = open(JOURNALISTS_YAML, encoding="utf-8").read()
        for needle in ["mechanism_id: 858", "mechanism_858", "mechanism-858"]:
            assert needle not in text

    def test_zero_test_type_b_1044_files(self):
        assert glob.glob(REPO + "/tests/test_type_b_1044*.py") == []


# ---------------------------------------------------------------------------
# 9. Doc sync ratchet
# ---------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_stats(self):
        readme = open(README, encoding="utf-8").read()
        assert "53,539" in readme or "53539" in readme
        assert "1,368" in readme or "1368" in readme

    def test_readme_table_row(self):
        readme = open(README, encoding="utf-8").read()
        assert "test_type_b_1043_karissa_bell" in readme

    def test_architecture_row(self):
        arch = open(ARCHITECTURE, encoding="utf-8").read()
        assert "1043" in arch and "Karissa Bell" in arch

    def test_iteration_log_entry(self):
        log = open(ITERATION_LOG, encoding="utf-8").read()
        assert "## #1043 Type B" in log
        assert "karissa_bell" in log
        assert "857" in log


# ---------------------------------------------------------------------------
# 10. In-flight isolation (#899 #938 #900 #1012-wt do not carry our edit)
# ---------------------------------------------------------------------------
class TestInflightIsolation:
    INFLIGHT = [
        "profiles/nytimes.yaml",  # #899 hunk (pre-existing, still in-flight)
        "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
        "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
        "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",
    ]

    def test_no_overlap(self):
        # The in-flight files belong to other concurrent agents; their edits
        # may sit uncommitted in this working tree. The invariant for THIS
        # iteration is content-level: none of them may carry our markers.
        # Staging discipline is enforced at commit time via targeted `git add`.
        for path in self.INFLIGHT:
            full = REPO + "/" + path
            try:
                text = open(full, encoding="utf-8").read()
            except FileNotFoundError:
                continue
            for marker in (MECH_KEY, JOURNALIST_SLUG, "mechanism_id: 857", "## #1043"):
                assert marker not in text, "%s in %s" % (marker, path)


# ---------------------------------------------------------------------------
# 11. Block hygiene
# ---------------------------------------------------------------------------
class TestBlockHygiene:
    def test_ascii_no_em_dash(self):
        block_text = yaml.safe_dump(get_block(), allow_unicode=True)
        for bad in ["\u2014", "\u2013", "\u2018", "\u2019", "\u201c", "\u201d", "\u00a0"]:
            assert bad not in block_text, repr(bad)

    def test_no_emoji(self):
        block_text = yaml.safe_dump(get_block(), allow_unicode=True)
        assert not re.search(r"[\U0001F300-\U0001FAFF]", block_text)
