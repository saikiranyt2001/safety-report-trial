# routes_reports.py
# Report API routes
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi import Body
from ..services.report_service import generate_document


router = APIRouter()

@router.post("/generate-report")
async def create_report(payload: dict = Body(...)):
    industry = payload.get("industry", "")
    hazard = payload.get("hazard", "")
    location = payload.get("location", "")
    crew = payload.get("crew", "")
    report = generate_document(industry, location, hazard, crew)
    return JSONResponse(content={"report": report}, status_code=status.HTTP_200_OK)