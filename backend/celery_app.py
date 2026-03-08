from celery import Celery

celery_app = Celery(
    "safety_ai",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

celery_app.conf.task_routes = {
    "tasks.*": {"queue": "safety_queue"}
}
