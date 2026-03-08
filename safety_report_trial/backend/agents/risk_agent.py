# risk_agent.py
# Risk Agent for Risk Assessment

from ..risk.risk_matrix import calculate_risk

def assess_risk(likelihood: str, severity: str):
    if not likelihood or not severity:
        return {
            "risk_level": "Unknown",
            "message": "Missing likelihood or severity"
        }
    try:
        risk_level = calculate_risk(likelihood, severity)
        return {
            "likelihood": likelihood,
            "severity": severity,
            "risk_level": risk_level
        }
    except Exception as e:
        return {
            "risk_level": "Error",
            "message": str(e)
        }
