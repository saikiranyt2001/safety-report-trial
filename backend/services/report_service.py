from backend.workflow.safety_pipeline import run_safety_workflow
from backend.services.usage_tracker import track_usage


def generate_report(data, user_id=None):
    # Run AI workflow
    report = run_safety_workflow(data)
    # Track AI usage
    track_usage(
        user_id=user_id,
        tokens=len(str(report)),
        reports=1,
        cost=0.02
    )
    return report
