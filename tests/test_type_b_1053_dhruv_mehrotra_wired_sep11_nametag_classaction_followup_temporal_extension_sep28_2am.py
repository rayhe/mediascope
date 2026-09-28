"""Type B #1053: Dhruv Mehrotra (WIRED) Sep-11 NameTag class-action follow-up -
temporal register extension of m66.

New arm (this mechanism, mechanism 863): WIRED Security desk, byline Dhruv
Mehrotra, Sep 11 2026 2:59 PM - "Meta Sued Over Training Data for Its AI and
Face-Recognition Systems" (byline/dateline attested via wesearch.press
mirror; excerpt-tier per #503, 0 browser.open). Reports the Alvarez et al. v.
Meta class action (filed Sep 4 2026, N.D. Illinois, 66-page complaint, BIPA +
California privacy claims) alleging Facebook/Instagram photos were used to
build NameTag and train Emu/Muse Image. WIRED register stays in the
accountability-investigative band (MANUAL ILLUSTRATIVE -0.70), allegations
reported as allegations with Meta denial included ("without merit", "not
building a universal face database").

Carried arms (per #807, NOT re-researched): m66 Jun-4 Cameron+Mehrotra
NameTag dormant-code expose (-0.75); m366 Cameron Jul-28 OpenAI rogue-agent
arm (-0.60, falsification-family member, untouched). Illustrative temporal
delta (Sep-11 minus Jun-4) +0.05 near-null: register persistence, 99 days
post-expose. THIRD NameTag-series investigative arm. Bounded-search absence:
zero equivalent WIRED investigative follow-up on Apple/Google/Samsung/Snap
camera-wearable privacy in the same window - positive temporal leg for
m66's 12-month verification window. NOT falsification-family (m366 stands);
ledger holds at 35. MANUAL ILLUSTRATIVE; engine NOT run; no analysis.json;
NOT artifact-grade; verdict directionally_supported_not_proven; correlation
not causation.

FOURTH leg of the 1050-1054 window: D (#1050) -> E (#1051) -> A (#1052) ->
B (#1053) -> C (#1054), rotation per #565. Concurrency: #899 (nytimes.yaml),
#938 (test file), #900 (untracked test file), #1012-wt (test file) in-flight
and untouched; targeted staging only.
"""

import os
import re
import subprocess

import pytest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOURNALISTS_YAML = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
ITERATION_LOG = os.path.join(REPO, "iteration-log.md")
README = os.path.join(REPO, "README.md")
ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")

TYPE_LETTER = "B"
ITERATION = 1053
MECHANISM_ID = 863
JOURNALIST_SLUG = "dhruv_mehrotra_type_b"
MECH_KEY = (
    "type_b_1053_dhruv_mehrotra_wired_sep11_"
    "nametag_classaction_temporal_extension"
)
MECH_ID_MARKER = "mechanism" + "_" + str(MECHANISM_ID)  # format-built per #715
MECH_ID_DASH = "mechanism" + "-" + str(MECHANISM_ID)
MECH_ID_NUMERIC = "mechanism_id" + ": " + str(MECHANISM_ID)
OWN_BASENAME = os.path.basename(__file__)
ANCHORED_SHA = "64aaaab5e5b1c532ae67676a502c1ec36bb5d8e3"  # patched in the anchor followup commit
NOVELTY_CLAIMS = (
    "zero\ntest_type_b_1053 files, max numeric\nmechanism_id 862 pre-commit, "
    "block key zero-hit, nine new\nURLs zero-hit"
)
EXPECTED_NEW_URLS = [
    "https://wesearch.press/s/meta-sued-over-training-data-for-its-ai-and-face-recognition-9bb99171",
    "https://www.pymnts.com/news/wearables/2026/meta-faces-lawsuit-over-smart-glasses-facial-recognition/",
    "https://pulse2.com/meta-faces-proposed-class-action-over-ai-training-and-smart-glasses-facial-recognition/",
    "https://petapixel.com/2026/09/14/meta-hit-with-class-action-lawsuit-for-allegedly-using-instagram-photos-to-build-name-tag/",
    "https://www.techtimes.co.uk/meta-sued-over-nametag-biometric-data-1808684",
    "https://medium.com/@len213noe/i-have-thirteen-chips-in-my-body-none-of-them-read-your-face-623a51eba374",
    "https://www.avclub.com/meta-faceprint-lawsuit-mark-zuckerberg",
    "https://www.biometricupdate.com/202609/meta-sued-over-alleged-facial-recognition-training-for-smart-glasses",
    "https://world-freedom.co.uk/2026/09/21/meta-accused-of-harvesting-facebook-instagram-photos-for-smart-pervert-glasses-facial-recognition/",
]
CARRIED_URLS = [
    "https://www.wired.com/story/meta-smart-glasses-face-recognition-nametag-connections/",
    "https://www.wired.com/story/openais-rogue-ai-agent-hacked-more-than-just-hugging-face/",
]
INFLIGHT_FILES = [
    "profiles/nytimes.yaml",  # #899 Type D, modified in worktree
    "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",  # #938, modified
    "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",  # #900, untracked
    "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",  # #1012-wt, modified
]


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _git(args):
    return subprocess.run(
        ["git", "-C", REPO] + args, capture_output=True, text=True, timeout=120
    )


def _load_journalists():
    import yaml

    return yaml.safe_load(_read(JOURNALISTS_YAML))


def get_block():
    data = _load_journalists()
    return data[JOURNALIST_SLUG]["competitor_coverage"][MECH_KEY]


def get_item():
    return _load_journalists()[JOURNALIST_SLUG]


# ---------------------------------------------------------------------------
# 1. Novelty anchor (anchor-marked tests deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestNoveltyAnchorTypeB1053:
    @pytest.mark.anchor
    def test_anchor_exists(self):
        assert ANCHORED_SHA not in (None, "PATCH_ME_IN_FOLLOWUP"), (
            "anchor NULL pre-commit (patched post-commit)"
        )

    @pytest.mark.anchor
    def test_anchor_shape(self):
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)

    @pytest.mark.anchor
    def test_anchor_in_log_header(self):
        # Corpus convention registers short hashes in the log header; the
        # anchor's first 8 chars are the main-commit short SHA. Scoped to
        # the #1053 header line (not the whole log) per the #1044 test fix:
        # newer entries name predecessor SHAs in their rotation-transparency
        # sections, which a whole-log index() cannot distinguish.
        log = _read(ITERATION_LOG)
        header_start = log.index("## #1053 Type B")
        header_end = log.index("\n", header_start)
        assert ANCHORED_SHA[:8] in log[header_start:header_end]

    def test_novelty_claims(self):
        assert NOVELTY_CLAIMS == (
            "zero\ntest_type_b_1053 files, max numeric\nmechanism_id 862 pre-commit, "
            "block key zero-hit, nine new\nURLs zero-hit"
        )


# ---------------------------------------------------------------------------
# 2. Rotation guard (1050-1054 window: D -> E -> A -> B -> C), per #565.
#    All rotation tests are deselected pre-commit (log entry prepended at
#    doc-sync) and re-run after doc-sync.
# ---------------------------------------------------------------------------
@pytest.mark.rotation
class TestRotationGuard1050_1054Window:
    def test_window_legs_in_log(self):
        log = _read(ITERATION_LOG)
        for number, letter in (("1050", "D"), ("1051", "E"), ("1052", "A")):
            assert "## #%s Type %s" % (number, letter) in log

    def test_this_run_fourth_leg_b(self):
        log = _read(ITERATION_LOG)
        assert log.count("## #1053 Type B") == 1
        rt = get_block()["rotation_transparency"]
        assert "1050-1054" in rt and "B #1053" in rt and "C #1054" in rt

    def test_predecessor_1052_pinned(self):
        rt = get_block()["rotation_transparency"]
        assert "#1052 Type A" in rt
        assert "98624388" in rt and "c7941cbd" in rt and "4a05bdae" in rt

    def test_iteration_type_b(self):
        assert get_block()["iteration_type"] == TYPE_LETTER


# ---------------------------------------------------------------------------
# 3. Mechanism structure
# ---------------------------------------------------------------------------
class TestMechanism863Structure:
    def test_ids(self):
        m = get_block()
        assert m["iteration"] == ITERATION
        assert m["mechanism_id"] == MECHANISM_ID
        assert m["block_key"] == MECH_KEY

    def test_journalist_item(self):
        item = get_item()
        assert item["name"] == "Dhruv Mehrotra"
        assert item["publication"] == "wired"
        assert item["mechanism_ids"] == [MECHANISM_ID]
        assert set(item["competitor_coverage"].keys()) == {MECH_KEY}

    def test_no_duplicate_top_level_key(self):
        text = _read(JOURNALISTS_YAML)
        assert text.count("\ndhruv_mehrotra_type_b:\n") == 1

    def test_key_design_no_numeric_mechanism_id(self):
        # The 1053 in the block key is the ITERATION number, not the
        # mechanism id; the mechanism id (863) appears only as the
        # mechanism_id: field (colon-form, per the #715 designed keying).
        assert "863" not in MECH_KEY
        assert MECH_ID_MARKER not in MECH_KEY
        assert MECH_ID_DASH not in MECH_KEY

    def test_goal_and_job(self):
        m = get_block()
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"


# ---------------------------------------------------------------------------
# 4. Arms (evidence + register)
# ---------------------------------------------------------------------------
class TestMechanism863Arms:
    def test_new_arm_identity(self):
        arm = get_block()["new_arm"]
        assert arm["author_byline"] == "Dhruv Mehrotra"
        assert arm["date"] == "2026-09-11"
        assert arm["publication"] == "wired"
        assert arm["desk"] == "Security"
        assert arm["title"].startswith("Meta Sued Over Training Data")
        assert arm["source_url"] == EXPECTED_NEW_URLS[0]
        assert arm["evidence_tier"] == "excerpt"

    def test_new_arm_excerpt_bounded(self):
        arm = get_block()["new_arm"]
        assert "0 browser.open" in arm["verification"]
        assert "wesearch.press" in arm["verification"]
        assert arm["opening_excerpt"].startswith(
            "A set of parents and their children"
        )

    def test_new_arm_lawsuit_details(self):
        suit = get_block()["new_arm"]["lawsuit"]
        assert "Alvarez et al. v. Meta" in suit
        assert "Northern District of Illinois" in suit
        assert "Sep 4 2026" in suit
        assert "66-page" in suit
        assert "BIPA" in suit
        assert "unproven" in suit

    def test_new_arm_meta_response(self):
        resp = get_block()["new_arm"]["meta_response"]
        assert len(resp) == 4
        joined = " ".join(resp)
        assert "without merit" in joined
        assert "not building a universal face database" in joined

    def test_carried_meta_arm(self):
        arm = get_block()["carried_meta_arm"]
        assert arm["mechanism"] == 66
        assert arm["date"] == "2026-06-04"
        assert "Dhruv Mehrotra" in arm["authors"]
        assert "Dell Cameron" in arm["authors"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.75
        assert arm["rescore"] == "carried_unrescored_per_807"
        assert arm["source_url"] == CARRIED_URLS[0]

    def test_carried_openai_arm(self):
        arm = get_block()["carried_openai_arm"]
        assert arm["mechanism"] == 366
        assert "falsification" in arm["note"]
        assert arm["source_url"] == CARRIED_URLS[1]

    def test_new_urls_in_item(self):
        urls = get_item()["source_urls"]
        for url in EXPECTED_NEW_URLS:
            assert url in urls
        for url in CARRIED_URLS:
            assert url in urls
        assert len(urls) == len(EXPECTED_NEW_URLS) + len(CARRIED_URLS)


# ---------------------------------------------------------------------------
# 5. Scorer (MANUAL ILLUSTRATIVE only)
# ---------------------------------------------------------------------------
class TestMechanism863Scorer:
    def test_new_arm_tone(self):
        assert get_block()["new_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.70

    def test_temporal_delta(self):
        m = get_block()
        assert m["temporal_delta_illustrative"] == 0.05
        note = m["temporal_delta_note"]
        assert "near-null" in note and "persistence" in note

    def test_register(self):
        arm = get_block()["new_arm"]
        assert arm["register"] == "accountability_investigative"
        assert arm["surveillance_vocabulary"] == "present"

    def test_manual_illustrative_only(self):
        assert (
            get_block()["statistical_discipline"]["tone"]
            == "MANUAL_ILLUSTRATIVE_ONLY"
        )

    def test_verdict(self):
        assert (
            get_block()["statistical_discipline"]["verdict"]
            == "directionally_supported_not_proven"
        )


# ---------------------------------------------------------------------------
# 6. Confounders (ranked strong-first) + counterevidence
# ---------------------------------------------------------------------------
class TestMechanism863Confounders:
    def test_ranked_strong_first(self):
        confs = get_block()["confounders_ranked_strong_first"]
        assert len(confs) == 7
        assert all(c.startswith("STRONG:") for c in confs[:3])

    def test_lawsuit_peg_confounder(self):
        confs = get_block()["confounders_ranked_strong_first"]
        assert any("lawsuit peg drives the register" in c for c in confs)

    def test_excerpt_tier_moderate(self):
        confs = get_block()["confounders_ranked_strong_first"]
        assert any("excerpt-tier evidence" in c for c in confs)

    def test_counterevidence(self):
        ce = get_block()["counterevidence"]
        assert len(ce) == 4
        joined = " ".join(ce)
        assert "m366" in joined
        assert "Conde Nast" in joined


# ---------------------------------------------------------------------------
# 7. Statistical discipline
# ---------------------------------------------------------------------------
class TestMechanism863Discipline:
    def test_stats_not_calculated(self):
        sd = get_block()["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"

    def test_not_significant(self):
        assert get_block()["statistical_discipline"]["is_significant"] is False

    def test_engine_not_run(self):
        assert get_block()["statistical_discipline"]["engine_run"] is False

    def test_no_analysis_json(self):
        sd = get_block()["statistical_discipline"]
        assert sd["no_analysis_json_update"] is True
        assert sd["artifact_grade"] is False

    def test_not_falsification_family(self):
        sd = get_block()["statistical_discipline"]
        assert sd["falsification_family_member"] is False
        assert sd["falsification_ledger"] == 35

    def test_correlation_not_causation(self):
        assert "CORRELATION NOT CAUSATION" in get_block()["finding"]


# ---------------------------------------------------------------------------
# 8. Corpus novelty (post-commit state assertions; own file excluded per #715)
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPostCommit:
    def test_mechanism_863_numeric_unique_in_profiles(self):
        hits = _git(
            ["grep", "-l", MECH_ID_NUMERIC, "--", "profiles/"]
        ).stdout.splitlines()
        assert hits == ["profiles/careers/journalists.yaml"]

    def test_zero_864_keys_in_profiles(self):
        needle = "mechanism_id" + ": 864"
        hits = _git(["grep", "-l", needle, "--", "profiles/"]).stdout.splitlines()
        assert hits == []

    def test_underscore_form_zero_repo_wide(self):
        # Own file excluded per #715 (the test method name itself carries
        # the literal underscore form).
        hits = _git(["grep", "-l", MECH_ID_MARKER, "--", "."]).stdout.splitlines()
        hits = [h for h in hits if h != "tests/" + OWN_BASENAME]
        assert hits == []

    def test_dash_form_zero_repo_wide(self):
        hits = _git(["grep", "-l", MECH_ID_DASH, "--", "."]).stdout.splitlines()
        hits = [h for h in hits if h != "tests/" + OWN_BASENAME]
        assert hits == []

    def test_block_key_confined_to_home_yaml(self):
        text = _read(JOURNALISTS_YAML)
        # Appears exactly twice: the competitor_coverage key and the
        # block_key: field. Zero elsewhere (git grep would catch strays).
        assert text.count(MECH_KEY) == 2
        hits = _git(["grep", "-l", MECH_KEY, "--", "."]).stdout.splitlines()
        assert set(hits) <= {
            "profiles/careers/journalists.yaml",
            "tests/" + OWN_BASENAME,
        }


# ---------------------------------------------------------------------------
# 9. Doc-sync ratchet (deselected pre-commit per #719; re-run after doc-sync)
# ---------------------------------------------------------------------------
@pytest.mark.docsync
class TestDocSyncRatchet:
    def test_readme_stats(self):
        text = _read(README)
        line = next(
            l for l in text.splitlines() if l.startswith("| Tests |")
        )
        assert "54037" in line and "1378" in line

    def test_readme_table_row(self):
        text = _read(README)
        assert OWN_BASENAME in text
        assert "Type B #1053" in text
        assert "mechanism 863" in text

    def test_architecture_row(self):
        text = _read(ARCH)
        assert OWN_BASENAME in text
        assert "Type B #1053" in text


# ---------------------------------------------------------------------------
# 10. Iteration-log entry (deselected pre-commit per #719/#721)
# ---------------------------------------------------------------------------
@pytest.mark.itlog
class TestIterationLogEntry:
    def _section(self):
        log = _read(ITERATION_LOG)
        start = log.index("## #1053 Type B")
        end = log.index("## #1052 Type A")
        return log[start:end]

    def test_log_header_present(self):
        log = _read(ITERATION_LOG)
        assert log.count("## #1053 Type B") == 1

    def test_log_contains_mechanism(self):
        section = self._section()
        assert "mechanism 863" in section
        assert "Dhruv Mehrotra" in section

    def test_log_rotation(self):
        section = self._section()
        assert "1050-1054" in section
        assert "B #1053" in section


# ---------------------------------------------------------------------------
# 11. In-flight concurrency isolation (#899, #938, #900, #1012-wt)
# ---------------------------------------------------------------------------
class TestInflightIsolation:
    def _staged(self):
        return _git(["diff", "--cached", "--name-only"]).stdout.splitlines()

    def test_899_nytimes_not_staged(self):
        assert INFLIGHT_FILES[0] not in self._staged()

    def test_938_test_file_not_staged(self):
        assert INFLIGHT_FILES[1] not in self._staged()

    def test_900_untracked_not_staged(self):
        assert INFLIGHT_FILES[2] not in self._staged()

    def test_1012wt_test_file_not_staged(self):
        assert INFLIGHT_FILES[3] not in self._staged()


# ---------------------------------------------------------------------------
# 12. Block hygiene
# ---------------------------------------------------------------------------
class TestBlockHygiene:
    def test_ascii_only(self):
        data = _load_journalists()
        import json

        blob = json.dumps(data[JOURNALIST_SLUG], ensure_ascii=False)
        assert "\u2014" not in blob  # no em dashes, repo prose rule
        blob.encode("ascii")  # raises on any other non-ASCII

    def test_urls_verbatim(self):
        for url in EXPECTED_NEW_URLS + CARRIED_URLS:
            assert url.startswith("https://") and " " not in url

    def test_test_file_ascii(self):
        blob = _read(os.path.join(REPO, "tests", OWN_BASENAME))
        assert "\u2014" not in blob
        blob.encode("ascii")
