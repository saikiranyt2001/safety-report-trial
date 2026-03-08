class AgentManager:
    def __init__(self, hazard_agent, risk_agent, recommendation_agent, compliance_agent):
        self.hazard_agent = hazard_agent
        self.risk_agent = risk_agent
        self.recommendation_agent = recommendation_agent
        self.compliance_agent = compliance_agent

    def run_analysis(self, site_type, site_data):
        try:
            hazards = self.hazard_agent(site_type, site_data)
            risks = self.risk_agent(hazards)
            controls = self.recommendation_agent(hazards)
            compliance = self.compliance_agent(hazards)
            return {
                "hazards": hazards,
                "risks": risks,
                "controls": controls,
                "compliance": compliance
            }
        except Exception as e:
            return {"error": str(e)}
