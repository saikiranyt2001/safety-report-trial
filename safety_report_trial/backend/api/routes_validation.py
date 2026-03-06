from fastapi import APIRouter, Body, status
from fastapi.responses import JSONResponse
from ..agents.validation_agent import ValidationAgent

router = APIRouter()

@router.post("/api/validate-report")
async def validate_report(payload: dict = Body(...)):
    try:
        report_text = payload.get("report_text", "")
        hazard_list = payload.get("hazard_list", [])
        regulation_list = payload.get("regulation_list", [])
        agent = ValidationAgent(hazard_list=hazard_list, regulation_list=regulation_list)
        issues = agent.validate_report(report_text)
        return JSONResponse(content={"issues": issues}, status_code=status.HTTP_200_OK)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
