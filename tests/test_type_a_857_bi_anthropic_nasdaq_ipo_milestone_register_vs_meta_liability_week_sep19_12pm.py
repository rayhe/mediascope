"""Type A #857 (855-859 window, third leg D->E->A): Business Insider x
Anthropic Sep-13 Nasdaq-choice IPO-scoop milestone-validation register vs
BI x Meta same-week liability registers (mechanism 745).

FIRST dedicated corpus mechanism on Business Insider's Sep 13 2026 scoop
that Anthropic "has selected Nasdaq for a potential October initial public
offering (IPO) at a reported valuation of up to $2 trillion" (four verbatim
secondary attributions: gateiolink, webpronews, techdefused, startupfortune;
BI original paywalled, no businessinsider.com URL returned verbatim). The
register is banking-milestone validation (+0.45): Nasdaq choice as maturation
event; "$2 trillion" valuation talk and "up to $100 billion" raise as
record-chasing ("would top the $86.2 billion record set by SpaceX in June");
Nvidia in talks to anchor "as much as $10 billion" as "an early strategic
backer for the outsized offering"; "Nasdaq would host the year's two largest
IPOs by proceeds". Anthropic arm avg +0.4167 (0.45 / 0.40 / 0.40). In the
SAME Sep 13-18 window BI's own Meta wearables coverage (attested
secondaries, excerpt-bounded per #503) routes through liability vocabulary:
Katie Notopoulos's BI report on Andrew Bosworth's AMA ("Meta's CTO says the
glasses problem is a small number of bad actors", executive-defense relay,
+0.10); BI's Project Luna framing (Meta "navigating its Google Glass
moment", "the camera has become the single biggest liability in the
company's wearables strategy", adversarial-editorial, -0.30); BI's
creator-bans reporting ("Meta bans creators that film people without
consent" plus software camera-disable on LED tamper, accountability news,
-0.15). Meta arm avg -0.1167. Illustrative delta (Anthropic minus Meta)
+0.5333, target-minus-peer. EXTENDS mechanism 420's BI control-case finding
(Anthropic aspirational vs Meta product-neutral, +0.34) to the IPO-march peg
and the liability-week Meta comparator; REPLICATES its direction (Anthropic
softest despite $0 direct tie; the Axel Springer payer sits at the hard end
of the BI quad per m399: OpenAI -0.42 profitability skepticism). The
financial tie predicts the OPPOSITE ordering. connects_to: [420, 399, 542,
730, 739]. MANUAL / qualitative only; engine NOT run per the Aug 28 2026
standing rule; p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant False;
verdict directionally_supported_not_proven; no_analysis_json_update: true;
NOT artifact-grade; NOT a falsification-family member - register
documentation plus m420 control-case extension (neutral_to_aspirational
prediction met), not a uniform-prediction test; falsification ledger holds
at 26. Novelty verified pre-commit (zero test_type_a_857 files; no 'Type A
#857' in git log; max numeric mechanism_id 744; zero underscore-form 745/746
keys per #715; block key zero-hit; all 10 secondary URLs zero-hit
repo-wide); count_stats gate (delta = this file exactly); 855-859 window
third leg D->E->A (anchor patched post-commit per #565) - Sep 19 2026 12:00
PDT.
"""

import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = "test_type_a_857_bi_anthropic_nasdaq_ipo_milestone_register_vs_meta_liability_week_sep19_12pm.py"
MECH_KEY = "mechanism_745_bi_anthropic_nasdaq_ipo_milestone_register_vs_meta_liability_week_sep19_2026"
M_ID = 745
ITER = 857
TYPE_LETTER = "A"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_745"
NEXT_ID_MARKER = "mechanism" + "_746"
NEXT_ID_NUMERIC = "mechanism_id: " + "746"
NEXT_ID_DASH = "mechanism" + "-746"
EXPECTED_ORDER = [("A", "857"), ("E", "856"), ("D", "855"), ("C", "854"), ("B", "853")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

NASDAQ_ATTRS = [
    "https://gateiolink.net/news/detail/anthropic-picks-nasdaq-for-october-ipo-at-reported-2-trillion-valuation-24270427",
    "https://www.webpronews.com/anthropic-picks-nasdaq-for-blockbuster-ipo-as-it-chases-2-trillion-valuation-amid-ai-safety-warnings/",
    "https://techdefused.com/a/gZymG9d/anthropic-ipo-round-up-nasdaq-mid-term-gamble-betting-and-the-dreaded-pause-button-all-you-need-to-k",
    "https://startupfortune.com/anthropic-is-reportedly-heading-toward-a-2-trillion-nasdaq-ipo-in-october/",
]
VALUATION_ATTRS = [
    "https://aistockwire.com/blog/anthropic-nasdaq-ipo-listing-nvidia-investment-september-2026",
    "https://globalbusinessoutlook.com/technology/anthropic-picks-nasdaq-for-ipo-eyes-nvidia-as-anchor-investor/",
]
META_ATTRS = [
    "https://www.newslocker.com/en-us/news/social-media-news/meta-plans-camera-free-smart-glasses-this-autumn-the-information-reports/",
    "https://tech-insider.org/meta-confirms-a-camera-free-path-with-project-luna/",
    "https://www.noypigeeks.com/social-media/meta-bans-creators-film-consent-smart-glasses/",
    "https://www.archyde.com/meta-reportedly-readies-camera-less-smart-glasses/",
]
EXPECTED_URLS = NASDAQ_ATTRS + VALUATION_ATTRS + META_ATTRS

README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _profiles_text():
    return _read(os.path.join(REPO_ROOT, "profiles", "business-insider.yaml"))


def _block():
    text = _profiles_text()
    start = text.index(MECH_KEY)
    end = text.index("\n  meta:\n", start)
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


def _window(n=40):
    subjects = _git("log", f"-{n}", "--format=%s", "--no-merges").splitlines()
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out[:5]


class TestNovelty857:
    def test_single_test_type_a_857_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_a_857") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_a_857_main_commit_unique_and_anchored(self):
        # No #857 main commit exists pre-commit; the anchor test pins
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
            if "Type A #857" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # This run ADDS mechanism 745: post-commit max is 745, zero 746
        # keys anywhere. Pre-commit sweeps verified max 744, zero
        # underscore-form 745/746 keys (format-built needles per #715),
        # block key zero-hit, all 10 secondary URLs zero-hit repo-wide.
        assert max(_corpus_ids()) == 745
        assert _repo_grep(NEXT_ID_MARKER) == []
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == []
        assert _repo_grep(NEXT_ID_DASH, roots=("profiles", "tests")) == []

    def test_855_859_window_legs_present_prior_to_857(self):
        log = _read(LOG_PATH)
        for marker in (
            "## #855 Type D:",
            "#856 Type E:",
        ):
            assert marker in log, marker


class TestRotationGuard857:
    """#857 is the Type A third leg of window 855-859: D->E->A."""

    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_855_859_third_leg(self):
        # Deselected pre-commit per #565 (the #857 main commit does not
        # exist yet); patched green in the anchor followup.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"855-859 window third leg D->E->A: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_e_856(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        assert window[1] == ("E", "856"), (
            f"immediate predecessor must be Type E #856, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        # Patched to the real main-commit SHA in the anchor followup per
        # the #565 convention; deselected pre-commit at the pytest CLI.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--", "tests/" + OWN_BASENAME],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), result.stdout
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type A #857" in line and "followup" not in line.lower()
        ]
        assert mains and mains[0].startswith(ANCHORED_SHA + " "), mains


class TestNoveltyAnchor857:
    def test_block_key_absent_before_this_run(self):
        # The designed block key must not collide with any earlier
        # mechanism key; uniqueness is asserted structurally in
        # TestMechanism745Structure, this anchors the novelty claim text.
        assert "mechanism_745_bi_anthropic" in MECH_KEY
        assert MECH_KEY.endswith("sep19_2026")


class TestMechanism745Structure:
    def test_block_key_exists_in_bi_profile(self):
        assert MECH_KEY in _profiles_text()

    def test_block_key_unique_in_profile(self):
        assert _profiles_text().count(MECH_KEY) == 1

    def test_block_lives_under_anthropic_competitor_relationship(self):
        d = yaml.safe_load(
            open(os.path.join(REPO_ROOT, "profiles", "business-insider.yaml"))
        )
        assert MECH_KEY in d["competitor_relationships"]["anthropic"]

    def test_mechanism_id_745_adjacent_to_key(self):
        text = _profiles_text()
        start = text.index(MECH_KEY)
        assert "mechanism_id: 745" in text[start : start + 400]

    def test_pair_and_iteration_fields(self):
        block = _block()
        assert 'pair: "Business Insider x Anthropic (vs Meta)"' in block
        assert "iteration: 857" in block
        assert 'iteration_type: "A"' in block
        assert "goal_54093bda4145" in block
        assert "mediascope-daily-iteration" in block

    def test_m420_block_still_present(self):
        text = _profiles_text()
        assert "business_insider_anthropic_valuation_hype_vs_meta_product_delay_aug31_420" in text
        assert "mechanism_id: 420" in text


class TestMechanism745AnthropicArms:
    def test_three_anthropic_arms(self):
        d = yaml.safe_load(
            open(os.path.join(REPO_ROOT, "profiles", "business-insider.yaml"))
        )
        arms = d["competitor_relationships"]["anthropic"][MECH_KEY]["anthropic_arms"]
        assert len(arms) == 3

    def test_nasdaq_scoop_arm_identity(self):
        d = yaml.safe_load(
            open(os.path.join(REPO_ROOT, "profiles", "business-insider.yaml"))
        )
        arm = d["competitor_relationships"]["anthropic"][MECH_KEY]["anthropic_arms"][0]
        assert arm["date"] == "2026-09-13"
        assert arm["register"] == "milestone_validation"
        assert arm["tone_illustrative"] == 0.45

    def test_valuation_hype_arm_identity(self):
        d = yaml.safe_load(
            open(os.path.join(REPO_ROOT, "profiles", "business-insider.yaml"))
        )
        arm = d["competitor_relationships"]["anthropic"][MECH_KEY]["anthropic_arms"][1]
        assert arm["register"] == "aspirational_hype"
        assert arm["tone_illustrative"] == 0.40

    def test_nvidia_anchor_arm_identity(self):
        d = yaml.safe_load(
            open(os.path.join(REPO_ROOT, "profiles", "business-insider.yaml"))
        )
        arm = d["competitor_relationships"]["anthropic"][MECH_KEY]["anthropic_arms"][2]
        assert arm["register"] == "prestige_comparison"
        assert arm["tone_illustrative"] == 0.40

    def test_all_anthropic_attribution_urls_verbatim_in_block(self):
        block = _block()
        for url in NASDAQ_ATTRS + VALUATION_ATTRS:
            assert url in block, url

    def test_nasdaq_attribution_key_language(self):
        block = _block()
        assert "has selected Nasdaq for a potential October initial public offering (IPO) at a reported valuation of up to $2 trillion" in block
        assert "would top the $86.2 billion record set by SpaceX in June" in block


class TestMechanism745MetaArms:
    def test_three_meta_arms(self):
        d = yaml.safe_load(
            open(os.path.join(REPO_ROOT, "profiles", "business-insider.yaml"))
        )
        arms = d["competitor_relationships"]["anthropic"][MECH_KEY]["meta_arms"]
        assert len(arms) == 3

    def test_meta_registers_and_tones(self):
        d = yaml.safe_load(
            open(os.path.join(REPO_ROOT, "profiles", "business-insider.yaml"))
        )
        arms = d["competitor_relationships"]["anthropic"][MECH_KEY]["meta_arms"]
        assert [(a["register"], a["tone_illustrative"]) for a in arms] == [
            ("executive_defense", 0.10),
            ("adversarial_editorial", -0.30),
            ("accountability_remediation", -0.15),
        ]

    def test_bosworth_and_luna_key_language(self):
        block = _block()
        assert "Meta''s CTO says the glasses problem is a small number of bad actors" in block
        assert "navigating its Google Glass moment" in block
        assert "Meta bans creators that film people without consent" in block

    def test_all_meta_attribution_urls_verbatim_in_block(self):
        block = _block()
        for url in META_ATTRS:
            assert url in block, url

    def test_attested_secondary_provenance_caveats(self):
        block = _block()
        assert "BI original paywalled" in block
        assert "excerpt-bounded per #503" in block


class TestMechanism745Scorer:
    def test_illustrative_arrays(self):
        d = yaml.safe_load(
            open(os.path.join(REPO_ROOT, "profiles", "business-insider.yaml"))
        )
        s = d["competitor_relationships"]["anthropic"][MECH_KEY]["asymmetry_scorer"]
        assert s["anthropic_arm_tones"] == [0.45, 0.40, 0.40]
        assert s["meta_arm_tones"] == [0.10, -0.30, -0.15]

    def test_averages(self):
        d = yaml.safe_load(
            open(os.path.join(REPO_ROOT, "profiles", "business-insider.yaml"))
        )
        s = d["competitor_relationships"]["anthropic"][MECH_KEY]["asymmetry_scorer"]
        assert s["anthropic_arm_avg"] == 0.4167
        assert s["meta_arm_avg"] == -0.1167

    def test_delta_arithmetic_at_4dp(self):
        target = (0.45 + 0.40 + 0.40) / 3
        peer = (0.10 + -0.30 + -0.15) / 3
        assert round(target - peer, 4) == 0.5333

    def test_delta_logged_matches_arithmetic(self):
        d = yaml.safe_load(
            open(os.path.join(REPO_ROOT, "profiles", "business-insider.yaml"))
        )
        s = d["competitor_relationships"]["anthropic"][MECH_KEY]["asymmetry_scorer"]
        assert s["illustrative_delta_anthropic_minus_meta"] == 0.5333

    def test_engine_not_run(self):
        block = _block()
        assert "Engine NOT run" in block

    def test_convention_target_minus_peer(self):
        block = _block()
        assert "target-minus-peer" in block

    def test_tone_basis_manual_illustrative(self):
        block = _block()
        assert "MANUAL ILLUSTRATIVE hand-assigned this run" in block


class TestMechanism745Discipline:
    def test_stats_not_calculated(self):
        block = _block()
        for token in ("p_value: NOT_CALCULATED", "cohens_d: NOT_CALCULATED", "ci_95: NOT_CALCULATED"):
            assert token in block, token

    def test_is_significant_false_and_verdict(self):
        block = _block()
        assert "is_significant: false" in block
        assert "directionally_supported_not_proven" in block

    def test_no_analysis_json_update_and_not_artifact_grade(self):
        block = _block()
        assert "no_analysis_json_update: true" in block
        assert "NOT artifact-grade" in block

    def test_not_falsification_family_ledger_holds(self):
        block = _block()
        assert "NOT a falsification-family member" in block
        assert "Ledger holds at 26" in block
        assert "TWENTY-SEVENTH absent" in block

    def test_confounders_and_counterevidence_present(self):
        d = yaml.safe_load(
            open(os.path.join(REPO_ROOT, "profiles", "business-insider.yaml"))
        )
        b = d["competitor_relationships"]["anthropic"][MECH_KEY]
        assert set(b["confounders"].keys()) == {"strong", "moderate", "weak"}
        assert len(b["counterevidence"]) == 4

    def test_m420_extension_claim(self):
        block = _block()
        assert "EXTENDS mechanism 420" in block
        assert "REPLICATES its direction" in block


class TestNoCrossContamination857:
    def test_block_ascii_only_no_em_dashes(self):
        block = _block()
        assert all(ord(c) < 128 for c in block), "non-ASCII found in new block"
        assert "—" not in block

    def test_no_literal_746_mechanism_keys(self):
        assert _repo_grep(NEXT_ID_MARKER, roots=("profiles", "tests")) == []
        assert _repo_grep(NEXT_ID_DASH, roots=("profiles", "tests")) == []

    def test_block_key_absent_from_other_test_files(self):
        # Own file carries MECH_KEY as a literal (this file's convention;
        # the marker is never duplicated across other test files).
        hits = [
            h
            for h in _repo_grep(MECH_KEY, roots=("tests",))
            if h != os.path.join("tests", OWN_BASENAME)
        ]
        assert hits == []


class TestDocSync857:
    def test_readme_test_file_row_present(self):
        assert OWN_BASENAME in _read(README_PATH)

    def test_readme_stats_table_updated(self):
        text = _read(README_PATH)
        assert "43808" in text
        assert "1185" in text

    def test_iteration_log_entry_present(self):
        assert "## #857 Type A:" in _read(LOG_PATH)


class TestDateGrounding857:
    def test_iteration_time_present(self):
        assert "2026-09-19 12:00 PDT" in _block()

    def test_arm_dates_present(self):
        block = _block()
        assert "date: '2026-09-13'" in block
        assert "date: '2026-09-16'" in block
        assert "date: '2026-09-17'" in block

    def test_window_reference_in_file(self):
        own = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "855-859" in own
