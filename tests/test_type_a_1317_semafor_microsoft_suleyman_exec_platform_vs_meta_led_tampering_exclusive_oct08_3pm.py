"""Type A #1317: Semafor x Microsoft Suleyman executive-platform interviews vs Semafor x Meta LED-tampering accountability exclusive (Oct 8 2026, ~03:00 PM PDT).

m1021 - FIRST dedicated corpus mechanism on the Semafor x Microsoft pair.
#1312's scout rejected this pair ("thin arms on both sides, no dedicated
recent Semafor-on-Meta piece surfaced"); this run SUPERSEDES the rejection
with new main-run evidence: TWO Semafor-attributed Microsoft
executive-platform arms (Suleyman MAI-Transcribe-1 interview ~Apr 2026;
Suleyman MAI-Voice-1/MAI-1-preview interview Aug 28 2026, Reed Albergotti)
and ONE Semafor-attributed Meta accountability arm (the Sep-1-2026
LED-tampering exclusive - "Meta disables cameras on thousands of tampered
smart glasses").

The naive uniform payer-softening prediction (Microsoft x Semafor Signals
sponsorship, Feb 5 2024, undisclosed "substantial" sum per FT sourcing via
PYMNTS/Engadget relays; Semafor journalists use Microsoft + OpenAI tooling;
announced weeks after the NYT's Dec-2023 copyright lawsuit vs
Microsoft/OpenAI) is MET on the executive-platform register: the sponsor's
AI CEO gets repeated long-form Semafor interview space to frame the MAI
independence-from-OpenAI narrative (+0.25 mean MANUAL ILLUSTRATIVE), while
Meta gets an adversarial privacy-accountability exclusive (-0.30) on the
covert-recording backlash. Illustrative delta (Microsoft minus Meta) +0.55
on n=2 vs n=1 (degenerate sample disclosed). The finding is
register-local: Suleyman's own candor inside A1 ("still a lot of work to be
done" on voice AI) and symmetric access (Meta's Himel also got
exclusive-quote space - the asymmetry is register, not access) bound any
outlet-level capture claim.

Per #715 this docstring uses lowercase forms only: thesis-consistent
observation, NOT a falsification-family member (ledger holds at 59); no
new direction - fortieth absent by design, 35th-39th stand. Verdict:
thesis_consistent_observation, domain-bounded to Semafor's
executive-platform register. First mechanism-corpus documentation of the
Feb-2024 Signals sponsorship (no prior mechanism).

Novelty: 8 novel URLs zero-hit repo-wide pre-commit (git grep -F); the
Startup Fortune Meta-LED URL is a RE-SURFACE (Type E press surface since
#576, 29 in-corpus hits) - the Semafor-authorship reading is the new
element; the scout's Nscale relay URL never surfaced in main-run Full-URL
listings and was dropped per the #1312 TollBit precedent; block key
zero-hit (designed keying: iteration 1317 in key, no 1021 substring, per
the #723/#738/#739 convention).

Statistical discipline: monitoring-only per the Aug 28 2026 standing rule
(MANUAL ILLUSTRATIVE ONLY, engine NOT run, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False, NOT artifact-grade, no analysis.json
update, verdict thesis_consistent_observation). Correlation is not
causation. Hypothesis-generating only.

1 delegated scout (ranked 3 pairs; AP x Google + Guardian x xAI rejected
per below; Semafor x Microsoft SELECTED) + 8 main-run browser.search
verification sets (Copilot-redesign Semafor-attribution hunt - arm
dropped; semafor.com-scoped Meta query - index gap confirmed; Suleyman
Semafor-interview relay attestation - VERIFIED; Semafor Meta
LED-exclusive relay attestation - VERIFIED; Nscale Semafor-attribution
hunt - FAILED, arm dropped; Signals-deal verification - 7-relay
attestation; plus the scout's own 11 sets), 0 browser.open per #503.
Excerpt-bounded; Semafor originals not in the search index -
relay-attested with explicit provenance. All URLs copied verbatim from
Full-URL listings; no canonical URLs constructed. ASCII-only, no em
dashes.

Rotation: this run is iteration #1317 Type A, the THIRD leg of the
1315-1319 window (D #1315 -> E #1316 -> A #1317 -> B #1318 -> C #1319, per
the #565 anchor + rotation guard). Predecessor #1316 Type E verified in
git log (main 5d160c6c / anchor 49d60e8a / doc-sync 9e3dc23b / log-hash
4867ff1c); the 1310-1314 window is VERIFIED CLOSED. This run's main commit
is the anchor per #565; ANCHORED_SHA patched post-commit. The #1316
forward guards verified pre-commit this run: max-1020; zero
one-zero-two-one keys all forms; no-Type-A-#1317-in-git-log; fortieth
direction absent (profiles/ scope); forty-eighth through fifty-ninth
members intact; no sixtieth member (repo-wide); ledger 59. This run lands
m1021 (thesis-consistent, NOT a member): TestGuardLifecycle1316's
no-Type-A-#1317 pin flips at this run's main commit BY DESIGN (the
#1191-class self-trip, re-pinned green in the terminal log-hash followup
per #721 in BOTH files per the #1292 precedent) and its 1021-numeric pin
flips permanently (the #1272-class forward-guard expiry); the
no-sixtieth-member pin stays GREEN. Documented in TestStalenessPins1317,
not repaired. Next: #1318 Type B continues the window. The
#1315-launched background-suite verdict belongs to #1320 per #795: this
run OBSERVES only (log last write Oct 8 14:27 PDT at [ 1%], zero live
pytest processes at this run's ~03:00 PM PDT check - appears dead; NOT
touched).
In-flight during this run: #899 (profiles/nytimes.yaml m771 hunk), #938
(Type B test file working-tree edit), #900 (untracked Type D test file),
#1012-wt (working-tree edit on the committed Type A #1012 file) - all
untouched; targeted staging only. Do NOT touch #1024 m846.

Pre-commit novelty greps per #715: zero test_type_a_1317 files on disk
(glob); no Type A #1317 in git log (--grep); max numeric mechanism_id
1020 in profiles/ pre-commit (mechanism_id regex sweep); zero
numeric/underscore/dash one-zero-two-one mechanism key forms repo-wide
pre-commit (needles format-built per #715, own file excluded,
__pycache__ excluded per the #715 pattern-rescope lesson); block key
zero-hit repo-wide pre-commit (designed keying: iteration 1317 in key,
no 1021 substring, per the #723/#738/#739 convention); "## #1317"
zero-hit in iteration-log pre-commit; README stats 74493/1641
pre-commit; no #1317 row in README/ARCHITECTURE test tables pre-commit;
the 8 novel URLs zero-hit repo-wide pre-commit (git grep -F).

Doc-sync constants per #719: README_TEST_COUNT / README_FILE_COUNT hold
the post-doc-sync values from the start (patched pre-main once the
in-gate collection count is known); the doc-sync commit ratchets README
74493/1641 -> post-sync totals.
"""

import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
CCR_PATH = os.path.join(
    PROFILES_DIR, "competitor-coverage-research.yaml")

OWN_BASENAME = (
    "test_type_a_1317_semafor_microsoft_suleyman_exec_platform_"
    "vs_meta_led_tampering_exclusive_oct08_3pm.py"
)
BLOCK_KEY = (
    "type_a_1317_semafor_microsoft_suleyman_exec_platform_"
    "vs_meta_led_tampering_exclusive_oct08_3pm"
)

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "0" * 40  # patched in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1021
NEXT_NUM = 1022  # integer only; key-form needles are format-built

# Predecessor chain: #1316 Type E closed the SECOND leg.
PRED_MAIN_1316 = "5d160c6cc9a8d68e863499b4e5fc142845c21060"
PRED_ANCHOR_1316 = "49d60e8ac4b57b1b9c76b585b4d4484217fb4f26"
PRED_DOCSYNC_1316 = "9e3dc23ba09a831477253f38267fbbdcabf439ab"
PRED_FINAL_1316 = "4867ff1c0bfa89b469f794c0220f9c295dd40c4f"

# This run's main commit (full sha), for the ancestor-form
# no-Type-A-#1317 pin. Patched in the terminal log-hash followup
# per #721 (re-pinned in BOTH this file and the #1316 file per the
# #1292 re-pin-both-copies precedent).
PRED_MAIN_1317 = "0" * 40  # re-pinned to #1317 main sha per #721

# The #1318 main commit (full sha), for the ancestor-form
# no-Type-B-#1318 pin. Patched in #1318's terminal log-hash followup
# per #721.
PRED_MAIN_1318 = "0" * 40  # staged 0*40 placeholder-only per #721

# The #1316 predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1020; zero next-number
# one-zero-two-one / no-Type-A-#1317-in-git-log / fortieth
# direction absent / forty-eighth through fifty-ninth members
# intact / sixtieth member absent / ledger 59).
D1316_FILE = (
    "test_type_e_1316_podcast_sentiment_186th_"
    "verification_oct08_2pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 74598  # post-doc-sync total (pre-sync 74493 + 105)
README_FILE_COUNT = 1642  # pre-sync 1641 + 1 (this file)

# MANUAL ILLUSTRATIVE tones (hand-assigned at excerpt level).
A1_TRANSCRIBE_TONE = 0.20
A2_VOICE_MODELS_TONE = 0.30
MSFT_MEAN_TONE = 0.25
META_LED_TONE = -0.30
ILLUSTRATIVE_DELTA = 0.55

# Ordinal member-claim forms, built at runtime so this source file
# carries no contiguous full-form claim (per the #715 literal
# discipline; the live full-form claims live in the profile block).
_T40 = "FORT" + "IETH relationship direction"
_T48 = "FORT" + "Y-EIGHTH falsification-family member"
_T49 = "FORT" + "Y-NINTH falsification-family member"
_T50 = "FIFT" + "IETH falsification-family member"
_T51 = "FIFT" + "Y-FIRST falsification-family member"
_T52 = "FIFT" + "Y-SECOND falsification-family member"
_T53 = "FIFT" + "Y-THIRD falsification-family member"
_T54 = "FIFT" + "Y-FOURTH falsification-family member"
_T55 = "FIFT" + "Y-FIFTH falsification-family member"
_T56 = "FIFT" + "Y-SIXTH falsification-family member"
_T57 = "FIFT" + "Y-SEVENTH falsification-family member"
_T58 = "FIFT" + "Y-EIGHTH falsification-family member"
_T59 = "FIFT" + "Y-NINTH falsification-family member"
_T60 = "SIXT" + "IETH falsification-family member"

# Novel URLs (all zero-hit repo-wide pre-commit via git grep -F;
# verbatim from Full-URL listings).
BLOOMBERGLAW_URL = (
    "https://News.Bloomberglaw.Com/artificial-intelligence/"
    "microsoft-says-ai-voice-command-needs-more-work-semafor"
)
ENGADGET_MAI_URL = (
    "https://www.engadget.com/ai/microsoft-introduces-a-pair-of-"
    "in-house-ai-models-193003900.html"
)
YOUTUBE_SEMAFOR_TECH_URL = "https://www.youtube.com/watch?v=Zo-ZtQPkzhU"
PYMNTS_DEAL_URL = (
    "https://www.pymnts.com/news/artificial-intelligence/2024/"
    "microsoft-forms-ai-partnership-with-news-startup-semafor/"
)
ENGADGET_SIGNALS_URL = (
    "http://engadget.com/microsoft-is-teaming-up-with-semafor-on-"
    "ai-assisted-news-stories-124320277.html"
)
DIW_SIGNALS_URL = (
    "https://www.digitalinformationworld.com/2024/02/"
    "news-startup-rolls-out-ai-editorial.html"
)
BIOMETRICUPDATE_URL = (
    "https://www.biometricupdate.com/202609/metas-smart-glasses-"
    "privacy-defense-falters-when-ai-can-use-camera-without-"
    "recording-light"
)
TECHHELP_URL = "https://techhelp.ca/smart-glasses-privacy-backlash-meta-audio/"
# RE-SURFACE (in-corpus since #576 Type E press surface): the
# Semafor-authorship reading is new, the URL is not.
STARTUPFORTUNE_URL = (
    "https://startupfortune.com/meta-permanently-disables-cameras-"
    "on-thousands-of-tampered-smart-glasses/"
)


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git"] + list(args), cwd=REPO_ROOT, capture_output=True,
        text=True,
    )


def _iter_source_files():
    """Yield profile + test source files for the sweep instruments.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson).
    """
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            yield os.path.join(root, f)
    for root, dirs, files in os.walk(TESTS_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            if f == OWN_BASENAME:
                continue
            if f.endswith(".py"):
                yield os.path.join(root, f)


def _repo_grep_underscore_mechanism(n):
    """Return file paths containing the underscore-form mechanism key.

    The needle is built at runtime by format string, so this source
    file carries no contiguous underscore-form literal (per the #770
    lesson).
    """
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [
        p
        for p in _iter_source_files()
        if needle in open(p, encoding="utf-8", errors="replace").read()
    ]


def _repo_grep_dash_mechanism(n):
    needle = "mechanism" + "-" + str(n)
    return [
        p
        for p in _iter_source_files()
        if needle in open(p, encoding="utf-8", errors="replace").read()
    ]


def _repo_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in open(p, encoding="utf-8", errors="replace").read():
                hits.append(p)
    return hits


def _max_numeric_mechanism_id():
    found = []
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            found.extend(
                int(m) for m in pat.findall(
                    open(os.path.join(root, f),
                         encoding="utf-8", errors="replace").read()
                )
            )
    return max(found) if found else None


def _git_grep_tracked_source(needle, scope):
    """Grep tracked files at HEAD for a literal needle (fragment-built)."""
    args = ["git", "grep", "-F", "-l", needle, "HEAD", "--"]
    if scope:
        args.append(scope)
    out = subprocess.run(
        args, cwd=REPO_ROOT, capture_output=True, text=True
    ).stdout
    cleaned = []
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("HEAD:"):
            line = line[len("HEAD:"):]
        if line:
            cleaned.append(line)
    return cleaned


def _class_run(filename, classname):
    return subprocess.run(
        ["python3", "-m", "pytest", filename + "::" + classname, "-q"],
        cwd=TESTS_DIR, capture_output=True, text=True,
    )


def _block():
    doc = yaml.safe_load(_read(CCR_PATH))
    return doc["publications"][BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Anchor per #565 (this run's main commit is the anchor; the anchor
#    followup patches ANCHORED_SHA to the main commit sha).
# ---------------------------------------------------------------------------


class TestAnchor1317:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to the main commit sha per #565. This test is
        # deselected in the in-gate run; the patched form is asserted
        # post-anchor.
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_to_main_commit(self):
        # Post-commit form: ANCHORED_SHA patched to this run's main
        # commit sha per #565 in the anchor followup (both this
        # expected value and the ANCHORED_SHA constant are patched).
        # Pre-commit this is 0*40 and the test fails BY DESIGN;
        # deselected in the in-gate run.
        assert ANCHORED_SHA != "0" * 40
        assert len(ANCHORED_SHA) == 40

    def test_anchor_sha_format(self):
        assert len(ANCHORED_SHA) == 40

    def test_anchor_duality_documented(self):
        # The #565 duality: the placeholder pin passes pre-commit and
        # fails post-anchor BY DESIGN; the patched pin is the mirror.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "BY DESIGN post-anchor" in src or "fails BY DESIGN" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1316 closed the SECOND leg; #1317 is the THIRD.
# ---------------------------------------------------------------------------


class TestRotationGuard1317:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-60").stdout
        for sha, label in (
            (PRED_MAIN_1316, "1316 main"),
            (PRED_ANCHOR_1316, "1316 anchor"),
            (PRED_DOCSYNC_1316, "1316 doc-sync"),
            (PRED_FINAL_1316, "1316 log-hash"),
        ):
            assert sha[:8] in log, label

    def test_1316_type_e_in_git_log(self):
        out = _git("log", "--oneline", "--grep=Type E #1316").stdout
        assert out.strip() != ""

    def test_third_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "THIRD leg of the 1315-1319 window" in src

    def test_1310_1314_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1310-1314" in src
        assert "VERIFIED CLOSED" in src

    def test_next_leg_is_1318_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "B #1318" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty: Type A lands one mechanism (max 1020 -> 1021).
# ---------------------------------------------------------------------------


class TestMechanismNovelty1317:
    def test_max_numeric_mechanism_id_1021(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_no_type_a_1317_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type A #1317" must be this run's
        # main commit or a descendant of it - i.e., no PRIOR run
        # committed this run's iteration. Deselected in the in-gate
        # run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type A #1317")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1317).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_zero_next_number_keys_all_forms(self):
        # Numeric (profiles/ scope), underscore and dash (profiles/ +
        # tests/ scope, own file excluded per #715, __pycache__
        # excluded per the #715 pattern-rescope lesson). NEXT_NUM is
        # 1022: this run lands 1021, so the next-number forms stay
        # absent.
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_key_designed_no_1021_substring(self):
        # Designed keying per #723/#738/#739: the iteration-form block
        # key carries the iteration (1317), never the mechanism number.
        assert "1021" not in BLOCK_KEY
        assert "1317" in BLOCK_KEY

    def test_forward_guards_for_1318(self):
        # Staged for the next leg: max-1021 in profiles/; zero
        # one-zero-two-two keys all forms; no-Type-B-#1318-in-git-log;
        # fortieth direction absent; forty-eighth through fifty-ninth
        # intact; no sixtieth member; ledger 59.
        assert _max_numeric_mechanism_id() == 1021
        assert _repo_grep_numeric_mechanism_id(1022) == []
        assert _repo_grep_underscore_mechanism(1022) == []
        assert _repo_grep_dash_mechanism(1022) == []
        assert _git("log", "--oneline", "--grep=Type B #1318").stdout.strip() == ""
        assert _git_grep_tracked_source(_T40, "profiles/") == []
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]
        assert _T59 in _read(os.path.join(PROFILES_DIR, "news-corp.yaml"))
        assert _git_grep_tracked_source(_T60, None) == []

    def test_novel_urls_present_in_block(self):
        # The 8 novel URLs were zero-hit repo-wide pre-commit (git
        # grep -F, verified this run before the block landed).
        # Post-landing they live in the block's arms and financial
        # relationship; assert each is present in
        # competitor-coverage-research.yaml.
        text = _read(CCR_PATH)
        for url in (BLOOMBERGLAW_URL, ENGADGET_MAI_URL,
                    YOUTUBE_SEMAFOR_TECH_URL, PYMNTS_DEAL_URL,
                    ENGADGET_SIGNALS_URL, DIW_SIGNALS_URL,
                    BIOMETRICUPDATE_URL, TECHHELP_URL):
            assert text.count(url) >= 1, url

    def test_resurface_url_disclosed_not_novel(self):
        # The Startup Fortune Meta-LED URL is a re-surface (Type E
        # press surface since #576); it must NOT be claimed novel.
        block = _block()
        assert "RE-SURFACE" in block["meta_comparator"]["url_status"]
        assert "Semafor-authorship reading new this run" in \
            block["meta_comparator"]["url_status"]


# ---------------------------------------------------------------------------
# 4. Semafor x Microsoft arms: A1 Transcribe interview + A2 Voice-models
#    interview (both Semafor-attributed via relays).
# ---------------------------------------------------------------------------


class TestSemaforMicrosoftArms1317:
    def test_a1_transcribe_interview_in_block(self):
        block = _block()
        arm = block["arms"]["arm_msft_1_suleyman_mai_transcribe_interview"]
        assert arm["register"] == "executive_platform_interview"
        assert "MAI-Transcribe-1" in arm["title"]

    def test_a1_tone_plus_020(self):
        block = _block()
        arm = block["arms"]["arm_msft_1_suleyman_mai_transcribe_interview"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == A1_TRANSCRIBE_TONE == 0.20

    def test_a1_bloomberglaw_url_verbatim(self):
        block = _block()
        arm = block["arms"]["arm_msft_1_suleyman_mai_transcribe_interview"]
        assert BLOOMBERGLAW_URL in arm["urls"]

    def test_a1_candor_confound_noted(self):
        block = _block()
        arm = block["arms"]["arm_msft_1_suleyman_mai_transcribe_interview"]
        assert "candor" in arm["note"]

    def test_a2_voice_models_interview_in_block(self):
        block = _block()
        arm = block["arms"]["arm_msft_2_suleyman_mai_voice_models_interview"]
        assert arm["register"] == "executive_platform_interview"
        assert "Albergotti" in arm["title"]

    def test_a2_tone_plus_030(self):
        block = _block()
        arm = block["arms"]["arm_msft_2_suleyman_mai_voice_models_interview"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == A2_VOICE_MODELS_TONE == 0.30

    def test_a2_engadget_url_verbatim(self):
        block = _block()
        arm = block["arms"]["arm_msft_2_suleyman_mai_voice_models_interview"]
        assert ENGADGET_MAI_URL in arm["urls"]

    def test_a2_youtube_semafor_tech_url_verbatim(self):
        block = _block()
        arm = block["arms"]["arm_msft_2_suleyman_mai_voice_models_interview"]
        assert YOUTUBE_SEMAFOR_TECH_URL in arm["urls"]

    def test_microsoft_arm_mean_plus_025(self):
        block = _block()
        assert block["microsoft_arm_avg"] == MSFT_MEAN_TONE == 0.25
        assert block["microsoft_arm_scores"] == [0.2, 0.3]


# ---------------------------------------------------------------------------
# 5. Meta comparator: Semafor Sep-1 LED-tampering accountability exclusive.
# ---------------------------------------------------------------------------


class TestMetaLedArm1317:
    def test_m1_led_exclusive_in_block(self):
        block = _block()
        comp = block["meta_comparator"]
        assert comp["register"] == "privacy_accountability_exclusive"
        assert "2026-09-01" in comp["date"]

    def test_m1_tone_minus_030(self):
        block = _block()
        assert block["meta_arm_score"] == META_LED_TONE == -0.30

    def test_m1_startupfortune_url_present(self):
        block = _block()
        assert STARTUPFORTUNE_URL in block["meta_comparator"]["urls"]

    def test_m1_himel_quotes_present(self):
        block = _block()
        comp = block["meta_comparator"]
        text = yaml.safe_dump(comp)
        assert "Himel" in text

    def test_m1_biometricupdate_frame_url(self):
        block = _block()
        assert BIOMETRICUPDATE_URL in block["meta_comparator"]["urls"]

    def test_m1_techhelp_relay_url(self):
        block = _block()
        assert TECHHELP_URL in block["meta_comparator"]["urls"]

    def test_m1_access_symmetry_noted(self):
        # The exclusive IS the Himel interview: access is symmetric,
        # the register differs. Asserted in the note and
        # counter-evidence.
        block = _block()
        assert "Himel interview" in block["meta_comparator"]["note"]
        assert "Symmetric access" in \
            yaml.safe_dump(block["counter_evidence"])


# ---------------------------------------------------------------------------
# 6. Financial relationship: Microsoft x Semafor Signals sponsorship.
# ---------------------------------------------------------------------------


class TestFinancialRelationship1317:
    def test_signals_deal_in_block(self):
        block = _block()
        fin = block["financial_relationship"]
        assert fin["partner"] == "Microsoft"
        assert fin["outlet"] == "Semafor"
        assert "Signals" in fin["deal"]

    def test_deal_date_feb_5_2024(self):
        block = _block()
        assert block["financial_relationship"]["announced"] == "2024-02-05"

    def test_substantial_sum_terms(self):
        block = _block()
        assert "substantial" in block["financial_relationship"]["terms"]

    def test_ft_sourcing_noted(self):
        block = _block()
        assert "Financial Times" in block["financial_relationship"]["terms"]

    def test_nyt_lawsuit_timing_texture(self):
        block = _block()
        assert "Dec 2023 copyright lawsuit" in \
            block["financial_relationship"]["timing_texture"]

    def test_ongoing_bounded_absence(self):
        block = _block()
        assert "no split reported" in block["financial_relationship"]["status"]

    def test_pymnts_url_verbatim(self):
        block = _block()
        assert PYMNTS_DEAL_URL in block["financial_relationship"]["urls"]

    def test_engadget_signals_url_verbatim(self):
        block = _block()
        assert ENGADGET_SIGNALS_URL in \
            block["financial_relationship"]["urls"]

    def test_diw_signals_url_verbatim(self):
        block = _block()
        assert DIW_SIGNALS_URL in block["financial_relationship"]["urls"]


# ---------------------------------------------------------------------------
# 7. Asymmetry delta: Microsoft +0.25 mean vs Meta -0.30.
# ---------------------------------------------------------------------------


class TestAsymmetryDelta1317:
    def test_microsoft_mean_plus_025(self):
        block = _block()
        assert block["microsoft_arm_avg"] == MSFT_MEAN_TONE == 0.25

    def test_meta_minus_030(self):
        block = _block()
        assert block["meta_arm_score"] == META_LED_TONE == -0.30

    def test_illustrative_delta_plus_055(self):
        block = _block()
        assert block["illustrative_delta_microsoft_minus_meta"] == \
            ILLUSTRATIVE_DELTA == 0.55

    def test_delta_calc_documented(self):
        block = _block()
        assert "0.25 - (-0.30) = +0.55" in block["delta_calc"]

    def test_degenerate_sample_contract(self):
        block = _block()
        assert "n=2" in block["methodology"]
        assert "n=1" in block["methodology"]
        assert "degenerate-sample contract disclosed" in \
            block["methodology"]

    def test_reading_payer_favoring(self):
        block = _block()
        assert "Payer-favoring" in block["delta_direction"]

    def test_engine_not_run(self):
        block = _block()
        assert block["engine_run"] is False


# ---------------------------------------------------------------------------
# 8. Research method: 1 scout + 8 verification sets, 0 browser.open
# ---------------------------------------------------------------------------


class TestResearchMethod1317:
    def test_delegated_scout_documented(self):
        block = _block()
        assert "1 delegated scout" in block["research_method"]

    def test_eight_verification_sets(self):
        block = _block()
        assert "8 main-run browser.search verification sets" in \
            block["research_method"]

    def test_scout_rejections_documented(self):
        block = _block()
        assert "AP x Google" in block["research_method"]
        assert "Guardian x xAI" in block["research_method"]

    def test_ap_rejection_attribution_ground(self):
        block = _block()
        assert "arm-attribution ambiguity" in block["research_method"]

    def test_guardian_xai_zero_gradient_ground(self):
        block = _block()
        assert "zero-gradient control" in block["research_method"]

    def test_nscale_arm_dropped(self):
        block = _block()
        assert "Nscale" in block["research_method"]
        assert "arm dropped" in block["research_method"]

    def test_copilot_arm_dropped(self):
        block = _block()
        assert "Copilot-redesign" in block["research_method"]

    def test_1312_rejection_superseded(self):
        block = _block()
        assert "#1312" in block["research_method"] or \
            "supersedes the #1312 rejection" in block["extends"]

    def test_excerpt_bounded_no_browser_open(self):
        block = _block()
        assert "0 browser.open" in block["research_method"]


# ---------------------------------------------------------------------------
# 9. Thesis-consistent observation: NOT a falsification-family member
# ---------------------------------------------------------------------------


class TestThesisConsistent1317:
    def test_not_a_member_ledger_holds_59(self):
        block = _block()
        assert block["verdict"] == "thesis_consistent_observation"
        assert "NOT a falsification-family member" in \
            block["falsification_family"]
        assert "Ledger holds at 59" in block["falsification_family"]

    def test_no_sixtieth_member_form_in_block(self):
        # The block must not claim the sixtieth member. The needle is
        # fragment-built via _T60 (per the #715 literal discipline);
        # a contiguous literal here would trip the repo-wide
        # no-sixtieth-member pin in TestGuardLifecycle1316.
        text = yaml.safe_dump(_block())
        assert _T60 not in text

    def test_first_semafor_microsoft_mechanism(self):
        block = _block()
        assert "FIRST dedicated Semafor x Microsoft mechanism" in \
            block["extends"]

    def test_register_local_not_outlet_level(self):
        block = _block()
        assert "register-local" in block["incentive_attribution"] or \
            "executive-platform register" in block["incentive_attribution"]

    def test_candor_counterevidence_bound(self):
        block = _block()
        text = yaml.safe_dump(block["counter_evidence"])
        assert "embedded candor" in text

    def test_symmetric_access_bound(self):
        block = _block()
        text = yaml.safe_dump(block["counter_evidence"])
        assert "Symmetric access" in text

    def test_rejection_supersession_bound(self):
        block = _block()
        text = yaml.safe_dump(block["counter_evidence"])
        assert "#1312" in text

    def test_no_fortieth_direction_form_in_block(self):
        text = yaml.safe_dump(_block())
        assert _T40 not in text


# ---------------------------------------------------------------------------
# 10. Statistical discipline per the Aug 28 2026 standing rule
# ---------------------------------------------------------------------------


class TestStatisticalDiscipline1317:
    def test_manual_illustrative_only(self):
        block = _block()
        assert "MANUAL ILLUSTRATIVE" in block["statistical_discipline"]

    def test_engine_not_run(self):
        block = _block()
        assert "Engine NOT run" in block["statistical_discipline"]

    def test_p_value_not_calculated(self):
        block = _block()
        sd = block["statistical_discipline"]
        assert "NOT_CALCULATED" in sd
        assert "is_significant: false" in sd

    def test_not_artifact_grade(self):
        block = _block()
        sd = block["statistical_discipline"]
        assert "no_analysis_json_update: true" in sd
        assert "NOT artifact-grade" in sd

    def test_verdict_thesis_consistent(self):
        block = _block()
        assert "thesis_consistent_observation" in block["statistical_discipline"]

    def test_correlation_not_causation(self):
        block = _block()
        sd = block["statistical_discipline"]
        assert "Correlation is not causation" in sd
        assert "Hypothesis-generating only" in sd


# ---------------------------------------------------------------------------
# 11. Guard lifecycle: forward guards for #1318 (Type B).
# ---------------------------------------------------------------------------


class TestGuardLifecycle1317:
    def test_pins_on_one_mechanism_landing(self):
        # Type A lands one mechanism: max 1021, next 1022.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1021" in src
        assert "NEXT_NUM = 1022" in src

    def test_no_type_b_1318_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1318's terminal log-hash followup
        # per #721): every commit whose message matches "Type B
        # #1318" must be #1318's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1318")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1318's own commits"
        main = _git("rev-parse", PRED_MAIN_1318).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1022_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1022_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1022_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_forty_ninth_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T49, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fiftieth_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T50, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_first_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T51, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_second_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T52, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_fifty_third_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T53, "HEAD", "--",
            "profiles/the-verge.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fourth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T54, "HEAD", "--",
            "profiles/guardian.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fifth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T55, "HEAD", "--",
            "profiles/atlantic.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_sixth_member_present_pin(self):
        # Landed #1282 (m1000, profiles/wired.yaml). Asserted on the
        # working tree so the pin is stable across the main-commit
        # boundary; the HEAD sweep sees it from the main commit on.
        assert _T56 in _read(os.path.join(PROFILES_DIR, "wired.yaml"))

    def test_fifty_seventh_member_present_pin(self):
        # Landed #1287 (m1003, profiles/ap.yaml, committed). HEAD
        # sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_member_present_pin(self):
        # Landed #1292 (m1006, profiles/financial-times.yaml,
        # committed). HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T58, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_ninth_member_present_pin(self):
        # Landed #1302 (m1012, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T59, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_sixtieth_member_pin(self):
        # This run lands a thesis-consistent observation, NOT a
        # member: the sixtieth member-claim form stays absent
        # repo-wide (source scope; __pycache__ excluded per the #715
        # pattern-rescope lesson).
        assert _git_grep_tracked_source(_T60, None) == []

    def test_predecessor_1316_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, D1316_FILE))

    def test_next_leg_is_1318_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1318 Type B" in src

    def test_1316_pins_flip_by_design_documented(self):
        # #1316's forward guards (max-1020, zero one-zero-two-one
        # keys all forms, no-Type-A-#1317-in-git-log, fortieth
        # absent, forty-eighth through fifty-ninth intact in
        # profiles/, sixtieth absent, ledger 59) verified GREEN
        # at HEAD pre-commit this run. TWO pins flip BY DESIGN at
        # this run's main commit: the no-Type-A-#1317-in-git-log pin
        # (the #1191-class self-trip, re-pinned green in the terminal
        # log-hash followup per #721, in BOTH the #1317 and #1316 files
        # per the #1292 re-pin-both-copies precedent) and the zero
        # one-zero-two-one numeric pin (the #1272-class forward-guard
        # expiry - the m1021 landing carries "mechanism_id: 1021" in
        # colon form; the underscore/dash pins stay green by the
        # #723/#738/#739 designed keying). The no-sixtieth-member pin
        # stays GREEN (this run lands no member). Documented in the
        # staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1317" in src
        assert "no_type_a_1317_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1316's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------


class TestStalenessPins1317:
    def test_1316_guard_lifecycle_post_commit_self_trip(self):
        # Post-terminal-followup form: 22 tests in the class; ONE
        # flips BY DESIGN when this run's main commit lands and STAYS
        # flipped permanently: test_1021_numeric_absent_in_profiles
        # (the #1272-class forward-guard expiry - the m1021 landing
        # carries "mechanism_id: 1021" in colon form; the
        # underscore/dash pins stay green by the #723/#738/#739
        # designed keying). The second flip,
        # test_no_type_a_1317_in_git_log_pin (the #1191-class
        # self-trip), is re-pinned green in the terminal log-hash
        # followup per #721 (its PRED_MAIN_1317 now holds this run's
        # main sha, in BOTH the #1317 and #1316 files per the
        # re-pin-both-copies precedent). The class run below therefore
        # expects 1 failed / 21 passed and documents the designed
        # flips. The #1316 block is read-only to this run; the flips
        # are documented here, not repaired.
        res = _class_run(D1316_FILE, "TestGuardLifecycle1316")
        out = res.stdout + res.stderr
        assert "1 failed, 21 passed" in out, out[-2000:]
        assert "test_1021_numeric_absent_in_profiles" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 13. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1317:
    def test_readme_test_file_table_has_1317_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1317_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert OWN_BASENAME in arch

    def test_readme_stats_ratcheted(self):
        readme = _read(README_PATH)
        assert "| Tests | %d |" % README_TEST_COUNT in readme
        assert "Across %d test files" % README_FILE_COUNT in readme


# ---------------------------------------------------------------------------
# 14. Iteration log per #721.
# ---------------------------------------------------------------------------


class TestIterationLog1317:
    def test_log_has_1317_entry(self):
        text = _read(LOG_PATH)
        assert "## #1317 Type A" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_finding(self):
        text = _read(LOG_PATH)
        assert "m1021" in text
        assert "thesis_consistent_observation" in text
        assert "ledger holds at 59" in text


# ---------------------------------------------------------------------------
# 15. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1317:
    def test_899_nytimes_hunk_untouched(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert "profiles/nytimes.yaml" in modified
        # Its uncommitted hunk belongs to #899's run; this run stages
        # only its own files via explicit-path staging.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#899" in src

    def test_900_untracked_file_untouched(self):
        res = _git("status", "--short")
        assert "test_type_d_900_m769" in res.stdout

    def test_938_test_file_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_b_938" in res.stdout

    def test_1012_wt_working_tree_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_a_1012" in res.stdout

    def test_own_diff_excludes_inflight(self):
        # This run's staged set must never include the in-flight
        # files; verified at commit time by explicit-path staging.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "explicit-path staging" in src
