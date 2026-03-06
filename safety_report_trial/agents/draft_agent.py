# draft_agent.py
# Generates draft WHS safety report sections with risk matrix calculation
from backend.risk.risk_matrix import calculate_risk

def generate_draft_report(hazard, likelihood, consequence):
    risk_level = calculate_risk(likelihood, consequence)
    report = f"""
Hazard: {hazard}
Likelihood: {likelihood}
Consequence: {consequence}
Risk Level: {risk_level}
"""
    return report
