from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.services.report_service import generate_report
from backend.celery_app import celery_app

router = APIRouter(tags=["Reports"])

class ReportRequest(BaseModel):
    project_id: int
    hazards: list[str]
    description: str | None = None

@router.post("/generate-report")
def generate_report_endpoint(data: ReportRequest):
    try:
        task = celery_app.send_task("generate_report_task", args=[data.dict()])
        return {"task_id": task.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
