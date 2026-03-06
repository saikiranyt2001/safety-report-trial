# Risk Agent for Risk Assessment
from backend.risk.risk_matrix import calculate_risk

def assess_risk(likelihood, severity):
    return calculate_risk(likelihood, severity)
