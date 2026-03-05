# AI assistant/chat endpoint
import openai
import os

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

@app.get("/analytics/{company_id}")
async def analytics(company_id: int):
    db = SessionLocal()
    total_projects = db.query(func.count(Project.id)).filter(Project.company_id == company_id).scalar()
    total_reports = db.query(func.count(Report.id)).join(Project).filter(Project.company_id == company_id).scalar()
    db.close()
    return {"total_projects": total_projects, "total_reports": total_reports}
# Company and project management endpoints
from safety_report_trial.backend.database.models import Company, Project
from safety_report_trial.backend.database.database import SessionLocal
from pydantic import BaseModel

class CompanyCreate(BaseModel):
    name: str

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
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from safety_report_trial.backend.api.routes_reports import router as report_router



app = FastAPI()


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



from safety_report_trial.backend.auth.jwt_handler import create_access_token
from safety_report_trial.backend.database.models import User
from safety_report_trial.backend.database.database import SessionLocal
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from passlib.hash import bcrypt
from fastapi import Depends
from fastapi import status

app.include_router(report_router)

# Login endpoint
@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user = db.query(User).filter(User.username == form_data.username).first()
    db.close()
    if not user or not bcrypt.verify(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token({"sub": user.username, "role": user.role.value, "company_id": user.company_id})
    return {"access_token": token, "token_type": "bearer"}

from pydantic import BaseModel
from safety_report_trial.backend.services.report_generator import generate_ai_report

class ReportRequest(BaseModel):
    industry: str
    hazard: str
    location: str
    crew: int

@app.post("/generate-report")
async def generate_report(data: ReportRequest):
    report = generate_ai_report(data.industry, data.hazard, data.location, data.crew)
    return {"report": report}


@app.get("/")
def home():
    return {"message": "AI Safety Platform Running"}