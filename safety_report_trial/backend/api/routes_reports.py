# routes_reports.py
# Report API routes
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi import Body
from ..services.report_service import generate_document
from ..database.models import Report
from ..database.database import SessionLocal
from fastapi import Depends
from datetime import datetime


router = APIRouter()


# Save generated report to DB
@router.post("/generate-report")
async def create_report(payload: dict = Body(...)):
    industry = payload.get("industry", "")
    hazard = payload.get("hazard", "")
    location = payload.get("location", "")
    crew = payload.get("crew", "")
    report = generate_document(industry, location, hazard, crew)
    db = SessionLocal()
    new_report = Report(project_id=payload.get("project_id", 1), content=report, created_at=datetime.utcnow())
    db.add(new_report)
    db.commit()
    db.refresh(new_report)
    db.close()
    return JSONResponse(content={"report": report, "report_id": new_report.id}, status_code=status.HTTP_200_OK)

# Get report history
@router.get("/report-history/{project_id}")
async def get_report_history(project_id: int):
    db = SessionLocal()
    reports = db.query(Report).filter(Report.project_id == project_id).order_by(Report.created_at.desc()).all()
    db.close()
    return [{"id": r.id, "content": r.content, "created_at": r.created_at.isoformat()} for r in reports]