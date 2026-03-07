from fastapi import APIRouter, Body, Query, File, UploadFile, Depends, HTTPException
from fastapi.responses import FileResponse, JSONResponse
import os
from backend.rag.rag_engine import RAGEngine
from backend.services.report_generator import generate_pdf
from backend.vision.image_analyzer import ImageAnalyzer
from backend.database.database import SessionLocal
from backend.database.models import Project, Report

router = APIRouter()

# Project creation endpoint
@router.post("/create-project")
async def create_project(project_name: str = Body(...), location: str = Body(...)):
    db = SessionLocal()
    project = Project(name=project_name, description=location)
    db.add(project)
    db.commit()
    db.refresh(project)
    db.close()
    return {"project_id": project.id, "project_name": project.name, "location": project.description}

# Report history endpoint
@router.get("/reports")
async def get_reports():
    db = SessionLocal()
    reports = db.query(Report).all()
    result = [
        {
            "report_id": r.id,
            "project": r.project.name if r.project else None,
            "created_at": r.created_at.strftime("%Y-%m-%d")
        } for r in reports
    ]
    db.close()
    return result

# Report chat endpoint
@router.post("/report-chat")
async def report_chat(report_id: int = Body(...), message: str = Body(...)):
    db = SessionLocal()
    report = db.query(Report).filter(Report.id == report_id).first()
    db.close()
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    # Dummy AI response
    answer = f"AI: The report for project '{report.project.name if report.project else 'Unknown'}' says: {report.content}"
    return {"answer": answer}
from fastapi import APIRouter, Body, Query, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
import os
from backend.rag.rag_engine import RAGEngine
from backend.services.report_generator import generate_pdf
from backend.vision.image_analyzer import ImageAnalyzer

router = APIRouter()

# RAG report generation endpoint
@router.post("/generate-rag-report")
async def generate_rag_report(user_request: str = Body(...)):
    rag = RAGEngine()
    context = rag.retrieve(user_request)
    report = rag.generate_report(context, user_request)
    return {"report": report}

# PDF download endpoint
@router.get("/download-report/{report_id}")
async def download_report(report_id: int):
    filename = f"storage/reports/report_{report_id}.pdf"
    if not os.path.exists(filename):
        return JSONResponse(content={"error": "Report not found"}, status_code=404)
    return FileResponse(path=filename, filename=f"report_{report_id}.pdf", media_type="application/pdf")

# Image analysis endpoint
@router.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...)):
    image_path = f"storage/reports/{file.filename}"
    with open(image_path, "wb") as f:
        f.write(await file.read())
    analyzer = ImageAnalyzer()
    hazards = analyzer.analyze(image_path)
    return {"hazards": hazards}
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database.models import Report, Project, User
from backend.database.database import SessionLocal
import jwt
from backend.rag.rag_engine import retrieve_regulation

SECRET_KEY = "your_secret_key"
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@router.get("/reports")
def get_reports(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    user = db.query(User).filter(User.username == payload["sub"]).first()
    return db.query(Report).filter(Report.company_id == user.company_id).all()

@router.post("/report-chat")
def report_chat(report_id: int, question: str, db: Session = Depends(get_db)):
    report = db.query(Report).filter(Report.id == report_id).first()
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    regulations = retrieve_regulation(question)
    if not regulations:
        return {"answer": "No relevant regulations found for your query."}
    formatted = "Relevant regulations for your question:\n"
    for idx, reg in enumerate(regulations, 1):
        formatted += f"{idx}. {reg}\n"
    return {"answer": formatted.strip()}

@router.post("/generate-report")
def generate_report(report_type: str, project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    # Use your agents/templates to generate document
    document = f"Generated {report_type} for project {project.name}"
    return {"document": document}
