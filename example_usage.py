"""Example usage for Revenue Intelligence Deal Risk & Buying Signal Detector."""
from client import RevenueDealRiskDetector

if __name__ == "__main__":
    turns = [
        {"speaker": "sales_rep", "text": "Thanks for taking the time today. How are you thinking about next steps?"},
        {"speaker": "customer", "text": "Our VP approved the initiative and we want to understand your payment terms and procurement process for an annual contract."},
        {"speaker": "customer", "text": "Also could you send over your SOC2 report for our security review team?"},
    ]

    res = RevenueDealRiskDetector.evaluate_call_transcript(turns)
    print("Deal Health Score:", res["deal_health_score"], "/ 100")
    print("Risk Category:", res["risk_category"])
    print("Action:", res["recommended_sales_action"])
    for b in res["buying_signals"]:
        print(f"  + Buying Signal [{b['category']}]: {b['matched_triggers']}")
