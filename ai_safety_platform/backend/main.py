# main.py
# Entry point for backend
from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from generator import generate_document
from audit import audit_document
from document_export import create_word

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Safety Generator Running"}

@app.post("/generate")
def generate(
    industry: str = Form(...),
    location: str = Form(...),
    hazard: str = Form(...),
    crew_size: int = Form(...)
):

    draft = generate_document(industry, location, hazard, crew_size)

    audited = audit_document(draft)

    file_path = create_word(audited)

    return FileResponse(file_path, filename="safety_document.docx")