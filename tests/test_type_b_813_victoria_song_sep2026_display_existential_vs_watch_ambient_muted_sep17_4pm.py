"""Type B iteration #813 (Sep 17 2026, 4pm PDT): Victoria Song same-register
Sep 2026 pair (mechanism 719), the fourth leg of the 810-814 window.

D #810 -> E #811 -> A #812 -> B #813 -> C (#814 to follow).

Follows the #808 single-file structural pattern (novelty anchor, rotation guard,
corpus/post-#812 supersession tests, ledger constancy, careers, doc-sync rows,
iteration-log entry).

Deselected pre-commit per the #565 convention: anchor 1.
Doc-sync 2 + iteration-log 2 go green in the doc-sync followup.
Patched green in the anchor followup.

FINDING: Victoria Song (The Verge, senior reviewer, wearables desk) Sep 2026
same-register pair EXTENDS mechanism 605 (#618, register-conditioned model)
and NARROWS its product-register fairness claim. Meta arm: her own Optimizer
newsletter reflecting on her Meta Ray-Ban Display review (read first-hand this
run, 110 rendered lines, internewscast mirror, byline Victoria Song / The
Verge): "my recently published Meta Ray-Ban Display review and the minor
existential crisis it had sparked"; "these glasses were a marvel of modern
technology. Yet, they posed significant privacy and cultural questions, which
left me torn"; "glasshole behavior I fretted about in my review"; "Commuting
to The Verge office, I feel creepy recording video or taking photos" (-0.10
illustrative). Apple arm: The Verge "Faster health tracking collides with
unfinished AI" (Sep 17 2026, Apple Watch Series 12 review; byline attributed
Victoria Song via the appleinsider Sep 17 roundup, read first-hand this run,
97 rendered lines; 90/100 via TechSpot aggregation, "the best Apple Watch
yet"; praised faster charging and one-handed gestures, heart-rate close to a
Polar H10; several major health and Audio Intelligence features unavailable
during review; privacy concerns on ambient listening "may persist despite
Apple's safeguards"; excerpt-bounded per #503) (+0.30 illustrative).
Illustrative Meta-minus-Apple delta -0.40: the privacy register BLEEDS into
her Meta product coverage while staying muted in her Apple product coverage of
a device shipping always-on ambient-audio features (Siri Recap summarizes your
conversations; Live Rewind rewinds nearby speech) - one contained caveat inside
a 90/100 review. Strong confounders ranked first: genre asymmetry (confessional
newsletter reflection vs embargo-week review), privacy-vector asymmetry
(third-party camera exposure vs first-party wrist ambience - domain-justified),
review-cycle asymmetry (months of lived use vs launch-week beta features).
Counter-evidence: her Sep 2025 Display hands-on "best glasses I have ever
tried", Feb 2024 "Meta approach may be BETTER than Apple's", she DID flag
Apple Audio Intelligence privacy concerns, #599's writer-level money-gradient
falsification, #723's Engadget control replication on the same ambient-listening
topic. Verdict refines #618 from "fair in product register" to "fair in product
register except where the product itself is a face-worn camera, where the
privacy register activates." MANUAL ILLUSTRATIVE only; NOT a
falsification-family member; ledger holds at 26.
"""
import glob
import os
import re
import subprocess
import pytest
import yaml

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = "test_type_b_813_victoria_song_sep2026_display_existential_vs_watch_ambient_muted_sep17_4pm.py"
MECH_KEY = "victoria song sep2026 display existential vs watch ambient muted"
M_ID = 719
MECH_ID_MARKER = "mechanism" + "_719"
NEXT_ID_MARKER = "mechanism" + "_720"
NEXT_ID_NUMERIC = "mechanism_id: 720"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # patched post-commit per #565
BLOCK_KEY = "type_b_813_victoria_song_sep2026_display_existential_vs_watch_ambient_muted_sep17"

CAREERS_PROFILE = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
ITERATION_LOG = os.path.join(REPO, "iteration-log.md")


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO] + list(args),
        capture_output=True,
        text=True,
        check=False,
    )


def _careers_text():
    with open(CAREERS_PROFILE) as fh:
        return fh.read()


def _song():
    with open(CAREERS_PROFILE) as fh:
        doc = yaml.safe_load(fh)
    hits = [j for j in doc["journalists"] if j.get("name") == "Victoria Song"]
    assert len(hits) == 1
    return hits[0]


def _block():
    return _song()["competitor_coverage"][BLOCK_KEY]


# --- Novelty ---------------------------------------------------------------


class TestNovelty813:
    def test_type_b_813_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type B #813")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_no_type_b_813_file_on_disk_pre_commit(self):
        hits = [p for p in glob.glob(os.path.join(REPO, "tests", "test_type_b_813*"))
                if os.path.basename(p) != TEST_BASENAME]
        assert not hits, f"unexpected pre-existing Type B #813 test files: {hits}"

    def test_watch_review_title_zero_hit_repo_wide_pre_commit(self):
        # Against HEAD (the committed, pre-#813 tree), not the working tree:
        # the profile edits are intentional post-commit additions.
        res = _run_git("grep", "-ci", "faster health tracking collides", "HEAD",
                       "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and (not res.stdout.strip() or res.stdout.strip() == ""), \
            f"Watch review title already referenced pre-commit: {res.stdout}"

    def test_block_key_zero_hit_repo_wide_pre_commit(self):
        res = _run_git("grep", "-c", BLOCK_KEY, "HEAD", "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and (not res.stdout.strip() or res.stdout.strip() in ("", "0")), \
            f"block key already referenced pre-commit: {res.stdout}"


# --- Rotation guard --------------------------------------------------------


ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
EXPECTED_ORDER = [
    ("B", "813"), ("A", "812"), ("E", "811"), ("D", "810"), ("C", "809"),
]
WINDOW_SEQ = "D (#810) -> E (#811) -> A (#812) -> B (#813) -> C (#814)"


class TestRotationCycleGuard813:
    def test_iteration_sequence_is_809_through_813(self):
        assert EXPECTED_ORDER == [
            ("B", "813"), ("A", "812"), ("E", "811"), ("D", "810"), ("C", "809"),
        ]

    def test_rotation_legs_adjacency(self):
        for (t1, n1), (t2, n2) in zip(EXPECTED_ORDER, EXPECTED_ORDER[1:]):
            assert int(n1) == int(n2) + 1
            assert (ORDER[t1] - ORDER[t2]) % 5 == 1

    def test_type_b_813_position_is_fourth_leg_of_810_814_window(self):
        assert EXPECTED_ORDER[0] == ("B", "813")

    def test_predecessor_is_type_a_812(self):
        assert EXPECTED_ORDER[1] == ("A", "812")


# --- Mechanism 719 content -------------------------------------------------


class TestMechanism719Content:
    def test_block_parses_under_song_competitor_coverage(self):
        song = _song()
        assert BLOCK_KEY in song["competitor_coverage"]
        assert song["competitor_coverage"][BLOCK_KEY]["mechanism_id"] == M_ID

    def test_block_key_unique(self):
        field = "      block_key: 'type_b_813_victoria_song_sep2026_display_existential_vs_watch_ambient_muted_sep17'\n"
        assert _careers_text().count(field) == 1

    def test_block_719_identity_fields(self):
        b = _block()
        assert b["mechanism_id"] == M_ID
        assert b["iteration"] == 813
        assert b["type"] == "B"
        assert b["date"] == "2026-09-17 16:00 PDT"
        assert b["test_file"] == "tests/" + TEST_BASENAME

    def test_meta_arm_fields(self):
        b = _block()
        meta = b["meta_arm"]
        assert meta["author_byline"] == "Victoria Song"
        assert meta["date"] == "2026-09"
        assert meta["tone_MANUAL_ILLUSTRATIVE"] == -0.10
        assert meta["url"] == "https://internewscast.com/tech/exploring-renaissance-art-with-meta-ray-ban-a-unique-journey-through-romes-masterpieces/"
        quotes = " ".join(meta["key_quotes"])
        assert "minor existential crisis" in quotes
        assert "marvel of modern technology" in quotes
        assert "glasshole behavior" in quotes
        assert "feel creepy" in quotes

    def test_apple_arm_fields(self):
        b = _block()
        apple = b["apple_arm"]
        assert apple["title"] == "Faster health tracking collides with unfinished AI"
        assert apple["date"] == "2026-09-17"
        assert apple["tone_MANUAL_ILLUSTRATIVE"] == 0.30
        assert apple["url"] == "https://appleinsider.com/articles/26/09/17/apple-watch-series-12-and-apple-watch-ultra-4-reviewers-praise-health-upgrades"
        quotes = " ".join(apple["key_quotes"])
        assert "close to a Polar H10" in quotes
        assert "best Apple Watch yet" in quotes
        assert "safeguards for ambient listening" in quotes

    def test_spread_delta_calc(self):
        b = _block()
        assert b["illustrative_delta_meta_minus_apple"] == -0.40
        assert b["delta_calc"] == "(-0.10) - (0.30) = -0.40"

    def test_statistical_discipline(self):
        b = _block()
        disc = b["statistical_discipline"]
        assert "p_value NOT_CALCULATED" in disc
        assert "cohens_d NOT_CALCULATED" in disc
        assert "is_significant False" in disc
        assert "Engine NOT run" in disc
        assert b["no_analysis_json_update"] is True
        assert "EXTENDS mechanism 605" in b["verdict"]

    def test_research_method_documents_ruled_out_candidates(self):
        b = _block()
        method = b["research_method"]
        assert "Lauren Goode ruled out" in method
        assert "Boone Ashworth ruled out" in method
        assert "theverge.com direct fetch policy-blocked" in method
        assert "Excerpt-bounded" in method or "excerpt-bounded" in method

    def test_confounder_strong_triple_present(self):
        b = _block()
        strong = b["confounders_ranked"]["strong"]
        assert len(strong) == 3
        assert any(c.startswith("Genre asymmetry") for c in strong)
        assert any(c.startswith("Privacy-vector asymmetry") for c in strong)
        assert any(c.startswith("Review-cycle asymmetry") for c in strong)

    def test_counterevidence_present(self):
        b = _block()
        assert len(b["counterevidence"]) >= 4
        joined = " ".join(b["counterevidence"])
        assert "best glasses I have ever tried" in joined
        assert "#723" in joined

    def test_cross_references_include_605_and_723(self):
        b = _block()
        joined = " ".join(b["cross_refs"])
        assert "#605" in joined
        assert "#723" in joined
        assert "#668" in joined
        assert "#593" in joined


# --- Supersession and corpus post-#812 --------------------------------------


class TestSupersessionAndCorpusPost812:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout))

    def test_corpus_max_is_719(self):
        assert max(self._numeric_ids()) == 719

    def test_iteration_812_max_718_sweep_superseded_by_design(self):
        # #812's max-718 sweeps fail by designed supersession now that 719 exists.
        assert max(self._numeric_ids()) != 718

    def test_zero_underscore_720_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_720_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_812_zero_underscore_719_sweep_stays_green(self):
        # The #812 zero-underscore-719 sweeps stay green post-#813 by designed keying:
        # neither the careers block nor this test file carries a literal underscore-719 key.
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", MECH_ID_MARKER, "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), \
                f"literal underscore-719 key leaked into {root}: {res.stdout.strip()[:200]}"

    def test_iteration_812_zero_numeric_719_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 719", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected #812's zero-numeric-719 sweep to fail by designed supersession"

    def test_numeric_719_keys_in_exactly_the_designed_location(self):
        res = _run_git("grep", "-r", "mechanism_id: 719", "--", "profiles/")
        hits = [l for l in res.stdout.strip().splitlines() if l.strip()]
        # Designed keying: one numeric 719 key in Song's careers competitor_coverage
        # block; no other profiles/ location.
        assert len(hits) == 1, f"unexpected numeric 719 key spread in profiles/: {hits}"
        assert "profiles/careers/journalists.yaml" in hits[0]


# --- Ledger -----------------------------------------------------------------


class TestLedger813:
    def _profiles_corpus(self):
        parts = []
        for root, _dirs, files in os.walk(os.path.join(REPO, "profiles")):
            for f in files:
                p = os.path.join(root, f)
                with open(p, encoding="utf-8", errors="replace") as fh:
                    parts.append(fh.read())
        return "\n".join(parts)

    def test_twenty_sixth_present_and_twenty_seventh_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference "TWENTY-SEVENTH" inside their own
        # negative guards, so a tests/ sweep would false-positive).
        corpus = self._profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus

    def test_m719_not_falsification_family_and_holds_26(self):
        b = _block()
        assert "ledger holds at 26" in b["falsification_family"]
        assert b["no_analysis_json_update"] is True


# --- Careers ----------------------------------------------------------------


class TestCareers813:
    def test_victoria_song_entry_present(self):
        song = _song()
        assert song["name"] == "Victoria Song"

    def test_victoria_song_beats(self):
        song = _song()
        assert "wearables" in song["beats"]
        assert "smart_glasses" in song["beats"]
        assert "health_tech" in song["beats"]

    def test_victoria_song_mechanism_ids(self):
        song = _song()
        assert song["mechanism_ids"] == [593, 605, 719]

    def test_victoria_song_813_block(self):
        song = _song()
        assert BLOCK_KEY in song["competitor_coverage"]
        cc = song["competitor_coverage"][BLOCK_KEY]
        assert cc["mechanism_id"] == 719
        assert cc["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.10
        assert cc["apple_arm"]["tone_MANUAL_ILLUSTRATIVE"] == 0.30

    def test_victoria_song_prior_blocks_untouched(self):
        song = _song()
        assert "type_b_618_victoria_song_jul2026_escalation_audit" in song["competitor_coverage"]
        assert song["competitor_coverage"]["type_b_618_victoria_song_jul2026_escalation_audit"]["mechanism_id"] == 605
        assert "type_c_599_victoria_song_vox_financial_stack_behavioral_pin" in song["competitor_coverage"]

    def test_ece_yildirim_entry_untouched(self):
        with open(CAREERS_PROFILE) as fh:
            doc = yaml.safe_load(fh)
        assert doc["ece_yildirim"]["mechanism_ids"] == [716]


# --- Doc sync ----------------------------------------------------------------


class TestDocSync813:
    def test_readme_row_present(self):
        with open(os.path.join(REPO, "README.md")) as fh:
            assert TEST_BASENAME in fh.read()

    def test_architecture_row_present(self):
        with open(os.path.join(REPO, "docs", "ARCHITECTURE.md")) as fh:
            assert TEST_BASENAME in fh.read()


# --- Iteration log -----------------------------------------------------------


class TestIterationLog813:
    def _tail(self):
        with open(ITERATION_LOG) as fh:
            lines = fh.readlines()
        return "".join(lines[-80:])

    def test_iteration_log_entry_present(self):
        assert "Type B #813" in self._tail()

    def test_iteration_log_window_sequence(self):
        assert WINDOW_SEQ in self._tail()
