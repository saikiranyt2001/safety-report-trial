from fastapi import APIRouter
from agents.safety_advisor_agent import safety_advisor

router = APIRouter()

@router.post("/safety-advisor")
def ask_ai(question: str):
    answer = safety_advisor(question, {})
    return {"response": answer}
