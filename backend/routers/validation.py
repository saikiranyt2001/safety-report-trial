from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.agents.validation_agent import ValidationAgent

router = APIRouter(tags=["Validation"])

class ValidationRequest(BaseModel):
    report_text: str

@router.post("/validate")
def validate_report(data: ValidationRequest):
    try:
        agent = ValidationAgent()
        issues = agent.validate_report(data.report_text)
        return {
            "valid": len(issues) == 0,
            "issues": issues
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
