"""Type C #684: Microsoft Publisher Content Marketplace (PCM) x Conde Nast
bilateral deal-level leg formalization (Feb 2026) - the FIRST dedicated
deal-level mechanism on WIRED's parent's Microsoft AI licensing leg.

Conde Nast is a first-wave PCM pilot partner (Feb 9 2026 announcement via
WebWire press-release distribution sourced to condenast.com): its US
text-based editorial content is licensed for grounding AI-generated
summary responses across Microsoft's Copilot experiences. One first-hand
read this run: the Digiday Q and A with Nikhil Kolar, VP Microsoft AI
(92 rendered lines, ~Feb 2026) - pilot moving beyond the initial phase
toward a broader ecosystem; first-wave publishers BI Inc, Vox Media Inc,
USA Today Co, People Inc, AP, Hearst Magazines, Conde Nast; pricing
anchored on pay for demonstrated value (still experimental); standardized
click-to-sign contracts planned on the MSN 18,000-brands playbook;
bring-your-own-license for existing deals; demand side first-party
Copilot (MAI consumer + M365 enterprise) plus Yahoo onboarding.
WSJ Jul 2026 marketplaces piece (search-snippet attested): pilot with
eight publishers, Microsoft invested north of $10M including publisher
payments (Tim Frank) - the FIRST PCM-spend quantum datum in the corpus,
NOT a Conde Nast payment figure. Sep 2026 status ACTIVE per the #599
convention (bounded absence of exit reporting per the iteration-492
rule). Gradient: Microsoft-payer PRESENT at Conde Nast (fourth named AI
licensor) vs Meta $0 AI legs (mechanism 331 bundle excludes Conde Nast);
Meta is a zero-PCM participant (mechanism 443). Tone-predictor grade
MODERATE-WEAK (AI-grounding licensing inside a direct Meta AI competitor
product with structural exclusion dynamics, but CN-specific quantum
undisclosed, pricing experimental, Microsoft operator-plus-first-buyer
dual role); no tone scores, qualitative only, no engine run,
NOT artifact-grade. Distinct from mechanism 443 (architecture-level; this
is the bilateral deal-level leg), mechanism 504/564/391 (OpenAI first,
Amazon Rufus second, Perplexity payers), mechanism 642 (Apple News/News+
revenue-share leg, different mechanics), mechanism 539 (DDM: first
dedicated PCM bilateral leg; Conde Nast is the second), mechanism 559
(Amazon x NYT quantum comparator), mechanism 549 (News Corp x Meta
counterpart). Correlation only.

Research method: 3 browser.search query sets + 1 first-hand browser.open
read. All URLs verbatim from Full-URL listings; WSJ and Adweek quotes
search-snippet attested where noted. No zero-coverage claims.

Rotation: Type C follows Type B (#683) per A,B,C,D,E. Rotation guard,
doc-sync, and novelty-anchor test deselected pre-commit per the #565
followup convention; anchor patched in the followup commit once the main
commit SHA is known.
"""

import ast
import glob
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENTITIES_PATH = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = "mechanism_645_microsoft_pcm_conde_nast_bilateral_leg"
FILENAME = "test_type_c_684_microsoft_pcm_conde_nast_bilateral_leg_sep11_6pm.py"

DIGIDAY_URL = "https://digiday.com/media/qa-nikhil-kolar-vp-microsoft-ai-scales-its-click-to-sign-ai-content-marketplace/"
WEBWIRE_URL = "https://www.WebWire.com/ViewPressRel.asp?aId=350303"
ADWEEK_URL = "https://www.adweek.com/media/conde-nast-vasanth-williams-chief-product-technology-officer-microsoft-ai-licensing-pilot/"
WSJ_URL = "https://www.wsj.com/business/media/marketplaces-are-the-next-frontier-in-publisher-deals-with-ai-companies-11515b00"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. The rotation-guard class is deselected pre-commit.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"


def _entities():
    with open(ENTITIES_PATH) as f:
        return yaml.safe_load(f)


def _microsoft():
    return _entities()["entities"]["microsoft"]


def _mechanism():
    m = _microsoft()
    assert MECH_KEY in m, f"{MECH_KEY} missing from entities.microsoft"
    return m[MECH_KEY]


def _mechanism_text():
    return yaml.safe_dump(_mechanism(), allow_unicode=True)


def _count_def_tests():
    path = os.path.join(TESTS_DIR, FILENAME)
    tree = ast.parse(open(path).read())
    return sum(
        isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
        and n.name.startswith("test_")
        for n in ast.walk(tree)
    )


def read_readme():
    with open(README_PATH) as f:
        return f.read()


def read_arch():
    with open(ARCH_PATH) as f:
        return f.read()


def read_log_start():
    with open(LOG_PATH) as f:
        return f.read()


class TestIterationMetadata684:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 684

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 645

    def test_mechanism_id_unique_repo_wide(self):
        # Per the #674 convention: only this run's mechanism_id is asserted
        # unique (legacy ids like 80 have pre-existing corpus collisions).
        seen = []
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                if int(m.group(1)) == 645:
                    seen.append(path)
        assert len(seen) == 1, f"mechanism_id 645 not unique: {seen}"
        assert seen[0].endswith("competitor-entities.yaml")

    def test_rotation_type_c(self):
        assert _mechanism()["rotation"] == "Type C"

    def test_job_and_goal_ids(self):
        m = _mechanism()
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_type_c_focus_names_first_dedicated(self):
        assert "first dedicated deal-level mechanism" in _mechanism()["type_c_focus"]


class TestDealLegFormalization684:
    def test_launch_date_feb_2026(self):
        assert "2026-02-03" in _mechanism()["launch_date"]

    def test_first_wave_seven_partners(self):
        partners = _mechanism()["conde_nast_participation"]["first_wave_partners"]
        for name in (
            "Business Insider Inc",
            "Vox Media Inc",
            "USA Today Co",
            "People Inc",
            "Associated Press",
            "Hearst Magazines",
            "Conde Nast",
        ):
            assert name in partners, f"first-wave partner missing: {name}"

    def test_conde_nast_scope_copilot_grounding(self):
        scope = _mechanism()["conde_nast_participation"]["scope"]
        assert "grounding AI-generated summary responses" in scope
        assert "Copilot" in scope

    def test_pay_for_demonstrated_value(self):
        assert "pay for demonstrated value" in _mechanism()["deal_terms"]["pricing_model"]

    def test_demand_side_copilot_and_yahoo(self):
        demand = _mechanism()["deal_terms"]["demand_side"]
        assert "Copilot" in demand
        assert "Yahoo" in demand

    def test_click_to_sign_planned(self):
        assert "click-to-sign" in _mechanism()["deal_terms"]["contract_path"]

    def test_wsj_10m_datum_with_quantum_caveat(self):
        scale = _mechanism()["scale_2026"]
        assert "north of $10M" in scale["microsoft_investment"]
        assert "Tim Frank" in scale["microsoft_investment"]
        assert "NOT a Conde Nast payment figure" in scale["quantum_caveat"]

    def test_status_active(self):
        assert _mechanism()["status_sep_2026"]["verdict"] == "ACTIVE"

    def test_gradient_microsoft_present_meta_zero(self):
        gradient = _mechanism()["asymmetry_relevance"]["gradient"]
        assert "Microsoft-payer PRESENT" in gradient
        assert "Meta $0" in gradient
        assert "zero-PCM participant" in gradient

    def test_tone_predictor_moderate_weak_and_no_tone_claim(self):
        ar = _mechanism()["asymmetry_relevance"]
        assert ar["tone_predictor_grade"] == "MODERATE-WEAK"
        assert ar["no_tone_claim"] is True


class TestCrossReferences684:
    def test_mechanism_443_architecture_cited(self):
        refs = " ".join(_mechanism()["cross_references"])
        assert "mechanism 443" in refs

    def test_openai_504_first_payer_cited(self):
        refs = " ".join(_mechanism()["cross_references"])
        assert "mechanism 504" in refs

    def test_amazon_rufus_564_cited(self):
        refs = " ".join(_mechanism()["cross_references"])
        assert "mechanism 564" in refs

    def test_nyt_559_quantum_comparator_cited(self):
        refs = " ".join(_mechanism()["cross_references"])
        assert "mechanism 559" in refs

    def test_meta_counterparts_cited(self):
        refs = " ".join(_mechanism()["cross_references"])
        assert "mechanism 549" in refs
        assert "mechanism 331" in refs

    def test_conventions_cited(self):
        refs = " ".join(_mechanism()["cross_references"])
        assert "#599" in refs
        assert "#492" in refs

    def test_distinct_from_443_and_539(self):
        focus = _mechanism()["type_c_focus"]
        assert "mechanism 539" in focus
        assert "first dedicated PCM bilateral leg" in focus


class TestNovelty684:
    def test_single_684_file_on_disk(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_c_684*"))
        assert files == [os.path.join(TESTS_DIR, FILENAME)], files

    def test_no_duplicate_645_mechanism_key(self):
        count = 0
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path).read()
            count += len(re.findall(r"^    mechanism_645_microsoft_pcm", text, re.M))
        assert count == 1, f"mechanism_645 key appears {count} times"

    def test_no_prior_dedicated_microsoft_conde_nast_bilateral_mechanism(self):
        # Prior mentions are the mechanism 443 architecture block, the
        # septuple_publisher_leverage lines, and portfolio notes. No prior
        # block names a Microsoft x Conde Nast bilateral deal-level leg.
        # (Parsed via YAML, not raw-text regex: the mechanism_name carries
        # ''-escaped apostrophes that truncate a naive '[^']*' capture.)
        names = []

        def walk(o):
            if isinstance(o, dict):
                for k, v in o.items():
                    if isinstance(k, str) and k.startswith("mechanism_") and isinstance(v, dict):
                        nm = v.get("mechanism_name")
                        if isinstance(nm, str) and "Microsoft" in nm:
                            names.append(nm)
                    walk(v)
            elif isinstance(o, list):
                for v in o:
                    walk(v)

        walk(_entities())
        dedicated = [n for n in names if "Conde Nast" in n and "bilateral" in n]
        assert dedicated == [_mechanism()["mechanism_name"]], dedicated

    def test_meta_zero_pcm_participant_carried(self):
        # The focus carries mechanism 443's Meta-is-zero-PCM-participant
        # line into the Sep 2026 gradient (Meta runs 13 bilateral deals but
        # no marketplace presence).
        assert "zero-PCM participant" in _mechanism()["mechanism_name"]


class TestResearchMethod684:
    def test_mechanism_key_naming(self):
        assert MECH_KEY.startswith("mechanism_645_")
        assert MECH_KEY in _microsoft()

    def test_no_em_dash_or_curly_quotes_in_mechanism(self):
        text = _mechanism_text()
        assert "\u2014" not in text, "em dash found in mechanism block"
        assert "\u2018" not in text and "\u2019" not in text, "curly quote in mechanism block"

    def test_mechanism_text_ascii_only(self):
        text = _mechanism_text()
        bad = [c for c in text if ord(c) > 127]
        assert not bad, f"non-ASCII chars in mechanism block: {set(bad)!r}"

    def test_type_c_684_main_commit_unique_and_anchored(self):
        # Novelty anchor: exactly one "Type C #684:" main commit post-followup
        # (deselected pre-commit per the #565 convention; the followup and
        # doc-sync commits are "Type C #684 followup:" / "Type C #684
        # doc-sync:" and do NOT match the main-commit filter).
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type C #684:", l)]
        assert len(mains) == 1, f"expected exactly one Type C #684 main commit, got {len(mains)}"
        assert mains[0].startswith(ANCHORED_SHA), (
            f"main commit SHA does not match patched anchor: {mains[0][:12]}"
        )

    def test_first_hand_digiday_read(self):
        urls = _mechanism()["source_urls"]
        assert DIGIDAY_URL in urls
        assert "92 rendered lines" in _mechanism()["research_method"]

    def test_webwire_adweek_urls_present(self):
        urls = _mechanism()["source_urls"]
        assert WEBWIRE_URL in urls
        assert ADWEEK_URL in urls

    def test_research_method_names_query_sets_and_opens(self):
        rm = _mechanism()["research_method"]
        assert "3 browser.search query sets" in rm
        assert "1 first-hand browser.open read" in rm

    def test_no_canonical_urls_constructed(self):
        assert "no canonical URLs constructed" in _mechanism()["research_method"]

    def test_bounded_absence_discipline(self):
        assert "iteration-492 rule" in _mechanism()["research_method"]

    def test_precommit_novelty_greps_documented(self):
        rm = _mechanism()["research_method"]
        assert "zero test_type_c_684 files on disk" in rm
        assert "max numeric mechanism id pre-commit 644" in rm

    def test_snippet_attestation_flagged(self):
        rm = _mechanism()["research_method"]
        assert "WSJ Jul 2026 snippet-attested" in rm
        assert WSJ_URL in _mechanism()["source_urls"]


class TestStatisticalDiscipline684:
    def test_no_scorer_run(self):
        sd = _mechanism()["statistical_discipline"]
        assert sd["scorer"] == "none"
        assert sd["tone_scores"] == "NOT_SCORED"

    def test_tone_scores_not_scored(self):
        sd = _mechanism()["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"

    def test_qualitative_only(self):
        sd = _mechanism()["statistical_discipline"]
        assert sd["qualitative_only"] is True
        assert sd["correlation_not_causation"] is True

    def test_correlational_note_names_moderate_weak_grade(self):
        ar = _mechanism()["asymmetry_relevance"]
        assert ar["tone_predictor_grade"] == "MODERATE-WEAK"
        assert "why_moderate_weak" in ar

    def test_verification_block(self):
        sd = _mechanism()["statistical_discipline"]
        assert sd["is_significant"] is False
        assert sd["artifact_grade"] is False


class TestRotationCycleGuard684:
    @staticmethod
    def _distinct_mains(limit=5):
        # First occurrence of each distinct iteration number, newest first.
        # Robust to the followup/doc-sync SHA-fix history: followup commits
        # titled "Type B #683 followup: ..." match the main-commit filter,
        # so raw subjects show repeats. Distinct numbering is the intent.
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        seen_nums = set()
        mains = []
        for s in out:
            if not re.match(r"^Type [A-E] #\d+:", s):
                continue
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            if m.group(2) in seen_nums:
                continue
            seen_nums.add(m.group(2))
            mains.append((m.group(1), m.group(2)))
            if len(mains) == limit:
                break
        return mains

    def test_window_680_684_closes_b_to_c(self):
        observed = self._distinct_mains(5)
        assert observed == [
            ("C", "684"),
            ("B", "683"),
            ("A", "682"),
            ("E", "681"),
            ("D", "680"),
        ], f"rotation window 680-684 wrong: {observed}"

    def test_rotation_adjacency_cycle_valid(self):
        observed = [t for t, _ in self._distinct_mains(5)]
        assert observed == ["C", "B", "A", "E", "D"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                f"rotation broken: {a} -> {b} is not a valid cycle edge"
            )

    def test_anchor_is_main_patch_in_followup(self):
        # Post-commit anchor: the #684 main commit. Patched in the followup
        # per the #565 convention once the main commit SHA is known.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [
            l for l in out if re.match(r"^[0-9a-f]{40} Type [A-E] #\d+:", l)
        ]
        sha, subject = mains[0].split(" ", 1)
        assert sha.startswith(ANCHORED_SHA), f"anchor not yet patched: {sha}"
        assert subject.startswith("Type C #684:"), (
            f"post-commit anchor broken: newest main is not #684: {subject!r}"
        )

    def test_rotation_guard_regex_actually_matches(self):
        # #632 process note: a rotation guard whose regex never matches is a
        # silent no-op. Verify the guard regexes match a real main-commit
        # subject (the double-backslash r"...#(\\d+)..." form silently matches
        # nothing). Written as a semantic check rather than a literal-pattern
        # check so the test cannot defeat itself by containing the pattern.
        src = open(os.path.join(TESTS_DIR, FILENAME)).read()
        patterns = re.findall(r're\.search\(r"([^"]+)"', src)
        guard_patterns = [p for p in patterns if p.startswith("Type (")]
        assert guard_patterns, "no rotation-guard regex found in this file"
        sample = "Type C #684: Microsoft Publisher Content Marketplace x Conde Nast bilateral leg"
        for p in guard_patterns:
            m = re.search(p, sample)
            assert m and m.group(1) == "C" and m.group(2) == "684", (
                f"rotation regex {p!r} fails to match a real subject "
                "(double-backslash bug?)"
            )


class TestDocSyncRatchet684:
    def test_readme_has_684_row(self):
        assert "#684" in read_readme()

    def test_arch_has_684_row(self):
        assert "684" in read_arch()

    def test_readme_row_mentions_microsoft_pcm(self):
        assert "Microsoft PCM" in read_readme()
        assert "Conde Nast" in read_readme()

    def test_log_starts_with_684(self):
        assert read_log_start().startswith("#684 Type C:")

    def test_def_test_count_matches(self):
        # The README row for #684 must carry this file's own def-test count.
        n = _count_def_tests()
        assert str(n) in read_readme(), (
            f"README #684 row should mention this file's def-test count {n}"
        )


class TestNoBrittlePatterns684:
    def test_yaml_reparses_clean(self):
        m = _mechanism()
        assert isinstance(m["mechanism_id"], int)
        assert isinstance(m["iteration"], int)
        assert isinstance(m["confounders_ranked"], list)

    def test_mechanism_key_format(self):
        assert MECH_KEY == "mechanism_645_microsoft_pcm_conde_nast_bilateral_leg"
