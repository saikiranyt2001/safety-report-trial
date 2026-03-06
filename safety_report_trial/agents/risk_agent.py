# risk_agent.py
# Handles risk assessment and risk matrix calculations

RISK_MATRIX = {
    ("Rare", "Minor"): "Low",
    ("Possible", "Moderate"): "Medium",
    ("Likely", "Major"): "High",
    ("Almost Certain", "Fatal"): "Extreme"
}

LIKELIHOOD_SCORES = {
    "Rare": 1,
    "Possible": 2,
    "Likely": 3,
    "Almost Certain": 4
}
SEVERITY_SCORES = {
    "Minor": 1,
    "Moderate": 2,
    "Major": 3,
    "Fatal": 4
}

def calculate_risk_score(likelihood, severity):
    return LIKELIHOOD_SCORES.get(likelihood, 0) * SEVERITY_SCORES.get(severity, 0)

def get_risk_level(likelihood, severity):
    return RISK_MATRIX.get((likelihood, severity), "Unknown")
