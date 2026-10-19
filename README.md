# genpark-revenue-intelligence-deal-risk-and-buying-signal-detector-skill

B2B sales conversation intelligence, buying signal classifier, and multi-factor pipeline deal health risk scorer.

100% Python Standard Library implementation with zero external dependencies.

## Key Capabilities

- **Buying Signal Extraction**: Identifies high-intent signals (procurement process questions, executive sign-off, SOC2/security reviews, go-live timeline requests).
- **Deal Health Risk Scoring**: Quantifies deal momentum and slip likelihood based on objection patterns, ghosting hints, and budget freezes.
- **Actionable Sales Next-Steps**: Automatically emits targeted sales recommendations for account executives.

## Architecture

```
[B2B Sales Call Turns (Rep & Prospect)]
                  │
                  ▼
┌──────────────────────────────────────────────────┐
│             RevenueDealRiskDetector              │
│  - Buying Signal Lexical Classifier              │
│  - Competitor & Budget Risk Evaluator            │
│  - Weighted Deal Health Score Algorithm (0-100)  │
└──────────────────────────────────────────────────┘
                  │
                  ▼
[Deal Health Score & Prescriptive Action Plan]
```

## MCP Server Integration

Run standard MCP stdio server:
```bash
python mcp_server.py
```

Exposed Tools:
- `evaluate_sales_call_transcript`: Analyzes conversation transcripts to detect customer buying signals, competitor risks, and calculate deal health score.

## Quickstart (Python API)

```python
from client import RevenueDealRiskDetector

turns = [{"speaker": "customer", "text": "Our VP approved the budget, please send your payment terms."}]
res = RevenueDealRiskDetector.evaluate_call_transcript(turns)
print("Score:", res["deal_health_score"], "Status:", res["risk_category"])
```

---

## GenPark Ecosystem

- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)
