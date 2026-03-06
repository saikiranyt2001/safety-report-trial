from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
import openai
import os

from backend.api.routes_reports import router as report_router
from backend.api.routes_analytics import router as analytics_router
from backend.api.routes_admin import router as admin_router
from backend.api.routes_uploads import router as uploads_router
from backend.api.routes_validation import router as validation_router

from backend.agents.hazard_agent import identify_hazards
from backend.agents.risk_agent import assess_risk
from backend.agents.compliance_agent import get_compliance_reference
from backend.agents.recommendation_agent import generate_recommendations

from backend.services.report_agent import generate_structured_report
from backend.services.usage_tracker import track_usage
from backend.utils.logger import logger

from backend.vision.hazard_detector import detect_ppe

from backend.database.models import User, Report, Project, Company
from backend.database.database import SessionLocal

from sqlalchemy import func
from passlib.hash import bcrypt

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(report_router)
app.include_router(analytics_router)
app.include_router(admin_router)
app.include_router(uploads_router)
app.include_router(validation_router)

# Home
@app.get("/")
def home():
    return {"message": "AI Safety Platform Running"}