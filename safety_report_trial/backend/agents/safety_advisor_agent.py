# AI Safety Advisor Agent
from ..risk.hazard_library import HAZARDS
from ..rag.whs_regulations import get_regulation

def analyze_site(site_type, observations):
    hazards = HAZARDS.get(site_type, [])
    risks = {h: "High" for h in hazards}  # Example risk
    recommendations = []
    for h in hazards:
        recommendations.append(f"Review procedures for {h}")
    return {
        "top_risks": hazards,
        "recommendations": recommendations,
        "regulations": [get_regulation(h) for h in hazards]
    }
