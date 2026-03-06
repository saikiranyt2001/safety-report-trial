# Inspection Workflow Engine for Australian WHS
from backend.risk.hazard_library import HAZARDS
from backend.risk.risk_matrix import calculate_risk
from backend.risk.control_recommender import recommend_controls

def run_safety_workflow(site_data):
    hazards = detect_hazards(site_data)
    risks = assess_risk(hazards)
    controls = recommend_controls_for_hazards(hazards)
    report = generate_report(site_data, hazards, risks, controls)
    return report

def detect_hazards(site_data):
    industry = site_data.get("site_type", "construction")
    return HAZARDS.get(industry, [])

def assess_risk(hazards):
    # Dummy likelihood/severity for demo
    return {hazard: calculate_risk(3, 4) for hazard in hazards}

def recommend_controls_for_hazards(hazards):
    return {hazard: recommend_controls(hazard) for hazard in hazards}

def generate_report(site_data, hazards, risks, controls):
    return {
        "site": site_data,
        "hazards": hazards,
        "risks": risks,
        "controls": controls
    }
