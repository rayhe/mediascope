"""Type B #848 (845-849 window, fourth leg D->E->A->B): Sabrina Ortiz
outlet-migration register constancy + disclosed junket leg - The Deep View
Snap Specs launch-event hands-on (Sep 16 2026) vs carried Meta arms
(mechanism 740).

FIRST dedicated corpus mechanism on Sabrina Ortiz at The Deep View, and
the FIRST disclosed-junket smart-glasses hands-on in the corpus. Ortiz
migrated from ZDNet Senior Editor to The Deep View Senior Reporter
between Feb and Sep 2026 (verified via Talking Biz News this run; Jason
Hiner editor-in-chief, ex-ZDNet). Her Sep 16 2026 launch-event hands-on
"Here's our take on the new Snap Specs with AI" (read first-hand this
run, 55 rendered lines) delivers her strongest superlative on record -
"out of all the AR glasses I have tested ... the best on the market right
now" (explicitly AR-glasses-scoped) - with Snap-paid travel to the LA
launch event DISCLOSED in the piece: "***Disclaimer**: Sabrina Ortiz's
travel to the Snap Specs launch event was paid for by Snap." The privacy
section is vendor-claim relay only (LED glow, on-device processing,
permission prompts - Snap's spec claims verbatim), with zero critical or
adversarial privacy vocabulary despite two Snapdragon chips (one
dedicated to computer vision) and cameras. She also flagged the $2,195
price as puzzling, caveated the 4-hour comfort claim, and pressed Snap on
the undisclosed AI model.

Meta arms carried un-rescored from mechanism 713 (Type B #803, Sep 17
2026) per the #807 pattern: Meta Ray-Ban Display "nearly sold" (+0.45),
Meta Ray-Bans first-party purchase "absolute nobrainer", Oakley Meta HSTN
"exceeded my expectations". Illustrative Snap-minus-Meta delta is 0.00 -
the finding is REGISTER CONSTANCY (Ortiz stays product-forward on Snap
exactly as on Meta), not a tone gap. EXTENDS mechanism 713 to a fourth
entity (Snap) across the outlet migration. Confounders 3/3/3
(launch-event junket genre DOMINANT; genuine product novelty; disclosure
itself; voice-consistency; qualified praise; genre boundary; AR-scope;
outlet-migration; n=1). Counter-evidence 4 (disclosure satisfied the
transparency norm; price puzzlement; comfort caveat + AI-model press;
m713 shows she is Meta-positive too). MANUAL ILLUSTRATIVE only, engine
NOT run, p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False,
verdict directionally_supported_not_proven; NOT falsification-family,
ledger holds at 26; no analysis.json update. Novelty verified pre-commit
(zero test_type_b_848 files; no 'Type B #848' in git log; max numeric
mechanism_id 739; zero underscore-form 740 keys by designed keying per
#715; block key zero-hit; the Snap Specs headline string zero-hit
repo-wide); count_stats gate (delta = this file exactly); 845-849 window
fourth leg D->E->A->B (anchor patched post-commit per #565) - Sep 19 2026
03:00 PDT.
"""

import os
import re
import subprocess
import datetime

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = "test_type_b_848_sabrina_ortiz_deepview_snap_specs_junket_disclosure_vs_meta_arms_sep19_3am.py"
MECH_KEY = "type_b_848_sabrina_ortiz_deepview_snap_specs_junket_disclosure_vs_meta_arms_sep19_3am"
M_ID = 740
ITER = 848
TYPE_LETTER = "B"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_740"
NEXT_ID_MARKER = "mechanism" + "_741"
NEXT_ID_NUMERIC = "mechanism_id: " + "741"
EXPECTED_ORDER = [("B", "848"), ("A", "847"), ("E", "846"), ("D", "845"), ("C", "844")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "ece818370590e8fb209a16942f878485b852d41b"

SNAP_ARM_URL = "https://www.thedeepview.com/articles/here-s-our-take-on-the-new-snap-specs-with-ai"
AUTHOR_URL = "https://www.thedeepview.com/author/sabrina-ortiz"
TALKINGBIZ_URL = "https://talkingbiznews.com/media-news/the-deep-view-hires-ortiz-to-cover-ai/"
META_URLS = [
    "https://www.zdnet.com/article/i-tried-the-meta-ray-ban-display-glasses-including-this-unreleased-feature-and-im-nearly-sold/",
    "https://Www.Zdnet.Com/article/i-finally-tried-samsungs-xr-headset-and-it-beats-my-apple-vision-pro-in-meaningful-ways/",
]
EXPECTED_URLS = [SNAP_ARM_URL, AUTHOR_URL, TALKINGBIZ_URL] + META_URLS

README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _profiles_text():
    return _read(os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml"))


def _block():
    text = _profiles_text()
    start = text.index(MECH_KEY)
    end = text.index("\nece_yildirim:")
    return text[start:end]


def _corpus_ids():
    ids = []
    for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith(".yaml"):
                text = _read(os.path.join(root, fn))
                for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                    ids.append(int(m.group(1)))
    return ids


def _repo_grep(needle, roots=("profiles", "tests")):
    hits = []
    for r in roots:
        base = os.path.join(REPO_ROOT, r)
        for root, _, files in os.walk(base):
            for fn in files:
                if fn.rsplit(".", 1)[-1] in ("py", "yaml", "md", "json"):
                    p = os.path.join(root, fn)
                    try:
                        if needle in _read(p):
                            hits.append(os.path.relpath(p, REPO_ROOT))
                    except OSError:
                        pass
    return hits


def _git(*args):
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def _git_log_mains(qualifier):
    out = _git("log", "--all", "--format=%H %s", "--grep", qualifier)
    mains = {}
    for line in out.splitlines():
        if not line.strip():
            continue
        sha, _, subject = line.partition(" ")
        if "Type B #848" in subject:
            mains[sha] = subject
    return mains


def _window(n=40):
    # First occurrence of each distinct iteration number, newest first
    # (robust to followup commits that repeat the same "Type X #N" wording
    # without the colon, per the #752 convention).
    subjects = _git("log", f"-{n}", "--format=%s", "--no-merges").splitlines()
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out[:5]


class TestNovelty848:
    def test_single_test_type_b_848_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_b_848") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_b_848_main_commit_unique_and_anchored(self):
        # No #848 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--", "tests/" + OWN_BASENAME],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type B #848" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # This run ADDS mechanism 740: post-commit max is 740, zero 741
        # keys anywhere. Pre-commit sweeps verified max 739, zero
        # underscore-form 740 keys (designed keying per #715), block key
        # zero-hit, Snap Specs headline string zero-hit repo-wide.
        assert max(_corpus_ids()) == 740
        assert _repo_grep(NEXT_ID_MARKER) == []
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == []

    def test_845_849_window_legs_present_prior_to_848(self):
        log = _read(LOG_PATH)
        for marker in (
            "## #845 Type D:",
            "## #846 Type E:",
            "## #847 Type A:",
        ):
            assert marker in log, marker


class TestRotationGuard848:
    """#848 is the Type B fourth leg of window 845-849: D->E->A->B."""

    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_845_849_fourth_leg(self):
        # Deselected pre-commit per #565 (the #848 main commit does not
        # exist yet); patched green in the anchor followup.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"845-849 window fourth leg D->E->A->B: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_a_847(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        assert window[1] == ("A", "847"), (
            f"immediate predecessor must be Type A #847, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        # Patched to the real main-commit SHA in the anchor followup per
        # the #565 convention; deselected pre-commit at the pytest CLI.
        mains = _git_log_mains("Type B #848: Sabrina Ortiz")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism740Structure:
    def test_block_key_exists_in_journalists_profile(self):
        assert MECH_KEY in _profiles_text()

    def test_block_key_unique(self):
        keys = re.findall(r"^    " + MECH_KEY + r":$", _profiles_text(), re.M)
        assert len(keys) == 1, keys

    def test_iteration_and_type_and_time_pdt(self):
        block = _block()
        assert "iteration: 848" in block
        assert "rotation_type: B" in block
        assert "2026-09-19 03:00 PDT" in block
        assert "mechanism_id: 740" in block

    def test_designed_keying_no_underscore_740_in_block(self):
        # Per #715: block keys and prose must not carry the underscore-form
        # mechanism id; the colon form mechanism_id: 740 is the only allowed
        # 740 reference.
        block = _block()
        assert MECH_ID_MARKER not in block
        assert "mechanism_id: 740" in block

    def test_yaml_parses_and_fields(self):
        d = yaml.safe_load(_profiles_text())
        mech = d["sabrina_ortiz"]["competitor_coverage"][MECH_KEY]
        assert mech["mechanism_id"] == 740
        assert mech["iteration"] == 848
        assert mech["rotation_type"] == "B"
        assert mech["verdict"] == "directionally_supported_not_proven"
        assert mech["no_analysis_json_update"] is True
        assert mech["connects_to"] == [713]
        assert mech["is_significant"] is False

    def test_sabrina_ortiz_outlet_migration_fields(self):
        d = yaml.safe_load(_profiles_text())
        o = d["sabrina_ortiz"]
        assert o["current_role"] == "Senior Reporter"
        assert o["current_publication"] == "The Deep View"
        assert o["previous_role"] == "Senior Editor"
        assert o["previous_publication"] == "ZDNet"
        assert o["mechanism_ids"] == [713, 740]
        assert SNAP_ARM_URL in o["source_urls"]


class TestMechanism740SnapArm:
    def _snap(self):
        d = yaml.safe_load(_profiles_text())
        return d["sabrina_ortiz"]["competitor_coverage"][MECH_KEY]["snap_arm"]

    def test_snap_arm_title_verbatim(self):
        assert self._snap()["title"] == "Here's our take on the new Snap Specs with AI"

    def test_snap_arm_date_sep_16_2026(self):
        assert self._snap()["date"] == "2026-09-16"

    def test_snap_arm_byline_attribution_and_role(self):
        snap = self._snap()
        assert snap["author_byline"] == "Sabrina Ortiz"
        assert snap["publication"] == "the_deep_view"
        assert "Senior Reporter" in snap["role"]
        urls = snap["byline_attribution_urls"]
        assert SNAP_ARM_URL in urls
        assert AUTHOR_URL in urls
        assert TALKINGBIZ_URL in urls

    def test_junket_disclosure_verbatim(self):
        disc = self._snap()["junket_disclosure"]
        assert "travel to the Snap Specs launch event was paid for by Snap" in disc
        assert "editorially independent" in disc

    def test_best_on_the_market_right_now_verbatim(self):
        quotes = " ".join(self._snap()["key_quotes"])
        assert "the best on the market right now" in quotes
        assert "out of all the AR glasses I have tested" in quotes

    def test_privacy_vendor_relay_verbatim(self):
        quotes = " ".join(self._snap()["key_quotes"])
        assert "LED light glows when recording" in quotes
        assert "on-device data processing prioritized" in quotes
        assert "prompted before accessing sensitive information" in quotes

    def test_first_hand_evidence_tier(self):
        snap = self._snap()
        assert "first-hand" in snap["evidence_tier"]
        assert "55" in snap["evidence_tier"]
        assert len(snap["key_quotes"]) == 6


class TestMechanism740MetaArms:
    def _carried(self):
        d = yaml.safe_load(_profiles_text())
        return d["sabrina_ortiz"]["competitor_coverage"][MECH_KEY][
            "meta_arms_carried_from_713"
        ]

    def test_meta_arms_carried_from_713_unrescored(self):
        assert "un-rescored" in self._carried()["note"]
        assert "#807" in self._carried()["note"]

    def test_meta_display_arm_tone_045(self):
        arms = self._carried()["arms"]
        display = [a for a in arms if "Display" in a["title"]]
        assert len(display) == 1
        assert display[0]["tone_illustrative"] == 0.45
        assert "nearly sold" in display[0]["title"]

    def test_meta_arms_supporting_notes(self):
        notes = " ".join(a.get("note", "") for a in self._carried()["arms"])
        assert "absolute nobrainer" in notes
        assert "exceeded my expectations" in notes

    def test_no_duplicate_meta_arm_mechanism_740(self):
        # The Meta arms carry tones from mechanism 713; they must not
        # introduce any new numeric mechanism id in the block.
        block = _block()
        assert "mechanism_id: 713" not in block
        assert re.search(r"mechanism_id:\s*(\d+)", block).group(1) == "740"


class TestMechanism740Scorer:
    def _scorer(self):
        d = yaml.safe_load(_profiles_text())
        return d["sabrina_ortiz"]["competitor_coverage"][MECH_KEY]["asymmetry_scorer"]

    def test_snap_arm_tone_045_illustrative(self):
        d = yaml.safe_load(_profiles_text())
        snap = d["sabrina_ortiz"]["competitor_coverage"][MECH_KEY]["snap_arm"]
        assert snap["tone_illustrative"] == 0.45
        assert "MANUAL ILLUSTRATIVE" in snap["tone_basis"]

    def test_delta_zero_math(self):
        s = self._scorer()
        assert s["snap_arm_avg"] == 0.45
        assert s["meta_arm_avg"] == 0.45
        assert s["illustrative_delta_snap_minus_meta"] == 0.0
        assert round(s["snap_arm_avg"] - s["meta_arm_avg"], 2) == 0.0

    def test_extends_m713_connects_to(self):
        d = yaml.safe_load(_profiles_text())
        mech = d["sabrina_ortiz"]["competitor_coverage"][MECH_KEY]
        assert mech["connects_to"] == [713]
        assert "EXTENDS mechanism 713" in mech["extends"]

    def test_disclosed_junket_first_in_corpus_framing(self):
        d = yaml.safe_load(_profiles_text())
        mech = d["sabrina_ortiz"]["competitor_coverage"][MECH_KEY]
        assert "FIRST in the corpus" in mech["extends"]
        assert "disclosed-junket" in mech["extends"]

    def test_register_constancy_not_tone_gap(self):
        note = self._scorer()["note"]
        assert "register constancy" in note
        assert "not a tone gap" in note


class TestMechanism740Discipline:
    def _mech(self):
        d = yaml.safe_load(_profiles_text())
        return d["sabrina_ortiz"]["competitor_coverage"][MECH_KEY]

    def test_p_value_not_calculated(self):
        assert self._mech()["p_value"] == "NOT_CALCULATED"

    def test_cohens_d_not_calculated(self):
        assert self._mech()["cohens_d"] == "NOT_CALCULATED"

    def test_ci_95_not_calculated(self):
        assert self._mech()["ci_95"] == "NOT_CALCULATED"

    def test_is_significant_false_and_engine_not_run(self):
        mech = self._mech()
        assert mech["is_significant"] is False
        assert "engine NOT run" in mech["engine"]

    def test_verdict_and_correlation_note(self):
        mech = self._mech()
        assert mech["verdict"] == "directionally_supported_not_proven"
        assert "Correlation is not causation" in mech["correlation_note"]

    def test_no_analysis_json_update_and_not_artifact_grade(self):
        mech = self._mech()
        assert mech["no_analysis_json_update"] is True
        assert mech["artifact_grade"] == "NOT artifact-grade"

    def test_falsification_ledger_holds_at_26_and_research_method(self):
        mech = self._mech()
        assert "ledger holds at 26" in mech["falsification_family"]
        assert "TWENTY-SIXTH" in mech["falsification_family"]
        assert "4 browser.search query sets" in mech["research_method"]
        assert "1 browser.open" in mech["research_method"]
        assert len(mech["confounders"]) == 9
        assert len(mech["counterevidence"]) == 4


class TestDocSync848:
    def test_readme_row_848(self):
        assert OWN_BASENAME in _read(README_PATH)

    def test_architecture_row_848(self):
        assert OWN_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_848_file(self):
        doc = _read(ARCH_PATH)
        assert OWN_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog848:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #848 Type B:")
        return log[idx : idx + 12000]

    def test_log_entry_present(self):
        assert "## #848 Type B:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism 740" in entry
        assert "Sabrina Ortiz" in entry
        assert "Snap Specs" in entry

    def test_log_rotation_window_845_849(self):
        entry = self._entry()
        assert "845-849" in entry


class TestDateGrounding848:
    def test_sep_19_2026_is_saturday(self):
        assert datetime.datetime(2026, 9, 19).strftime("%A") == "Saturday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 19, 3, 0).strftime("%H:%M") == "03:00"
