# AI Safety Advisor Agent
from ..risk.hazard_library import HAZARDS
from ..rag.whs_regulations import get_regulation

def analyze_site(site_type, observations):
    hazards = HAZARDS.get(site_type, [])

    risks = {}
    recommendations = []

    for h in hazards:
        risks[h] = "High"

        if h.lower() in observations.lower():
            recommendations.append(f"Immediate action required for {h}")
        else:
            recommendations.append(f"Review procedures for {h}")

    return {
        "top_risks": hazards,
        "risk_levels": risks,
        "recommendations": recommendations,
        "regulations": [get_regulation(h) for h in hazards]
    }
