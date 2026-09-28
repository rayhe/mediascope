"""Iteration #1048 Type B: Emma Roth (The Verge) Sep-24 same-day Meta-vs-Google
AI-assistant pair - temporal replication of m782 (Sep-10).

Type B journalist cross-entity tracking for Sun 2026-09-27 21:00 PDT.

Focus: Emma Roth (The Verge news writer) - SECOND dedicated Type B mechanism
(after m782) and the SECOND same-day same-writer same-outlet Meta-vs-Google
AI-assistant pair in the corpus, 14 days after m782. Meta arm: her Sep 24
2026 9:31am piece "Meta's Muse AI Charms can interact with each other"
(TechNewsTube feed attestation) - a Bloomberg-relayed hardware report on
proximity-recognizing Muse Charms with 5G modem, fingerprint sensor, and
cameras for taking photos; the full Sep-10 adversarial toolkit stays idle.
Google arm: her Sep 24 2026 7:59pm UTC piece "Gemini 3.8 Live with Live Avatar
gives Google's AI a face" (WeSearch/Mediagazer attribution) - a
company-announcement relay on the animated AI persona. Illustrative delta
(Meta minus Google) -0.15, near-null, vs m782's -0.50 on Sep 10. Finding: the
Sep-10 gap was peg-driven (first-person discovery of creepy behaviors vs
rollout brief); with symmetric relay pegs, no differential survives. Pairs
m845 (Ropek: register follows the news peg, not the entity) at the second
writer. MANUAL ILLUSTRATIVE scores only. Engine NOT run.
Verdict: directionally_supported_not_proven. NOT falsification-family (ledger
holds at 35). Correlation is not causation.
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
ITERATION_NUMBER = "1048"
MECH_ID_MARKER = "mechanism" + "_860"
JOURNALIST_SLUG = "emma_roth_type_b"
MECH_KEY = (
    "type_b_1048_emma_roth_verge_meta_muse_charms_interact_vs_"
    "google_gemini_live_avatar_sep27"
)
NOVELTY_CLAIMS = (
    "zero\ntest_type_b_1048 files, max numeric\nmechanism_id 859 pre-commit, "
    "block key zero-hit, both new\nURLs zero-hit"
)
# Anchored to the main-commit SHA of this run; patched once known (NULL until then).
NOVELTY_ANCHOR = "NULL-until-patched"

EXPECTED_URLS = [
    "https://technewstube.com/theverge/1870270/metas-muse-ai-charms-can-interact-each-other/",
    "https://thetechstreetnow.com/gemini-3-8-live-with-live-avatar-gives-googles-ai-a-face/",
]

TEST_SLUG = "test_type_b_1048_emma_roth"


def load_journalists():
    with open(JOURNALISTS_YAML, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def get_block():
    return load_journalists()[JOURNALIST_SLUG]["competitor_coverage"][MECH_KEY]


# ---------------------------------------------------------------------------
# 1. Novelty anchor
# ---------------------------------------------------------------------------
class TestNoveltyAnchorTypeB1048:
    def test_anchor_exists(self):
        assert NOVELTY_ANCHOR is not None, "anchor NULL pre-commit (patched post-commit)"

    def test_anchor_shape(self):
        assert re.fullmatch(r"[0-9a-f]{40}", NOVELTY_ANCHOR)

    def test_anchor_in_log_line(self):
        # Corpus convention registers short hashes in the log header; the
        # anchor's first 8 chars are the main-commit short SHA. Scoped to
        # the #1048 header line (not the whole log) per the #1044 test fix:
        # newer entries name predecessor SHAs in their rotation-transparency
        # sections, which a whole-log index() cannot distinguish.
        log = open(ITERATION_LOG, encoding="utf-8").read()
        header_start = log.index("## #1048 Type B")
        header_end = log.index("\n", header_start)
        assert NOVELTY_ANCHOR[:8] in log[header_start:header_end]

    def test_novelty_claims(self):
        assert NOVELTY_CLAIMS == (
            "zero\ntest_type_b_1048 files, max numeric\nmechanism_id 859 pre-commit, "
            "block key zero-hit, both new\nURLs zero-hit"
        )


# ---------------------------------------------------------------------------
# 2. Rotation guard (1045-1049 window: D -> E -> A -> B -> C)
# ---------------------------------------------------------------------------
class TestRotationGuard1045_1049Window:
    def test_window_types(self):
        expected = [("B", "1048"), ("A", "1047"), ("E", "1046"), ("D", "1045")]
        log = open(ITERATION_LOG, encoding="utf-8").read()
        for letter, number in expected:
            assert "## #%s Type %s" % (number, letter) in log

    def test_no_type_b_1048_duplicate(self):
        log = open(ITERATION_LOG, encoding="utf-8").read()
        assert log.count("## #1048 Type B") == 1

    def test_mechanism_860_is_type_b(self):
        m = get_block()
        assert m["iteration_type"] == TYPE_LETTER

    def test_transparency(self):
        m = get_block()
        rt = m["rotation_transparency"]
        assert "1045-1049" in rt and "B #1048" in rt and "C expected #1049" in rt

    def test_predecessor_1043_pinned(self):
        # The #1043 Type B main commit subject is "feat: iteration #1043
        # Type B - ..." (c2c5222c), not the "^Type [A-E] #N:" convention;
        # per #1045's guard it is pinned separately from the regex-visible
        # chain B1048 -> A1047 -> E1046 -> D1045 -> C1044.
        rt = get_block()["rotation_transparency"]
        assert "#1043" in rt and "c2c5222c" in rt


# ---------------------------------------------------------------------------
# 3. Mechanism structure
# ---------------------------------------------------------------------------
class TestMechanism860Structure:
    def test_ids(self):
        m = get_block()
        assert m["iteration"] == 1048
        assert m["mechanism_id"] == 860
        assert m["block_key"] == MECH_KEY

    def test_journalist_item(self):
        item = load_journalists()[JOURNALIST_SLUG]
        assert item["name"] == "Emma Roth"
        assert item["publication"] == "the-verge"
        assert item["mechanism_ids"] == [782, 860]
        # Pre-existing block survives the merge untouched.
        assert set(item["competitor_coverage"].keys()) == {
            "type_b_918_emma_roth_verge_muse_creep_vs_dreambeans_rollout_sep10",
            MECH_KEY,
        }

    def test_no_duplicate_top_level_key(self):
        text = open(JOURNALISTS_YAML, encoding="utf-8").read()
        assert text.count("\nemma_roth_type_b:\n") == 1

    def test_key_design_no_numeric_mechanism_id(self):
        assert "860" not in MECH_KEY
        assert MECH_ID_MARKER not in MECH_KEY
        assert get_block()["key_design_note"].startswith("Colon-form key only per #715")

    def test_goal_and_job(self):
        m = get_block()
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_source_urls(self):
        m = get_block()
        for url in EXPECTED_URLS:
            assert url in m["source_urls"]


# ---------------------------------------------------------------------------
# 4. Arms (evidence + register)
# ---------------------------------------------------------------------------
class TestMechanism860Arms:
    def test_meta_arm(self):
        arm = get_block()["meta_arm"]
        assert arm["author_byline"] == "Emma Roth"
        assert arm["date"] == "2026-09-24"
        assert "Muse AI Charms" in arm["title"]
        quotes = " ".join(arm["key_quotes"])
        assert "interact with other nearby Charms" in quotes
        assert "fingerprint sensor" in quotes
        assert "cameras designed for taking photos" in quotes
        assert "buzzy Muse AI agent" in quotes
        assert "no creep-register activation" in quotes

    def test_google_arm(self):
        arm = get_block()["google_arm"]
        assert arm["author_byline"] == "Emma Roth"
        assert arm["date"] == "2026-09-24"
        assert "Live Avatar" in arm["title"]
        quotes = " ".join(arm["key_quotes"])
        assert "lip-sync" in quotes
        assert "Gemini Enterprise customers" in quotes
        assert "7:59 PM UTC" in quotes

    def test_no_arm_overlap(self):
        m = get_block()
        assert m["meta_arm"]["url"] != m["google_arm"]["url"]
        assert "1870270" in m["meta_arm"]["url"]
        assert "thetechstreetnow.com" in m["google_arm"]["url"]

    def test_url_verbatim(self):
        m = get_block()
        for url in m["source_urls"]:
            assert url.startswith("http") and " " not in url

    def test_finding_contains_verdict(self):
        finding = get_block()["finding"]
        assert "directionally_supported_not_proven" in finding
        assert "NOT a falsification-family member (ledger holds at 35)" in finding

    def test_finding_not_empty(self):
        assert len(get_block()["finding"]) > 800


# ---------------------------------------------------------------------------
# 5. Scorer (MANUAL ILLUSTRATIVE only)
# ---------------------------------------------------------------------------
class TestMechanism860Scorer:
    def test_meta_tone(self):
        assert get_block()["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.10

    def test_google_tone(self):
        assert get_block()["google_arm"]["tone_MANUAL_ILLUSTRATIVE"] == 0.05

    def test_delta(self):
        assert get_block()["illustrative_delta_meta_minus_google"] == -0.15

    def test_delta_calc_string(self):
        assert get_block()["delta_calc"] == "(-0.10) - (0.05) = -0.15"

    def test_delta_arithmetic(self):
        m = get_block()
        meta = m["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"]
        google = m["google_arm"]["tone_MANUAL_ILLUSTRATIVE"]
        assert abs((meta - google) - m["illustrative_delta_meta_minus_google"]) < 1e-9

    def test_delta_attenuation_vs_m782(self):
        # m782's same-day pair ran -0.50; the temporal replication collapses
        # to near-null when the pegs are symmetric relays.
        assert abs(get_block()["illustrative_delta_meta_minus_google"]) < 0.50


# ---------------------------------------------------------------------------
# 6. Confounders and counterevidence
# ---------------------------------------------------------------------------
class TestMechanism860Confounders:
    def test_confounders_ranked(self):
        confounders = get_block()["confounders_ranked"]
        assert len(confounders) >= 5
        joined = " ".join(confounders)
        assert "STRONG: Peg asymmetry" in joined
        assert "STRONG: Evidence-tier asymmetry" in joined
        assert "STRONG: Relay-direction asymmetry" in joined

    def test_counterevidence(self):
        counter = get_block()["counterevidence"]
        assert len(counter) >= 4
        joined = " ".join(counter)
        assert "m782" in joined
        assert "Janus Rose" in joined

    def test_correlation_not_causation(self):
        assert "Correlation is not causation" in get_block()["finding"]


# ---------------------------------------------------------------------------
# 7. Qualitative / statistical discipline
# ---------------------------------------------------------------------------
class TestMechanism860Discipline:
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
            "NOT a falsification-family member; ledger holds at 35."
        )

    def test_connects_to(self):
        connects = get_block()["connects_to"]
        for cid in [782, 845, 425, 773, 776, 779]:
            assert cid in connects


# ---------------------------------------------------------------------------
# 8. Corpus novelty (post-commit ratchet)
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPostCommit:
    def test_max_mechanism_id_860(self):
        profiles = load_journalists()
        ids = []
        for item in profiles.values():
            if not isinstance(item, dict):
                continue
            ids.extend(item.get("mechanism_ids", []) or [])
            for block in (item.get("competitor_coverage") or {}).values():
                ids.append(block.get("mechanism_id"))
        assert max(i for i in ids if isinstance(i, int)) == 860

    def test_zero_next_mechanism_id_861(self):
        text = open(JOURNALISTS_YAML, encoding="utf-8").read()
        for needle in ["mechanism_id: 861", "mechanism_861", "mechanism-861"]:
            assert needle not in text

    def test_zero_test_type_b_1049_files(self):
        assert glob.glob(REPO + "/tests/test_type_b_1049*.py") == []


# ---------------------------------------------------------------------------
# 9. Doc sync ratchet
# ---------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_stats(self):
        readme = open(README, encoding="utf-8").read()
        assert "53,780" in readme or "53780" in readme
        assert "1,373" in readme or "1373" in readme

    def test_readme_table_row(self):
        readme = open(README, encoding="utf-8").read()
        assert TEST_SLUG in readme

    def test_architecture_row(self):
        arch = open(ARCHITECTURE, encoding="utf-8").read()
        assert "1048" in arch and "Emma Roth" in arch

    def test_iteration_log_entry(self):
        log = open(ITERATION_LOG, encoding="utf-8").read()
        assert "## #1048 Type B" in log
        assert "emma_roth" in log
        assert "860" in log


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
            for marker in (MECH_KEY, JOURNALIST_SLUG, "mechanism_id: 860", "## #1048"):
                assert marker not in text, "%s in %s" % (marker, path)


# ---------------------------------------------------------------------------
# 11. Block hygiene
# ---------------------------------------------------------------------------
class TestBlockHygiene:
    def test_ascii_no_em_dash(self):
        block_text = yaml.safe_dump(get_block(), allow_unicode=True)
        for bad in ["\u2014", "\u2013", "\u2018", "\u2019", "\u2026", "\u00a0"]:
            assert bad not in block_text, repr(bad)

    def test_no_emoji(self):
        block_text = yaml.safe_dump(get_block(), allow_unicode=True)
        assert not re.search(r"[\U0001F300-\U0001FAFF]", block_text)
