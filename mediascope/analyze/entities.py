"""Entity detection and clustering for media coverage analysis.

Identifies mentions of tech companies, executives, and products in article
text using configurable entity clusters with regex-based matching.

Entity clusters can be specified in two formats:

1. **Dict format** (documented API, used in YAML profiles)::

       {"Meta": {"aliases": ["Meta", "Facebook", ...], "regex": r"\\b(Meta|Facebook)\\b"}}

   The ``regex`` key is optional; if omitted, a word-boundary pattern is
   auto-generated from the alias list.

2. **List format** (shorthand)::

       {"Meta": ["Meta", "Facebook", ...]}

   Automatically wrapped into the dict format internally.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from typing import Any, Union

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Homograph disambiguation: aliases that are also common English words.
# Each key is a lowercased alias; the value is a compiled negative-context
# regex that, if it matches text[end:end+30], indicates verb/adjective usage
# rather than a proper-noun entity reference.
# ---------------------------------------------------------------------------
_HOMOGRAPH_VERB_FILTERS: dict[str, re.Pattern] = {
    # "wired" the verb: "wired into/to/for/in/up/together/through/the"
    "wired": re.compile(
        r"\s+(?:into|to|for|in|up|together|through|the|its|their|his|her)\b",
        re.IGNORECASE,
    ),
}

# ---------------------------------------------------------------------------
# Case-sensitive entity filters: aliases that MUST appear with specific
# capitalisation to count as entity references.  Lowercase occurrences
# are common-noun phrases, not proper nouns.  Each key is the lowercased
# alias; the value is a compiled regex that the *matched text* must satisfy
# (i.e. re.match against the matched string itself, not surrounding context).
# ---------------------------------------------------------------------------
_CASE_SENSITIVE_ENTITIES: dict[str, re.Pattern] = {
    # "The Information" (tech publication) vs "the information" (common
    # noun phrase, e.g. "refusing to provide the information needed").
    # Only match when the I is capitalised.
    "the information": re.compile(r"The Information"),
}

# ---------------------------------------------------------------------------
# Lookbehind homograph filters: aliases that need the PRECEDING context to
# distinguish product names from common English words.  Each key is a
# lowercased alias; the value is a compiled regex that matches the text
# *before* the alias.  If the lookbehind matches, the mention is skipped.
# ---------------------------------------------------------------------------
_HOMOGRAPH_LOOKBEHIND_FILTERS: dict[str, re.Pattern] = {
    # "context windows" / "attention windows" / "sliding windows" etc.
    # are ML/AI terminology, not Microsoft Windows references.
    "windows": re.compile(
        r"(?:context|attention|token|sliding|observation|inference|"
        r"reception|receptive|temporal|overlapping|rolling)\s+$",
        re.IGNORECASE,
    ),
    # "Mid-Atlantic" / "Trans-Atlantic" / "North Atlantic" are geographic
    # references, not The Atlantic magazine.
    "atlantic": re.compile(
        r"(?:mid|trans|north|south|cross)[- ]$",
        re.IGNORECASE,
    ),
    # "District of Columbia" is a geographic entity, not Columbia University.
    "columbia": re.compile(
        r"(?:District\s+of\s+|British\s+)$",
        re.IGNORECASE,
    ),
}

# Type alias — clusters accept either format; code normalizes to dict format.
ClusterEntry = Union[dict[str, Any], list[str]]
ClusterDict = dict[str, ClusterEntry]

# Default entity clusters: canonical name -> {aliases, regex?}
DEFAULT_ENTITY_CLUSTERS: ClusterDict = {
    "Meta": {
        "aliases": [
            "Meta", "Meta Platforms", "Facebook", "Instagram", "WhatsApp",
            "Threads", "Mark Zuckerberg", "Zuckerberg", "Zuck", "Meta AI",
            "Reality Labs", "Oculus", "Ray-Ban Meta", "Ray-Ban",
            "Oakley smart glasses", "Andrew Bosworth", "Bosworth", "Boz",
            "Meta's smart glasses", "Meta's Ray-Ban",
            "Chris Cox", "Maher Saba", "Meta Superintelligence Labs",
            "Applied AI",
            "Model Capability Initiative", "MCI",
            "Agent Transformation Accelerator", "ATA",
            "Stephane Kasriel", "Kasriel",
            "Tracy Clayton", "Dave Arnold", "Andy Stone",
            "NameTag",
            "Alex Himel", "Himel",
            "Ankit Brahmbhatt", "Brahmbhatt",
            "Will Cathcart", "Cathcart",
            "Peter Bristol", "Bristol",
            "Muse Spark", "Muse Image", "Muse Video", "Content Seal",
            "MTIA", "Iris",  # Meta Training and Inference Accelerator chip
            "Mango",  # Internal codename for Muse Image (Jul 2026)
            "Watermelon",  # Next-gen frontier model codename (after Avocado/Muse Spark), 10x compute
            "Creator",  # Meta AI assistant app (Jul 2026)
            "Pocket",  # Meta vibe-code app (Jul 2026)
            "Facebook Marketplace",
            "Meta Fury", "Fury",
            "Adventurer", "Starfire",
            "Meta Ray-Ban Display",
            "Llama 4", "Llama",
            "Joel Kaplan", "Kaplan",
            "Sheryl Sandberg", "Sandberg",
            "Nick Clegg", "Clegg",
            "Dina Powell McCormick",
            "Arena", "Francis Brennan",
            # Virtue AI acqui-hire principals — listed here for reference.
            # Their names are detected through Academic/Research cluster
            # because they are primarily university professors (UIUC, UC
            # Berkeley, Stanford).  The "Virtue AI" alias itself still
            # matches this cluster.
            "Virtue AI",
            "FAIR", "Fundamental AI Research",
            "Ime Archibong", "Archibong",
            "the social media giant", "the social media company",
            "Meta One", "Conversation Focus",
            "Alexandr Wang",
            # LeCun spent a decade as Meta/Facebook's Chief AI Scientist;
            # coverage of his departure is Meta-relevant talent coverage.
            "Yann LeCun", "LeCun",
            # Instagram leadership — key figure in child safety litigation
            "Adam Mosseri", "Mosseri",
            # Meta legal representatives appearing in trial coverage
            "Phyllis Jones",
            # Meta Compute cloud initiative + leadership (Jul 2026)
            "Meta Compute", "Santosh Janardhan", "Janardhan",
            "Daniel Gross",
            "Metamate",  # Internal LLM assistant cited in AI layoff discrimination lawsuit (Jul 2026)
        ],
        "regex": r"(?<!\w)(Meta Compute|Meta Superintelligence Labs|Meta Platforms|Meta Ray-Ban Display|Meta Fury|Meta One|Meta AI|Meta(?!\s+(?:tag|data|description|charset|name|http|content|property|viewport|Compute|Platforms|Ray-Ban|Fury|One|AI|Superintelligence))|Facebook|Instagram|WhatsApp|(?-i:Threads)|Mark Zuckerberg|Zuckerberg|(?-i:Zuck)(?=(?:'s|\s+(?:is|was|has|had|wants?|thinks?|believes?|said|says|will|would|could|should|might|may|does|did|isn|didn|can|won|cannot|also|personally|himself|recently|even|just|too|and|,|'s|')))|Reality Labs|Oculus|Ray-Ban Meta|Ray-Ban|Oakley smart glasses|Andrew Bosworth|Bosworth|Boz|Chris Cox|Maher Saba|Applied AI|Model Capability Initiative|(?-i:MCI)|Agent Transformation Accelerator|(?-i:ATA)|Stephane Kasriel|Kasriel|Tracy Clayton|Dave Arnold|Andy Stone|NameTag|Alex Himel|Himel|Ankit Brahmbhatt|Brahmbhatt|Will Cathcart|Cathcart|Peter Bristol|Bristol|Muse Spark|Muse Image|Muse Video|Content Seal|(?-i:MTIA)|(?-i:Iris)(?=(?:\s|,\s*)(?:chip|accelerator|silicon|production|is|was|will|would|could|plan|design))|(?-i:Mango)(?=(?:\s|,\s*)(?:is|was|code.?named?|model|image|AI|generator))|Facebook Marketplace|(?-i:Creator)(?=(?:\s|,\s*)(?:app|assistant|AI|is|was|and|,))|(?-i:Pocket)(?=(?:\s|,\s*)(?:app|vibe|is|was|and|,))|(?-i:Watermelon)(?=(?:\s|,\s*)(?:model|AI|is|was|has|had|'s|requires?|needs?|costs?|will|would|could|next|compute|training|frontier))|(?-i:Fury)(?=(?:\s|,\s*)(?:glasses|are|is|was|cost|have|included|and|AI|smart))|Adventurer|Starfire|Llama 4|(?:Meta'?s? )(?-i:Llama)|(?-i:Llama)(?=(?:\s|,\s*)(?:model|AI|language|LLM|is|was|and))|Joel Kaplan|Kaplan|Sheryl Sandberg|Sandberg|Nick Clegg|Clegg|Dina Powell McCormick|(?-i:Arena)(?=(?:\s|,\s*)(?:app|prediction|market|is|was|would|will|being|the))|Francis Brennan|Virtue AI|Fundamental AI Research|(?-i:FAIR)(?=(?:\s|,\s*)(?:Lab|lab|research|team|group))|Ime Archibong|Archibong|the social media (?:giant|company)|Conversation Focus|Alexandr Wang|Yann LeCun|(?-i:LeCun)|Adam Mosseri|Mosseri|Phyllis Jones|Santosh Janardhan|Janardhan|Daniel Gross|Metamate)(?!\w)",
    },
    "Cambridge Analytica": {
        "aliases": [
            "Cambridge Analytica",
        ],
        "regex": r"(?<!\w)Cambridge Analytica(?!\w)",
    },
    "Google": {
        "aliases": [
            "Alphabet", "Google", "YouTube", "DeepMind", "Waymo",
            "Sundar Pichai", "Gemini", "Google Cloud", "Android",
            "AlphaFold", "Google Messages",
            "the search giant",
        ],
        "regex": r"(?<!\w)(Alphabet|Google Messages|Google(?!\s+(?:Sheet|Doc|Drive|Form|Search|Messages))|YouTube|DeepMind|Waymo|Sundar Pichai|Gemini|Google Cloud|Android|AlphaFold|the search giant)(?!\w)",
    },
    "Apple": {
        "aliases": [
            "Apple", "iPhone", "iPad", "Tim Cook", "John Ternus",
            "Apple Intelligence", "Apple Vision Pro", "Siri", "macOS",
            "AirPods", "Apple Watch", "iMessage",
        ],
        "regex": r"(?<!\w)(Apple(?!\s+(?:pie|cider|sauce|tree|juice|cinnamon))|iPhone|iPad|Tim Cook|John Ternus|Apple Intelligence|Apple Vision Pro|Siri|macOS|AirPods|Apple Watch|iMessage)(?!\w)",
    },
    "Amazon": {
        "aliases": [
            "Amazon", "AWS", "Alexa", "Jeff Bezos", "Andy Jassy",
            "Amazon Web Services", "Kindle", "Ring", "Prime Video",
        ],
        "regex": r"(?<!\w)(Amazon(?!\s+(?:rain|forest|river|basin))|AWS|Alexa|Jeff Bezos|Andy Jassy|Amazon Web Services|Kindle|Ring|Prime Video)(?!\w)",
    },
    "Microsoft": {
        "aliases": [
            "Microsoft", "Satya Nadella", "Azure", "Bing", "LinkedIn",
            "GitHub", "Copilot", "Xbox", "Windows",
        ],
    },
    "OpenAI": {
        "aliases": [
            "OpenAI", "Sam Altman", "ChatGPT", "GPT-4", "GPT-5",
            "DALL-E", "Sora", "GPT-4o", "Stargate", "Sora 2",
            "Jalapeño",  # OpenAI custom chip codename
            "GPT-2", "gpt-oss",  # Historical + open-weight models
            "Miles Brundage",  # Former OpenAI researcher
        ],
    },
    "X/Twitter": {
        "aliases": [
            "Twitter", "X Corp", "Elon Musk", "Musk",
        ],
        "regex": r"(?<!\w)(Twitter(?!-(?:like|esque|style|inspired))|X Corp|Elon Musk(?!'s xAI)|(?<!Elon\s)Musk(?!\s+(?:Ox|ox|melon|deer)))(?!\w)",
    },
    "xAI": {
        "aliases": [
            "xAI", "SpaceXAI", "Grok", "Colossus", "Colossus II",
        ],
        "regex": r"(?<!\w)(xAI|SpaceXAI|Grok(?!\s+(?:the|TV|Network))|Colossus(?:\s+II)?)(?!\w)",
    },
    "Tesla/SpaceX": {
        "aliases": [
            "Tesla", "SpaceX", "Starlink", "Neuralink",
        ],
        "regex": r"(?<!\w)(Tesla(?!\s+(?:coil|tower|valve))|SpaceX|Starlink|Neuralink)(?!\w)",
    },
    "Nvidia": {
        "aliases": [
            "Nvidia", "NVIDIA", "NVDA", "Jensen Huang", "CUDA", "H100",
            "H200", "A100", "B200", "GB200", "DGX", "GeForce", "Omniverse",
            "Isaac Sim", "NVLink", "Rubin", "Blackwell",
        ],
        "regex": r"(?<!\w)((?-i:NVIDIA|NVDA)|Nvidia|Jensen Huang|(?-i:CUDA)|(?-i:H100|H200|A100|B200|GB200|DGX)|GeForce|Omniverse|Isaac Sim|NVLink|(?-i:Rubin)(?=[,\s]+(?:platform|chip|GPU|system|cycle|generation|architecture|and|later))|(?-i:Blackwell)(?=[,\s]+(?:platform|chip|GPU|system|architecture|cluster|and|later)))(?!\w)",
    },
    "Qualcomm": {
        "aliases": [
            "Qualcomm", "Qualcomm Technologies", "Cristiano Amon",
            "Snapdragon", "Dragonfly", "Hexagon",
        ],
        "regex": r"(?<!\w)(Qualcomm(?:\s+Technologies)?|Cristiano Amon|Snapdragon|Dragonfly(?:\s+C?\d+)?|Hexagon)(?!\w)",
    },
    "Intel": {
        "aliases": [
            "Intel", "Intel Corporation", "Pat Gelsinger", "Lip-Bu Tan",
            "Gaudi", "Xeon", "Intel Foundry",
        ],
        "regex": r"(?<!\w)(Intel(?:\s+(?:Corporation|Foundry))?|Pat Gelsinger|Lip-Bu Tan|(?-i:Gaudi)(?=\s+(?:\d|AI|accelerator|chip|processor))|(?-i:Xeon))(?!\w)",
    },
    "AMD": {
        "aliases": [
            "AMD", "Advanced Micro Devices", "Lisa Su",
            "EPYC", "Ryzen", "Radeon", "Instinct",
        ],
        "regex": r"(?<!\w)((?-i:AMD)|Advanced Micro Devices|Lisa Su|(?-i:EPYC)|Ryzen|Radeon|(?-i:Instinct)(?=\s+(?:MI\d|accelerator|GPU)))(?!\w)",
    },
    "TSMC": {
        "aliases": [
            "TSMC", "Taiwan Semiconductor", "C.C. Wei", "Mark Liu",
        ],
        "regex": r"(?<!\w)((?-i:TSMC)|Taiwan Semiconductor(?:\s+Manufacturing)?)(?!\w)",
    },
    "Micron": {
        "aliases": [
            "Micron", "Micron Technology", "Sanjay Mehrotra",
        ],
        "regex": r"(?<!\w)(Micron(?:\s+Technology)?|Sanjay Mehrotra)(?!\w)",
    },
    "Arm": {
        "aliases": [
            "Arm", "Arm Holdings", "ARM", "Rene Haas",
            "Arm Neoverse", "Neoverse",
        ],
        "regex": r"(?<!\w)((?-i:Arm)(?=\s+(?:Holdings|Neoverse|architecture|chip|processor|design|core|CPU|Ltd|is|was|has|had|'s|,))|(?-i:ARM)(?=\s+(?:chip|processor|core|architecture|design|v\d|Ltd))|Arm Holdings|Rene Haas|(?-i:Neoverse))(?!\w)",
    },
    "Broadcom": {
        "aliases": [
            "Broadcom", "Hock Tan", "VMware",
        ],
        "regex": r"(?<!\w)(Broadcom|Hock Tan|VMware)(?!\w)",
    },
    "CoreWeave": {
        "aliases": [
            "CoreWeave", "Mike Intrator",
        ],
        "regex": r"(?<!\w)(CoreWeave|Mike Intrator)(?!\w)",
    },
    "Nebius": {
        "aliases": [
            "Nebius", "Nebius Group",
        ],
        "regex": r"(?<!\w)(Nebius(?:\s+Group)?)(?!\w)",
    },
    "Palantir": {
        "aliases": [
            "Palantir", "Alex Karp", "Peter Thiel", "Palantir Technologies",
        ],
    },
    "Anthropic": {
        "aliases": [
            "Anthropic", "Anthropic PBC", "Dario Amodei", "Daniela Amodei", "Claude",
            "Mythos", "Fable", "Project Glasswing", "Amanda Askell",
        ],
    },
    "IBM": {
        "aliases": [
            "IBM", "Deep Blue", "Watson", "Red Hat",
        ],
        "regex": r"(?<!\w)((?-i:IBM)|Deep Blue|Watson|Red Hat)(?!\w)",
    },
    "Uber": {
        "aliases": [
            "Uber", "Uber Technologies", "Dara Khosrowshahi",
        ],
        "regex": r"(?<!\w)(Uber(?!\s+Eats)|Uber Technologies|Dara Khosrowshahi)(?!\w)",
    },
    # Added from MIT Tech Review AI agents article (Jul 4, 2026 iteration)
    "Salesforce": {
        "aliases": [
            "Salesforce", "Marc Benioff", "Agentforce",
        ],
    },
    # Added from MIT Tech Review world models article (Jul 4, 2026)
    "World Labs": {
        "aliases": [
            "World Labs",
        ],
        "regex": r"(?<!\w)(World Labs)(?!\w)",
    },
    "Manus AI": {
        "aliases": [
            "Manus", "Butterfly Effect",
        ],
        "regex": r"(?<!\w)((?-i:Manus)(?=\s+(?:AI|app|is|was|the|agent|a |'s|,))|Butterfly Effect)(?!\w)",
    },
    "Duolingo": {
        "aliases": [
            "Duolingo", "Luis von Ahn",
        ],
        "regex": r"(?<!\w)(Duolingo|Luis von Ahn)(?!\w)",
    },
    "US Government": {
        "aliases": [
            "Pentagon", "Department of Defense", "FBI", "CIA",
            "NSA", "National Security Agency",
            "US Marshals Service", "US Special Operations Command",
            "Naval Criminal Investigative Service", "NCIS",
            "Commerce Department", "FTC",
            "ICE", "Immigration and Customs Enforcement",
            "Drug Enforcement Administration", "DEA",
            "Department of Government Efficiency", "DOGE",
            "Internal Revenue Service", "IRS",
            "Centers for Medicare & Medicaid Services", "CMS",
            "Edward Snowden", "Snowden",
            "Bureau of Alcohol Tobacco Firearms", "ATF",
            "Securities and Exchange Commission", "SEC",
            "Justice Department", "Department of Justice", "DOJ",
            "Bureau of Industry and Security", "BIS",
            "Center for AI Standards and Innovation", "CAISI",
            "Howard Lutnick",
            "US Army", "the Army", "Army",
            "US Navy", "US Marine Corps", "US Air Force",
            "US Special Operations Command",
            "White House",
            "ICAC", "Internet Crimes Against Children",
            "Internet Crimes Against Children Task Force",
        ],
        "regex": r"(?<!\w)(Pentagon|Department of Defense|FBI|CIA"
                 r"|NSA|National Security Agency"
                 r"|US Marshals Service|US Special Operations Command"
                 r"|Naval Criminal Investigative Service|(?-i:NCIS)"
                 r"|Commerce Department|(?-i:FTC)"
                 r"|(?-i:ICE)|Immigration and Customs Enforcement"
                 r"|Drug Enforcement Administration|(?-i:DEA)"
                 r"|Department of Government Efficiency|(?-i:DOGE)"
                 r"|Internal Revenue Service|(?-i:IRS)"
                 r"|Centers for Medicare & Medicaid Services|(?-i:CMS)"
                 r"|Edward Snowden|Snowden"
                 r"|Bureau of Alcohol Tobacco Firearms|(?-i:ATF)"
                 r"|Bureau of Industry and Security|(?-i:BIS)"
                 r"|Center for AI Standards and Innovation|(?-i:CAISI)"
                 r"|Howard Lutnick"
                 r"|Securities and Exchange Commission|(?-i:SEC)"
                 r"|Justice Department|Department of Justice|(?-i:DOJ)"
                 r"|(?:US |U\.S\. |the )Army"
                 r"|(?:US |U\.S\. )(?:Navy|Marine Corps|Air Force)"
                 r"|White House"
                 r"|(?-i:ICAC)|Internet Crimes Against Children(?:\s+Task Force)?)(?!\w)",
    },
    "Surveillance/Biometrics": {
        "aliases": [
            "Rank One Computing", "Rank One", "Clearview AI", "Clearview",
            "NEC", "Cognitec", "Idemia", "Palantir Technologies",
        ],
    },
    "Privacy/Civil Liberties Orgs": {
        "aliases": [
            "Electronic Frontier Foundation", "EFF",
            "ACLU", "American Civil Liberties Union",
            "Access Now", "Fight for the Future",
            "Electronic Privacy Information Center", "EPIC",
            "NOYB", "Irish Council for Civil Liberties", "ICCL",
            "Public Citizen",
        ],
    },
    "Media/Publications": {
        "aliases": [
            "The New York Times", "New York Times", "NYT",
            "The Washington Post", "Washington Post",
            "The Guardian", "Guardian",
            "WIRED", "Wired",
            "The Atlantic", "Atlantic",
            "MIT Technology Review",
            "Reuters", "Associated Press", "AP",
            "Bloomberg", "Financial Times",
            "TechCrunch", "The Verge", "Ars Technica",
            "The Information",
            "Business Insider", "404 Media",
            "Gizmodo",
            "The New Yorker", "New Yorker",
            "Fast Company",
            "PYMNTS", "Barron's", "Wall Street Journal", "WSJ",
            # Editorial leaders tracked for career-migration analysis
            "Nicholas Thompson",  # Former Wired EIC (2017-2022), Atlantic CEO (2022-)
        ],
    },
    "Whistleblowers/Critics": {
        "aliases": [
            "Sarah Wynn-Williams", "Wynn-Williams",
            "Frances Haugen", "Haugen",
            "Sophie Zhang",
            "Christopher Wylie", "Wylie",
            "Carole Cadwalladr", "Cadwalladr",
            "Tim Wu",
        ],
    },
    "Defense Tech": {
        "aliases": [
            "Anduril", "Anduril Industries", "Palmer Luckey", "Luckey",
            "Elbit Systems", "Elbit", "Rivet",
            "L3Harris", "Northrop Grumman", "Lockheed Martin",
            "Raytheon", "General Dynamics", "BAE Systems",
            "Shield AI", "Skydio",
            "Quay Barnett", "Barnett",
            "Lattice", "EagleEye",
            "SBMC", "Soldier Born Mission Command",
        ],
    },
    "Policy Research": {
        "aliases": [
            "RAND Corporation", "RAND",
            "Brookings Institution", "Brookings",
            "Center for Strategic and International Studies", "CSIS",
            "Council on Foreign Relations", "CFR",
            "Carnegie Endowment",
            "Pew Research Center", "Pew Research",
            "Graphite",
            "Jonathan Wong",
        ],
    },
    "Political Figures": {
        "aliases": [
            "Donald Trump", "Trump",
            "Joe Biden", "Biden",
            "Kamala Harris",
            "J.D. Vance", "Vance",
        ],
        "regex": r"(?<!\w)(Donald Trump|Trump(?!\s+(?:Tower|Hotel|Organization|National|International))|Joe Biden|Biden|Kamala Harris|J\.?\s*D\.?\s+Vance|Vance)(?!\w)",
    },
    "Labor/Unions": {
        "aliases": [
            "United Tech and Allied Workers", "United Tech & Allied Workers",
            "Communication Workers Union", "CWU",
            "Alphabet Workers Union",
            "SEIU", "AFL-CIO",
            "SAG-AFTRA", "SAG AFTRA", "Screen Actors Guild",
            "Writers Guild of America", "WGA",
            "Directors Guild of America", "DGA",
            "IATSE", "Teamsters",
            "unionize", "unionization", "labor union",
        ],
    },
    "Entertainment/Talent": {
        "aliases": [
            "Creative Artists Agency", "CAA",
            "William Morris Endeavor", "WME",
            "United Talent Agency", "UTA",
            "ICM Partners",
            "Hannah Einbinder",
        ],
    },
    "TikTok": {
        "aliases": [
            "TikTok", "ByteDance", "Shou Zi Chew",
        ],
    },
    "Chinese AI": {
        "aliases": [
            "Zhipu", "Z.ai", "GLM", "DeepSeek", "Baidu", "Alibaba Cloud",
            "Qwen", "Yi", "01.AI", "Moonshot AI", "Kimi",
            "SenseTime", "iFLYTEK",
        ],
    },
    "OpenClaw": {
        "aliases": [
            "OpenClaw", "Hatch",
        ],
        "regex": r"(?<!\w)(OpenClaw|(?-i:Hatch)(?=\s+(?:agent|AI|platform|app|tool|agents)))(?!\w)",
    },
    "Chinese Tech Platforms": {
        "aliases": [
            "Lark", "DingTalk", "Rednote", "Xiaohongshu",
            "WeChat", "Weibo", "Taobao", "Alipay",
            "Tencent", "Alibaba",
        ],
        "regex": r"(?<!\w)((?-i:Lark|DingTalk|Rednote|Xiaohongshu|WeChat|Weibo|Taobao|Alipay)|Tencent|Alibaba(?!\s+Cloud))(?!\w)",
    },
    "Spotify": {
        "aliases": [
            "Spotify", "Daniel Ek",
        ],
    },
    "Snap": {
        "aliases": [
            "Snap", "Snapchat", "Spectacles", "Evan Spiegel",
        ],
        "regex": r"(?<!\w)(Snap(?:chat)?|Spectacles|Evan Spiegel)(?!\w)",
    },
    "Discord": {
        "aliases": [
            "Discord",
        ],
        "regex": r"(?<!\w)(Discord)(?!\w)",
    },
    "Roblox": {
        "aliases": [
            "Roblox", "Roblox Corporation", "David Baszucki",
        ],
        "regex": r"(?<!\w)(Roblox(?:\s+Corporation)?|David Baszucki)(?!\w)",
    },
    "Midjourney": {
        "aliases": [
            "Midjourney", "Midjourney Inc",
        ],
        "regex": r"(?<!\w)(Midjourney(?:\s+Inc\.?)?)(?!\w)",
    },
    "Black Forest Labs": {
        "aliases": [
            "Black Forest Labs", "BFL",
            "FLUX", "FLUX.1",
        ],
        "regex": r"(?<!\w)(Black\s+Forest\s+Labs|(?-i:BFL)(?=\s)|(?-i:FLUX)(?:\.1)?)(?!\w)",
    },
    "Creative Artists Agency": {
        "aliases": [
            "Creative Artists Agency", "CAA",
        ],
        "regex": r"(?<!\w)(Creative\s+Artists?\s+Agency|(?-i:CAA)(?=\s|[,.'\")\]]|$))(?!\w)",
    },
    "EssilorLuxottica": {
        "aliases": [
            "EssilorLuxottica", "Essilor", "Luxottica",
            "Francesco Milleri", "Milleri",
            "LensCrafters",
        ],
    },
    "Garmin": {
        "aliases": [
            "Garmin",
        ],
    },
    "Education/Advocacy": {
        "aliases": [
            "National PTA", "National Education Association", "NEA",
            "American Federation of Teachers", "AFT",
        ],
        "regex": r"(?<!\w)(National PTA"
                 r"|National Education Association|(?-i:NEA)"
                 r"|American Federation of Teachers|(?-i:AFT))(?!\w)",
    },
    "EU Regulatory": {
        "aliases": [
            "GDPR", "General Data Protection Regulation",
            "DPC", "Data Protection Commission",
            "European Commission", "EU Commission",
            "Autorité de la concurrence",
            "France's competition authority",
            "French competition authority",
            "Henna Virkkunen",
            "Margrethe Vestager",
            "Tech Sovereignty, Security and Democracy",
        ],
    },
    "Patent/IP Research": {
        "aliases": [
            "Patentlyze", "PatSnap", "Innography",
            "patent application", "patent filing",
        ],
    },
    "French Media Associations": {
        "aliases": [
            "DVP", "Digital Video Publishers",
            "APIG", "Alliance de la Presse d'Information Générale",
            "Le Monde", "Les Echos",
        ],
        "regex": r"(?<!\w)((?-i:DVP)|Digital Video Publishers"
                 r"|(?-i:APIG)|Alliance de la Presse d'Information G[ée]n[ée]rale"
                 r"|Le Monde|Les Echos)(?!\w)",
    },
    "Data/Intelligence Industry": {
        "aliases": [
            "ShadowDragon", "Babel Street", "LexisNexis",
            "Thomson Reuters CLEAR", "Voyager Labs", "Dataminr",
            "Recorded Future", "Cellebrite", "NSO Group",
            "Pegasus", "S2 Global", "Pen-Link",
        ],
    },
    "VR/Metaverse": {
        "aliases": [
            "Horizon Worlds", "Horizon", "Quest", "Meta Quest",
            "Quest 3S", "Quest 3", "Quest Pro",
            "VRChat", "metaverse",
            "Reality Labs",
        ],
        "regex": r"(?<!\w)(Horizon Worlds|Horizon(?:\s+(?:Spaces|Central|Unity))|"
                 r"(?:Meta\s+)?(?-i:Quest)(?:\s+(?:3S?|Pro))?|VRChat|metaverse|Reality Labs)(?!\w)",
    },
    "Smart Glasses Competitors": {
        "aliases": [
            "Gentle Monster",
            "XREAL", "Even Realities",
            "Halo", "Solos",
            "Brilliant Labs",
        ],
        "regex": r"(?<!\w)(Gentle Monster|(?-i:XREAL)|Even Realities|(?-i:Halo)|Solos|Brilliant Labs)(?!\w)",
    },
    "VC/Tech Investors": {
        "aliases": [
            "Marc Andreessen", "Andreessen",
            "Andreessen Horowitz", "a16z",
            "Sequoia Capital", "Sequoia",
            "Benchmark", "Kleiner Perkins",
            "Y Combinator", "YC",
        ],
        "regex": r"(?<!\w)(Marc Andreessen|Andreessen(?!\s+Horowitz)|Andreessen Horowitz|(?-i:a16z)|Sequoia(?:\s+Capital)?|(?-i:Benchmark)(?=\s+(?:Capital|partner|led|invested|VC|venture|firm|GP|stake))|Kleiner Perkins|Y Combinator|(?-i:YC))(?!\w)",
    },
    "Celebrity/Influencer": {
        "aliases": [
            "Kylie Jenner", "Jenner",
        ],
        "regex": r"(?<!\w)(Kylie Jenner|Jenner(?:'s)?)(?!\w)",
    },
    "Indian Fintech": {
        "aliases": [
            "CRED", "Kunal Shah",
            "PhonePe", "UPI",
        ],
        "regex": r"(?<!\w)((?-i:CRED)|Kunal Shah|PhonePe|(?-i:UPI))(?!\w)",
    },
    "Prediction Markets/Fintech": {
        "aliases": [
            "Polymarket", "Kalshi", "Robinhood", "Interactive Brokers",
            "PredictIt", "Metaculus", "Manifold Markets",
            "CFTC", "Commodity Futures Trading Commission",
            "event contracts", "prediction market",
            "Coatue", "Tarun Chitra",
        ],
        "regex": r"(?<!\w)(Polymarket|Kalshi|Robinhood|Interactive Brokers"
                 r"|PredictIt|Metaculus|Manifold Markets"
                 r"|(?-i:CFTC)|Commodity Futures Trading Commission"
                 r"|event contracts|prediction market"
                 r"|Coatue|Tarun Chitra)(?!\w)",
    },
    "Insurance/Litigation Finance": {
        "aliases": [
            "The Hartford", "Hartford", "Chubb", "ACE American",
            "Flashlight Capital", "Innsworth Capital", "Burford Capital",
            "Marsh", "AIG", "Zurich Insurance", "Lloyd's",
            "Reed Smith", "Calfee Halter",
        ],
        "regex": r"(?<!\w)(The Hartford|Hartford Insurance|Chubb"
                 r"|ACE American|Flashlight Capital|Innsworth Capital"
                 r"|Burford Capital|Reed Smith|Calfee,?\s*Halter"
                 r"|litigation fund(?:ing|er)|third.?party fund(?:ing|er))(?!\w)",
    },
    "Legal/Judicial": {
        "aliases": [
            "Delaware Superior Court", "Delaware Supreme Court",
            "Section 230", "Communications Decency Act",
            "Digital Services Act", "DSA",
        ],
        "regex": r"(?<!\w)(Delaware (?:Superior|Supreme) Court"
                 r"|Section 230|Communications Decency Act"
                 r"|Digital Services Act|(?-i:DSA)"
                 r"|(?-i:MDL)\s*\d+"
                 r"|bellwether (?:trial|verdict|case)"
                 # Federal courts and judges — common in litigation coverage.
                 # Gap discovered in Reuters $1.4T penalty article (Jul 2026):
                 # "U.S. District Judge Yvonne Gonzalez Rogers" was invisible.
                 r"|U\.S\. District (?:Judge|Court)"
                 r"|federal (?:court|trial|judge)"
                 r"|(?:district|circuit|appeals?) court"
                 r"|(?:the )?Supreme Court)(?!\w)",
    },
    # State enforcement entities — state attorneys general are central actors
    # in child safety, antitrust, and consumer protection litigation.  Gap
    # discovered in Reuters $1.4T penalty article (Jul 2026): California,
    # Colorado, Kentucky, and New Jersey AGs were invisible as entities.
    "State Attorneys General": {
        "aliases": [
            "attorney general", "attorneys general",
            "state attorney general", "state attorneys general",
        ],
        "regex": r"(?<!\w)((?:state )?attorney(?:s)? general"
                 r"|(?-i:AG)s?\b"
                 r"|Raúl Torrez|Rob Bonta|Phil Weiser"
                 r"|Matthew Platkin|Russell Coleman"
                 r"|Brenna Bird|Andrea Joy Campbell"
                 r"|Bob Ferguson)(?!\w)",
    },
    "US Congress": {
        "aliases": [
            "Congress", "Senate", "House of Representatives",
            "Senate Judiciary Committee", "Senate Commerce Committee",
            "House Energy and Commerce Committee",
            "lawmakers", "legislators",
        ],
        "regex": r"(?<!\w)(Congress(?:ional)?|(?:the )?Senate(?:\s+(?:Judiciary|Commerce|Intelligence|Armed Services)\s+Committee)?"
                 r"|House of Representatives"
                 r"|House Energy and Commerce Committee"
                 r"|lawmakers|legislators)(?!\w)",
    },
    "Academic/Research": {
        "aliases": [
            "NYU", "New York University",
            "Northeastern University", "Northeastern",
            "Stanford University", "Stanford",
            "MIT", "Massachusetts Institute of Technology",
            "Georgetown University", "Georgetown",
            "UC Berkeley", "University of California",
            "Harvard University", "Harvard",
            "Oxford University", "Oxford",
            "Cambridge University",
            "Columbia University",
            "University of Michigan",
            "Carnegie Mellon", "CMU",
            "Cornell University", "Cornell",
            # Academic journals — frequently cited as authority signals
            "Nature", "Nature Neuroscience", "Nature Medicine",
            "Nature Machine Intelligence", "Nature Communications",
            "Science", "PNAS",
            "The Lancet", "JAMA",
            "Cell",
            "IEEE",
            "ACM",
            # Virtue AI co-founders — primarily academics, secondarily
            # associated with Meta through the acqui-hire.
            "Bo Li", "Dawn Song", "Sanmi Koyejo",
            # Universities that appear as source affiliations
            "Duke University",
            "University of Wisconsin",
            "University of Illinois",
            # Added from MIT Tech Review AI agents article (Jul 4, 2026)
            "University of Montreal",
            "Australian National University",
            "University of Virginia",
            # Added from MIT Tech Review world models article (Jul 4, 2026)
            "Fei-Fei Li",
            "Daron Acemoglu",
            # AI security/agent researchers — appear across multiple MIT TR,
            # NYT, and Wired articles on AI agent vulnerabilities (Jul 5, 2026)
            "Neil Gong",
            "Somesh Jha",
            "Jessica Ji",
            # Added from MIT TR open-weight models article (Jul 9, 2026)
            "Princeton University", "Princeton",
            "Peter Henderson",
            "Percy Liang",
            "Rishi Bommasani",
        ],
        "regex": r"(?<!\w)((?-i:NYU)|New York University"
                 r"|Northeastern(?:\s+University)?"
                 r"|Stanford(?:\s+University)?"
                 r"|(?-i:MIT)|Massachusetts Institute of Technology"
                 r"|Georgetown(?:\s+University)?"
                 r"|(?-i:UC)\s+Berkeley|University of California"
                 r"|Harvard(?:\s+University)?"
                 r"|Oxford(?:\s+University)?"
                 r"|Cambridge(?:\s+University)?"
                 r"|Columbia(?:\s+University)?"
                 r"|University of Michigan"
                 r"|Carnegie Mellon|(?-i:CMU)"
                 r"|Cornell(?:\s+(?:University|Law\s+School))?"
                 r"|Duke University"
                 r"|University of Wisconsin(?:\s+Madison)?"
                 r"|University of Illinois(?:\s+Urbana-Champaign)?"
                 r"|University of Montreal"
                 r"|Australian National University"
                 r"|University of Virginia"
                 r"|Bo Li|Dawn Song|Sanmi Koyejo"
                 r"|Fei-Fei Li|Daron Acemoglu"
                 r"|Neil Gong|Somesh Jha|Jessica Ji"
                 r"|Princeton(?:\s+University)?"
                 r"|Peter Henderson|Percy Liang|Rishi Bommasani"
                 # Academic journals — case-sensitive: "nature" (common
                 # noun) must not match the journal Nature.
                 r"|(?-i:Nature)(?:\s+(?:Neuroscience|Medicine|Machine"
                 r"\s+Intelligence|Communications))?"
                 r"|(?-i:Science)(?=\s+(?:journal|paper|published|study))"
                 r"|(?-i:PNAS)"
                 r"|The\s+Lancet|(?-i:JAMA)"
                 r"|(?-i:Cell)(?=\s+(?:journal|paper|published|study))"
                 r"|(?-i:IEEE)|(?-i:ACM))(?!\w)",
    },
    # Added from MIT TR open-weight models article (Jul 9, 2026)
    "AI Research Orgs": {
        "aliases": [
            "Allen Institute for AI", "AI2",
            "EleutherAI",
        ],
        "regex": r"(?<!\w)(Allen Institute for AI|(?-i:AI2)|EleutherAI)(?!\w)",
    },
    "HuggingFace": {
        "aliases": [
            "HuggingFace", "Hugging Face", "Clement Delangue",
        ],
        "regex": r"(?<!\w)(Hugging\s?Face|Clement Delangue)(?!\w)",
    },
    "Research Centers": {
        "aliases": [
            "Cybersafety Research Center",
            "Center for Countering Digital Hate", "CCDH",
            "Center for Humane Technology",
            "Humane Intelligence",
            "Internet Watch Foundation", "IWF",
            "National Center for Missing & Exploited Children", "NCMEC",
            "CyberTipline",
            "Thorn",
            "Family Online Safety Institute", "FOSI",
            # Added from MIT Tech Review AI agents article (Jul 4, 2026)
            "Centre for the Governance of AI",
            "Palisade Research",
        ],
        "regex": r"(?<!\w)(Cybersafety Research Center"
                 r"|Center for Countering Digital Hate|(?-i:CCDH)"
                 r"|Center for Humane Technology"
                 r"|Humane Intelligence"
                 r"|Internet Watch Foundation|(?-i:IWF)"
                 r"|National Center for Missing (?:&|and) Exploited Children|(?-i:NCMEC)"
                 r"|CyberTip(?:line|s?)"
                 r"|Thorn"
                 r"|Family Online Safety Institute|(?-i:FOSI)"
                 r"|Centre for the Governance of AI"
                 r"|Palisade Research)(?!\w)",
    },
    "Child Safety Legislation": {
        "aliases": [
            "KIDS Act", "Kids Internet Design and Safety Act",
            "COPPA", "Children's Online Privacy Protection Act",
            "KOSA", "Kids Online Safety Act",
            "EARN IT Act",
            "Age Appropriate Design Code",
            "Report Act", "REPORT Act",
        ],
        "regex": r"(?<!\w)((?-i:KIDS)\s+Act|Kids Internet Design and Safety Act"
                 r"|(?-i:COPPA)|Children's Online Privacy Protection Act"
                 r"|(?-i:KOSA)|Kids Online Safety Act"
                 r"|(?-i:EARN\s+IT)\s+Act"
                 r"|Age Appropriate Design Code"
                 r"|(?-i:REPORT)\s+Act|Report Act)(?!\w)",
    },
    "Child Safety Researchers": {
        "aliases": [
            "Arturo Béjar", "Béjar",
            "Lexie Matsumoto", "Matsumoto",
            "Laura Edelson", "Edelson",
            "Damon McCoy",
            "Abdulraheem Arar",
            "Rumman Chowdhury", "Chowdhury",
        ],
    },
    "Australia": {
        "aliases": [
            "Australia", "Australian government",
            "eSafety Commissioner", "Julie Inman Grant", "Inman Grant",
        ],
        "regex": r"(?<!\w)(Australia(?:n(?:\s+government)?)?|eSafety Commissioner|Julie Inman Grant|Inman Grant)(?!\w)",
    },
    "Cybersecurity/Research": {
        "aliases": [
            "Brian Krebs", "Krebs",
            "Jane Manchun Wong",
            "Troy Hunt",
            "Bruce Schneier", "Schneier",
            "Mudge", "Peiter Zatko",
            "METR",
            "CISA",
            "NIST",
        ],
    },
    "AI Infrastructure": {
        "aliases": [
            "Scale AI",
        ],
        "regex": r"(?<!\w)(Scale AI)(?!\w)",
    },
    "AI Chatbot Products": {
        "aliases": [
            "Character.AI", "Character AI",
        ],
        "regex": r"(?<!\w)(Character\.?AI)(?!\w)",
    },
    "Outsourcing/Contractors": {
        "aliases": [
            "Covalen",
            "Sama",
            "Accenture",
        ],
        "regex": r"(?<!\w)(Covalen|Sama(?=\s+(?:issued|employees|redundancy|outsourc|engagement|Meta|content))|Accenture)(?!\w)",
    },
    "Energy/Utilities": {
        "aliases": [
            "Entergy", "Entergy Corporation",
            "Duke Energy", "Duke",
            "Southern Company", "Georgia Power", "Alabama Power",
            "Dominion Energy", "Dominion",
            "NextEra Energy", "NextEra", "FPL",
            "AES Corporation", "AES",
            "Xcel Energy", "Xcel",
            "Eversource", "National Grid",
            "PG&E", "Pacific Gas and Electric",
            "Con Edison", "ConEd",
            "TVA", "Tennessee Valley Authority",
        ],
        "regex": r"(?<!\w)(Entergy(?:\s+Corporation)?|Duke Energy"
                 r"|Southern Company|Georgia Power|Alabama Power"
                 r"|Dominion(?:\s+Energy)?"
                 r"|NextEra(?:\s+Energy)?|(?-i:FPL)"
                 r"|AES(?:\s+Corporation)?|Xcel(?:\s+Energy)?"
                 r"|Eversource|National Grid"
                 r"|(?-i:PG&E)|Pacific Gas and Electric"
                 r"|Con(?:\s+)?Edison|ConEd"
                 r"|(?-i:TVA)|Tennessee Valley Authority)(?!\w)",
    },
    "Energy Research/Regulatory": {
        "aliases": [
            "EPRI", "Electric Power Research Institute",
            "EIA", "Energy Information Administration",
            "LPSC", "Louisiana Public Service Commission",
            "FERC", "Federal Energy Regulatory Commission",
            "Rhodium Group", "Rhodium",
            "IEA", "International Energy Agency",
            "NREL", "National Renewable Energy Laboratory",
            "Department of Energy", "DOE",
        ],
        "regex": r"(?<!\w)((?-i:EPRI)|Electric Power Research Institute"
                 r"|(?-i:EIA)|Energy Information Administration"
                 r"|(?-i:LPSC)|Louisiana Public Service Commission"
                 r"|(?-i:FERC)|Federal Energy Regulatory Commission"
                 r"|Rhodium(?:\s+Group)?"
                 r"|(?-i:IEA)|International Energy Agency"
                 r"|(?-i:NREL)|National Renewable Energy Laboratory"
                 r"|Department of Energy|(?-i:DOE))(?!\w)",
    },
    "Environmental Advocacy": {
        "aliases": [
            "Alliance for Affordable Energy",
            "Union of Concerned Scientists",
            "Southern Environmental Law Center", "SELC",
            "Sierra Club",
            "Greenpeace",
            "Natural Resources Defense Council", "NRDC",
            "Environmental Defense Fund", "EDF",
            "Earthjustice",
            "350.org",
        ],
        "regex": r"(?<!\w)(Alliance for Affordable Energy"
                 r"|Union of Concerned Scientists"
                 r"|Southern Environmental Law Center|(?-i:SELC)"
                 r"|Sierra Club"
                 r"|Greenpeace"
                 r"|Natural Resources Defense Council|(?-i:NRDC)"
                 r"|Environmental Defense Fund|(?-i:EDF)"
                 r"|Earthjustice"
                 r"|350\.org)(?!\w)",
    },
    "Oracle": {
        "aliases": [
            "Oracle", "Oracle Cloud", "Oracle Corporation",
            "Larry Ellison", "Ellison",
            "Safra Catz",
        ],
        "regex": r"(?<!\w)(Oracle(?:\s+(?:Cloud|Corporation))?|Larry Ellison|Ellison(?='s|,|\s+(?:is|was|has|said|also))|Safra Catz)(?!\w)",
    },
    "Samsung": {
        "aliases": [
            "Samsung", "Samsung Electronics", "Samsung Semiconductor",
            "Samsung Foundry", "Samsung HBM",
        ],
        "regex": r"(?<!\w)(Samsung(?:\s+(?:Electronics|Semiconductor|Foundry|HBM))?)(?!\w)",
    },
    "SK Hynix": {
        "aliases": [
            "SK Hynix", "SK hynix", "Hynix",
        ],
        "regex": r"(?<!\w)(SK [Hh]ynix|Hynix)(?!\w)",
    },
    "Semiconductor Equipment": {
        "aliases": [
            "KLA", "KLA Corporation",
            "Lam Research", "Lam",
            "Applied Materials", "AMAT",
            "ASML",
            "Tokyo Electron",
        ],
        "regex": r"(?<!\w)(KLA(?:\s+Corporation)?|Lam Research|(?-i:Lam)(?=\s+(?:Research|is|was|shares?))|Applied Materials|(?-i:AMAT)|(?-i:ASML)|Tokyo Electron)(?!\w)",
    },
    "Sumitomo Electric": {
        "aliases": [
            "Sumitomo Electric", "Sumitomo Electric Industries",
            "Sumitomo",
        ],
        "regex": r"(?<!\w)(Sumitomo(?:\s+Electric(?:\s+Industries)?)?)(?!\w)",
    },
    "Storage/Memory": {
        "aliases": [
            "SanDisk", "Western Digital", "WD",
            "Seagate",
        ],
        "regex": r"(?<!\w)(SanDisk|Western Digital|(?-i:WD)(?=\s+(?:shares?|stock|is|was|drives?))|Seagate)(?!\w)",
    },
    "Financial Services": {
        "aliases": [
            "Visa", "Mastercard", "American Express", "Amex",
            "Goldman Sachs", "JPMorgan", "JPMorgan Chase", "JP Morgan",
            "J.P. Morgan", "J.P.Morgan",
            "Morgan Stanley", "Bank of America", "BofA Securities", "BofA",
            "Citigroup", "Citi",
            "Wells Fargo",
            "PayPal", "Stripe", "Square", "Block Inc",
            "Adyen", "Worldpay", "Fiserv", "FIS",
            "Discover Financial", "Discover",
            "Capital One",
            "SWIFT", "Visa Direct", "Mastercard Send",
            "Bernstein", "Deloitte",
            "D.A. Davidson", "Needham", "Jefferies", "Wedbush",
            "Piper Sandler", "Baird", "Morningstar", "Cowen",
            # Financial research / equity analyst firms (Jul 9)
            "Melius Research", "New Street Research", "New Street",
            "Evercore ISI", "Evercore", "Oppenheimer",
            "Raymond James", "KeyBanc", "KeyBanc Capital Markets",
            "Stifel", "Wolfe Research", "MoffettNathanson",
            "Loop Capital", "Rosenblatt Securities", "Rosenblatt",
            "Berkshire Hathaway", "Warren Buffett", "Buffett",
            # Asset managers / private credit (Jul 13 — data center financing)
            "BlackRock", "Vanguard", "State Street",
            "Blue Owl Capital", "Blue Owl",
            "KKR", "Apollo Global", "Apollo",
            "Brookfield Asset Management", "Brookfield",
            "BNP Paribas",
            # Research firms (Jul 13 — capex analysis)
            "Epoch AI",
        ],
        "regex": r"(?<!\w)(Visa(?!\s+(?:application|interview|status|waiver|holder|stamp|fee|office|policy|requirement|process|categor))|Mastercard|American Express|(?-i:Amex)|Goldman Sachs|J\.P\.?\s*Morgan(?:\s+Chase)?|JPMorgan(?:\s+Chase)?|JP Morgan|Morgan Stanley|Bank of America|BofA(?:\s+Securities)?|Citigroup|(?-i:Citi)(?=\s+(?:is|was|has|had|'s|,|group|bank))|Wells Fargo|PayPal|Stripe(?=\s+(?:is|was|has|had|'s|,|payment|process|partner|integration|Inc|announced|said|report))|Square(?=\s+(?:is|was|has|had|'s|,|payment|terminal|reader|Inc|announced|said))|Block Inc|Adyen|Worldpay|Fiserv|(?-i:FIS)(?=\s+(?:is|was|has|had|payment|process|Global))|Discover Financial|Capital One|(?-i:SWIFT)(?=\s+(?:network|payment|transfer|system|code|message))|Visa Direct|Mastercard Send|Bernstein|Deloitte|D\.A\.\s*Davidson|Needham|Jefferies|Wedbush|Piper\s+Sandler|Baird|Morningstar|Cowen|Melius\s+Research|New\s+Street(?:\s+Research)?|Evercore(?:\s+ISI)?|Oppenheimer|Raymond\s+James|KeyBanc(?:\s+Capital\s+Markets)?|Stifel|Wolfe\s+Research|MoffettNathanson|Loop\s+Capital|Rosenblatt(?:\s+Securities)?|Berkshire Hathaway|Warren Buffett|(?-i:Buffett)(?=\s+(?:is|was|has|had|'s|,|said|warned|portfolio|stake))|BlackRock|Vanguard|State Street|Blue\s+Owl(?:\s+Capital)?|(?-i:KKR)|Apollo(?:\s+Global)?|Brookfield(?:\s+Asset\s+Management)?|BNP\s+Paribas|Epoch\s+AI)(?!\w)",
    },
    # Privacy & digital rights advocacy organizations — needed to track
    # non-Meta sources frequently cited in privacy/AI backlash coverage.
    # Gap discovered during The Tab Muse Image analysis (Jul 2026):
    # Foxglove and Privacy International appeared as sources but had no
    # entity cluster, so entity distribution was 100% Meta-cluster.
    "Privacy Advocacy": {
        "aliases": [
            "Foxglove", "Privacy International",
            "Electronic Frontier Foundation", "EFF",
            "Access Now", "Big Brother Watch",
            "Open Rights Group", "ORG",
            "Center for AI and Digital Policy", "CAIDP",
            "noyb", "NOYB",
            "Fight for the Future",
            "Digital Rights Foundation",
            "Ranking Digital Rights",
            "AlgorithmWatch",
        ],
        "regex": r"(?<!\w)(Foxglove|Privacy International|Electronic Frontier Foundation|(?-i:EFF)(?=\s+(?:is|was|has|had|'s|,|said|argued|warned|filed|called|urged))|Access Now|Big Brother Watch|Open Rights Group|(?-i:ORG)(?=\s+(?:is|was|has|had|'s|,|said|argued))|Center for AI and Digital Policy|(?-i:CAIDP)|(?-i:noyb|NOYB)|Fight for the Future|Digital Rights Foundation|Ranking Digital Rights|AlgorithmWatch)(?!\w)",
    },
}


@dataclass
class EntityMention:
    """A single entity mention detected in text."""

    entity: str          # The exact text matched
    canonical_name: str  # The canonical alias name (e.g., "Mark Zuckerberg")
    cluster: str         # The cluster this belongs to (e.g., "Meta")
    start: int           # Character offset start
    end: int             # Character offset end
    context: str = ""    # Surrounding sentence for context


def _normalize_cluster(entry: ClusterEntry) -> dict[str, Any]:
    """Normalize a cluster entry to the dict format ``{aliases: [...], regex?: str}``.

    Accepts either a plain list of aliases (shorthand) or the full dict format.
    """
    if isinstance(entry, list):
        return {"aliases": entry}
    if isinstance(entry, dict):
        # Already in dict format — ensure "aliases" key exists
        if "aliases" not in entry:
            logger.warning("Cluster dict missing 'aliases' key: %s", list(entry.keys()))
            return {"aliases": []}
        return entry
    raise TypeError(f"Cluster entry must be a list or dict, got {type(entry).__name__}")


def _build_patterns(
    clusters: ClusterDict,
) -> list[tuple[re.Pattern, str, str]]:
    """Build compiled regex patterns from entity clusters.

    Handles both formats:
    - Dict format: ``{aliases: [...], regex?: "..."}``
    - List format: ``["alias1", "alias2", ...]``

    When a cluster provides a ``regex`` key, that pattern is compiled once for
    the whole cluster.  The canonical name for each match is resolved at match
    time (see ``detect_entities``); the tuple stores the alias list so the
    closest alias can be found.

    Returns a list of (compiled_pattern, canonical_name_or_aliases, cluster_name)
    tuples.  For cluster-level regex patterns, canonical_name_or_aliases is the
    alias list (as a ``|``-joined string prefixed with ``__ALIASES__:``); for
    individual alias patterns, it is the alias string itself.
    """
    # Phase 1: clusters that supply their own regex — one pattern per cluster
    cluster_patterns: list[tuple[re.Pattern, str, str]] = []
    # Phase 2: individual alias patterns for clusters without custom regex
    alias_entries: list[tuple[str, str, str]] = []

    for cluster_name, raw_entry in clusters.items():
        entry = _normalize_cluster(raw_entry)
        aliases: list[str] = entry.get("aliases", [])
        custom_regex: str | None = entry.get("regex")

        if custom_regex:
            try:
                compiled = re.compile(custom_regex, re.IGNORECASE)
                # Store aliases for later canonical-name resolution
                aliases_tag = "__ALIASES__:" + "|".join(aliases)
                cluster_patterns.append((compiled, aliases_tag, cluster_name))
            except re.error as exc:
                logger.warning(
                    "Invalid regex for cluster %s, falling back to alias matching: %s",
                    cluster_name,
                    exc,
                )
                # Fall through to alias-based matching
                for alias in aliases:
                    alias_entries.append((alias, alias, cluster_name))
        else:
            for alias in aliases:
                alias_entries.append((alias, alias, cluster_name))

    # Sort alias entries by length descending so longer/more-specific patterns match first
    alias_entries.sort(key=lambda x: len(x[0]), reverse=True)

    alias_patterns: list[tuple[re.Pattern, str, str]] = []
    for alias, canonical, cluster in alias_entries:
        escaped = re.escape(alias)
        # Replace escaped literal spaces with \s+ to handle line breaks and
        # multiple whitespace in article text (e.g. "The New York\nTimes")
        escaped = re.sub(r"\\ ", r"\\s+", escaped)
        pattern = re.compile(
            rf"(?<!\w){escaped}(?![\w]|-(?:like|esque|style|inspired|adjacent)\b)",
            re.IGNORECASE,
        )
        alias_patterns.append((pattern, canonical, cluster))

    # Cluster-level patterns first (they tend to be more precise), then alias patterns
    return cluster_patterns + alias_patterns


def _resolve_canonical(matched_text: str, aliases_tag: str) -> str:
    """Resolve the canonical name for a cluster-level regex match.

    When a cluster uses a custom regex, the matched text could be any
    entity in the cluster (e.g., "Andrew Bosworth" from the Meta cluster).
    This function finds the closest alias to use as the canonical name,
    preserving individual entity identity instead of collapsing everything
    to the first alias.

    Args:
        matched_text: The actual text matched by the regex.
        aliases_tag: The ``__ALIASES__:...`` string from ``_build_patterns``.

    Returns:
        The best canonical name — either an exact alias match or the
        matched text itself if no alias matches.
    """
    aliases_str = aliases_tag.removeprefix("__ALIASES__:")
    aliases = aliases_str.split("|")

    # Try exact match (case-insensitive) first
    matched_lower = matched_text.lower()
    for alias in aliases:
        if alias.lower() == matched_lower:
            return alias

    # Try substring containment — e.g., matched "Bosworth" is contained in
    # alias "Andrew Bosworth"
    for alias in aliases:
        if matched_lower in alias.lower() or alias.lower() in matched_lower:
            return alias

    # Fallback: return matched text as-is (preserves entity identity)
    return matched_text


def _extract_sentence(text: str, start: int, end: int) -> str:
    """Extract the sentence containing the character range [start, end).

    Uses simple sentence boundary detection (period, question mark,
    exclamation mark followed by space or end of text).
    """
    # Find sentence start: search backwards for sentence boundary
    sent_start = 0
    for i in range(start - 1, -1, -1):
        if text[i] in ".!?" and (i + 1 >= len(text) or text[i + 1] in " \n\t"):
            sent_start = i + 1
            break

    # Find sentence end: search forwards for sentence boundary
    sent_end = len(text)
    for i in range(end, len(text)):
        if text[i] in ".!?" and (i + 1 >= len(text) or text[i + 1] in " \n\t"):
            sent_end = i + 1
            break

    return text[sent_start:sent_end].strip()


def detect_entities(
    text: str,
    clusters: ClusterDict | None = None,
) -> list[EntityMention]:
    """Detect entity mentions in text using cluster-based matching.

    Args:
        text: The article text to analyze.
        clusters: Entity clusters dict (dict or list format). If None, uses
            DEFAULT_ENTITY_CLUSTERS.

    Returns:
        List of EntityMention objects sorted by position in text.
    """
    if not text:
        return []

    if clusters is None:
        clusters = DEFAULT_ENTITY_CLUSTERS

    patterns = _build_patterns(clusters)
    mentions: list[EntityMention] = []
    # Track covered character spans to avoid overlapping matches
    covered: list[tuple[int, int]] = []

    for pattern, canonical, cluster in patterns:
        for match in pattern.finditer(text):
            start, end = match.start(), match.end()

            # Skip if this span overlaps with an already-matched (longer) span
            if any(
                not (end <= cov_start or start >= cov_end)
                for cov_start, cov_end in covered
            ):
                continue

            # Disambiguate homographs (e.g. "wired" verb vs WIRED pub)
            matched_lower = match.group().lower()
            if matched_lower in _HOMOGRAPH_VERB_FILTERS:
                lookahead = text[end : end + 30]
                if _HOMOGRAPH_VERB_FILTERS[matched_lower].match(lookahead):
                    # Exception: attribution contexts like "by Wired",
                    # "from Wired", "reported by Wired", "says Wired"
                    # indicate proper-noun usage even when followed by
                    # a preposition that would normally trigger the
                    # verb filter.
                    lookback_hom = text[max(0, start - 30) : start]
                    _ATTRIBUTION_OVERRIDE = re.compile(
                        r"(?:by|from|per|says|said|told|reported\s+by|"
                        r"found\s+by|according\s+to|source[sd]?\s+by|"
                        r"covered\s+by|published\s+by)\s*$",
                        re.IGNORECASE,
                    )
                    if not _ATTRIBUTION_OVERRIDE.search(lookback_hom):
                        continue

            # Lookbehind homograph filter (e.g. "context windows" vs Windows)
            if matched_lower in _HOMOGRAPH_LOOKBEHIND_FILTERS:
                lookbehind = text[max(0, start - 40) : start]
                if _HOMOGRAPH_LOOKBEHIND_FILTERS[matched_lower].search(lookbehind):
                    continue

            # Case-sensitive entity filter (e.g. "The Information" pub vs
            # "the information" common noun)
            if matched_lower in _CASE_SENSITIVE_ENTITIES:
                if not _CASE_SENSITIVE_ENTITIES[matched_lower].match(match.group()):
                    continue

            # Disambiguate "Access Now" (org) from "Access now" (verb phrase)
            # at sentence start.  The org name requires mid-sentence context
            # (not preceded by sentence boundary).
            if matched_lower == "access now":
                _lookback_an = text[max(0, start - 3):start]
                if start == 0 or _lookback_an.rstrip().endswith(('.', '!', '?', '\n')):
                    # Likely sentence-start verb phrase, not the organization
                    continue

            covered.append((start, end))
            context = _extract_sentence(text, start, end)

            # Resolve canonical name for cluster-level regex matches
            resolved_canonical = canonical
            if canonical.startswith("__ALIASES__:"):
                resolved_canonical = _resolve_canonical(match.group(), canonical)

            mentions.append(
                EntityMention(
                    entity=match.group(),
                    canonical_name=resolved_canonical,
                    cluster=cluster,
                    start=start,
                    end=end,
                    context=context,
                )
            )

    # Sort by position in text
    mentions.sort(key=lambda m: m.start)
    return mentions


def get_primary_entity(mentions: list[EntityMention]) -> str | None:
    """Determine which entity cluster the article is primarily about.

    Based on mention count — the cluster with the most mentions is primary.

    Args:
        mentions: List of EntityMention objects from detect_entities().

    Returns:
        The cluster name with the most mentions, or None if no mentions.
    """
    if not mentions:
        return None

    dist = get_entity_distribution(mentions)
    if not dist:
        return None

    return max(dist, key=dist.get)


def get_entity_distribution(mentions: list[EntityMention]) -> dict[str, int]:
    """Count entity mentions per cluster.

    Args:
        mentions: List of EntityMention objects.

    Returns:
        Dict mapping cluster name to mention count, sorted by count descending.
    """
    counts: dict[str, int] = {}
    for mention in mentions:
        counts[mention.cluster] = counts.get(mention.cluster, 0) + 1

    # Sort by count descending
    return dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))


def load_clusters_from_yaml(path: str) -> ClusterDict:
    """Load custom entity clusters from a YAML file.

    Supports both formats::

        # Dict format (recommended)
        Meta:
          aliases:
            - Meta Platforms
            - Facebook
          regex: "\\\\b(Meta|Facebook)\\\\b"

        # List format (shorthand)
        Google:
          - Alphabet
          - Google

    Args:
        path: Path to the YAML file.

    Returns:
        Dict mapping cluster name to cluster entry.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the YAML structure is invalid.
    """
    import yaml

    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not isinstance(data, dict):
        raise ValueError(f"Entity clusters YAML must be a mapping, got {type(data).__name__}")

    clusters: ClusterDict = {}
    for cluster_name, entry in data.items():
        if isinstance(entry, list):
            clusters[str(cluster_name)] = [str(a) for a in entry]
        elif isinstance(entry, dict):
            clusters[str(cluster_name)] = entry
        else:
            logger.warning(
                "Skipping cluster %s: expected list or dict, got %s",
                cluster_name,
                type(entry).__name__,
            )

    return clusters


def merge_clusters(
    base: ClusterDict,
    override: ClusterDict,
) -> ClusterDict:
    """Merge two cluster dicts, with override adding to/replacing base entries.

    Args:
        base: The base clusters (e.g., DEFAULT_ENTITY_CLUSTERS).
        override: Additional or replacement clusters.

    Returns:
        Merged cluster dict. Override clusters replace base clusters of the
        same name entirely.
    """
    merged = dict(base)
    for cluster_name, entry in override.items():
        merged[cluster_name] = entry
    return merged
