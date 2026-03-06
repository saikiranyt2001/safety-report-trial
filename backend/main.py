from fastapi import FastAPI, HTTPException, Depends, status, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
import openai
import os
from passlib.hash import bcrypt
from safety_report_trial.backend.api.routes_reports import router as report_router
from safety_report_trial.backend.api.routes_analytics import router as analytics_router
from safety_report_trial.backend.workflow.inspection_engine import run_safety_workflow
from safety_report_trial.backend.agents.hazard_agent import identify_hazards
from safety_report_trial.backend.agents.risk_agent import assess_risk
from safety_report_trial.backend.agents.compliance_agent import get_compliance_reference
from safety_report_trial.backend.agents.recommendation_agent import generate_recommendations
from safety_report_trial.backend.services.report_agent import generate_structured_report
from safety_report_trial.backend.services.usage_tracker import track_usage
from safety_report_trial.backend.utils.logger import logger
from safety_report_trial.backend.auth.jwt_handler import create_access_token, create_refresh_token, verify_refresh_token
from safety_report_trial.backend.vision.hazard_detector import detect_ppe

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(data: ChatRequest):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": data.message}],
        max_tokens=300
    )
    return {"reply": response.choices[0].message.content.strip()}
# Analytics endpoint
from safety_report_trial.backend.database.models import Report, Project
from safety_report_trial.backend.database.database import SessionLocal
from sqlalchemy import func