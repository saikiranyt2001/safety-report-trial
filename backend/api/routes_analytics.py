#done
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database.models import Report
from backend.database.database import SessionLocal
from sqlalchemy import func
from fastapi.security import HTTPBearer

router = APIRouter()
security = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/dashboard/metrics")
async def dashboard_metrics(token=Depends(security), db: Session = Depends(get_db)):
    metrics = db.query(Report.severity, func.count(Report.id)).group_by(Report.severity).all()
    return {"metrics": metrics}
