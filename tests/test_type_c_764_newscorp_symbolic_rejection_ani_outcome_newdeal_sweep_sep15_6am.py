"""Type C #764: News Corp additional-arrangements watch + ANI Sep 14 outcome
re-verification sweep + new-deal bounded-absence sweep (Sep 15 2026, 06:00 PDT).

On Tue Sep 15 2026 this run re-verifies the financial-incentive threads
carried from Type C #709/#744/#759 as bounded-absence sweeps with since
filters, plus a News Corp "additional arrangements" watch arm:

New-deal arm: AI news-publisher licensing deals announced since
2026-09-10 - ZERO new competitor-counterparty deals. The one new
AI-licensing URL surfaced (Publishers Weekly: Princeton University Press
x Cashmere, Sep 2026) is already mapped at mechanism 663 (the PW URL is
present in m663 sources) - roster corroboration only, not a new deal.

News Corp arm: NO new post-March-2026 News Corp x AI-company licensing
deal surfaced in bounded search (CEO Robert Thomson's Morgan Stanley
"you won't have too long to wait" hint has not materialized in the
bounded window). The one novel News Corp x AI deal in corpus-history is
Symbolic.ai (Jan 15 2026, TechCrunch): AI journalism startup (founders
Devin Wenig ex-eBay CEO, Jon Stokes Ars Technica co-founder) signed for
Dow Jones Newswires editorial-workflow tooling. REJECTED for mechanism
mapping per the #729 precedent: non-competitor counterparty
(Symbolic.ai is not a tracked competitor entity), vendor direction
(News Corp is the buyer of tooling, not the licensing recipient), terms
undisclosed, Jan 2026 vintage. The TechCrunch URL zero-hit repo-wide
pre-commit; recorded in the sweep note, NOT added as a source on any
mechanism block.

ANI arm: third consecutive bounded-absence check on the Sep 14 2026
Division Bench hearing outcome - still no outcome reporting surfaced;
the MediaNama appeal-analysis piece (in corpus) remains the newest
commentary; the Rao-appointed-Chief-Justice-of-Patna-HC datum is
already in corpus (mechanism 657).

This run is VERIFICATION-ONLY: no new mechanism is mapped (max
mechanism_id stays 690), NOT a falsification-family member (ledger holds
at 26), NOT artifact-grade (no analysis.json update). The mechanism 660
economics block carries verification_sweep_sep15_6am. Search-excerpt-
bounded per #503 (4 browser.search query sets this run, no browser.open
attempts - fleet egress outage persists). ASCII-only.
"""

import glob
import os
import re
import subprocess

import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = os.path.basename(__file__)
MECH_KEY = "mechanism_660_openai_india_attribution_deal_economics_layer_sep2026"
MECH_663_KEY = (
    "mechanism_663_perplexity_premium_data_licensing_cashmere_sep2026"
)
MECH_657_KEY = "mechanism_657_ani_openai_india_litigation_leg_sep2026"
SWEEP_DATE = "2026-09-15"
SYMBOLIC_URL_KEY = (
    "symbolic-ai-signs-deal-with-rupert-murdochs-news-corp"
)
PUP_CASHMERE_URL = "http://www.publishersweekly.com/pw/by-topic/industry-news/publisher-news/article/100971-princeton-university-press-partners-with-cashmere-on-ai-licensing.html"


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


def _block663():
    return _entities_doc()["entities"]["perplexity"][MECH_663_KEY]


def _block657():
    return _entities_doc()["entities"]["openai"][MECH_657_KEY]


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


class TestNovelty764:
    def test_single_type_c_764_file(self):
        hits = glob.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_c_764*.py")
        )
        assert hits == [os.path.join(REPO_ROOT, "tests", TEST_BASENAME)], hits

    def test_type_c_764_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_c_764 files, no #764 in git log, zero
        # verification_sweep_sep15_6am keys repo-wide, max mechanism_id 690
        # pre-commit, Symbolic.ai / Devin Wenig / TechCrunch URL zero-hit
        # repo-wide pre-commit); this test pins that no duplicate #764 main
        # commit ever appears.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%H %s"],
            capture_output=True,
            text=True,
        )
        mains = [
            line for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type C #764:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type C #764 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        anchor = TestRotationCycleGuard764.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)


class TestRotationCycleGuard764:
    """Rotation: distinct-mains window test, #721-style.

    Robust to the #678 history artifact and the #565 followup convention:
    first occurrence of each distinct iteration number, newest first. #764
    closes the 760-764 window, closing D->E->A->B->C (761-765 window opens
    E->A->B->C->D).
    """

    ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # main commit this run, per #565

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

    def test_window_760_764_closes_d_to_c(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("C", "764"),
            ("B", "763"),
            ("A", "762"),
            ("E", "761"),
            ("D", "760"),
        ], "rotation window 760-764 wrong: %r" % (observed,)

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

    def test_mains_parse_sanity(self):
        subjects = self._mains()
        nums = []
        for s in subjects[:5]:
            m = re.match(r"^Type [A-E] #(\d+):", s)
            assert m, "unparseable main subject: %r" % (s,)
            nums.append(int(m.group(1)))
        assert nums == sorted(nums, reverse=True), "mains not newest-first: %r" % (nums,)
        assert len(set(nums)) == 5, "duplicate iteration numbers in window"


class TestNewDealSweep764:
    def test_block_660_present(self):
        block = _block660()
        assert block["mechanism_id"] == 660
        assert block["iteration"] == 709

    def test_block_660_has_6am_sweep_note(self):
        note = _block660()["verification_sweep_sep15_6am"]
        assert "Type C #764" in note
        assert "Last verified 2026-09-15" in note

    def test_sweep_records_zero_new_competitor_deals(self):
        note = _block660()["verification_sweep_sep15_6am"]
        assert "ZERO new competitor-counterparty deals" in note

    def test_pup_cashmere_url_mapped_at_663(self):
        urls = _block663()["sources"]
        assert PUP_CASHMERE_URL in urls, "m663 must already carry the PW PUP x Cashmere URL"

    def test_sweep_note_records_pup_cashmere_corpus_hit(self):
        note = _block660()["verification_sweep_sep15_6am"]
        assert "already mapped at mechanism 663" in note
        assert "roster corroboration only" in note

    def test_sweep_note_discipline(self):
        note = _block660()["verification_sweep_sep15_6am"]
        assert "per #503" in note
        assert "excerpt-bounded" in note
        assert "fleet egress outage" in note


class TestSymbolicAiRejection764:
    def test_symbolic_url_not_a_source(self):
        # The TechCrunch Symbolic.ai URL was zero-hit repo-wide pre-commit
        # and is recorded in the sweep note only - never as a source on any
        # mechanism block.
        for key in ("entities",):
            blocks = _entities_doc()[key]
            for ent, payload in blocks.items():
                for bname, bval in payload.items():
                    if isinstance(bval, dict) and "sources" in bval:
                        joined = " ".join(bval["sources"])
                        assert SYMBOLIC_URL_KEY not in joined, (
                            "Symbolic.ai URL must not be a source on %s/%s" % (ent, bname)
                        )

    def test_symbolic_recorded_in_sweep_note(self):
        note = _block660()["verification_sweep_sep15_6am"]
        assert SYMBOLIC_URL_KEY in note, "sweep note must record the rejected Symbolic.ai URL key"

    def test_symbolic_rejection_terms(self):
        note = _block660()["verification_sweep_sep15_6am"]
        assert "Symbolic.ai" in note
        assert "Devin Wenig" in note
        assert "Jon Stokes" in note
        assert "Dow Jones Newswires" in note

    def test_symbolic_rejection_rationale(self):
        note = _block660()["verification_sweep_sep15_6am"]
        assert "REJECTED" in note
        assert "#729" in note
        assert "non-competitor counterparty" in note
        assert "vendor direction" in note
        assert "terms undisclosed" in note

    def test_no_symbolic_entity_block(self):
        doc = _entities_doc()
        assert "symbolic" not in doc["entities"]
        assert "symbolic_ai" not in doc["entities"]
        assert "wenig" not in doc["entities"]

    def test_symbolic_mentions_scoped_to_note(self):
        # "Symbolic.ai" (dotted form) appears in the profiles corpus ONLY
        # inside the #764 sweep note - twice (the deal sentence and the
        # non-competitor rationale). (Lowercase "symbolic" also occurs in
        # unrelated prose like "symbolically significant" - the dotted form
        # is the rejection-scoped string.)
        corpus = _profiles_corpus()
        assert corpus.count("Symbolic.ai") == 2, (
            "Symbolic.ai should appear exactly twice (both in the #764 sweep note), got %d"
            % corpus.count("Symbolic.ai")
        )
        note_start = corpus.find("verification_sweep_sep15_6am")
        note_end = corpus.find("verification:", note_start)
        note_region = corpus[note_start:note_end]
        assert note_region.count("Symbolic.ai") == 2


class TestAniOutcomeWatch764:
    def test_m657_appeal_status_still_lists_sep14(self):
        status = _block657()["appeal_status"]
        assert "Sep 14 2026" in status

    def test_third_consecutive_bounded_absence(self):
        note = _block660()["verification_sweep_sep15_6am"]
        assert "third consecutive bounded-absence check" in note
        assert "no outcome reporting surfaced" in note

    def test_medianama_remains_newest_commentary(self):
        note = _block660()["verification_sweep_sep15_6am"]
        assert "MediaNama appeal-analysis piece" in note
        assert "newest commentary" in note

    def test_rao_patna_datum_already_in_corpus(self):
        note = _block660()["verification_sweep_sep15_6am"]
        assert "Chief-Justice-of-Patna-HC" in note
        assert "mechanism 657" in note
        assert "Chief Justice of Patna High Court" in _profiles_corpus()

    def test_india_attribution_deals_unchanged(self):
        note = _block660()["verification_sweep_sep15_6am"]
        assert "fee terms remain undisclosed" in note
        assert "BCCL Sep 7" in note
        assert "Indian Express Sep 8" in note


class TestStatisticalDiscipline764:
    def test_verification_only_no_new_mechanism(self):
        ids = _mechanism_ids()
        assert max(ids) == 690, max(ids)

    def test_no_new_underscore_691_keys(self):
        assert "mechanism" + "_691" not in _profiles_corpus()

    def test_762_763_blocks_present(self):
        # m689 (Type A #762) lives on news-corp.yaml and m690 (Type B #763)
        # on competitor-coverage-research.yaml, both in colon form - so the
        # sweep asserts them across the extended profiles corpus, not the
        # two-file _profiles_corpus().
        chunks = []
        for rel in (
            "profiles/competitor-entities.yaml",
            "profiles/competitor-coverage-research.yaml",
            "profiles/news-corp.yaml",
        ):
            chunks.append(_read(rel))
        corpus = "\n".join(chunks)
        assert re.search(r"mechanism_id:\s*689\b", corpus), "m689 block missing"
        assert re.search(r"mechanism_id:\s*690\b", corpus), "m690 block missing"

    def test_ledger_holds_at_26(self):
        corpus = _profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus

    def test_no_analysis_json_update_warranted(self):
        # Verification-only run: the iteration log must record that no
        # analysis.json update was warranted.
        log = _read("iteration-log.md")
        idx = log.find("#764 Type C:")
        assert idx != -1
        entry = log[idx:idx + 8000]
        assert "no analysis.json update" in entry


class TestDocSync764:
    def test_readme_row(self):
        assert TEST_BASENAME in _read("README.md")

    def test_architecture_row(self):
        assert TEST_BASENAME in _read("docs/ARCHITECTURE.md")


class TestIterationLog764:
    def test_log_entry_present(self):
        assert "#764 Type C:" in _read("iteration-log.md")

    def test_log_bounded_absences(self):
        log = _read("iteration-log.md")
        idx = log.find("#764 Type C:")
        entry = log[idx:idx + 8000]
        assert "ZERO new competitor-counterparty deals" in entry
        assert "bounded-absence" in entry
        assert "Symbolic.ai" in entry
        assert "third consecutive" in entry

    def test_log_rotation_window(self):
        log = _read("iteration-log.md")
        idx = log.find("#764 Type C:")
        entry = log[idx:idx + 8000]
        assert "760-764" in entry
        assert "D->E->A->B->C" in entry


class TestDateGrounding764:
    def test_sep_15_2026_is_tuesday(self):
        import datetime

        assert datetime.date(2026, 9, 15).strftime("%A") == "Tuesday"
