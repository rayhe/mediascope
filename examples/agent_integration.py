"""MediaScope Agent Integration Example.

Shows how an AI agent (any framework) can use MediaScope
as a tool for media accountability research.
"""

import json
import subprocess
import sys
from typing import Any


class MediaScopeAgent:
    """Minimal agent wrapper around MediaScope CLI.
    
    This demonstrates how any AI agent can integrate MediaScope
    using subprocess calls to the CLI. For tighter integration,
    import the Python modules directly.
    """

    def __init__(self):
        self.history = []

    def run_command(self, command: str) -> dict[str, Any]:
        """Run a MediaScope CLI command and return parsed output."""
        full_cmd = f"mediascope {command} --format json"
        result = subprocess.run(
            full_cmd, shell=True, capture_output=True, text=True
        )

        self.history.append({
            "command": full_cmd,
            "returncode": result.returncode,
            "stdout_len": len(result.stdout),
        })

        if result.returncode != 0:
            return {"error": result.stderr, "returncode": result.returncode}

        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError:
            return {"raw_output": result.stdout}

    def investigate_publication(
        self,
        publication: str,
        target: str,
        since: str = "2025-01-01",
    ) -> dict:
        """Full investigation workflow.
        
        An AI agent would call this with natural language translated
        to the structured parameters.
        """
        results = {}

        # Step 1: Ingest articles
        print(f"[Agent] Ingesting articles from {publication}...")
        ingest = self.run_command(
            f"ingest --publication {publication} --since {since}"
        )
        results["ingest"] = ingest

        # Step 2: Analyze
        print(f"[Agent] Analyzing coverage of {target}...")
        analysis = self.run_command(
            f"analyze --publication {publication} --target {target} --since {since}"
        )
        results["analysis"] = analysis

        # Step 3: Score
        print(f"[Agent] Calculating asymmetry scores...")
        scores = self.run_command(
            f"score --publication {publication} --target {target}"
        )
        results["scores"] = scores

        # Step 4: Generate disclosure
        print(f"[Agent] Generating conflict disclosure...")
        disclosure = self.run_command(
            f"disclose --publication {publication} --target {target}"
        )
        results["disclosure"] = disclosure

        return results


# Function calling schema for OpenAI-compatible agents
MEDIASCOPE_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "mediascope_analyze",
            "description": "Analyze a media publication's coverage of a target company for bias, ownership conflicts, and editorial asymmetry. Returns sentiment scores, asymmetry metrics, and conflict disclosures.",
            "parameters": {
                "type": "object",
                "properties": {
                    "publication": {
                        "type": "string",
                        "description": "Publication slug (e.g., 'wired', 'nytimes', 'guardian', 'atlantic', 'mit-tech-review')",
                        "enum": ["wired", "nytimes", "guardian", "atlantic", "mit-tech-review"],
                    },
                    "target_entity": {
                        "type": "string",
                        "description": "Company or entity to check for coverage asymmetry (e.g., 'Meta', 'Google', 'OpenAI')",
                    },
                    "since": {
                        "type": "string",
                        "description": "Start date for analysis (YYYY-MM-DD format)",
                    },
                    "action": {
                        "type": "string",
                        "description": "What to do",
                        "enum": ["full_analysis", "score_only", "disclosure_only", "ingest_only"],
                    },
                },
                "required": ["publication", "target_entity", "action"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "mediascope_disclose",
            "description": "Generate a conflict of interest disclosure statement for a publication's coverage of a target entity.",
            "parameters": {
                "type": "object",
                "properties": {
                    "publication": {
                        "type": "string",
                        "description": "Publication slug",
                    },
                    "target_entity": {
                        "type": "string",
                        "description": "Entity covered",
                    },
                    "article_url": {
                        "type": "string",
                        "description": "Optional: specific article URL",
                    },
                    "format": {
                        "type": "string",
                        "enum": ["full", "social", "json"],
                        "description": "Output format. 'social' is short enough for X/Twitter.",
                    },
                },
                "required": ["publication", "target_entity"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "mediascope_list",
            "description": "List available publication profiles with their conflict counts and coverage stats.",
            "parameters": {
                "type": "object",
                "properties": {},
            },
        },
    },
]


def handle_tool_call(tool_name: str, arguments: dict) -> str:
    """Handle a function call from an AI agent.
    
    This is the bridge between any agent's function calling
    and MediaScope's CLI/API.
    """
    agent = MediaScopeAgent()

    if tool_name == "mediascope_analyze":
        pub = arguments["publication"]
        target = arguments["target_entity"]
        action = arguments.get("action", "full_analysis")
        since = arguments.get("since", "2025-01-01")

        if action == "full_analysis":
            results = agent.investigate_publication(pub, target, since)
            return json.dumps(results, indent=2, default=str)
        elif action == "score_only":
            return json.dumps(agent.run_command(
                f"score --publication {pub} --target {target}"
            ), indent=2, default=str)
        elif action == "disclosure_only":
            return json.dumps(agent.run_command(
                f"disclose --publication {pub} --target {target}"
            ), indent=2, default=str)
        elif action == "ingest_only":
            return json.dumps(agent.run_command(
                f"ingest --publication {pub} --since {since}"
            ), indent=2, default=str)

    elif tool_name == "mediascope_disclose":
        pub = arguments["publication"]
        target = arguments["target_entity"]
        fmt = arguments.get("format", "full")
        article = arguments.get("article_url", "")
        cmd = f"disclose --publication {pub} --target {target} --format {fmt}"
        if article:
            cmd += f" --article-url {article}"
        return json.dumps(agent.run_command(cmd), indent=2, default=str)

    elif tool_name == "mediascope_list":
        return json.dumps(
            agent.run_command("list-publications"),
            indent=2, default=str,
        )

    return json.dumps({"error": f"Unknown tool: {tool_name}"})


if __name__ == "__main__":
    # Demo: run a full investigation
    agent = MediaScopeAgent()
    results = agent.investigate_publication(
        publication="wired",
        target="Meta",
        since="2025-01-01",
    )
    print(json.dumps(results, indent=2, default=str))
