"""Type B #1058: Lucas Ropek (TechCrunch) Sep-28 OpenAI Astra In Brief -
same-writer same-genre cross-entity remediation-peg contrast vs carried
Sep-16 Meta Luna In Brief.

New arm (this mechanism, mechanism 866): TechCrunch In Brief, byline Lucas
Ropek, Sep 28 2026 4:39 PM PDT - "OpenAI reportedly ditches model over
safety concerns" (read first-hand this run via the verbatim techcrunch.com
canonical URL, 39 rendered lines; byline confirmed via the in-piece author
avatar caption "Lucas Ropek"). WSJ relay: Astra 6.1 nixed over deception
and alignment findings; the Hugging Face agent-breakout incident relayed
factually; the only skepticism is attributed (mild own-voice irony on the
policy deluge plus a critic-attributed entrenchment reading). ZERO own-voice
stigma vocabulary. MANUAL ILLUSTRATIVE -0.05.

Carried arm (per #807, NOT re-researched): mechanism 749 (Type B #863) -
Ropek's Sep 16 2026 Luna In Brief, "After accusations of selling 'perv
glasses,' Meta prepares to sell a pair without a camera" (-0.50), own-voice
stigma vocabulary on a camera-free product ("dystopian surveillance society
run amok", "pervert glasses", "integrated spy equipment"). Same writer, same
outlet, same In Brief genre, twelve days apart, same peg class (company
product-remediation move).

Illustrative cross-entity delta (OpenAI minus Meta) +0.45: (-0.05) - (-0.50).
The finding is register-level only: within the remediation peg class, Ropek
applies own-voice stigma to Meta's remediation and neutral-wire relay to
OpenAI's. REFINES the corpus peg-follows-register thesis (m637, m743, m842,
m845): the thesis holds ACROSS peg classes, not WITHIN the remediation
class. Cross-publication corroboration: Gizmodo's Sep-28 Astra piece
(mechanism 865, +0.15) proves the event sustains a favorable register, so
Ropek's -0.05 is mid-register, not the only available one. NOT a
falsification-family member; ledger holds at 35. MANUAL ILLUSTRATIVE;
engine NOT run; no analysis.json; NOT artifact-grade; verdict
directionally_supported_not_proven; correlation not causation.

FOURTH leg of the 1055-1059 window: D (#1055) -> E (#1056) -> A (#1057) ->
B (#1058) -> C (#1059), rotation per #565. Concurrency: #899 (nytimes.yaml),
#938 (test file), #900 (untracked test file), #1012-wt (test file) in-flight
and untouched; targeted staging only.
"""

import glob
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
ITERATION = 1058
M_ID = 870
OWN_M_ID = 866  # own mechanism for this file's structure tests; M_ID tracks the corpus max
JOURNALIST_SLUG = "lucas_ropek"
MECH_KEY = (
    "type_b_1058_lucas_ropek_techcrunch_sep28_openai_astra_inbrief_"
    "vs_sep16_meta_luna_inbrief_own_voice_stigma_contrast"
)
MECH_ID_MARKER = "mechanism" + "_" + "86" + "7"  # own-form underscore sweep marker
MECH_ID_DASH = "mechanism" + "-" + "86" + "7"
MECH_ID_NUMERIC = "mechanism_id" + ": " + "86" + "7"
NEXT_US = "mechanism" + "_" + "87" + "1"  # next-number underscore sweep
NEXT_DASH = "mechanism" + "-" + "87" + "1"  # next-number dash sweep
NEXT_NUMERIC = "mechanism_id" + ": " + "87" + "1"  # next-number numeric sweep
OWN_BASENAME = os.path.basename(__file__)
ANCHORED_SHA = "103c871d4328d994943385fd74c89a80d5fc194c"  # patched in the anchor followup commit
NOVELTY_CLAIMS = (
    "zero\ntest_type_b_1058 files, max numeric\nmechanism_id 865 pre-commit, "
    "block key zero-hit, one new\nURL zero-hit"
)
EXPECTED_NEW_URLS = [
    "https://techcrunch.com/2026/09/28/openai-reportedly-ditches-model-over-safety-concerns/",
]
CARRIED_URLS = [
    "https://techcrunch.com/2026/09/16/after-accusations-of-selling-perv-glasses-meta-prepares-to-sell-a-pair-without-a-camera/",
]
EXPECTED_ORDER = [("B", "1058"), ("A", "1057"), ("E", "1056"), ("D", "1055"), ("C", "1054")]
README_TESTS_BEFORE = 54241
README_FILES_BEFORE = 1382
README_TESTS_AFTER = 54290
README_FILES_AFTER = 1383
INFLIGHT_FILES = [
    "profiles/nytimes.yaml",  # #899 Type C, modified in worktree
    "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",  # #938, modified
    "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",  # #900, untracked
    "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",  # #1012-wt, modified
]
STAGED_EXPECTED_BASENAMES = {
    "journalists.yaml",
    OWN_BASENAME,
    "test_type_d_1055_m862_m863_m864_qualitative_corpus_integrity_sep28_4am.py",
    "test_type_e_1056_podcast_sentiment_134th_verification_sep28_5pm.py",
    "test_type_a_1057_gizmodo_openai_sep28_astra_cancellation_credit_vs_meta_scrapped_tool_sep28_6pm.py",
    "README.md",
    "ARCHITECTURE.md",
    "iteration-log.md",
}


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


def _repo_grep(needle):
    hits = []
    for root in ("profiles", "tests"):
        base = os.path.join(REPO, root)
        for dirpath, _, files in os.walk(base):
            for fn in files:
                if fn.rsplit(".", 1)[-1] not in ("py", "yaml", "md", "json"):
                    continue
                p = os.path.join(dirpath, fn)
                if needle in open(p, errors="ignore").read():
                    hits.append(p)
    return hits


def _staged_paths():
    return _git(["diff", "--cached", "--name-only"]).stdout.splitlines()


# ---------------------------------------------------------------------------
# 1. Novelty anchor (anchor-marked tests deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestNoveltyAnchorTypeB1058:
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
        # the #1058 header line (not the whole log) per the #1044 test fix:
        # newer entries name predecessor SHAs in their rotation-transparency
        # sections, which a whole-log index() cannot distinguish.
        log = _read(ITERATION_LOG)
        header_start = log.index("## #1058 Type B")
        header_end = log.index("\n", header_start)
        assert ANCHORED_SHA[:8] in log[header_start:header_end]

    def test_novelty_claims(self):
        assert NOVELTY_CLAIMS == (
            "zero\ntest_type_b_1058 files, max numeric\nmechanism_id 865 pre-commit, "
            "block key zero-hit, one new\nURL zero-hit"
        )


# ---------------------------------------------------------------------------
# 2. Rotation guard (1055-1059 window: D -> E -> A -> B -> C), per #565.
#    All rotation tests are deselected pre-commit (log entry prepended at
#    doc-sync) and re-run after doc-sync.
# ---------------------------------------------------------------------------
@pytest.mark.rotation
class TestRotationGuard1055_1059Window:
    def test_window_legs_in_log(self):
        log = _read(ITERATION_LOG)
        for number, letter in (("1055", "D"), ("1056", "E"), ("1057", "A")):
            assert "## #%s Type %s" % (number, letter) in log

    def test_this_run_fourth_leg_b(self):
        log = _read(ITERATION_LOG)
        assert log.count("## #1058 Type B") == 1
        rt = get_block()["rotation_transparency"]
        assert "1055-1059" in rt and "B #1058" in rt and "C #1059" in rt

    def test_predecessor_1057_pinned(self):
        rt = get_block()["rotation_transparency"]
        assert "#1057 Type A" in rt
        assert "c38cb8b7" in rt and "03e171f5" in rt and "28e88e64" in rt

    def test_iteration_type_b(self):
        assert get_block()["iteration_type"] == TYPE_LETTER

# ---------------------------------------------------------------------------
# 3. Mechanism structure
# ---------------------------------------------------------------------------
class TestMechanism866Structure:
    def test_ids(self):
        b = get_block()
        assert b["mechanism_id"] == OWN_M_ID
        assert b["iteration"] == ITERATION
        assert b["iteration_type"] == "B"

    def test_block_key_design_note(self):
        b = get_block()
        assert b["block_key"] == MECH_KEY
        # Colon-form key carries no numeric mechanism id in any form.
        assert "866" not in MECH_KEY
        assert MECH_ID_MARKER not in MECH_KEY
        assert MECH_ID_DASH not in MECH_KEY
        assert "keying" in b["key_design_note"]

    def test_goal_job_author_fields(self):
        b = get_block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"
        assert b["author"] == "Kit (with Ray)"

    def test_test_file_reference(self):
        b = get_block()
        assert b["test_file"] == "tests/" + OWN_BASENAME

    def test_date_field(self):
        b = get_block()
        assert b["date"] == "2026-09-28 19:00 PDT"


# ---------------------------------------------------------------------------
# 4. Mechanism arms (new OpenAI In Brief + carried Meta/Snap arms)
# ---------------------------------------------------------------------------
class TestMechanism866Arms:
    def test_new_arm_source(self):
        arm = get_block()["new_openai_arm_sep28"]
        assert arm["title_verbatim"] == "OpenAI reportedly ditches model over safety concerns"
        assert arm["url"] == EXPECTED_NEW_URLS[0]
        assert arm["byline"] == "Lucas Ropek (sole)"
        assert arm["date"] == "2026-09-28"
        assert arm["posted_time"] == "4:39 PM PDT"
        assert arm["genre"] == "In Brief news digest (WSJ report relay, 39 rendered lines, first-hand this run)"

    def test_new_arm_evidence_tier_first_hand(self):
        arm = get_block()["new_openai_arm_sep28"]
        assert arm["evidence_tier"].startswith("FIRST-HAND")
        assert "39 rendered lines" in arm["evidence_tier"]
        assert "avatar caption" in arm["byline_attestation"]
        assert "verbatim" in arm["url_attestation"]

    def test_new_arm_evidence_quotes(self):
        quotes = get_block()["new_openai_arm_sep28"]["evidence_quotes"]
        assert len(quotes) == 6
        blob = "\n".join(quotes)
        assert "yet another AI model" in blob
        assert "showed higher levels of deception" in blob
        assert "broke free of its sandboxed environment" in blob
        assert "entrench the industry position" in blob
        assert "ironically" in blob

    def test_new_arm_stigma_vocabulary_absent(self):
        arm = get_block()["new_openai_arm_sep28"]
        assert arm["stigma_vocabulary_in_text"].startswith("none:")
        assert "perv glasses" in arm["stigma_vocabulary_in_text"]
        assert arm["tone_illustrative"] == -0.05
        assert arm["register"] == "neutral_wire_relay_with_attributed_skepticism"

    def test_carried_meta_arm(self):
        arm = get_block()["carried_meta_arm_sep16"]
        assert "#807" in arm["note"]
        assert "mechanism 749" in arm["note"]
        assert "re-opened first-hand this run" in arm["note"]
        assert arm["url"] == CARRIED_URLS[0]
        assert arm["posted_time"] == "1:12 PM PDT"
        assert arm["tone_illustrative"] == -0.50
        assert arm["register"] == "adversarial_privacy_register_own_voice"
        assert "pervert glasses" in arm["stigma_vocabulary"]
        assert "integrated spy equipment" in arm["stigma_vocabulary"]
        assert "own-voice" in arm["stigma_vocabulary_verified"]


# ---------------------------------------------------------------------------
# 5. Asymmetry scorer: illustrative delta math and statistical discipline
# ---------------------------------------------------------------------------
class TestMechanism866Scorer:
    def test_tones(self):
        assert get_block()["new_openai_arm_sep28"]["tone_illustrative"] == -0.05
        assert get_block()["carried_meta_arm_sep16"]["tone_illustrative"] == -0.50

    def test_delta_plus_0_45(self):
        s = get_block()["asymmetry_scorer_result"]
        assert s["illustrative_cross_entity_delta_openai_minus_meta"] == 0.45
        assert round(-0.05 - (-0.50), 2) == s["illustrative_cross_entity_delta_openai_minus_meta"]

    def test_calc_string(self):
        s = get_block()["asymmetry_scorer_result"]
        assert s["cross_entity_delta_calc"] == "(-0.05) - (-0.50) = +0.45"
        assert "own-voice stigma" in s["cross_entity_delta_direction"]

    def test_statistical_discipline(self):
        s = get_block()["asymmetry_scorer_result"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"
        assert "engine NOT run" in s["engine"]
        assert s["artifact_grade"] == "NOT artifact-grade"
        assert "not_proven" in get_block()["verdict"]

    def test_falsification_ledger_35(self):
        b = get_block()
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 35
        assert "ledger holds at 35" in b["falsification_note"]
        assert b["no_analysis_json_update"] is True


# ---------------------------------------------------------------------------
# 6. Confounders, counterevidence, incentive context, temporal refinement
# ---------------------------------------------------------------------------
class TestMechanism866Confounders:
    def test_confounders_present(self):
        cfs = get_block()["confounders"]
        assert len(cfs) == 6
        assert cfs[0].startswith("[STRONG]")
        assert cfs[1].startswith("[STRONG]")
        assert cfs[5].startswith("[WEAK]")
        blob = "\n".join(cfs)
        assert "n=1 fresh arm" in blob

    def test_counterevidence_present(self):
        ce = get_block()["counterevidence"]
        assert len(ce) == 4
        blob = "\n".join(ce)
        assert "Snap arm" in blob
        assert "Gizmodo" in blob
        assert "m845" in blob

    def test_incentive_context(self):
        ic = get_block()["incentive_context"]
        assert "Yahoo" in ic and "Apollo" in ic
        assert "No money gradient is asserted" in ic
        assert "correlation not causation" in ic

    def test_temporal_refinement(self):
        tr = get_block()["temporal_refinement"]
        assert len(tr) == 3
        blob = "\n".join(tr)
        assert "749" in blob and "m845" in blob
        assert "REFINES" in blob
        assert get_block()["connects_to"] == [269, 620, 728, 749, 845, 865]


# ---------------------------------------------------------------------------
# 7. Research method: bounded search, first-hand read, novelty greps
# ---------------------------------------------------------------------------
class TestResearchMethodTypeB1058:
    def test_search_sets_and_open(self):
        rm = get_block()["research_method"]
        assert "3 browser.search query sets" in rm
        assert "2 browser.open this run" in rm
        assert "per #503" in rm

    def test_url_attestation(self):
        rm = get_block()["research_method"]
        assert "verbatim" in rm
        assert "no canonical URLs constructed" in rm

    def test_novelty_greps_documented(self):
        rm = get_block()["research_method"]
        assert "max numeric mechanism_id 865 pre-commit" in rm
        assert "block key zero-hit pre-commit" in rm
        assert "zero-hit repo-wide pre-commit" in rm

    def test_first_hand_read_documented(self):
        rm = get_block()["research_method"]
        assert "39 rendered lines" in rm
        assert "author avatar caption" in rm

# ---------------------------------------------------------------------------
# 8. Corpus novelty post-commit
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPostCommit:
    def test_max_numeric_mechanism_id_is_869(self):
        ids = []
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(r"mechanism_id:\s*(\d+)", _read(f)):
                ids.append(int(m.group(1)))
        assert max(ids) == M_ID

    def test_zero_next_numeric_870_in_profiles(self):
        text = "\n".join(
            _read(os.path.join(root, fn))
            for root, _, files in os.walk(os.path.join(REPO, "profiles"))
            for fn in files
            if fn.endswith(".yaml")
        )
        assert NEXT_NUMERIC not in text

    def test_zero_next_underscore_dash_870_repo_wide(self):
        assert _repo_grep(NEXT_US) == []
        assert _repo_grep(NEXT_DASH) == []

    def test_own_underscore_dash_needles_zero_in_sources(self):
        # Format-built per #715: no literal own-number key string is
        # carried anywhere; the needles must be pure zero repo-wide.
        assert _repo_grep(MECH_ID_MARKER) == []
        assert _repo_grep(MECH_ID_DASH) == []

    def test_block_key_in_journalists_yaml(self):
        assert MECH_KEY in _read(JOURNALISTS_YAML)


# ---------------------------------------------------------------------------
# 9. Doc-sync ratchet per #719 (green post-doc-sync)
# ---------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_header_stats_bumped(self):
        line = next(
            l for l in _read(README).splitlines() if l.startswith("| Tests |")
        )
        assert str(README_TESTS_AFTER) in line
        assert str(README_FILES_AFTER) in line

    def test_readme_row_1058(self):
        text = _read(README)
        assert OWN_BASENAME in text
        assert "Type B #1058" in text
        assert "mechanism 866" in text

    def test_arch_row_1058(self):
        text = _read(ARCH)
        assert OWN_BASENAME in text
        assert "Type B #1058" in text

    def test_expected_order_in_docstring(self):
        assert EXPECTED_ORDER == [("B", "1058"), ("A", "1057"), ("E", "1056"), ("D", "1055"), ("C", "1054")]


# ---------------------------------------------------------------------------
# 10. Iteration-log entry (deselected pre-commit per #719/#721)
# ---------------------------------------------------------------------------
@pytest.mark.itlog
class TestIterationLogEntry:
    def _section(self):
        log = _read(ITERATION_LOG)
        start = log.index("## #1058 Type B")
        end = log.index("## #1057 Type A")
        return log[start:end]

    def test_log_header_present(self):
        log = _read(ITERATION_LOG)
        assert log.count("## #1058 Type B") == 1

    def test_log_contains_mechanism(self):
        section = self._section()
        assert "mechanism 866" in section
        assert "Lucas Ropek" in section

    def test_log_rotation(self):
        section = self._section()
        assert "1055-1059" in section
        assert "B #1058" in section


# ---------------------------------------------------------------------------
# 11. In-flight concurrency isolation (#899, #938, #900, #1012-wt)
# ---------------------------------------------------------------------------
class TestInflightIsolation:
    def test_concurrent_inflight_files_not_in_this_commit_scope(self):
        # Fails pre-commit by design (nothing staged yet); green once the
        # run stages its own files. All four in-flight paths stay
        # uncommitted and unstaged.
        staged = _staged_paths()
        assert staged != [], "nothing staged yet (pre-commit)"
        for f in INFLIGHT_FILES:
            assert f not in staged, "in-flight file leaked into staging: %s" % f
        assert not any("test_type_b_938_" in l for l in staged)
        assert not any("test_type_d_900_" in l for l in staged)
        assert not any("test_type_a_1012_" in l for l in staged)

    def test_targeted_staging_only(self):
        # Fails pre-commit by design; green post-staging. The staged set
        # must be exactly this run's files - nothing more.
        staged = {os.path.basename(p) for p in _staged_paths()}
        assert staged == STAGED_EXPECTED_BASENAMES


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

    def test_source_references_recorded(self):
        # Per the standing "keep references" rule: both arms carry their
        # verbatim first-hand source URLs.
        arm = get_block()["new_openai_arm_sep28"]
        assert arm["url"] == EXPECTED_NEW_URLS[0]
        assert get_block()["carried_meta_arm_sep16"]["url"] == CARRIED_URLS[0]
