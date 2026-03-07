#done
from backend.agents.hazard_agent import identify_hazards
from backend.agents.risk_agent import assess_risk
from backend.agents.recommendation_agent import generate_recommendations
from backend.agents.compliance_agent import get_compliance_reference


def run_safety_workflow(data):
    # Step 1: Inspection input
    site_type = data.get("site_type", "construction")

    # Step 2: Hazard detection
    hazards = identify_hazards(site_type)

    # Step 3: Risk matrix scoring
    risks = assess_risk(hazards)

    # Step 4: Control recommendation
    controls = generate_recommendations(hazards)

    # Step 5: Regulation matching
    compliance = get_compliance_reference(hazards)

    # Step 6: Compile report data
    report_data = {
        "company": data.get("company", ""),
        "location": data.get("location", ""),
        "inspection_date": data.get("inspection_date", ""),
        "hazards": hazards,
        "risks": risks,
        "controls": controls,
        "compliance": compliance,
        "recommendations": data.get("recommendations", ""),
        "review_date": data.get("review_date", "")
    }

    return report_data
