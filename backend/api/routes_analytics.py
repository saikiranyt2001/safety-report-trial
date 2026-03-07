#done
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database.models import Report
from backend.database.database import SessionLocal
from sqlalchemy import func

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/dashboard/metrics")
def dashboard_metrics(db: Session = Depends(get_db)):
    metrics = db.query(Report.severity, func.count(Report.id)).group_by(Report.severity).all()
    return {"metrics": metrics}
