from fastapi import APIRouter
from .inspection_service import create_inspection, get_inspections
from .inspection_schema import Inspection
from backend.agents.agent_manager import AgentManager
from backend.agents.hazard_agent import identify_hazards
from backend.agents.risk_agent import assess_risk
from backend.agents.recommendation_agent import generate_recommendations
from backend.agents.compliance_agent import get_compliance_reference

agent_manager = AgentManager(
    identify_hazards,
    assess_risk,
    generate_recommendations,
    get_compliance_reference
)

router = APIRouter()

@router.post("/inspections")
def add_inspection(data: Inspection):
    return create_inspection(data.dict())

@router.get("/inspections")
def list_inspections():
    return get_inspections()

def run_safety_workflow(data):
    site_type = data.get("site_type", "construction")
    results = agent_manager.run_analysis(site_type)
    return results

class AgentManager:
    def __init__(self, hazard_agent, risk_agent, recommendation_agent, compliance_agent):
        self.hazard_agent = hazard_agent
        self.risk_agent = risk_agent
        self.recommendation_agent = recommendation_agent
        self.compliance_agent = compliance_agent

    def run_analysis(self, site_type):
        hazards = self.hazard_agent(site_type)
        risks = self.risk_agent(hazards)
        controls = self.recommendation_agent(hazards)
        compliance = self.compliance_agent(hazards)
        return {
            "hazards": hazards,
            "risks": risks,
            "controls": controls,
            "compliance": compliance
        }
