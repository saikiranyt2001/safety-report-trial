# Risk Agent for Risk Assessment

def calculate_risk_level(score: int) -> str:
    if score >= 16:
        return "Extreme"
    elif score >= 9:
        return "High"
    elif score >= 4:
        return "Medium"
    else:
        return "Low"


def assess_risk(hazards, likelihood: int = 3, severity: int = 3):
    risk_score = likelihood * severity
    level = calculate_risk_level(risk_score)

    return {hazard: level for hazard in hazards}
