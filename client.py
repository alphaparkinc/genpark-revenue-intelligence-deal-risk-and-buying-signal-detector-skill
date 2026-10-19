"""Revenue Intelligence Deal Risk and Buying Signal Detector.
100% Python Standard Library.
"""

from typing import List, Dict, Any, Optional
import re


class RevenueDealRiskDetector:
    """Analyzes B2B sales call transcripts and email threads to detect buying signals,
    competitor threats, decision-maker absence, and overall pipeline deal health risks."""

    BUYING_SIGNALS = {
        "pricing_and_procurement": ["how much does it cost", "procurement process", "payment terms", "annual vs monthly", "discount for multi-year"],
        "security_readiness": ["soc2 report", "security review", "privacy team", "compliance checklist"],
        "implementation_urgency": ["roll out date", "kickoff next week", "go-live timeline", "onboarding resources"],
        "executive_alignment": ["vp approved", "cfo signed off", "leadership team is aligned"],
    }

    RISK_SIGNALS = {
        "competitor_entrenchment": ["evaluating other tools", "already using competitor", "prefer their feature set"],
        "ghosting_or_delay": ["revisit next quarter", "freeze on hiring", "budget cut", "put on hold", "too busy right now"],
        "lack_of_authority": ["need to ask my boss", "not my decision", "don't have signing authority"],
        "price_shock": ["way over budget", "cannot justify this cost", "ridiculously expensive"],
    }

    @classmethod
    def evaluate_call_transcript(cls, transcript_turns: List[Dict[str, str]]) -> Dict[str, Any]:
        """Scans conversation turns (`speaker`, `text`) for buying signals and pipeline deal risks."""
        customer_utterances = [
            t.get("text", "") for t in transcript_turns if t.get("speaker", "").lower() in ["customer", "prospect", "buyer"]
        ]
        full_customer_text = " ".join(customer_utterances).lower()

        detected_buying_signals = []
        for category, triggers in cls.BUYING_SIGNALS.items():
            hits = [tr for tr in triggers if tr in full_customer_text]
            if hits:
                detected_buying_signals.append({"category": category, "matched_triggers": hits})

        detected_risk_signals = []
        for category, triggers in cls.RISK_SIGNALS.items():
            hits = [tr for tr in triggers if tr in full_customer_text]
            if hits:
                detected_risk_signals.append({"category": category, "matched_triggers": hits})

        # Calculate composite deal momentum score (0 to 100)
        base_score = 50.0
        base_score += len(detected_buying_signals) * 15.0
        base_score -= len(detected_risk_signals) * 18.0
        deal_health_score = max(5.0, min(95.0, round(base_score, 1)))

        risk_category = "LOW_RISK_HIGH_MOMENTUM"
        if deal_health_score < 40.0:
            risk_category = "CRITICAL_SLIP_RISK"
        elif deal_health_score < 60.0:
            risk_category = "MODERATE_RISK"

        return {
            "deal_health_score": deal_health_score,
            "risk_category": risk_category,
            "buying_signals_count": len(detected_buying_signals),
            "buying_signals": detected_buying_signals,
            "risk_signals_count": len(detected_risk_signals),
            "risk_signals": detected_risk_signals,
            "recommended_sales_action": (
                "Expedite contract generation and secure procurement slot." if deal_health_score >= 60.0
                else "Multi-thread with economic buyer to address stated objections."
            ),
        }
