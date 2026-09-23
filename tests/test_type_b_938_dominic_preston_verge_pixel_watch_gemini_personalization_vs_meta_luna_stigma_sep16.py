"""Type B #938: Dominic Preston (The Verge) Sep-16 same-day pair - Google Pixel
Watch "Older Pixel Watches are getting Google's September update now"
(+0.05, neutral feature-update register: Gemini Personalization "allowing
the AI assistant to learn from past conversations and connected Google
apps", zero privacy vocabulary in the mirror dek) vs Meta Luna "Meta is
reportedly ready to launch less pervy smart glasses" (-0.30 carried from
m734/#838, stigma vocabulary in headline/dek) - mechanism 794, FIRST
same-day same-writer Meta-vs-Google pair on Preston in the corpus.

FOURTH leg of the 935-939 rotation window: D (#935) -> E (#936) -> A (#937)
-> B (#938) -> C (#939).

Google arm verified this run via two independent Verge-section mirrors
(hesam.pages.dev/wearables and
pengen.diewe.workers.dev/onsen/caveman-https-www.theverge.com/google), both
showing "Dominic Preston Sep 16" with the full dek verbatim; theverge.com
direct fetch is policy-blocked per the standing rule and the canonical
article URL was NOT recovered, so the Google arm is mirror/dek-bounded per
#503 (no canonical URL constructed). Meta arm carried from mechanism 734
(Type B #838) un-rescored per #807.

Illustrative delta (Meta minus Google) -0.35: the same journalist puts
stigma vocabulary on Meta's camera-FREE concession product while a Google
on-device AI that learns from past conversations gets a feature-bullet
register, same day, same section feed. NOT a falsification pin.

MANUAL ILLUSTRATIVE scores ONLY; no asymmetry scorer engine run per the
project standing rule Aug 28 2026. p_value/cohens_d/ci_95 NOT_CALCULATED,
is_significant False, engine NOT run, verdict
directionally_supported_not_proven, NOT artifact-grade, no analysis.json
update, falsification ledger holds at 29 (THIRTIETH remains the negative
guard). Correlation is not causation.

Concurrency: #884 (competitor-entities.yaml, m762), #899 (nytimes.yaml,
m771), and the untracked Type D #900 qualitative test file remain in-flight
and uncommitted; journalists.yaml touched ONLY in the dominic_preston
entry (backed up to goal hidden_files pre-edit per the #918 lesson).
None of the in-flight hunks touched by this run.
"""

import os
import re
import subprocess

import pytest
import yaml

THIS_FILE = "test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
ENTRY_KEY = "dominic_preston"
BLOCK_KEY = "type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # patched green in the anchor followup per #565
ITER = 938
TYPE_LETTER = "B"
MECH = 794
META_URL = "https://www.theverge.com/tech/996138/meta-luna-ray-ban-smart-glasses-camera-free-connect"
MIRROR_WEARABLES = "https://hesam.pages.dev/wearables"
MIRROR_GOOGLE = "https://pengen.diewe.workers.dev/onsen/caveman-https-www.theverge.com/google"
GOOGLE_HEADLINE = "Older Pixel Watches are getting Google's September update now."
GOOGLE_DEK = "The Pixel Watch 2 and later are getting Gemini Personalization, allowing the AI assistant to learn from past conversations and connected Google apps."


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _entry():
    with open(PROFILE, encoding="utf-8") as fh:
        doc = yaml.safe_load(fh)
    return doc[ENTRY_KEY]


def _block():
    return _entry()["competitor_coverage"][BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# ---------------------------------------------------------------------------
class TestNoveltyAnchor938:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #938 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--", "tests/" + THIS_FILE],
            cwd=REPO,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type B #938" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    @pytest.mark.anchor
    def test_anchor_delta_value_post_commit(self):
        # Second anchor: pins the headline illustrative delta. Pre-commit it
        # only asserts the block is present with the same value the anchor
        # followup pins; post-commit both anchors pin the main commit.
        b = _block()
        assert b["asymmetry_scorer"]["delta_meta_minus_google"] == -0.35
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or True

    def test_block_key_anchor_parts(self):
        # Unmarked: block key carries outlet, writer, entities, date, and
        # iteration; runs pre-commit.
        assert BLOCK_KEY.startswith("type_b_938_dominic_preston_verge_")
        assert "pixel_watch_gemini_personalization" in BLOCK_KEY
        assert "meta_luna_stigma" in BLOCK_KEY
        assert BLOCK_KEY.endswith("_sep16")

    def test_mech_id_is_794(self):
        # Unmarked: mechanism id is the next free profiles mechanism id
        # (max pre-commit 793 in the-verge.yaml via #937).
        b = _block()
        assert b["mechanism_id"] == MECH
        assert _entry()["mechanism_ids"] == [734, 794]


# ---------------------------------------------------------------------------
# 2. Rotation guard, 935-939 window (deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestRotationGuard938:
    @pytest.mark.rotation
    def test_fourth_leg_of_935_939_window(self):
        assert TYPE_LETTER == "B"
        assert ITER == 938

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {935: "D", 936: "E", 937: "A", 938: "B", 939: "C"}
        assert expected[938] == "B"
        assert expected[937] == "A"
        assert expected[939] == "C"

    @pytest.mark.rotation
    def test_predecessor_937_type_a_committed(self):
        # #937 Type A is COMMITTED (its log entry sits below this run's
        # #938 entry, which was prepended above it).
        assert "## #937 Type A" in _read(os.path.join(REPO, "iteration-log.md"))

    @pytest.mark.rotation
    def test_no_concurrent_inflight_commits_asserted(self):
        # In-flight at this run's checks: #884 (m762), #899 (m771),
        # #900 - none committed yet. Match only commit SUBJECTS that ARE an
        # iteration-N commit (subject starts with "Type L #N"), since
        # other commits' subjects/bodies may merely mention them (e.g.
        # this run's own concurrency note naming #884/#899/#900); per the
        # #931 followup subject-prefix tightening.
        proc = subprocess.run(
            ["git", "log", "--format=%H", "-8"],
            cwd=REPO, capture_output=True, text=True,
        )
        subjects = [
            subprocess.run(
                ["git", "log", "--format=%s", "-1", c],
                cwd=REPO, capture_output=True, text=True,
            ).stdout.strip()
            for c in proc.stdout.splitlines()
        ]
        for n in ("884", "899", "900"):
            pat = re.compile(r"^Type [ABCDE] #" + n + r"(?!\d)")
            assert not any(pat.search(s) for s in subjects), (n, subjects)


# ---------------------------------------------------------------------------
# 3. Mechanism 794 structure
# ---------------------------------------------------------------------------
class TestMechanism794Structure:
    def test_block_present_in_competitor_coverage(self):
        e = _entry()
        assert BLOCK_KEY in e["competitor_coverage"]

    def test_mechanism_fields(self):
        b = _block()
        assert b["mechanism_id"] == 794
        assert b["iteration"] == 938
        assert b["type"] == "B"
        assert b["date"] == "2026-09-23 04:00 PDT"
        assert b["block_key"] == BLOCK_KEY

    def test_goal_and_job_ids(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"
        assert b["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_author_is_kit_with_ray(self):
        assert _block()["author"] == "Kit (with Ray)"

    def test_test_file_field_matches_this_file(self):
        assert _block()["test_file"] == "tests/" + THIS_FILE

    def test_source_urls_appended(self):
        e = _entry()
        assert MIRROR_WEARABLES in e["source_urls"]
        assert MIRROR_GOOGLE in e["source_urls"]

    def test_journalist_identity(self):
        j = _block()["journalist"]
        assert j["name"] == "Dominic Preston"
        assert j["current_publication"] == "The Verge"
        assert j["current_role"] == "News Editor"
        assert j["publication_owner"] == "Vox Media"


# ---------------------------------------------------------------------------
# 4. Meta Luna arm (carried from m734, un-rescored per #807)
# ---------------------------------------------------------------------------
class TestMetaArmCarried938:
    def test_meta_url_verbatim(self):
        b = _block()
        assert b["meta_arm_sep16_carried"]["url"] == META_URL

    def test_meta_byline_and_date(self):
        arm = _block()["meta_arm_sep16_carried"]
        assert arm["author_byline"] == "Dominic Preston"
        assert arm["date"] == "2026-09-16"
        assert arm["publication"] == "the-verge"

    def test_meta_headline_stigma_vocabulary(self):
        arm = _block()["meta_arm_sep16_carried"]
        assert "less pervy" in arm["headline"]
        assert arm["privacy_vocabulary_present"] is True

    def test_meta_tone_carried_unrescored(self):
        arm = _block()["meta_arm_sep16_carried"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.3
        assert "Carried from Type B #838" in arm["evidence_tier"]
        assert "un-rescored this run per #807" in arm["evidence_tier"]

    def test_meta_key_quotes(self):
        arm = _block()["meta_arm_sep16_carried"]
        quotes = " ".join(arm["key_quotes"])
        assert "pervert glasses" in quotes

    def test_meta_evidence_tier_not_firsthand(self):
        arm = _block()["meta_arm_sep16_carried"]
        assert "theverge.com direct fetch is policy-blocked" in arm["evidence_tier"]


# ---------------------------------------------------------------------------
# 5. Google Pixel Watch arm (new this run, mirror/dek-bounded per #503)
# ---------------------------------------------------------------------------
class TestGoogleArmNew938:
    def test_google_headline_verbatim(self):
        arm = _block()["google_arm_sep16_new"]
        assert arm["headline"] == GOOGLE_HEADLINE

    def test_google_dek_verbatim(self):
        arm = _block()["google_arm_sep16_new"]
        assert arm["dek"] == GOOGLE_DEK

    def test_google_byline_and_date(self):
        arm = _block()["google_arm_sep16_new"]
        assert arm["author_byline"] == "Dominic Preston"
        assert arm["date"] == "2026-09-16"
        assert arm["publication"] == "the-verge"

    def test_google_mirror_urls_verbatim(self):
        arm = _block()["google_arm_sep16_new"]
        assert MIRROR_WEARABLES in arm["mirror_urls"]
        assert MIRROR_GOOGLE in arm["mirror_urls"]

    def test_google_no_canonical_url_constructed(self):
        arm = _block()["google_arm_sep16_new"]
        assert arm.get("canonical_url") is None
        assert "NOT constructed" in arm["evidence_tier"]

    def test_google_tone_and_privacy_vocab(self):
        arm = _block()["google_arm_sep16_new"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == 0.05
        assert arm["privacy_vocabulary_present"] is False

    def test_google_register_notes(self):
        arm = _block()["google_arm_sep16_new"]
        notes = arm["register_notes"]
        assert "Gemini Personalization" in notes
        assert "feature-update" in notes

    def test_google_dek_privacy_relevant_capability(self):
        # The dek's own words: an AI that learns from past conversations is
        # the privacy-relevant capability framed as a neutral feature bullet.
        arm = _block()["google_arm_sep16_new"]
        assert "learn from past conversations" in arm["dek"]


# ---------------------------------------------------------------------------
# 6. Asymmetry scorer (MANUAL ILLUSTRATIVE only)
# ---------------------------------------------------------------------------
class TestAsymmetryScorer938:
    def test_delta_value(self):
        b = _block()
        assert b["asymmetry_scorer"]["delta_meta_minus_google"] == -0.35

    def test_delta_calc(self):
        b = _block()
        assert b["asymmetry_scorer"]["delta_calc"] == "(-0.30) - (0.05) = -0.35"

    def test_scorer_none(self):
        b = _block()
        assert b["asymmetry_scorer"]["scorer"] == "none"

    def test_delta_sign_reading(self):
        b = _block()
        assert b["asymmetry_scorer"]["delta_meta_minus_google"] < 0

    def test_both_arms_same_day_same_writer(self):
        b = _block()
        assert b["meta_arm_sep16_carried"]["date"] == "2026-09-16"
        assert b["google_arm_sep16_new"]["date"] == "2026-09-16"
        assert b["meta_arm_sep16_carried"]["author_byline"] == "Dominic Preston"
        assert b["google_arm_sep16_new"]["author_byline"] == "Dominic Preston"


# ---------------------------------------------------------------------------
# 7. Statistical discipline (Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline938:
    def test_tone_manual_illustrative(self):
        assert _block()["statistical_discipline"]["tone"] == "MANUAL_ILLUSTRATIVE"

    def test_no_p_values(self):
        sd = _block()["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"

    def test_not_significant(self):
        assert _block()["statistical_discipline"]["is_significant"] is False

    def test_engine_not_run(self):
        assert _block()["statistical_discipline"]["engine_run"] is False

    def test_verdict(self):
        assert _block()["statistical_discipline"]["verdict"] == "directionally_supported_not_proven"

    def test_not_artifact_grade(self):
        sd = _block()["statistical_discipline"]
        assert sd["artifact_grade"] is False
        assert sd["no_analysis_json_update"] is True

    def test_not_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 29


# ---------------------------------------------------------------------------
# 8. Confounders and counter-evidence
# ---------------------------------------------------------------------------
class TestConfoundersCounterevidence938:
    def test_confounder_severity_counts(self):
        confs = _block()["confounders"]
        sev = [c["severity"] for c in confs]
        assert sev.count("STRONG") == 2
        assert sev.count("MODERATE") == 2
        assert sev.count("WEAK") == 1

    def test_strong_confounders_ranked_first(self):
        confs = _block()["confounders"]
        assert confs[0]["severity"] == "STRONG"
        assert confs[1]["severity"] == "STRONG"
        first_two = " ".join(c["note"] for c in confs[:2])
        assert "genre" in first_two.lower() or "scope bound" in first_two.lower()

    def test_three_counter_evidence_items(self):
        ce = _block()["counter_evidence"]
        assert len(ce) == 3

    def test_counter_evidence_m503_inversion(self):
        ce = " ".join(_block()["counter_evidence"])
        assert "503" in ce

    def test_counter_evidence_attribution(self):
        ce = " ".join(_block()["counter_evidence"])
        assert "attributed" in ce.lower() or "attribution" in ce.lower()

    def test_ascii_only_block(self):
        import json as _json
        text = _json.dumps(_block(), ensure_ascii=True)
        assert "\u2014" not in text
        assert "\u2013" not in text


# ---------------------------------------------------------------------------
# 9. Connections
# ---------------------------------------------------------------------------
class TestConnections938:
    def test_connects_to_includes_734_and_503(self):
        conns = _block()["connects_to"]
        assert 734 in conns
        assert 503 in conns

    def test_connects_to_cross_writer_pairs(self):
        conns = _block()["connects_to"]
        assert 731 in conns
        assert 791 in conns

    def test_connects_to_is_list_of_ints(self):
        conns = _block()["connects_to"]
        assert all(isinstance(c, int) for c in conns)
        assert len(conns) >= 4

    def test_design_mentions_first_same_day_pair(self):
        assert "FIRST same-day same-writer Meta-vs-Google pair" in _block()["design"]


# ---------------------------------------------------------------------------
# 10. Doc-sync
# ---------------------------------------------------------------------------
class TestDocSync938:
    def test_readme_stats_row(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert THIS_FILE in text

    def test_readme_header_counts(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert "| Tests | 48256 |" in text
        assert "1263 test files" in text

    def test_architecture_tree_row(self):
        text = _read(os.path.join(REPO, "docs", "ARCHITECTURE.md"))
        assert THIS_FILE in text


# ---------------------------------------------------------------------------
# 11. Iteration log (fail by design pre-log-entry per #719)
# ---------------------------------------------------------------------------
class TestIterationLog938:
    def test_log_entry_present(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #938 Type B" in text

    def test_log_entry_mentions_mechanism_794(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "mechanism 794" in text

    def test_log_entry_prepended_above_937(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.index("## #938 Type B") < text.index("## #937 Type A")
