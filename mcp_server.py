"""MCP server for Revenue Intelligence Deal Risk & Buying Signal Detector."""
import sys
import json
from client import RevenueDealRiskDetector


def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [
                {
                    "name": "evaluate_sales_call_transcript",
                    "description": "Analyzes conversation transcripts to detect customer buying signals, competitor risks, and calculate deal health score",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "transcript_turns": {
                                "type": "array",
                                "description": "Array of turns with 'speaker' (agent/customer) and 'text'",
                            }
                        },
                        "required": ["transcript_turns"],
                    },
                }
            ]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "evaluate_sales_call_transcript":
            res = RevenueDealRiskDetector.evaluate_call_transcript(
                args.get("transcript_turns", [])
            )
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}


if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
