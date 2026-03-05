# routes_reports.py
# Report API routes
from fastapi import APIRouter
from services.report_service import generate_report

router = APIRouter()

@router.post("/generate-report")

def create_report(industry: str, hazard: str):

    report = generate_report(industry, hazard)

    return {"report": report}