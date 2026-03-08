from backend.tasks import hazard_task, risk_task

class AgentManager:
    def __init__(self, recommendation_agent, compliance_agent):
        self.recommendation_agent = recommendation_agent
        self.compliance_agent = compliance_agent

    def run_analysis(self, site_type, likelihood, severity):
        try:
            hazard_job = hazard_task.delay(site_type)
            hazards = hazard_job.get()

            risk_job = risk_task.delay(likelihood, severity)
            risk = risk_job.get()

            controls = self.recommendation_agent(hazards)
            compliance = self.compliance_agent(hazards)

            return {
                "hazards": hazards,
                "risk": risk,
                "controls": controls,
                "compliance": compliance
            }
        except Exception as e:
            return {"error": str(e)}
