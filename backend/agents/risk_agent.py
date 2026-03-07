#done
# Risk Agent for Risk Assessment

RISK_PROFILES = {
    "working at height": (5,5),
    "electrical hazard": (4,5),
    "machine entanglement": (3,4)
}

def assess_risk(hazards):
    risks = {}
    for h in hazards:
        likelihood, severity = RISK_PROFILES.get(h, (3,3))
        score = likelihood * severity
        if score >= 16:
            level = "Extreme"
        elif score >= 9:
            level = "High"
        elif score >= 4:
            level = "Medium"
        else:
            level = "Low"
        risks[h] = level
    return risks
