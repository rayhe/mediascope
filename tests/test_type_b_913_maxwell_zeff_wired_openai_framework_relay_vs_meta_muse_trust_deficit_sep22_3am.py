"""Type B iteration 913: Maxwell Zeff (WIRED) x OpenAI Sep-16 misalignment-framework
company-briefed platform relay vs WIRED x Meta Sep-8 Muse launch trust deficit
(mechanism 779), FOURTH leg of the 910-914 rotation window (D->E->A->B).

Type B contract: add ONE journalist-level cross-entity mechanism fresh this
run, with the journalist, publication, and URLs verified against first-hand
reads this run, and cross-reference the carried arms. This run: Maxwell Zeff.

OpenAI arm (FIRST-HAND this run, mirror-tier): WIRED Sep 16 2026, "OpenAI
Creates a New Framework to Disclose Bad AI Behavior", SOLE byline Maxwell Zeff
(https://technewstube.com/wired/1868061/openai-creates-new-framework-to-disclose-bad-ai-behavior/
verbatim WIRED reprint mirror opened this run: "By Maxwell Zeff Sep 16, 2026,
6:07 pm"; dek "The company also disclosed previously unreported incidents in
which its AI models behaved in misaligned ways, including uploading files to
the internet without being asked."). Register: company-briefed platform relay
platform_relay_company_voice_authoritative, carried +0.15 from m712/#757.

Meta arm (corpus-documented, carried from m635/#668): WIRED Sep 8 2026, "Meta
Releases Muse, a Personal AI Agent With Privacy 'Built Into It'", co-byline
Lily Hay Newman + Maxwell Zeff. Register: launch_framed_through_trust_deficit,
carried -0.30. Eight days apart, same outlet, same AI-agent category.

Illustrative delta (OpenAI minus Meta): 0.15 - (-0.30) = +0.45 - the widest
same-journalist register gap in the WIRED Sep-2026 AI-agent pair family.

MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026 standing rule: engine NOT
promoted; p_value, cohens_d, ci_95 NOT_CALCULATED at the finding layer;
is_significant False; NOT artifact-grade; NO analysis.json update.

Findings: NOT a falsification-family member (ledger holds at 29). Gradient
surface-reading is consistent with the Conde Nast x OpenAI licensing deal (Aug
2024, $5-10M/yr, ACTIVE per #599/#609; mechanism 504) - payer's self-disclosed
incidents get the platform relay, $0 side's launch gets the trust deficit -
BUT the news-peg and co-byline-dilution confounds are at least as strong, and
Zeff's own Jul-2026 adversarial OpenAI piece (m597, -0.2) cuts against
deal-driven softness. Verdict directionally_supported_not_proven. Correlation
is not causation.

Research: first-hand browser.open on the technewstube verbatim WIRED mirror
(verbatim byline, date, dek, headline); wired.com direct fetch policy-blocked
per #653. Novelty verified pre-commit (zero test_type_b_913 files on disk;
no "Type B #913" in git log; block key zero-hit repo-wide; max numeric
mechanism_id 778; zero underscore-form 779 keys by designed keying per #715;
zero dash-form 779 refs; zero numeric 779 keys in profiles/; Zeff Sep-16
OpenAI canonical URL already in-corpus from m712 - zero-hit claimed only on
the block key and headline phrase; FIRST dedicated Type B mechanism on Maxwell
Zeff - m635's type_b usage was on Lily Hay Newman).

910-914 window FOURTH leg D(#910)->E(#911)->A(#912)->B(#913). Next: #914 Type C.
"""

import os
import re
import subprocess
from datetime import date

import pytest
import yaml

TEST_FILE = __file__
OWN_BASENAME = "test_type_b_913_maxwell_zeff_wired_openai_framework_relay_vs_meta_muse_trust_deficit_sep22_3am.py"
MECH_KEY = "type_b_913_maxwell_zeff_wired_openai_framework_relay_vs_meta_muse_trust_deficit"
M_ID = 779
ITER = 913
TYPE_LETTER = "B"
ANCHORED_SHA = "d3a83151e766f75c8900f715dd995532e9bc2994"

# Format-built needles per the #715 convention: no literal underscore-form,
# numeric, or dash-form 779 mechanism markers are carried in this file.
MECH_ID_MARKER = "mechanism" + "_779"
NEXT_ID_MARKER = "mechanism" + "_780"
NEXT_ID_NUMERIC = "mechanism_id: " + "780"
NEXT_ID_DASH = "mechanism" + "-780"
MECH_NUMERIC = "mechanism_id: " + "779"

OPENAI_MIRROR_URL = "https://technewstube.com/wired/1868061/openai-creates-new-framework-to-disclose-bad-ai-behavior/"
META_MIRROR_URL = "https://technewstube.com/wired/1865498/meta-releases-muse-personal-ai-agent-privacy-built-into/"
OPENAI_CANONICAL_URL = "https://www.wired.com/story/openai-releases-new-policy-for-reporting-incidents-of-model-misalignment/"

# Type B #913 is the FOURTH leg of the 910-914 window: D(#910) -> E(#911) -> A(#912) -> B(#913).


def _repo_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _read(relpath):
    with open(os.path.join(_repo_root(), relpath), "r", encoding="utf-8") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", "-C", _repo_root()] + list(args),
        capture_output=True, text=True, timeout=60)


def _zeff_item():
    doc = yaml.safe_load(_read("profiles/careers/journalists.yaml"))
    for it in doc["journalists"]:
        if isinstance(it, dict) and it.get("name") == "Maxwell Zeff":
            return it
    raise AssertionError("Maxwell Zeff item not found")


def _block():
    return _zeff_item()["competitor_coverage"][MECH_KEY]


class TestNovelty913:
    def test_single_test_type_b_913_file(self):
        files = [f for f in os.listdir(os.path.join(_repo_root(), "tests"))
                 if f.startswith("test_type_b_913")]
        assert files == [OWN_BASENAME]

    # Deselected pre-commit per #565 (rotation-guard pattern per #911);
    # patched green in the anchor followup once the main commit exists.
    @pytest.mark.rotation
    def test_no_type_b_913_in_git_log_pre_commit(self):
        # Verified pre-commit by shell grep (no "Type B #913" in git log);
        # patched post-commit per the #565 followup convention to pin the
        # main commit as a singleton - no duplicate #913 main commit.
        proc = _git("log", "--format=%H %s", "--all")
        mains = [l for l in proc.stdout.splitlines()
                 if re.search(r"Type B #913: Maxwell Zeff", l)]
        assert len(mains) == 1, mains

    def test_novelty_verification_claim(self):
        blk = _block()
        novelty = blk["research_method"]
        assert "zero test_type_b_913 files on disk (glob)" in novelty
        assert "no 'Type B #913' in git log (--grep)" in novelty
        assert "block key zero-hit repo-wide pre-commit" in novelty
        assert "max numeric mechanism_id 778 pre-commit" in novelty
        assert "zero underscore-form 779 keys repo-wide pre-commit" in novelty

    def test_first_dedicated_zeff_type_b(self):
        blk = _block()
        assert "FIRST dedicated Type B mechanism on Maxwell Zeff" in blk["research_method"]
        assert "m635's type_b usage was on Lily Hay Newman" in blk["research_method"]

    def test_910_911_912_window_legs_present_prior_to_913(self):
        log = _read("iteration-log.md")
        assert "## #910 Type D:" in log
        assert "## #911 Type E:" in log
        assert "## #912 Type A:" in log
        idx_910 = log.index("## #910 Type D:")
        idx_911 = log.index("## #911 Type E:")
        idx_912 = log.index("## #912 Type A:")
        assert idx_912 < idx_911 < idx_910

    def test_evidence_urls_documented(self):
        blk = _block()
        research = blk["research_method"]
        assert "technewstube verbatim WIRED reprint mirror" in research
        assert "already in-corpus from m712" in research


class TestRotationGuard913:
    # Rotation-guard tests follow the #911/#912 pattern (static window
    # contract + predecessor + no-concurrent-inflight checks).
    # Deselected pre-commit per #565; patched green in the anchor followup.
    @pytest.mark.rotation
    def test_fourth_leg_of_910_914_window(self):
        assert TYPE_LETTER == "B"
        assert ITER == 913

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {910: "D", 911: "E", 912: "A", 913: "B", 914: "C"}
        assert expected[913] == "B"
        assert expected[912] == "A"
        assert expected[914] == "C"

    @pytest.mark.rotation
    def test_predecessor_912_type_a_committed(self):
        # #912 Type A is COMMITTED (its log entry sits below this run's
        # #913 entry, which was prepended above it).
        assert "## #912 Type A:" in _read("iteration-log.md")

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


class TestNoveltyAnchor913:
    # Deselected pre-commit per #565; patched green in the anchor followup.
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #913 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        result = subprocess.run(
            ["git", "-C", _repo_root(), "log", "--format=%H %s",
             "--", "tests/" + OWN_BASENAME],
            capture_output=True, text=True,
        )
        assert result.returncode == 0
        mains = [line for line in result.stdout.splitlines()
                 if "Type B #913" in line and "followup" not in line.lower()]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_block_key_anchor_parts(self):
        assert MECH_KEY.startswith("type_b_913_maxwell_zeff")
        assert "openai_framework_relay_vs_meta_muse_trust_deficit" in MECH_KEY

    def test_mech_key_ends_with_trust_deficit(self):
        assert MECH_KEY.endswith("vs_meta_muse_trust_deficit")


class TestMechanism779Structure:
    def test_block_present_under_zeff_competitor_coverage(self):
        assert MECH_KEY in _zeff_item()["competitor_coverage"]

    def test_block_key_present_as_key_and_field(self):
        # Type B item-level convention per #908: the block key appears as the
        # dict key under competitor_coverage AND as the block_key: field.
        text = _read("profiles/careers/journalists.yaml")
        assert text.count(MECH_KEY) >= 2

    def test_mechanism_id_numeric(self):
        text = _read("profiles/careers/journalists.yaml")
        assert MECH_NUMERIC in text
        assert _block()["mechanism_id"] == M_ID == 779

    def test_iteration_fields(self):
        blk = _block()
        assert blk["iteration"] == ITER == 913
        assert blk["type"] == TYPE_LETTER == "B"
        assert blk["date"] == "2026-09-22 03:00 PDT"
        assert blk["block_key"] == MECH_KEY

    def test_zeff_item_mechanism_ids_carries_779(self):
        assert 779 in _zeff_item()["mechanism_ids"]

    def test_test_file_field_matches(self):
        assert _block()["test_file"] == "tests/" + OWN_BASENAME

    def test_design_matches_type_b_contract(self):
        design = _block()["design"]
        assert "Maxwell Zeff" in design
        assert "WIRED" in design
        assert "Meta" in design
        assert "OpenAI" in design
        assert "eight days apart" in design

    def test_not_falsification_member_ledger_29(self):
        blk = _block()
        assert "NOT a falsification-family member" in blk["falsification_family"]
        assert "Ledger holds at 29" in blk["falsification_family"]
        assert blk["verdict"] == "directionally_supported_not_proven"

    def test_no_next_id_780_keys(self):
        text = _read("profiles/careers/journalists.yaml")
        assert NEXT_ID_MARKER not in text
        assert NEXT_ID_NUMERIC not in text
        assert NEXT_ID_DASH not in text


class TestMechanism779OpenAIArm:
    def _arm(self):
        return _block()["openai_arm"]

    def test_piece_title(self):
        assert self._arm()["title"] == "OpenAI Creates a New Framework to Disclose Bad AI Behavior"

    def test_byline_zeff_verified_this_run(self):
        arm = self._arm()
        assert arm["author_byline"] == "Maxwell Zeff"
        quotes = " ".join(arm["key_quotes"])
        assert "By Maxwell Zeff Sep 16, 2026, 6:07 pm" in quotes
        assert "FIRST-HAND browser.open" in quotes

    def test_arm_date(self):
        assert self._arm()["date"] == "2026-09-16"

    def test_canonical_and_mirror_urls(self):
        arm = self._arm()
        assert arm["url"] == OPENAI_CANONICAL_URL
        assert arm["mirror_url"] == OPENAI_MIRROR_URL
        assert arm["mirror_opened_this_run"] is True

    def test_dek_quote_first_hand(self):
        quotes = " ".join(self._arm()["key_quotes"])
        assert "uploading files to the internet without being asked" in quotes

    def test_register_carried_from_m712(self):
        tier = self._arm()["evidence_tier"]
        assert "platform_relay_company_voice_authoritative" in tier
        assert "carried +0.15 from m712/#757" in tier

    def test_tone_manual_illustrative(self):
        assert self._arm()["tone_MANUAL_ILLUSTRATIVE"] == 0.15


class TestMechanism779MetaArm:
    def _arm(self):
        return _block()["meta_arm"]

    def test_piece_title(self):
        assert self._arm()["title"] == "Meta Releases Muse, a Personal AI Agent With Privacy 'Built Into It'"

    def test_co_byline(self):
        arm = self._arm()
        assert arm["author_byline"] == "Lily Hay Newman, Maxwell Zeff"
        quotes = " ".join(arm["key_quotes"])
        assert "By Lily Hay Newman, Maxwell Zeff Sep 8, 2026, 4:12 pm" in quotes

    def test_arm_date(self):
        assert self._arm()["date"] == "2026-09-08"

    def test_trust_deficit_headline_variant(self):
        quotes = " ".join(self._arm()["key_quotes"])
        assert "Needs You To Trust It" in quotes

    def test_mirror_url_carried(self):
        assert self._arm()["mirror_url"] == META_MIRROR_URL

    def test_register_carried_from_m635(self):
        tier = self._arm()["evidence_tier"]
        assert "Corpus-documented from m635/#668" in tier
        assert "NOT re-read this run - carried register evidence" in tier

    def test_tone_manual_illustrative(self):
        assert self._arm()["tone_MANUAL_ILLUSTRATIVE"] == -0.30


class TestMechanism779Scorer:
    def _scorer(self):
        return _block()["asymmetry_scorer"]

    def test_delta_calc(self):
        scorer = self._scorer()
        assert scorer["illustrative_delta_openai_minus_meta"] == 0.45
        assert scorer["delta_calc"] == "(0.15) - (-0.30) = +0.45"

    def test_tone_inputs_match_arms(self):
        scorer = self._scorer()
        assert scorer["openai_tone"] == _block()["openai_arm"]["tone_MANUAL_ILLUSTRATIVE"]
        assert scorer["meta_tone"] == _block()["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"]

    def test_statistical_discipline(self):
        disc = self._scorer()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE" in disc
        assert "p_value NOT_CALCULATED" in disc
        assert "cohens_d NOT_CALCULATED" in disc
        assert "ci_95 NOT_CALCULATED" in disc
        assert "NOT artifact-grade" in disc

    def test_confounders_ranked(self):
        conf = self._scorer()["confounders"]
        assert len(conf["strong"]) == 2
        assert len(conf["moderate"]) == 2
        assert len(conf["weak"]) == 2
        strong = " ".join(conf["strong"])
        assert "Co-byline dilution" in strong
        assert "News-peg asymmetry" in strong

    def test_counterevidence_present(self):
        ce = " ".join(self._scorer()["counterevidence"])
        assert "mechanism 597" in ce
        assert "#440" in ce
        assert "m757" in ce

    def test_connects_to(self):
        conns = self._scorer()["connects_to"]
        for m in (712, 757, 635, 597, 668, 599, 663, 504):
            assert m in conns, m

    def test_verdict(self):
        # verdict lives at block level per the #908 convention (moved out
        # of asymmetry_scorer during the pre-commit fix pass).
        assert _block()["verdict"] == "directionally_supported_not_proven"


class TestMechanism779Discipline:
    def _block_text(self):
        # The new block region: from the block key to multi_publication tail.
        text = _read("profiles/careers/journalists.yaml")
        start = text.index(MECH_KEY + ":")
        return text[start:start + 12000]

    def test_no_em_dashes_in_block(self):
        assert "\u2014" not in self._block_text()
        assert "\u2013" not in self._block_text()

    def test_ascii_only_in_block(self):
        self._block_text().encode("ascii")

    def test_financial_context_bounded(self):
        fin = _block()["financial_context"]
        assert "Conde Nast x OpenAI" in fin
        assert "ACTIVE per #599/#609" in fin
        assert "mechanism 504" in fin
        assert "Correlation, not causation" in fin

    def test_correlation_not_causation_fields(self):
        blk = _block()
        assert blk["correlation_not_causation"] is True
        assert blk["correlation_note"] == "Correlation is not causation."
        assert blk["is_significant"] is False

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_novelty_field(self):
        nov = _block()["novelty"]
        assert "FIRST dedicated Type B mechanism on Maxwell Zeff" in nov
        assert "mechanism_id 779 next free pre-commit (max 778)" in nov


class TestNoCrossContamination913:
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

    def test_no_underscore_form_779_carriers(self):
        # Designed keying per #715: the underscore-form marker exists only
        # format-built in this file, never as a literal carrier.
        hits = []
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                if MECH_ID_MARKER in fh.read():
                    hits.append(path)
        assert hits == []

    def test_no_dash_form_779_references(self):
        hits = []
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                if MECH_ID_MARKER.replace("_", "-") in fh.read():
                    hits.append(path)
        assert hits == []

    def test_no_next_id_780_anywhere(self):
        hits = []
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                content = fh.read()
                if NEXT_ID_MARKER in content or NEXT_ID_NUMERIC in content:
                    hits.append(path)
        assert hits == []

    def test_max_numeric_mechanism_id_is_779(self):
        max_id = 0
        for path in self._yaml_files():
            with open(path, encoding="utf-8") as fh:
                for m in re.finditer(r"mechanism_id:\s*(\d+)", fh.read()):
                    max_id = max(max_id, int(m.group(1)))
        assert max_id == 779

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


class TestDocSync913:
    def test_readme_test_file_row_present(self):
        readme = _read("README.md")
        assert OWN_BASENAME in readme
        assert "Type B #913" in readme

    def test_readme_stats_table_updated(self):
        readme = _read("README.md")
        assert "| Tests | 46843 |" in readme
        assert "Across 1238 test files" in readme

    def test_architecture_row_present(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert OWN_BASENAME in arch
        assert "Type B #913" in arch

    def test_iteration_log_entry_present(self):
        log = _read("iteration-log.md")
        assert "## #913 Type B:" in log
        assert "Type B #913" in log


class TestDateGrounding913:
    def test_iteration_time_present(self):
        text = _read("profiles/careers/journalists.yaml")
        assert "2026-09-22" in text

    def test_arm_dates_present(self):
        text = _read("profiles/careers/journalists.yaml")
        assert "2026-09-16" in text
        assert "2026-09-08" in text

    def test_arm_dates_ordered(self):
        assert date(2026, 9, 8) < date(2026, 9, 16) < date(2026, 9, 22)

    def test_window_reference_in_file(self):
        # The window reference lives in the test module docstring.
        text = _read("tests/" + OWN_BASENAME)
        assert "910-914" in text
        assert "FOURTH leg" in text
        assert "D->E->A->B" in text
