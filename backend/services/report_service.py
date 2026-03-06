# Report Service Business Logic

from backend.workflow.safety_pipeline import run_safety_workflow


def generate_report(data):
    return run_safety_workflow(data)
