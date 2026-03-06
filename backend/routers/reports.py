# Reports Router

from fastapi import APIRouter
from backend.services.report_service import generate_report

router = APIRouter()

@router.post("/generate-report")
def generate_report_endpoint(data: dict):
    return generate_report(data)
