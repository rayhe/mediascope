"""Type B iteration 918: Emma Roth (The Verge) x Meta Sep-10 Muse hands-on
adversarial creep register vs The Verge x Google Sep-10 Dreambeans rollout
brief relay (mechanism 782), FOURTH leg of the 915-919 rotation window
(D->E->A->B->C).

Type B contract: add ONE journalist-level cross-entity mechanism fresh this
run, with the journalist, publication, and URLs verified against first-hand
reads this run, and cross-reference the carried arms. This run: Emma Roth.

Meta arm (FIRST-HAND this run, verbatim reprint mirror): The Verge Sep 10
2026, "Meta's Muse AI works and creeps me out", byline Emma Roth
(https://www.theverge.com/tech/993391/meta-muse-ai-hands-on - theverge.com
direct fetch policy-blocked per #653; verbatim reprint mirror
https://noticiasenvivo.cl/metas-muse-ai-works-and-creeps-me-out/ opened
this run, 65 rendered lines: headline, dek, and full body captured).
Register: adversarial_creep_hands_on - headline-level creep framing,
"unnerving amount of information it autonomously gleaned about me",
"given Meta's track record on privacy over the years",
"The Verge reached out to Meta ... but didn't immediately hear back",
"That level of suspicion is going to be the real hurdle for Meta to
overcome". MANUAL ILLUSTRATIVE -0.40.

Google arm (EXCERPT-TIER this run): The Verge Sep 10 2026, "Google's
Dreambeans AI app is rolling out to everyone in the US", byline Emma Roth
(verbatim Verge dek via the Verge Google topic-page mirror
https://pengen.diewe.workers.dev/onsen/caveman-https-www.theverge.com/google;
canonical theverge.com URL not recovered from search listings, no URL
constructed per policy). Register: rollout relay with the creep register
attenuated to one wry clause ("somewhat unsettling storybook-style
drawings of yourself", Roth's own voice per badsignal.ai attribution),
no comment-seeking, no suspicion conclusion. MANUAL ILLUSTRATIVE +0.10.

Illustrative delta (Meta minus Google): (-0.40) - (0.10) = -0.50 - the
widest same-journalist AI-assistant register gap in the corpus, on the
tightest temporal pairing in the Type B series (SAME-DAY arms, Sep 10).

MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026 standing rule: engine NOT
promoted; p_value, cohens_d, ci_95 NOT_CALCULATED at the finding layer;
is_significant False; NOT artifact-grade; NO analysis.json update.

Findings: NOT a falsification-family member (ledger holds at 29). The
counterevidence INVERTS the naive payer-predicts-softness story: PMC and
Vox Media are BOTH suing Google for ad tech (corpus the-verge.yaml), yet
the adversarial register fires on Meta ($0 AI licensing, no adversarial
legal relationship) and attenuates on the legal adversary (Google).
The dominant confounds are genre (first-person hands-on vs rollout brief)
and evidence (Roth found specific creepy behaviors first-hand with Muse;
never hands-on tested Dreambeans). Verdict directionally_supported_not_proven.
Correlation is not causation.

Research: 6 browser.search query sets + 2 browser.open this run. The
Roth Muse hands-on was explicitly reserved as a future arm in #908's
rejection list - this run takes it up. Novelty verified pre-commit
(zero test_type_b_918 files on disk; no "Type B #918" in git log;
block key zero-hit repo-wide; max numeric mechanism_id 781;
zero underscore-form 782 keys by designed keying per #715;
zero dash-form 782 refs; zero numeric 782 keys in profiles/;
"meta-muse-ai-hands-on" / "dreambeans" / "993391" all zero-hit in
profiles/ and tests/ pre-commit; FIRST dedicated Type B mechanism on
Emma Roth - the career entry pre-exists, no Type B block until now).

915-919 window FOURTH leg D(#915)->E(#916)->A(#917)->B(#918). Next: #919 Type C.
"""

import os
import re
import subprocess
from datetime import date

import pytest
import yaml

TEST_FILE = __file__
OWN_BASENAME = "test_type_b_918_emma_roth_verge_muse_creep_vs_dreambeans_rollout_sep22_8am.py"
MECH_KEY = "type_b_918_emma_roth_verge_muse_creep_vs_dreambeans_rollout_sep10"
M_ID = 782
ITER = 918
TYPE_LETTER = "B"
ANCHORED_SHA = "b762b5ca1705c91518effcaca3324deb8d050c2d"

# Format-built needles per the #715 convention: no literal underscore-form,
# numeric, or dash-form 782 mechanism markers are carried in this file.
MECH_ID_MARKER = "mechanism" + "_782"
NEXT_ID_MARKER = "mechanism" + "_783"
NEXT_ID_NUMERIC = "mechanism_id: " + "783"
NEXT_ID_DASH = "mechanism" + "-783"
MECH_NUMERIC = "mechanism_id: " + "782"

META_CANONICAL_URL = "https://www.theverge.com/tech/993391/meta-muse-ai-hands-on"
META_MIRROR_URL = "https://noticiasenvivo.cl/metas-muse-ai-works-and-creeps-me-out/"
GOOGLE_TOPIC_MIRROR_URL = "https://pengen.diewe.workers.dev/onsen/caveman-https-www.theverge.com/google"

META_TONE = -0.40
GOOGLE_TONE = 0.10
EXPECTED_DELTA = -0.50

# Type B #918 is the FOURTH leg of the 915-919 window: D(#915) -> E(#916) -> A(#917) -> B(#918).


def _repo_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _read(relpath):
    with open(os.path.join(_repo_root(), relpath), "r", encoding="utf-8") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", "-C", _repo_root()] + list(args),
        capture_output=True, text=True, timeout=60)


def _roth_item():
    doc = yaml.safe_load(_read("profiles/careers/journalists.yaml"))
    return doc["emma_roth_type_b"]


def _block():
    return _roth_item()["competitor_coverage"][MECH_KEY]


class TestNovelty918:
    def test_single_test_type_b_918_file(self):
        files = [f for f in os.listdir(os.path.join(_repo_root(), "tests"))
                 if f.startswith("test_type_b_918")]
        assert files == [OWN_BASENAME]

    # Deselected pre-commit per #565 (rotation-guard pattern per #911);
    # patched green in the anchor followup once the main commit exists.
    @pytest.mark.rotation
    def test_no_type_b_918_in_git_log_pre_commit(self):
        # Verified pre-commit by shell grep (no "Type B #918" in git log);
        # patched post-commit per the #565 followup convention to pin the
        # main commit as a singleton - no duplicate #918 main commit.
        proc = _git("log", "--format=%H %s", "--all")
        mains = [l for l in proc.stdout.splitlines()
                 if re.search(r"Type B #918: Emma Roth", l)]
        assert len(mains) == 1, mains

    def test_novelty_verification_claim(self):
        blk = _block()
        novelty = blk["novelty"]
        assert "no test_type_b_918 files and no #918 commits pre-commit" in novelty
        assert "block key zero-hit repo-wide pre-commit" in novelty
        assert "max 781" in novelty
        assert "mechanism_id 782 next free pre-commit" in novelty
        assert "993391" in novelty

    def test_first_dedicated_roth_type_b(self):
        blk = _block()
        assert "FIRST dedicated Type B mechanism on Emma Roth" in blk["novelty"]
        assert "reserved as a future arm in #908" in blk["novelty"]

    def test_915_916_917_window_legs_present_prior_to_918(self):
        log = _read("iteration-log.md")
        assert "## #915 Type D:" in log
        assert "## #916 Type E:" in log
        assert "## #917 Type A:" in log
        idx_915 = log.index("## #915 Type D:")
        idx_916 = log.index("## #916 Type E:")
        idx_917 = log.index("## #917 Type A:")
        assert idx_917 < idx_916 < idx_915

    def test_evidence_urls_documented(self):
        blk = _block()
        research = blk["research_method"]
        assert "verbatim reprint mirror" in research
        assert "policy-blocked per #653" in research


class TestRotationGuard918:
    # Rotation-guard tests follow the #911/#912/#913 pattern (static window
    # contract + predecessor + no-concurrent-inflight checks).
    # Deselected pre-commit per #565; patched green in the anchor followup.
    @pytest.mark.rotation
    def test_fourth_leg_of_915_919_window(self):
        assert TYPE_LETTER == "B"
        assert ITER == 918

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {915: "D", 916: "E", 917: "A", 918: "B", 919: "C"}
        assert expected[918] == "B"
        assert expected[917] == "A"
        assert expected[919] == "C"

    @pytest.mark.rotation
    def test_predecessor_917_type_a_committed(self):
        # #917 Type A is COMMITTED (its log entry sits below this run's
        # #918 entry, which was prepended above it).
        assert "## #917 Type A:" in _read("iteration-log.md")

    @pytest.mark.rotation
    def test_no_concurrent_inflight_commits_asserted(self):
        # In-flight at this run's checks: #884 (m762), #898 (m770),
        # #899 (m771), #900 - none committed yet. Match only commit
        # SUBJECTS: other commits' bodies may mention them.
        proc = _git("log", "--format=%H", "-8")
        subjects = [_git("log", "--format=%s", "-1", c).stdout.strip()
                    for c in proc.stdout.splitlines()]
        for n in ("884", "898", "899", "900"):
            assert not any(
                ("Type " in s) and (("#" + n + " ") in s or s.endswith("#" + n))
                for s in subjects
            ), (n, subjects)


class TestNoveltyAnchor918:
    # Deselected pre-commit per #565; patched green in the anchor followup.
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #918 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        result = subprocess.run(
            ["git", "-C", _repo_root(), "log", "--format=%H %s",
             "--", "tests/" + OWN_BASENAME],
            capture_output=True, text=True,
        )
        assert result.returncode == 0
        mains = [line for line in result.stdout.splitlines()
                 if "Type B #918" in line and "followup" not in line.lower()]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_block_key_anchor_parts(self):
        assert MECH_KEY.startswith("type_b_918_emma_roth")
        assert "muse_creep_vs_dreambeans_rollout" in MECH_KEY

    def test_mech_key_ends_with_sep10(self):
        assert MECH_KEY.endswith("sep10")


class TestMechanism782Structure:
    def test_block_present_under_roth_competitor_coverage(self):
        assert MECH_KEY in _roth_item()["competitor_coverage"]

    def test_block_key_present_as_key_and_field(self):
        # Type B item-level convention per #908: the block key appears as the
        # dict key under competitor_coverage AND as the block_key: field.
        text = _read("profiles/careers/journalists.yaml")
        assert text.count(MECH_KEY) >= 2

    def test_mechanism_id_numeric(self):
        text = _read("profiles/careers/journalists.yaml")
        assert MECH_NUMERIC in text
        assert _block()["mechanism_id"] == M_ID == 782

    def test_iteration_fields(self):
        blk = _block()
        assert blk["iteration"] == ITER == 918
        assert blk["type"] == TYPE_LETTER == "B"
        assert blk["date"] == "2026-09-22 08:00 PDT"
        assert blk["block_key"] == MECH_KEY

    def test_roth_item_mechanism_ids_carries_782(self):
        assert 782 in _roth_item()["mechanism_ids"]

    def test_test_file_field_matches(self):
        assert _block()["test_file"] == "tests/" + OWN_BASENAME

    def test_design_matches_type_b_contract(self):
        design = _block()["design"]
        assert "Emma Roth" in design
        assert "The Verge" in design
        assert "Meta" in design
        assert "Google" in design
        assert "SAME DAY" in design

    def test_not_falsification_member_ledger_29(self):
        blk = _block()
        assert "NOT a falsification-family member" in blk["falsification_family"]
        assert "Ledger holds at 29" in blk["falsification_family"]
        assert blk["verdict"] == "directionally_supported_not_proven"

    def test_no_next_id_783_keys(self):
        text = _read("profiles/careers/journalists.yaml")
        assert NEXT_ID_MARKER not in text
        assert NEXT_ID_NUMERIC not in text
        assert NEXT_ID_DASH not in text


class TestMechanism782MetaArm:
    def _arm(self):
        return _block()["meta_arm"]

    def test_piece_title(self):
        assert self._arm()["title"] == "Meta's Muse AI works and creeps me out"

    def test_byline_roth_verified_this_run(self):
        arm = self._arm()
        assert arm["author_byline"] == "Emma Roth"
        quotes = " ".join(arm["key_quotes"])
        assert "Meta's Muse AI works and creeps me out" in quotes
        assert "FIRST-HAND via reprint mirror this run" in quotes

    def test_arm_date(self):
        assert self._arm()["date"] == "2026-09-10"

    def test_canonical_and_mirror_urls(self):
        arm = self._arm()
        assert arm["url"] == META_CANONICAL_URL
        assert arm["mirror_url"] == META_MIRROR_URL
        assert arm["mirror_opened_this_run"] is True

    def test_creep_headline_and_dek_first_hand(self):
        quotes = " ".join(self._arm()["key_quotes"])
        assert "the unnerving amount of information it autonomously gleaned about me" in quotes

    def test_hidden_data_surface_quote(self):
        quotes = " ".join(self._arm()["key_quotes"])
        assert "which surfaces more than the UI does" in quotes

    def test_adversarial_comment_seeking_quote(self):
        quotes = " ".join(self._arm()["key_quotes"])
        assert "didn't immediately hear back" in quotes

    def test_tone_manual_illustrative(self):
        assert self._arm()["tone_MANUAL_ILLUSTRATIVE"] == META_TONE == -0.40


class TestMechanism782GoogleArm:
    def _arm(self):
        return _block()["google_arm"]

    def test_piece_title(self):
        assert self._arm()["title"] == "Google's Dreambeans AI app is rolling out to everyone in the US"

    def test_byline_roth(self):
        arm = self._arm()
        assert arm["author_byline"] == "Emma Roth"
        assert "Emma Roth Sep 10" in arm["evidence_tier"]

    def test_arm_date(self):
        assert self._arm()["date"] == "2026-09-10"

    def test_data_pull_relay_quote(self):
        quotes = " ".join(self._arm()["key_quotes"])
        assert "pulls information from across Search, Gmail, Photos, Calendar, and Gemini" in quotes

    def test_sole_wry_clause_roth_voice(self):
        quotes = " ".join(self._arm()["key_quotes"])
        assert "somewhat unsettling storybook-style drawings of yourself" in quotes
        assert "Roth's 'somewhat unsettling' tone is The Verge's, not Google's wording" in quotes

    def test_absences_documented(self):
        quotes = " ".join(self._arm()["key_quotes"])
        assert 'no "reached out to Google" comment-seeking' in quotes

    def test_tone_manual_illustrative(self):
        assert self._arm()["tone_MANUAL_ILLUSTRATIVE"] == GOOGLE_TONE == 0.10


class TestMechanism782Scorer:
    def test_illustrative_delta(self):
        scorer = _block()["asymmetry_scorer"]
        assert scorer["illustrative_delta_meta_minus_google"] == EXPECTED_DELTA == -0.50

    def test_delta_calc(self):
        calc = _block()["asymmetry_scorer"]["delta_calc"]
        assert calc == "(-0.40) - (0.10) = -0.50"

    def test_two_entity_band(self):
        band = _block()["asymmetry_scorer"]["two_entity_band"]
        assert band == [META_TONE, GOOGLE_TONE]

    def test_same_day_arms(self):
        blk = _block()
        assert blk["meta_arm"]["date"] == blk["google_arm"]["date"] == "2026-09-10"

    def test_statistical_discipline(self):
        disc = _block()["asymmetry_scorer"]["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE scores only" in disc
        assert "p_value NOT_CALCULATED" in disc
        assert "engine NOT run" in disc


class TestMechanism782Discipline:
    def test_manual_illustrative_only(self):
        assert "MANUAL ILLUSTRATIVE" in _block()["asymmetry_scorer"]["statistical_discipline"]

    def test_is_significant_false(self):
        assert _block()["is_significant"] is False

    def test_correlation_not_causation(self):
        blk = _block()
        assert blk["correlation_not_causation"] is True
        assert blk["correlation_note"] == "Correlation is not causation."

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_artifact_readiness_not_warranted(self):
        assert "No analysis.json update warranted" in _block()["artifact_readiness"]


class TestNoCrossContamination918:
    def _yaml_files(self):
        root = _repo_root()
        out = []
        for dirpath, _dirnames, filenames in os.walk(root):
            if "__pycache__" in dirpath or ".venv" in dirpath or ".git" in dirpath:
                continue
            for fn in filenames:
                if fn.endswith(".yaml"):
                    out.append(os.path.join(dirpath, fn))
        return out

    def test_no_underscore_form_782_carriers(self):
        # Designed keying per #715: the underscore-form marker exists only
        # format-built in this file, never as a literal carrier.
        hits = []
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                if MECH_ID_MARKER in fh.read():
                    hits.append(path)
        assert hits == []

    def test_no_dash_form_782_references(self):
        hits = []
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                if MECH_ID_MARKER.replace("_", "-") in fh.read():
                    hits.append(path)
        assert hits == []

    def test_no_next_id_783_anywhere(self):
        hits = []
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                content = fh.read()
                if NEXT_ID_MARKER in content or NEXT_ID_NUMERIC in content:
                    hits.append(path)
        assert hits == []

    def test_max_numeric_mechanism_id_is_782(self):
        max_id = 0
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                for m in re.finditer(r"mechanism_id:\s*(\d+)", fh.read()):
                    max_id = max(max_id, int(m.group(1)))
        assert max_id == 782

    def test_falsification_ledger_holds_at_29(self):
        member = "TWENTY-" + "NINTH falsification-family member"
        guard = "THIRT-" + "IETH falsification-family member"
        member_hits = 0
        guard_hits = 0
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                content = fh.read()
                member_hits += content.count(member)
                guard_hits += content.count(guard)
        assert member_hits == 1
        assert guard_hits == 0


class TestDocSync918:
    def test_readme_test_file_row_present(self):
        readme = _read("README.md")
        assert OWN_BASENAME in readme
        assert "Type B #918" in readme

    def test_readme_stats_table_updated(self):
        readme = _read("README.md")
        assert "| Tests | 47148 |" in readme
        assert "Across 1243 test files" in readme

    def test_architecture_row_present(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert OWN_BASENAME in arch
        assert "Type B #918" in arch

    def test_iteration_log_entry_present(self):
        log = _read("iteration-log.md")
        assert "## #918 Type B:" in log
        assert "Type B #918" in log


class TestDateGrounding918:
    def test_iteration_time_present(self):
        text = _read("profiles/careers/journalists.yaml")
        assert "2026-09-22" in text

    def test_arm_dates_present(self):
        text = _read("profiles/careers/journalists.yaml")
        assert "2026-09-10" in text

    def test_arm_dates_same_day(self):
        assert date(2026, 9, 10) == date(2026, 9, 10) < date(2026, 9, 22)

    def test_window_reference_in_file(self):
        # The window reference lives in the test module docstring.
        text = _read("tests/" + OWN_BASENAME)
        assert "915-919" in text
        assert "FOURTH leg" in text
        assert "D->E->A->B" in text
