from backend.workflow.safety_pipeline import run_safety_workflow
from backend.services.report_agent import generate_structured_report


def generate_report(data):
    workflow_output = run_safety_workflow(data)
    return generate_structured_report(
        data,
        workflow_output["hazards"],
        workflow_output["risks"],
        workflow_output["controls"],
        workflow_output["compliance"]
    )
