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
from safety_report_trial.backend.api.routes_admin import router as admin_router
from safety_report_trial.backend.api.routes_uploads import router as uploads_router
from safety_report_trial.backend.api.routes_validation import router as validation_router
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
from safety_report_trial.backend.database.models import User, Report, Project, Company

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
@app.get("/analytics/{company_id}")
async def analytics(company_id: int):
    db = SessionLocal()
    total_projects = db.query(func.count(Project.id)).filter(Project.company_id == company_id).scalar()
    total_reports = db.query(func.count(Report.id)).join(Project).filter(Project.company_id == company_id).scalar()
    db.close()
    return {"total_projects": total_projects, "total_reports": total_reports}
# Company and project management endpoints
@app.post("/companies")
async def create_company(data: CompanyCreate):
    db = SessionLocal()
    company = Company(name=data.name)
    db.add(company)
    db.commit()
    db.refresh(company)
    db.close()
    return {"id": company.id, "name": company.name}

@app.get("/companies")
async def list_companies():
    db = SessionLocal()
    companies = db.query(Company).all()
    db.close()
    return [{"id": c.id, "name": c.name} for c in companies]

class ProjectCreate(BaseModel):
    name: str
    description: str = ""
    company_id: int

@app.post("/projects")
async def create_project(data: ProjectCreate):
    db = SessionLocal()
    project = Project(name=data.name, description=data.description, company_id=data.company_id)
    db.add(project)
    db.commit()
    db.refresh(project)
    db.close()
    return {"id": project.id, "name": project.name, "description": project.description, "company_id": project.company_id}

@app.get("/projects/{company_id}")
async def list_projects(company_id: int):
    db = SessionLocal()
    projects = db.query(Project).filter(Project.company_id == company_id).all()
    db.close()
    return [{"id": p.id, "name": p.name, "description": p.description} for p in projects]


from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from safety_report_trial.backend.api.routes_reports import router as report_router
from safety_report_trial.backend.api.routes_analytics import router as analytics_router
from safety_report_trial.backend.api.routes_admin import router as admin_router
from safety_report_trial.backend.api.routes_uploads import router as uploads_router
from safety_report_trial.backend.api.routes_validation import router as validation_router

app = FastAPI()

# Prometheus metrics instrumentation
Instrumentator().instrument(app).expose(app, endpoint="/metrics")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend static files
app.mount("/frontend", StaticFiles(directory="../frontend"), name="frontend")
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(report_router)
app.include_router(analytics_router)
app.include_router(admin_router)
app.include_router(uploads_router)
app.include_router(validation_router)

# Login endpoint with access and refresh tokens
@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user = db.query(User).filter(User.username == form_data.username).first()
    db.close()
    if not user or not bcrypt.verify(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = create_access_token({"sub": user.username, "role": user.role.value, "company_id": user.company_id})
    refresh_token = create_refresh_token({"sub": user.username})
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

# Refresh endpoint
from fastapi import Request
class RefreshRequest(BaseModel):
    refresh_token: str

@app.post("/refresh")
async def refresh_token_endpoint(data: RefreshRequest):
    payload = verify_refresh_token(data.refresh_token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
    access_token = create_access_token({"sub": payload["sub"]})
    return {"access_token": access_token, "token_type": "bearer"}

from pydantic import BaseModel
from safety_report_trial.backend.services.report_generator import generate_ai_report


# Professional Safety Report Generation API
class InspectionData(BaseModel):
    company: str
    location: str
    site_type: str
    inspection_date: str
    workers: int
    observations: list
    recommendations: str = ""
    review_date: str = ""

@app.post("/api/structured-report")
async def structured_report(data: InspectionData):
    logger.info(f"Generating structured report for {data.company} at {data.location}")
    hazards = identify_hazards(data.site_type)
    risks = {h: assess_risk(3, 4) for h in hazards}  # Example: Likelihood=3, Severity=4
    controls = {h: generate_recommendations([h]) for h in hazards}
    compliance = [get_compliance_reference(h) for h in hazards]
    report = generate_structured_report(data.dict(), hazards, risks, controls, compliance)
    track_usage(user_id=None, tokens=len(report), reports=1, cost=0)  # Example usage tracking
    return {"report": report}

# Hazard Image Detection API
class ImageUpload(BaseModel):
    image_path: str

@app.post("/api/detect-ppe")
async def detect_ppe_api(data: ImageUpload):
    results = detect_ppe(data.image_path)
    return {"detections": str(results)}


@app.get("/")
def home():
    return {"message": "AI Safety Platform Running"}