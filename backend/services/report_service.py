from backend.workflow.safety_pipeline import run_safety_workflow
from backend.services.usage_tracker import track_usage
from celery import Celery

celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0"
)

@celery_app.task
def generate_report_task(data):
    # Run AI workflow
    report = run_safety_workflow(data)
    # Track AI usage
    track_usage(
        user_id=None,
        tokens=len(str(report)),
        reports=1,
        cost=0.02
    )
    return report
