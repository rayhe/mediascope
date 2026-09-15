"""Type C #759: OpenAI India attribution deals + ANI Sep 14 appeal outcome
re-verification sweep, new-deal bounded-absence sweep (Sep 15 2026, 01:00 PDT).

On Tue Sep 15 2026 this run re-verifies the financial-incentive threads
carried from Type C #709/#744 as bounded-absence sweeps with since filters:

India attribution arm: the Sep 7-8 2026 OpenAI deals (BCCL/Times Group,
Indian Express Group - mechanism 660 economics layer on mechanism 609)
stand unchanged - fee terms remain undisclosed. The Sep 14 2026 Division
Bench hearing outcome (ANI appeal, mechanism 657 leg) has NO reported
outcome in the bounded search (continuation of #744's watch); the
MediaNama appeal-analysis piece (already in corpus) is the newest
commentary.

New-deal arm: AI news-publisher licensing deals announced since
2026-09-05 - ZERO new deals surfaced. Results return only 2023-2024 deal
re-indexes (Bloomberg Law: Atlantic/Vox, News Corp, Hearst, Dotdash
Meredith) plus the already-mapped FourWeekMBA India synthesis piece
(mechanism 609 / #624 family).

Music-vertical arm (out of scope, logged per #729 precedent): UMG x
ElevenLabs multi-year AI music deal (announced Sep 10 2026) and Suno x
Warner/BMG v6 partnership (announced Sep 9 2026). All three Sep 2026 URLs
zero-hit repo-wide pre-commit; NOT added as sources (music vertical,
non-competitor counterparties).

This run is VERIFICATION-ONLY: no new mechanism is mapped (max
mechanism_id stays 688), NOT a falsification-family member (ledger holds
at 26), NOT artifact-grade (no analysis.json update). The mechanism 660
economics block carries verification_sweep_sep15. Search-excerpt-bounded
per #503 (3 browser.search query sets this run, no browser.open attempts
- fleet egress outage persists). ASCII-only.
"""

import glob
import os
import re
import subprocess

import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = os.path.basename(__file__)
MECH_KEY = "mechanism_660_openai_india_attribution_deal_economics_layer_sep2026"
SWEEP_DATE = "2026-09-15"
MUSIC_URL_KEYS = (
    "91690215007",  # tennessean UMG x ElevenLabs Sep 10 2026
    "302875284",  # prnewswire UMG x ElevenLabs release
    "suno-releases-new-ai-music-models-partnership-with-warner-music-bmg-2026-09-09",  # reuters Suno x Warner/BMG Sep 9 2026
)


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _entities_doc():
    with open(
        os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml"),
        encoding="utf-8",
    ) as fh:
        return yaml.safe_load(fh)


def _block660():
    return _entities_doc()["entities"]["openai"][MECH_KEY]


def _profiles_corpus():
    chunks = []
    for rel in (
        "profiles/competitor-entities.yaml",
        "profiles/competitor-coverage-research.yaml",
    ):
        chunks.append(_read(rel))
    return "\n".join(chunks)


def _mechanism_ids():
    return [
        int(x)
        for x in re.findall(r"mechanism_id:\s*(\d+)\b", _profiles_corpus())
    ]


class TestNovelty759:
    def test_single_type_c_759_file(self):
        hits = glob.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_c_759*.py")
        )
        assert hits == [os.path.join(REPO_ROOT, "tests", TEST_BASENAME)], hits

    def test_type_c_759_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_c_759 files, no #759 in git log, zero
        # verification_sweep_sep15 keys repo-wide, max mechanism_id 688
        # pre-commit, three music URL keys zero-hit repo-wide
        # pre-commit); this test pins that no duplicate #759 main commit
        # ever appears.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%H %s"],
            capture_output=True,
            text=True,
        )
        mains = [
            line for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type C #759:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type C #759 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        anchor = TestRotationCycleGuard759.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)


class TestRotationCycleGuard759:
    """Rotation: distinct-mains window test, #721-style.

    Robust to the #678 history artifact and the #565 followup convention:
    first occurrence of each distinct iteration number, newest first. #759
    closes the 755-759 window, closing D->E->A->B->C.
    """

    ANCHORED_SHA = "906b1ba708752b72eb04e621500319b7a4f78e0c"  # main commit this run, per #565

    @staticmethod
    def _mains():
        # First occurrence of each distinct iteration number, newest first.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%s"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        seen = set()
        mains = []
        for s in out:
            m = re.match(r"^Type [A-E] #(\d+):", s)
            if m and m.group(1) not in seen:
                seen.add(m.group(1))
                mains.append(s)
        return mains

    def test_window_755_759_closes_d_to_c(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("C", "759"),
            ("B", "758"),
            ("A", "757"),
            ("E", "756"),
            ("D", "755"),
        ], "rotation window 755-759 wrong: %r" % (observed,)

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["C", "B", "A", "E", "D"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                "rotation broken: %s -> %s is not a valid cycle edge" % (a, b)
            )


class TestIndiaAttributionVerificationSweep759:
    def test_block_660_present(self):
        block = _block660()
        assert block["mechanism_id"] == 660
        assert block["iteration"] == 709

    def test_block_660_sweep_note_present(self):
        note = _block660()["verification_sweep_sep15"]
        assert "Type C #759" in note
        assert "Last verified 2026-09-15" in note

    def test_block_660_sweep_records_bounded_absences(self):
        note = _block660()["verification_sweep_sep15"]
        assert "ZERO new deals" in note
        assert "bounded absence" in note
        assert "no outcome reporting surfaced" in note

    def test_block_660_sweep_notes_fee_undisclosed(self):
        note = _block660()["verification_sweep_sep15"]
        assert "fee terms remain undisclosed" in note
        assert "Indian Express Sep 8" in note
        assert "BCCL Sep 7" in note

    def test_block_660_sweep_note_discipline(self):
        note = _block660()["verification_sweep_sep15"]
        assert "per #503" in note
        assert "out-of-scope" in note

    def test_block_660_parent_deals_intact(self):
        block = _block660()
        parties = " ".join(block["counterparties"])
        assert "BCCL" in parties
        assert "Indian Express Group" in parties

    def test_block_660_sources_unchanged(self):
        urls = _block660()["sources"]
        joined = " ".join(urls)
        # No new source URLs added this verification-only run; the Sep 2026
        # music-vertical URLs were rejected, not added.
        for key in MUSIC_URL_KEYS:
            assert key not in joined
        assert "medianama.com/2026/09/223-bccl-openai-content-partnership-toi/" in joined


class TestMusicVerticalOutOfScope759:
    def test_music_urls_not_sources(self):
        # The three Sep 2026 music-licensing URLs were zero-hit repo-wide
        # pre-commit and are recorded as out-of-scope rejections in the
        # sweep note, NOT as sources - per the #729 precedent.
        note = _block660()["verification_sweep_sep15"]
        for key in MUSIC_URL_KEYS:
            assert key in note, "sweep note must record the rejected URL key %r" % (key,)

    def test_music_deals_flagged_out_of_scope(self):
        note = _block660()["verification_sweep_sep15"]
        assert "UMG x ElevenLabs" in note
        assert "Suno x Warner/BMG" in note
        assert "music vertical" in note
        assert "#729" in note

    def test_no_new_entity_blocks_for_music_deals(self):
        doc = _entities_doc()
        assert "elevenlabs" not in doc["entities"]
        assert "umg" not in doc["entities"]
        assert "suno" not in doc["entities"]

    def test_music_keys_appear_only_in_759_sweep_note(self):
        # The rejected music-licensing URL keys appear in the profiles
        # corpus ONLY inside the #759 verification_sweep_sep15 note - never
        # as sources on any mechanism block.
        corpus = _profiles_corpus()
        for key in MUSIC_URL_KEYS:
            assert corpus.count(key) == 1, (
                "music URL key %r should appear exactly once (in the #759 sweep note), got %d"
                % (key, corpus.count(key))
            )


class TestStatisticalDiscipline759:
    def test_verification_only_no_new_mechanism(self):
        ids = _mechanism_ids()
        assert max(ids) == 688, max(ids)

    def test_no_new_underscore_689_keys(self):
        assert "mechanism" + "_689" not in _profiles_corpus()

    def test_757_758_sweeps_stay_green(self):
        corpus = _profiles_corpus()
        assert "mechanism" + "_688" not in corpus
        assert "mechanism" + "_687" not in corpus

    def test_754_755_756_zero_686_sweeps_stay_green(self):
        assert "mechanism" + "_686" not in _profiles_corpus()

    def test_ledger_holds_at_26(self):
        corpus = _profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus

    def test_no_analysis_json_update_warranted(self):
        # Verification-only run: the iteration log must record that no
        # analysis.json update was warranted.
        log = _read("iteration-log.md")
        idx = log.find("#759 Type C:")
        assert idx != -1
        entry = log[idx:idx + 4000]
        assert "no analysis.json update" in entry


class TestDocSync759:
    def test_readme_row(self):
        assert TEST_BASENAME in _read("README.md")

    def test_architecture_row(self):
        assert TEST_BASENAME in _read("docs/ARCHITECTURE.md")


class TestIterationLog759:
    def test_log_entry_present(self):
        assert "#759 Type C:" in _read("iteration-log.md")

    def test_log_bounded_absences(self):
        log = _read("iteration-log.md")
        idx = log.find("#759 Type C:")
        entry = log[idx:idx + 4000]
        assert "ZERO new deals" in entry
        assert "bounded absence" in entry
        assert "India attribution" in entry
        assert "UMG x ElevenLabs" in entry

    def test_log_rotation_window(self):
        log = _read("iteration-log.md")
        idx = log.find("#759 Type C:")
        entry = log[idx:idx + 4000]
        assert "755-759" in entry
        assert "D->E->A->B->C" in entry


class TestDateGrounding759:
    def test_sep_15_2026_is_tuesday(self):
        import datetime

        assert datetime.date(2026, 9, 15).strftime("%A") == "Tuesday"
