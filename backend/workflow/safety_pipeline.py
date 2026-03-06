from agents.hazard_agent import identify_hazards
from agents.risk_agent import assess_risk
from agents.recommendation_agent import generate_recommendations
from agents.compliance_agent import get_compliance_reference
from services.report_service import generate_report

def run_pipeline(site_data):
    hazards = identify_hazards(site_data["site_type"])
    risks = {h: assess_risk(3,4) for h in hazards}
    controls = {h: generate_recommendations([h]) for h in hazards}
    compliance = [get_compliance_reference(h) for h in hazards]
    report = generate_report(site_data, hazards, risks, controls, compliance)
    return report

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

    # Step 6: Report generation
    report = generate_report({
        "company": data.get("company", ""),
        "location": data.get("location", ""),
        "inspection_date": data.get("inspection_date", ""),
        "hazards": hazards,
        "risks": risks,
        "controls": controls,
        "compliance": compliance,
        "recommendations": data.get("recommendations", ""),
        "review_date": data.get("review_date", "")
    })

    return report
