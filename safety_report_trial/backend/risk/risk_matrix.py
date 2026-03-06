# risk_matrix.py
# WHS Risk Matrix Calculation

LIKELIHOOD_SCORES = {
    "Rare": 1,
    "Possible": 2,
    "Likely": 3,
    "Almost Certain": 4
}
CONSEQUENCE_SCORES = {
    "Minor": 1,
    "Moderate": 2,
    "Major": 3,
    "Fatal": 4
}
RISK_LEVELS = {
    (1, 1): "Low",
    (2, 2): "Medium",
    (3, 3): "High",
    (4, 4): "Extreme"
}

def calculate_risk(likelihood, consequence):
    l_score = LIKELIHOOD_SCORES.get(likelihood, 0)
    c_score = CONSEQUENCE_SCORES.get(consequence, 0)
    risk_score = l_score * c_score
    # Map to risk level
    if risk_score >= 12:
        return "Extreme"
    elif risk_score >= 9:
        return "High"
    elif risk_score >= 4:
        return "Medium"
    else:
        return "Low"
