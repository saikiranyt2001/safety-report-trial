from fastapi import APIRouter
from sqlalchemy.orm import Session
from backend.database.database import SessionLocal
from backend.database.models import Report

router = APIRouter(tags=["Analytics"])

@router.get("/analytics/safety-metrics")
def get_safety_metrics():
    db = SessionLocal()
    total_reports = db.query(Report).count()
    high_risk = db.query(Report).filter(Report.severity >= 4).count()
    db.close()
    return {
        "total_reports": total_reports,
        "high_risk_reports": high_risk
    }
