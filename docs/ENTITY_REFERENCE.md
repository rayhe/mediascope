# Entity Detection & Clustering Quick Reference

> A compact lookup card for all 84 entity clusters (826 aliases) used by MediaScope's entity detection system. For the full code, disambiguation filters, and custom regex patterns, see [`mediascope/analyze/entities.py`](../mediascope/analyze/entities.py). For how entities feed into asymmetry scoring, see [METHODOLOGY.md §2](METHODOLOGY.md#2-asymmetry-scoring-engine).

---

## How to Use This Reference

Entity detection is the **first stage** of the analysis pipeline — every downstream system (topic classification, sentiment scoring, framing detection, asymmetry calculation, conflict disclosure) depends on entities being correctly identified and clustered.

### Core Concepts

| Concept | Definition |
|---|---|
| **Cluster** | A named group representing a single trackable entity (company, org, person category). Example: `Meta` |
| **Alias** | A text string that maps to a cluster. Example: `"Facebook"`, `"Zuckerberg"`, `"Instagram"` all → `Meta` |
| **Canonical Name** | The best alias match for a given text span. `"Andrew Bosworth"` matched in the Meta cluster resolves to canonical name `"Andrew Bosworth"`, not `"Meta"` |
| **Custom Regex** | A hand-tuned regex for the cluster (62 of 83 clusters). Handles homographs, negative lookaheads, and context-sensitive matching |
| **Auto Regex** | Word-boundary patterns auto-generated from the alias list (21 of 83 clusters). Simpler but adequate for unambiguous names |

### Pipeline Position

```
Article Text
    │
    ▼
┌─────────────────────┐
│  Entity Detection    │  ← YOU ARE HERE
│  (entities.py)       │
│                      │
│  Input:  raw text    │
│  Output: list of     │
│    EntityMention     │
│    (entity, cluster, │
│     canonical_name,  │
│     start, end,      │
│     context)         │
└──────────┬──────────┘
           │
     ┌─────┴─────┬────────────┬──────────────┐
     ▼           ▼            ▼              ▼
  Topics    Sentiment    Framing        Asymmetry
  (which    (tone per    (devices per   (compare
   bucket?)  entity)      entity)        target
                                        vs peers)
```

### How Matching Works

1. **Cluster-level regex patterns** are compiled first — one pattern per cluster, ordered before alias patterns. These are more precise (hand-tuned negative lookaheads, context-sensitive alternations).

2. **Individual alias patterns** fire for clusters without custom regex. Sorted by alias length descending so longer matches win (e.g., `"Apple Intelligence"` matches before `"Apple"`).

3. **Overlap prevention**: once a character span is matched, no other pattern can match overlapping characters. First match wins (cluster-level patterns have priority).

4. **Disambiguation filters** (see Part 6) prevent false positives: homograph verb filters, lookbehind context filters, and case-sensitive entity filters.

5. **Canonical name resolution**: for cluster-level regex matches, the matched text is resolved to the closest alias (exact match → substring containment → raw matched text).

---

## Part 1: Big Tech & AI Companies

The primary analysis targets — companies whose coverage is compared for asymmetry.

| # | Cluster | Aliases | Regex | Key Aliases | Notes |
|---|---------|---------|-------|-------------|-------|
| 1 | **Meta** | 88 | custom | Meta, Facebook, Instagram, WhatsApp, Threads, Zuckerberg, Reality Labs, Ray-Ban Meta, Llama, MTIA, Iris, Muse Spark/Image/Video, Fury, Virtue AI, LeCun, Mosseri | Largest cluster. Custom regex handles `Meta` vs HTML `<meta>` tag (negative lookahead for `tag`, `data`, `description`, etc.). Codenames (Mango, Watermelon, Creator, Pocket) require trailing context keywords. |
| 2 | **Google** | 11 | custom | Alphabet, Google, YouTube, DeepMind, Waymo, Sundar Pichai, Gemini, AlphaFold | Excludes `Google Sheet/Doc/Drive/Form/Search` to avoid tool-usage false positives |
| 3 | **Apple** | 11 | custom | Apple, iPhone, iPad, Tim Cook, John Ternus, Apple Intelligence, Apple Vision Pro, Siri | Excludes `Apple pie/cider/sauce/tree/juice/cinnamon` |
| 4 | **Amazon** | 9 | custom | Amazon, AWS, Alexa, Jeff Bezos, Andy Jassy, Kindle, Ring, Prime Video | Excludes `Amazon rain/forest/river/basin` |
| 5 | **Microsoft** | 9 | auto | Microsoft, Satya Nadella, Azure, Bing, LinkedIn, GitHub, Copilot, Xbox, Windows | Windows disambiguation via lookbehind filter (see Part 6) |
| 6 | **OpenAI** | 14 | auto | OpenAI, Sam Altman, ChatGPT, GPT-4/5, DALL-E, Sora, Stargate, Jalapeño (chip codename) | Includes historical (GPT-2) and open-weight (gpt-oss) models |
| 7 | **Anthropic** | 9 | auto | Anthropic, Dario/Daniela Amodei, Claude, Mythos, Fable, Project Glasswing, Amanda Askell | |
| 8 | **X/Twitter** | 4 | custom | Twitter, X Corp, Elon Musk, Musk | Excludes `Twitter-like/-esque/-style`. `Musk` excludes `Musk Ox/melon/deer`. `Elon Musk` excludes `Elon Musk's xAI` (routes to xAI cluster) |
| 9 | **xAI** | 5 | custom | xAI, Grok, Colossus, Colossus II | Grok excludes `Grok the/TV/Network` |
| 10 | **Tesla/SpaceX** | 4 | custom | Tesla, SpaceX, Starlink, Neuralink | Tesla excludes `Tesla coil/tower/valve` |
| 11 | **TikTok** | 3 | auto | TikTok, ByteDance, Shou Zi Chew | |

---

## Part 2: Semiconductor & Hardware

Companies in the chip supply chain and hardware ecosystem.

| # | Cluster | Aliases | Regex | Key Aliases | Notes |
|---|---------|---------|-------|-------------|-------|
| 12 | **Nvidia** | 17 | custom | Nvidia, NVIDIA, NVDA, Jensen Huang, CUDA, H100/H200/A100/B200/GB200, DGX, Rubin, Blackwell | Rubin/Blackwell require trailing context (`platform`, `chip`, `GPU`, etc.) to avoid person-name false positives |
| 13 | **Qualcomm** | 6 | custom | Qualcomm, Cristiano Amon, Snapdragon, Dragonfly, Hexagon | |
| 14 | **Intel** | 7 | custom | Intel, Pat Gelsinger, Lip-Bu Tan, Gaudi, Xeon, Intel Foundry | Gaudi requires trailing context (`AI`, `accelerator`, `chip`) |
| 15 | **AMD** | 7 | custom | AMD, Lisa Su, EPYC, Ryzen, Radeon, Instinct | Instinct requires trailing `MI\d` or `accelerator`/`GPU` |
| 16 | **TSMC** | 4 | custom | TSMC, Taiwan Semiconductor | |
| 17 | **Micron** | 3 | custom | Micron, Sanjay Mehrotra | |
| 18 | **Arm** | 6 | custom | Arm, ARM, Rene Haas, Neoverse | `Arm` requires trailing context (Holdings, architecture, chip, etc.) to avoid common English word |
| 19 | **Broadcom** | 3 | custom | Broadcom, Hock Tan, VMware | |
| 20 | **Samsung** | 5 | custom | Samsung, Samsung Electronics/Semiconductor/Foundry/HBM | |
| 21 | **SK Hynix** | 3 | custom | SK Hynix, Hynix | |
| 22 | **Semiconductor Equipment** | 8 | custom | KLA, Lam Research, Applied Materials, AMAT, ASML, Tokyo Electron | |
| 23 | **Sumitomo Electric** | 3 | custom | Sumitomo, Sumitomo Electric Industries | |
| 24 | **Storage/Memory** | 4 | custom | SanDisk, Western Digital, WD, Seagate | |

---

## Part 3: AI & Cloud Infrastructure

Cloud providers, AI startups, and infrastructure companies.

| # | Cluster | Aliases | Regex | Key Aliases | Notes |
|---|---------|---------|-------|-------------|-------|
| 25 | **CoreWeave** | 2 | custom | CoreWeave, Mike Intrator | |
| 26 | **Nebius** | 2 | custom | Nebius, Nebius Group | |
| 27 | **Oracle** | 6 | custom | Oracle, Larry Ellison, Safra Catz, Oracle Cloud | |
| 28 | **IBM** | 4 | custom | IBM, Deep Blue, Watson, Red Hat | |
| 29 | **Palantir** | 4 | auto | Palantir, Alex Karp, Peter Thiel | |
| 30 | **Salesforce** | 3 | auto | Salesforce, Marc Benioff, Agentforce | |
| 31 | **AI Infrastructure** | 1 | custom | Scale AI | |
| 32 | **AI Chatbot Products** | 2 | custom | Character.AI, Character AI | |
| 33 | **AI Research Orgs** | 3 | custom | Allen Institute for AI, AI2, EleutherAI | |
| 34 | **HuggingFace** | 3 | custom | HuggingFace, Hugging Face, Clement Delangue | |
| 35 | **World Labs** | 1 | custom | World Labs | |
| 36 | **Manus AI** | 2 | custom | Manus, Butterfly Effect | Manus requires trailing context (`AI`, `app`, `agent`) to avoid common noun |
| 37 | **Duolingo** | 2 | custom | Duolingo, Luis von Ahn | |
| 38 | **Chinese AI** | 13 | auto | Zhipu, DeepSeek, Baidu, Alibaba Cloud, Qwen, Yi, 01.AI, Moonshot AI, SenseTime, iFLYTEK | |

---

## Part 4: Consumer & Social Platforms

| # | Cluster | Aliases | Regex | Key Aliases | Notes |
|---|---------|---------|-------|-------------|-------|
| 39 | **Snap** | 4 | custom | Snap, Snapchat, Spectacles, Evan Spiegel | |
| 40 | **Spotify** | 2 | auto | Spotify, Daniel Ek | |
| 41 | **Uber** | 3 | custom | Uber, Dara Khosrowshahi | Excludes `Uber Eats` (separate brand context) |
| 42 | **Midjourney** | 2 | custom | Midjourney | |
| 43 | **Black Forest Labs** | 4 | custom | Black Forest Labs, BFL, FLUX, FLUX.1 | BFL/FLUX require word boundary; FLUX.1 variant included |
| 44 | **Creative Artists Agency** | 2 | custom | Creative Artists Agency, CAA | CAA requires trailing context to avoid acronym collisions |
| 45 | **Chinese Tech Platforms** | 10 | custom | Lark, DingTalk, Rednote, Xiaohongshu, WeChat, Weibo, Taobao, Alipay, Tencent, Alibaba | Alibaba excludes `Alibaba Cloud` (routes to Chinese AI cluster) |
| 46 | **OpenClaw** | 2 | custom | OpenClaw, Hatch | Hatch requires trailing context (`agent`, `AI`, `platform`) |

---

## Part 5: XR, Wearables & Optics

| # | Cluster | Aliases | Regex | Key Aliases | Notes |
|---|---------|---------|-------|-------------|-------|
| 47 | **VR/Metaverse** | 10 | custom | Horizon Worlds, Quest, Meta Quest, Quest 3/3S/Pro, VRChat, metaverse, Reality Labs | Quest requires capital Q in source text (case-sensitive inline flag) |
| 48 | **Smart Glasses Competitors** | 6 | custom | Gentle Monster, XREAL, Even Realities, Halo, Solos, Brilliant Labs | |
| 49 | **EssilorLuxottica** | 6 | auto | EssilorLuxottica, Essilor, Luxottica, Francesco Milleri, LensCrafters | |
| 50 | **Garmin** | 1 | auto | Garmin | |

---

## Part 6: Government & Regulatory

| # | Cluster | Aliases | Regex | Key Aliases | Notes |
|---|---------|---------|-------|-------------|-------|
| 51 | **US Government** | 47 | custom | Pentagon, DoD, FBI, CIA, NSA, FTC, ICE, DEA, DOGE, IRS, SEC, DOJ, BIS, White House, ICAC, military branches | Largest non-corporate cluster. All acronyms use case-sensitive inline flags (`(?-i:FBI)`) |
| 52 | **US Congress** | 8 | custom | Congress, Senate, House, committees, lawmakers, legislators | |
| 53 | **State Attorneys General** | 4 | custom | attorney(s) general + named AGs (Torrez, Bonta, Weiser, Platkin, Coleman, Bird, Campbell, Ferguson) | Critical for child safety and antitrust litigation coverage |
| 54 | **Political Figures** | 7 | custom | Trump, Biden, Kamala Harris, J.D. Vance | Trump excludes `Trump Tower/Hotel/Organization/National/International` |
| 55 | **EU Regulatory** | 9 | auto | GDPR, DPC, European Commission, Autorité de la concurrence | |
| 56 | **Australia** | 3 | custom | Australia, eSafety Commissioner | |
| 57 | **Legal/Judicial** | 6 | custom | Delaware courts, Section 230, DSA, MDL numbers, federal courts/judges, Supreme Court | Extended in Jul 2026 to catch federal judges invisible in Reuters $1.4T article |

---

## Part 7: Defense, Surveillance & Security

| # | Cluster | Aliases | Regex | Key Aliases | Notes |
|---|---------|---------|-------|-------------|-------|
| 58 | **Defense Tech** | 21 | auto | Anduril, Palmer Luckey, Elbit, L3Harris, Northrop Grumman, Lockheed, Raytheon, Shield AI, Skydio | Includes Anduril-specific product names (Lattice, EagleEye, SBMC) |
| 59 | **Surveillance/Biometrics** | 8 | auto | Rank One Computing, Clearview AI, NEC, Cognitec, Idemia | |
| 60 | **Data/Intelligence Industry** | 12 | auto | ShadowDragon, Babel Street, LexisNexis, Voyager Labs, Dataminr, Cellebrite, NSO Group, Pegasus | |
| 61 | **Cybersecurity/Research** | 11 | auto | Brian Krebs, Troy Hunt, Bruce Schneier, Mudge, METR, CISA, NIST | |
| 84 | **Privacy Advocacy** | 16 | auto | Foxglove, Privacy International, EFF, Access Now, Big Brother Watch, noyb, CAIDP | Jul 2026: The Tab Muse Image analysis |

---

## Part 8: Media, Publishing & Whistleblowers

| # | Cluster | Aliases | Regex | Key Aliases | Notes |
|---|---------|---------|-------|-------------|-------|
| 62 | **Media/Publications** | 31 | auto | NYT, Washington Post, Guardian, WIRED, Atlantic, MIT TR, Reuters, AP, Bloomberg, FT, TechCrunch, The Verge, Gizmodo, WSJ, 404 Media | These are the publications being analyzed. Detection enables self-referential investigation framing device. |
| 63 | **French Media Associations** | 6 | custom | DVP, APIG, Le Monde, Les Echos | French content licensing context |
| 64 | **Whistleblowers/Critics** | 10 | auto | Sarah Wynn-Williams, Frances Haugen, Sophie Zhang, Christopher Wylie, Carole Cadwalladr, Tim Wu | Key actors in Meta-specific narratives |
| 65 | **Cambridge Analytica** | 1 | custom | Cambridge Analytica | Separate from Meta cluster — distinct entity in coverage, frequently co-occurring |

---

## Part 9: Finance, Investment & Legal

| # | Cluster | Aliases | Regex | Key Aliases | Notes |
|---|---------|---------|-------|-------------|-------|
| 66 | **Financial Services** | 57 | custom | Visa, Mastercard, Goldman Sachs, JPMorgan, BofA, PayPal, Stripe, Berkshire Hathaway, Buffett | Second-largest cluster. Visa excludes `Visa application/interview/status/waiver`. Stripe/Square require trailing context. Includes 20+ equity analyst firms. |
| 67 | **VC/Tech Investors** | 10 | custom | Marc Andreessen, a16z, Sequoia, Benchmark, Kleiner Perkins, Y Combinator | Benchmark requires trailing context (`Capital`, `partner`, `led`, `invested`, etc.) |
| 68 | **Prediction Markets/Fintech** | 13 | custom | Polymarket, Kalshi, Robinhood, CFTC | |
| 69 | **Indian Fintech** | 4 | custom | CRED, Kunal Shah, PhonePe, UPI | |
| 70 | **Insurance/Litigation Finance** | 13 | custom | Hartford, Chubb, Flashlight Capital, Innsworth Capital, Burford Capital | Key cluster for litigation funding network analysis |
| 71 | **Child Safety Legislation** | 10 | custom | KIDS Act, COPPA, KOSA, EARN IT Act, REPORT Act, Age Appropriate Design Code | |

---

## Part 10: Academic, Research & Advocacy

| # | Cluster | Aliases | Regex | Key Aliases | Notes |
|---|---------|---------|-------|-------------|-------|
| 72 | **Academic/Research** | 54 | custom | 20+ universities (NYU, Stanford, MIT, Harvard, etc.), academic journals (Nature, Science, PNAS, Lancet, JAMA), IEEE, ACM, named researchers | Third-largest cluster. Journal names use case-sensitive flags to avoid "nature" (common noun) and "science" (common noun) |
| 73 | **Research Centers** | 15 | custom | CCDH, Center for Humane Technology, NCMEC, CyberTipline, Thorn, IWF, FOSI, Palisade Research | |
| 74 | **Child Safety Researchers** | 10 | auto | Arturo Béjar, Laura Edelson, Rumman Chowdhury | Named researchers who appear in child safety coverage |
| 75 | **Policy Research** | 13 | auto | RAND, Brookings, CSIS, CFR, Carnegie, Pew Research | |
| 76 | **Education/Advocacy** | 5 | custom | National PTA, NEA, AFT | |
| 77 | **Privacy/Civil Liberties Orgs** | 12 | auto | EFF, ACLU, Access Now, EPIC, NOYB | |
| 78 | **Environmental Advocacy** | 12 | custom | Sierra Club, Greenpeace, NRDC, EDF, Earthjustice, 350.org | |

---

## Part 11: Energy & Utilities

| # | Cluster | Aliases | Regex | Key Aliases | Notes |
|---|---------|---------|-------|-------------|-------|
| 79 | **Energy/Utilities** | 24 | custom | Entergy, Duke Energy, Southern Company, Dominion, NextEra, PG&E, TVA | Critical for `infrastructure_impact` and `energy_climate` topic coverage |
| 80 | **Energy Research/Regulatory** | 16 | custom | EPRI, EIA, FERC, IEA, NREL, DOE, Rhodium Group | |

---

## Part 12: Labor, Outsourcing & Miscellaneous

| # | Cluster | Aliases | Regex | Key Aliases | Notes |
|---|---------|---------|-------|-------------|-------|
| 81 | **Labor/Unions** | 10 | auto | UTAW, CWU, Alphabet Workers Union, SEIU, AFL-CIO | Includes organizing verbs (`unionize`, `unionization`) |
| 82 | **Outsourcing/Contractors** | 3 | custom | Covalen, Sama, Accenture | Sama requires trailing context (company-specific keywords) to avoid common word |
| 83 | **Celebrity/Influencer** | 2 | custom | Kylie Jenner | |

---

## Part 6 (Appendix): Disambiguation Filters

Entity detection in editorial text requires careful disambiguation. MediaScope uses four filter layers, applied in order during matching:

### A. Homograph Verb Filters

**Problem:** Some entity names are also common English verbs or adjectives.

| Alias | False Positive | How Filtered |
|---|---|---|
| `wired` | "The system is wired into the network" | Trailing context check: if followed by `into/to/for/in/up/together/through/the`, skip |

**Mechanism:** `_HOMOGRAPH_VERB_FILTERS` dict maps lowercase alias → compiled regex checked against `text[end:end+30]`.

### B. Lookbehind Homograph Filters

**Problem:** Some aliases are common nouns that need preceding context to distinguish.

| Alias | False Positive | How Filtered |
|---|---|---|
| `windows` | "context windows", "attention windows", "sliding windows" | If preceded by `context/attention/token/sliding/observation/inference/...`, skip |
| `atlantic` | "Mid-Atlantic", "Trans-Atlantic", "North Atlantic" | If preceded by `mid-/trans-/north-/south-/cross-`, skip |

**Mechanism:** `_HOMOGRAPH_LOOKBEHIND_FILTERS` dict maps lowercase alias → compiled regex checked against `text[start-40:start]`.

### C. Case-Sensitive Entity Filters

**Problem:** Some entity names are identical to common noun phrases when lowercased.

| Alias | Entity (match) | Common noun (skip) |
|---|---|---|
| `The Information` | "The Information reported…" ✅ | "refused to provide the information" ❌ |

**Mechanism:** `_CASE_SENSITIVE_ENTITIES` dict maps lowercase alias → compiled regex that the *matched text itself* must satisfy (i.e., capital I required).

### D. Custom Regex Context Windows

Many clusters handle disambiguation directly in their custom regex patterns using:

- **Negative lookaheads:** `Meta(?!\s+(?:tag|data|description|charset|...))` — prevents matching HTML `<meta>` attributes
- **Positive lookaheads:** `(?-i:Iris)(?=(?:\s|,\s*)(?:chip|accelerator|silicon|...))` — requires trailing product context for ambiguous codenames
- **Case-sensitive inline flags:** `(?-i:Zuck)` — only matches the capitalized form, not `zuck` in running prose
- **Exclusion groups:** `Apple(?!\s+(?:pie|cider|sauce|tree|...))` — prevents food/nature false positives

---

## Part 7 (Appendix): Adding New Entities

### Adding an Alias to an Existing Cluster

1. Add the alias string to the cluster's `aliases` list in `entities.py`
2. If the cluster has a custom `regex`, add the alias to the regex alternation
3. If the alias is ambiguous, add disambiguation (lookahead, lookbehind, case-sensitive flag, or homograph filter)
4. Add a test in `tests/test_entities.py`

### Adding a New Cluster

1. Add a new entry to `DEFAULT_ENTITY_CLUSTERS`:
   ```python
   "NewCompany": {
       "aliases": ["NewCompany", "NC", "CEO Name"],
       "regex": r"(?<!\w)(NewCompany|(?-i:NC)(?=\s+(?:is|was|...))|CEO Name)(?!\w)",
   }
   ```
2. If no ambiguous aliases exist, omit `regex` — auto-generation from aliases works
3. Add tests for both positive matches and expected non-matches
4. If the entity should appear in publication profiles, add a `target_entities` section to the relevant YAML profiles

### Via YAML Profiles

Publication-specific entity clusters are defined in the `target_entities` section of each profile YAML. These are merged with `DEFAULT_ENTITY_CLUSTERS` at analysis time using `merge_clusters()`, with profile entries overriding defaults of the same name.

```yaml
# profiles/wired.yaml
target_entities:
  CustomEntity:
    aliases:
      - "Custom Entity Name"
      - "CEN"
```

### Via YAML File (Standalone)

```python
from mediascope.analyze.entities import load_clusters_from_yaml, merge_clusters, DEFAULT_ENTITY_CLUSTERS

custom = load_clusters_from_yaml("my_entities.yaml")
clusters = merge_clusters(DEFAULT_ENTITY_CLUSTERS, custom)
mentions = detect_entities(text, clusters=clusters)
```

---

## Part 8 (Appendix): Cluster Size Distribution

Understanding the alias distribution helps prioritize disambiguation work — larger clusters need more careful regex engineering.

| Size Tier | Clusters | Examples |
|---|---|---|
| **50+ aliases** | 3 | Meta (88), Financial Services (57), Academic/Research (54) |
| **20–49 aliases** | 4 | US Government (47), Media/Publications (31), Energy/Utilities (24), Defense Tech (21) |
| **10–19 aliases** | 13 | Nvidia (17), Research Centers (15), OpenAI (14), etc. |
| **5–9 aliases** | 25 | Apple (11), Google (11), Microsoft (9), Amazon (9), etc. |
| **1–4 aliases** | 36 | Garmin (1), Cambridge Analytica (1), World Labs (1), etc. |

**Coverage by category:**
- Tech companies: 270+ aliases across 17 clusters
- Government/regulatory: 79 aliases across 7 clusters
- Finance/legal: 107 aliases across 6 clusters
- Academic/research: 109 aliases across 7 clusters
- Media/publishing: 48 aliases across 4 clusters
- Energy/infrastructure: 40 aliases across 2 clusters
- Defense/surveillance: 52 aliases across 4 clusters

---

## Part 9 (Appendix): Entity → Pipeline Interactions

### Entity ↔ Asymmetry Scoring

The primary entity cluster determines which "bucket" an article falls into for the Asymmetry Score (AS) formula:

```
AS = mean(tone_scores_target) - mean(tone_scores_peers)
```

If `get_primary_entity()` returns `"Meta"`, that article's tone contributes to `tone_scores_target`. If it returns `"Google"`, it contributes to `tone_scores_peers`. Misclustering an article directly corrupts the AS.

### Entity ↔ Framing Detection

Several framing devices are entity-aware:
- **CEO Personalization** (device #30) — requires detecting both the CEO alias and the company alias in the same article
- **Isolation Framing** (device #32) — requires identifying which entity is being singled out
- **Competitive Positioning/Deficit** (devices #34–36) — requires detecting multiple entity clusters to identify cross-company comparison

### Entity ↔ Source Analysis

Source extraction distinguishes between entity mentions that are *sources* (quoted, attributed) and entity mentions that are *subjects* (covered, discussed). The `canonical_name` field enables tracking whether `"Andrew Bosworth"` was a source (quoted) or merely mentioned as an organizational figure.

### Entity ↔ Conflict Disclosure

The `ownership.py` and `revenue.py` conflict detectors use entity clusters to identify when a publication covers an entity that its parent company has a financial relationship with. Correct entity detection is prerequisite for accurate conflict flagging.
