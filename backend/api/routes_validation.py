from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from ..agents.validation_agent import ValidationAgent

router = APIRouter(tags=["Validation"])

class ValidationRequest(BaseModel):
    report_text: str
    hazard_list: list[str]
    regulation_list: list[str]

@router.post("/validate-report")
async def validate_report(payload: ValidationRequest):
    try:
        agent = ValidationAgent(
            hazard_list=payload.hazard_list,
            regulation_list=payload.regulation_list
        )
        issues = agent.validate_report(payload.report_text)
        return JSONResponse(
            content={"issues": issues},
            status_code=status.HTTP_200_OK
        )
    except Exception as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )