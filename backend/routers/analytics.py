from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from backend.database.database import get_db
from backend.database.models import Report, Project

router = APIRouter(tags=["Analytics"])

@router.get("/analytics")
def get_analytics(db: Session = Depends(get_db)):
    total_reports = db.query(func.count(Report.id)).scalar()
    high_risk = db.query(func.count(Report.id)).filter(
        Report.severity >= 4
    ).scalar()
    total_projects = db.query(func.count(Project.id)).scalar()
    return {
        "total_reports": total_reports,
        "high_risk_reports": high_risk,
        "total_projects": total_projects
    }
