# Safety Workflow Engine for Industrial Safety Platform
from backend.risk.hazard_library import get_hazards
from backend.risk.risk_matrix import calculate_risk
from backend.risk.control_recommender import recommend_controls
from backend.rag.whs_regulations import get_regulation
from backend.services.report_agent import generate_structured_report


def run_safety_pipeline(data):
    hazards = get_hazards(data.get("site_type", "construction"))
    risks = {h: calculate_risk("Likely", "Major") for h in hazards}  # Example values
    controls = {h: recommend_controls(h) for h in hazards}
    compliance = [get_regulation(h) for h in hazards]
    report = generate_structured_report(data, hazards, risks, controls, compliance)
    return report
