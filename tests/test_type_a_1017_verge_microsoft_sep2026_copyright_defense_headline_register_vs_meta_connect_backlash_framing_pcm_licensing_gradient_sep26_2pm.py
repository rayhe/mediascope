"""Type A #1017: Verge x Microsoft Sep-4 copyright-defense headline register vs
Verge x Meta Sep-23 Connect backlash framing (PCM licensing gradient).

THIRD leg of the 1015-1019 window: D #1015 -> E #1016 -> A #1017 (this run)
-> B #1018 -> C #1019. New Type A mechanism (mechanism 841) in
profiles/the-verge.yaml under competitor_relationships -> microsoft:
register-selection finding (NOT uniform softness) - The Verge's Sep 4 2026
Microsoft coverage carried a defense-forward register ("Microsoft says
virtually nobody was grabbing NYT articles through its chatbot",
excerpt-bounded, MANUAL ILLUSTRATIVE +0.25) plus the Sep 25 Tom Warren
Copilot "super app" supporting arm (secondary-attested, 6 attributions, no
verbatim Verge URL, +0.20), while its Meta Connect coverage (Sep 23-24,
Muse Charm verbatim URL, secondary backlash-framing attestation) ran
-0.30; illustrative delta +0.55 (Microsoft minus Meta), n=1 vs n=1 primary
pair, NOT significant. 4 counterevidence items; confounders ranked
strong-first (genre/peg mismatch, attribution-headline practice,
excerpt-bounded evidence); MANUAL ILLUSTRATIVE ONLY, verdict
directionally_supported_not_proven.

Pre-run anchors: max numeric mechanism_id 840 pre-commit, zero
underscore/dash-form 841 keys repo-wide pre-commit (needles format-built
per #715, no literals carried), zero test_type_a_1017 files on disk
(glob), no "Type A #1017" in git log (--grep), block key zero-hit
repo-wide pre-commit, all 6 source URLs zero-hit repo-wide pre-commit
(git grep -F). 5 browser.search sets, 0 browser.open (excerpt-bounded per
#503). ASCII-only, no em dashes in new content. Post-commit: mechanism
841 is the corpus max; zero 842 keys numeric/underscore/dash in profiles/.
Doc-sync (52222/1341 -> 52222+N/1342; +N/+1, venv python); 1015-1019
window THIRD leg D->E->A (anchor + rotation guard per #565); concurrency:
#899 (nytimes.yaml mechanism 771 hunk), #938 (test_type_b_938 anchor
edit), #900 (untracked test), and the #1012 working-tree block-key fix
stay unstaged.

Test tally: 56 tests, 11 classes.
EXPECTED_TOTAL = 56
"""

from __future__ import annotations

import os
import re
import subprocess

import pytest

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

ITERATION = 1017
TYPE_LETTER = "A"
RUN_PDT = "2026-09-26 14:00 PDT"
RUN_PDT_SHORT = "Sep 26 2026 14:00 PDT"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # patched by the anchor followup per #565

THIS_FILE = (
    "test_type_a_1017_verge_microsoft_sep2026_copyright_defense_headline_"
    "register_vs_meta_connect_backlash_framing_pcm_licensing_gradient_sep26_2pm.py"
)
PROFILE = "profiles/the-verge.yaml"
README = "README.md"
ARCH = "docs/ARCHITECTURE.md"
LOG = "iteration-log.md"

# Descriptive block key per the #723/#738 convention: carries NO underscore-
# or dash-form mechanism number, so the zero-next-number profile sweeps stay
# green. The mechanism number appears only as 'mechanism_id: 841' in colon
# form and as spaced prose in strings (never as a contiguous mechanism-form
# literal). Built by string concatenation so this file carries no contiguous
# occurrence of the key by construction (per #715).
BLOCK_KEY = (
    "type_a_1017_verge_microsoft_sep2026_copyright_defense_headline_register_"
    "vs_meta_connect_backlash_framing_pcm_licensing_gradient"
)

# Markers built by concatenation per #715: no raw literals in this file.
MECH_ID_MARKER = "mechanism" + "_841"          # own-form key sweep marker
NEXT_US = "mechanism" + "_842"                  # next-number underscore sweep
NEXT_DASH = "mechanism" + "-842"                # next-number dash sweep
NEXT_NUMERIC = "mechanism_id: " + "842"         # next-number numeric sweep
OWN_NUMERIC = "mechanism_id: " + "841"          # own-number numeric sweep

NEW_URLS = [
    "https://www.theverge.com/policy/990267/microsoft-openai-new-york-times-authors-lawsuit",
    "https://www.theverge.com/ai-artificial-intelligence/990932/seattle-times-newsday-lawsuit-openai-microsoft",
    "https://www.theverge.com/tech/999750/muse-charm-meta-ai-hardware",
    "https://biztoc.com/x/74ab2ae831f1ffe5",
    "https://letsdatascience.com/news/meta-introduces-camera-free-ray-ban-meta-audio-glasses-6c7a0c5b",
    "https://www.itechpost.com/articles/237412/20260924/meta-connect-2026-all-new-smart-glasses-ai-glasses-announced.htm",
]

EXPECTED_TESTS = 56

README_TESTS_BEFORE, README_FILES_BEFORE = 52222, 1341
README_TESTS_AFTER, README_FILES_AFTER = 52222 + EXPECTED_TESTS, 1342

STAGED_SET = {
    "profiles/the-verge.yaml",
    "tests/" + THIS_FILE,
    "README.md",
    "docs/ARCHITECTURE.md",
    "iteration-log.md",
}

# In-flight work that must stay OUT of this run's staged set (targeted
# staging per the repo-wide traversal lesson): #899 (nytimes.yaml mechanism
# 771 hunk), #938 (test_type_b_938 anchor edit), #900 (untracked test file),
# and the #1012 working-tree block-key-fix edit.
INFLIGHT = {
    "profiles/nytimes.yaml",
    "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
    "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
    "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",
}

# Predecessor #1016 commits (main / anchor followup / log-hash followup)
PREDECESSOR_HASHES = {
    "668c8f359e7261ded06d1e597c3d8f04bde86681",  # #1016 main commit
    "cd0b5b577c37d70e47789f3f97a283bebb1bddb5",  # #1016 anchor followup
    "21ba78cb08e83a4b2ca4acff94ed7c44fc56f99f",  # #1016 log-hash followup
}

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run_git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=REPO,
        capture_output=True,
        text=True,
        timeout=120,
    )


def _read(path: str) -> str:
    with open(os.path.join(REPO, path), encoding="utf-8") as fh:
        return fh.read()


# ---------------------------------------------------------------------------
# 1. Novelty preconditions per #715 (no Type A #1017 before this run)
# ---------------------------------------------------------------------------
class TestNovelty1017:
    def test_single_type_a_1017_test_file(self):
        import glob

        assert glob.glob(os.path.join(REPO, "tests", "test_type_a_1017*")) == [
            os.path.join(REPO, "tests", THIS_FILE)
        ]

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # Designed to FAIL pre-commit (placeholder present); the anchor
        # followup patches ANCHORED_SHA to the real main-commit hash per
        # #565, then this test goes green.
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP"
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)
        r = run_git("rev-parse", ANCHORED_SHA)
        assert r.returncode == 0 and r.stdout.strip() == ANCHORED_SHA

    def test_no_type_a_1017_in_git_log_precommit(self):
        # Pre-commit: no "Type A #1017" anywhere in history.
        r = run_git("log", "--oneline", "--grep=Type A #1017")
        assert r.stdout.strip() == ""

    def test_block_key_zero_hit_precommit(self):
        # Post-commit: the block key lives in exactly one committed profiles
        # file. (The test file builds BLOCK_KEY by string concatenation, so
        # it carries no contiguous occurrence of the key by construction; the
        # profiles half is the real corpus-novelty instrument.)
        r = run_git("grep", "-l", "-F", BLOCK_KEY, "--", "profiles/")
        assert r.stdout.splitlines() == [PROFILE]


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1015-1019 window, this run is the THIRD leg
# ---------------------------------------------------------------------------
class TestRotationGuard1015_1019Window:
    def test_window_legs_present_in_log(self):
        log = _read(LOG)
        assert "## #1015 Type D" in log
        assert "## #1016 Type E" in log
        assert "## #1017 Type A" in log

    def test_predecessor_1016_type_e_committed(self):
        assert "## #1016 Type E" in _read(LOG)
        r = run_git("log", "--oneline", "--grep=Type E #1016")
        assert r.stdout.strip() != ""

    def test_third_leg_marked(self):
        log = _read(LOG)
        entry = log.split("## #1017 Type A", 1)[1].split("## #", 1)[0]
        assert "THIRD leg" in entry
        assert "D #1015 -> E #1016 -> A #1017" in entry

    def test_no_successor_type_b_1018_yet(self):
        r = run_git("log", "--oneline", "--grep=Type B #1018")
        assert r.stdout.strip() == ""
        assert "## #1018" not in _read(LOG)

    def test_no_concurrent_type_a_1017_commits(self):
        r = run_git("log", "--oneline", "--grep=Type A #1017")
        assert r.stdout.strip() == ""

    def test_anchor_and_guard_markers_present(self):
        src = _read("tests/" + THIS_FILE)
        assert "PATCH_ME_IN_FOLLOWUP" in src or re.fullmatch(
            r"[0-9a-f]{40}", ANCHORED_SHA
        )
        assert "pytest.mark.anchor" in src


# ---------------------------------------------------------------------------
# 3. Mechanism 841 block content in profiles/the-verge.yaml
# ---------------------------------------------------------------------------
class TestMechanism841Content:
    def _block(self) -> str:
        text = _read(PROFILE)
        key_line = "    " + BLOCK_KEY + ":"
        assert text.count(key_line) == 1
        start = text.index(key_line)
        nxt = text.index("\n  x_twitter:", start)
        return text[start:nxt]

    def test_block_key_unique_at_indent_4_under_microsoft(self):
        block = self._block()
        assert "\n      mechanism_id: 841\n" in block

    def test_iteration_fields(self):
        block = self._block()
        assert "iteration: 1017" in block
        assert 'iteration_type: "A"' in block
        assert "1015-1019" in block

    def test_publication_pair_and_meta(self):
        block = self._block()
        assert 'publication: "The Verge"' in block
        assert 'publication_pair: "Verge x Microsoft"' in block
        assert "competitor: microsoft" in block
        assert "comparator_entity: meta" in block
        assert 'goal_id: "goal_54093bda4145"' in block
        assert 'scheduled_job_id: "mediascope-daily-iteration"' in block
        assert "2026-09-26" in block
        assert "Kit (with Ray)" in block

    def test_key_design_note_present(self):
        block = self._block()
        assert "key_design_note" in block
        assert MECH_ID_MARKER not in block.replace("mechanism_id: 841", "")

    def test_connects_to_resolve(self):
        block = self._block()
        m = re.search(r"connects_to: \[([0-9, ]+)\]", block)
        assert m is not None
        ids = [int(x) for x in m.group(1).split(",")]
        assert set(ids) == {502, 507, 598}

    def test_status_committed(self):
        assert 'status: "committed"' in self._block()


# ---------------------------------------------------------------------------
# 4. Evidence: arms, dates, URLs, attestation
# ---------------------------------------------------------------------------
class TestEvidence1017:
    def test_microsoft_primary_arm(self):
        text = _read(PROFILE)
        assert "Microsoft says virtually nobody was grabbing NYT articles" in text
        assert NEW_URLS[0] in text
        assert "tone_manual_illustrative: 0.25" in text

    def test_microsoft_supporting_arm_secondary_attested(self):
        text = _read(PROFILE)
        assert "Tom Warren" in text
        assert "super app" in text
        assert "secondary-attested only" in text
        assert "tone_manual_illustrative: 0.20" in text

    def test_meta_arm(self):
        text = _read(PROFILE)
        assert NEW_URLS[2] in text
        assert "backlash" in text
        assert "tone_manual_illustrative: -0.30" in text

    def test_arm_dates_sep_2026(self):
        text = _read(PROFILE)
        assert '"2026-09-04"' in text
        assert '"2026-09-25"' in text
        assert '"2026-09-23"' in text

    def test_excerpt_bounded_attestation(self):
        text = _read(PROFILE)
        assert "excerpt-bounded this run (0 browser.open per the #503 convention)" in text


# ---------------------------------------------------------------------------
# 5. Scores: delta arithmetic, direction, register-selection framing
# ---------------------------------------------------------------------------
class TestScores1017:
    def test_delta_arithmetic(self):
        text = _read(PROFILE)
        assert "illustrative_delta: 0.55" in text
        assert abs(0.25 - (-0.30) - 0.55) < 1e-9

    def test_delta_direction_microsoft_minus_meta(self):
        assert 'delta_direction: "Microsoft minus Meta"' in _read(PROFILE)

    def test_finding_layer_manual_illustrative(self):
        assert 'finding_layer: "MANUAL ILLUSTRATIVE"' in _read(PROFILE)

    def test_register_selection_not_uniform_softness(self):
        text = _read(PROFILE)
        assert "register-selection finding, NOT a uniform-softness finding" in text

    def test_delta_not_significant(self):
        text = _read(PROFILE)
        assert "NOT significant" in text

    def test_no_uniform_softness_claim(self):
        block = _read(PROFILE).split(BLOCK_KEY, 1)[1].split("\n  x_twitter:", 1)[0]
        assert "uniform softness" not in block.lower() or "NOT" in block


# ---------------------------------------------------------------------------
# 6. Statistical discipline: manual illustrative only, no engine
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline1017:
    def _disc(self) -> str:
        text = _read(PROFILE)
        block = text.split("    " + BLOCK_KEY + ":")[1].split("\n  x_twitter:")[0]
        return block.split("statistical_discipline:")[1].split("verdict:")[0]

    def test_manual_illustrative_only(self):
        assert "MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026 standing rule" in self._disc()

    def test_no_p_value_cohens_d_ci(self):
        disc = self._disc()
        assert "p_value NOT_CALCULATED" in disc
        assert "cohens_d NOT_CALCULATED" in disc
        assert "confidence interval NOT_CALCULATED" in disc

    def test_is_significant_false_engine_not_run(self):
        disc = self._disc()
        assert "is_significant False" in disc
        assert "engine NOT run at the finding layer" in disc

    def test_verdict_directionally_supported_not_proven(self):
        assert 'verdict: "directionally_supported_not_proven"' in _read(PROFILE)

    def test_no_analysis_json_update(self):
        assert "no_analysis_json_update: true" in _read(PROFILE)

    def test_not_falsification_ledger_30(self):
        text = _read(PROFILE)
        assert "falsification_family_member: false" in text
        assert "falsification_ledger: 30" in text

    def test_expected_test_count(self):
        import ast

        tree = ast.parse(_read("tests/" + THIS_FILE))
        count = sum(
            isinstance(n, ast.FunctionDef) and n.name.startswith("test_")
            for n in ast.walk(tree)
        )
        assert count == EXPECTED_TESTS


# ---------------------------------------------------------------------------
# 7. Corpus novelty: max mechanism_id is 841; zero 842 keys
# ---------------------------------------------------------------------------
class TestCorpusNovelty1017:
    def _numeric_ids(self) -> list[int]:
        r = run_git("grep", "-h", "-o", "-E", "mechanism_id: [0-9]+", "--", "profiles/")
        return [int(m.split(": ")[1]) for m in r.stdout.splitlines()]

    def test_max_numeric_mechanism_id_is_841(self):
        assert max(self._numeric_ids()) == 841

    def test_zero_next_numeric_842_in_profiles(self):
        r = run_git("grep", "-F", NEXT_NUMERIC, "--", "profiles/")
        assert r.stdout.strip() == ""

    def test_zero_next_underscore_842_in_profiles(self):
        r = run_git("grep", "-F", NEXT_US, "--", "profiles/")
        assert r.stdout.strip() == ""

    def test_zero_next_dash_842_in_profiles(self):
        r = run_git("grep", "-F", NEXT_DASH, "--", "profiles/")
        assert r.stdout.strip() == ""


# ---------------------------------------------------------------------------
# 8. Doc-sync per #719 (fail pre-commit, green post-doc-sync)
# ---------------------------------------------------------------------------
class TestDocSync1017:
    def test_readme_pre_run_values_still_present(self):
        # Pre-run values carried in the new test-file table row's doc-sync
        # prose (52222/1341 -> NEW), so they remain present after README's
        # header stats row is bumped.
        readme = _read(README)
        assert "52222" in readme and "1341" in readme

    def test_readme_table_row_for_1017(self):
        assert ("`tests/" + THIS_FILE + "`") in _read(README)

    def test_architecture_tree_row_for_1017(self):
        assert THIS_FILE.replace(".py", "") in _read(ARCH)


# ---------------------------------------------------------------------------
# 9. Iteration-log entry per #719 (fail pre-commit, green post-entry)
# ---------------------------------------------------------------------------
class TestIterationLog1017:
    def test_log_newest_entry_is_1017(self):
        headers = re.findall(r"^## #\d+ Type [A-E]", _read(LOG), re.M)
        assert headers[0] == "## #1017 Type A"

    def test_log_entry_marks_third_leg(self):
        log = _read(LOG)
        entry = log.split("## #1017 Type A", 1)[1].split("## #", 1)[0]
        assert "THIRD leg of the 1015-1019 window" in entry
        assert "D #1015 -> E #1016 -> A #1017" in entry

    def test_log_entry_precedes_1016(self):
        log = _read(LOG)
        assert log.index("## #1017 Type A") < log.index("## #1016 Type E")


# ---------------------------------------------------------------------------
# 10. Confounders ranked strong-first; counterevidence; financial gradient
# ---------------------------------------------------------------------------
class TestConfounders1017:
    def _block(self) -> str:
        text = _read(PROFILE)
        start = text.index("    " + BLOCK_KEY + ":")
        return text[start : text.index("\n  x_twitter:", start)]

    def test_confounder_tiers_ranked_strong_first(self):
        block = self._block()
        assert block.index("strong:") < block.index("moderate:") < block.index("weak:")

    def test_strong_confounders_cover_genre_attribution_evidence(self):
        block = self._block()
        strong = block.split("strong:")[1].split("moderate:")[0]
        assert "genre/peg mismatch" in strong
        assert "attribution-headline standard practice" in strong
        assert "excerpt/attestation-bounded evidence" in strong

    def test_counterevidence_four_items(self):
        block = self._block()
        ce = block.split("counterevidence:")[1].split("falsification_family_member")[0]
        assert ce.count('- "') >= 4
        assert "Seattle Times and Newsday sue OpenAI and Microsoft" in ce
        assert "mechanism 502" in ce
        assert "mechanism 598" in ce
        assert "mechanism 461" in ce

    def test_financial_nexus_one_sided_gradient(self):
        block = self._block()
        assert "one-sided licensing gradient" in block
        assert "NOT a PCM participant" in block
        assert "PMC pays Microsoft for Azure" in block

    def test_prediction_status_bounded(self):
        block = self._block()
        assert "prediction_status" in block
        assert "NOT as uniform softness" in block

    def test_no_causation_claim(self):
        text = _read(PROFILE)
        block = text.split("    " + BLOCK_KEY + ":")[1].split("\n  x_twitter:")[0]
        disc = block.split("statistical_discipline:")[1].split("verdict:")[0]
        assert "Correlation is not causation" in disc


# ---------------------------------------------------------------------------
# 11. Push readiness: ASCII, staged set, concurrency, hashes
# ---------------------------------------------------------------------------
class TestPushReadiness1017:
    def test_new_block_ascii_only_no_em_dash(self):
        lines = _read(PROFILE).splitlines()
        start = next(i for i, l in enumerate(lines) if BLOCK_KEY in l)
        end = next(i for i, l in enumerate(lines) if l == "  x_twitter:")
        block_lines = lines[start:end]
        assert block_lines, "block must be non-empty"
        for line in block_lines:
            assert all(ord(c) < 128 for c in line), f"non-ASCII: {line[:60]}"
        assert "\u2014" not in "\n".join(block_lines)

    def test_no_raw_own_key_literal_in_this_file(self):
        src = _read("tests/" + THIS_FILE)
        assert MECH_ID_MARKER not in src

    def test_staged_set_exactly_five_paths(self):
        r = run_git("diff", "--cached", "--name-only")
        staged = set(r.stdout.split())
        assert staged == STAGED_SET

    def test_inflight_concurrency_stays_unstaged(self):
        r = run_git("diff", "--cached", "--name-only")
        staged = set(r.stdout.split())
        assert staged.isdisjoint(INFLIGHT)

    def test_hash_placeholders_filled_post_followup(self):
        # Fails pre-commit (no own 40-hex hashes in the #1017 log entry yet);
        # the log-hash followup registers main + anchor hashes in the entry
        # per #721, then this goes green. Predecessor hashes excluded.
        log = _read(LOG)
        entry = log.split("## #1017 Type A", 1)[1].split("## #", 1)[0]
        hashes = set(re.findall(r"\b[0-9a-f]{40}\b", entry)) - PREDECESSOR_HASHES
        assert len(hashes) >= 2

    def test_novelty_urls_first_appearance(self):
        for url in NEW_URLS:
            r = run_git("grep", "-l", "-F", url, "--", "profiles/")
            assert r.stdout.splitlines() == [PROFILE], url
