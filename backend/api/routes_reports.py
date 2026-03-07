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
