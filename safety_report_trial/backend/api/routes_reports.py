
from fastapi import APIRouter, Query, Body, status, File, UploadFile
from fastapi.responses import JSONResponse
from datetime import datetime
from ..database.database import SessionLocal
from ..database.models import Report

# Create router  ✅ VERY IMPORTANT
router = APIRouter()

# If using a rate limiter
try:
    from fastapi_limiter import Limiter
    from fastapi_limiter.depends import get_remote_address
except ImportError:
    Limiter = None
    get_remote_address = None

# Generate report function
try:
    from ..services.control_agent import generate_document
except ImportError:
    def generate_document(industry, location, hazard, crew):
        return f"Report for {industry}, {location}, {hazard}, {crew}"

# Audit logger
try:
    from ..logs.logger import log_audit_action
except ImportError:
    def log_audit_action(user, action, project_id):
        pass

if Limiter and get_remote_address:
    limiter = Limiter(key_func=get_remote_address)
else:
    class DummyLimiter:
        def limit(self, _):
            def decorator(func):
                return func
            return decorator
    limiter = DummyLimiter()

# Generate Report
@router.post(
    "/generate-report",
    tags=["Reports"],
    summary="Generate a safety report",
    description="Generate a WHS-compliant safety report using AI."
)
@limiter.limit("10/minute")
async def create_report(
    payload: dict = Body(
        ...,
        example={
            "industry": "Construction",
            "hazard": "Fall from height",
            "location": "Site A",
            "crew": "Team Alpha",
            "project_id": 1,
            "severity": 4,
            "likelihood": 5,
            "user": "admin@company.com"
        }
    )
):
    industry = payload.get("industry", "")
    hazard = payload.get("hazard", "")
    location = payload.get("location", "")
    crew = payload.get("crew", "")

    report = generate_document(industry, location, hazard, crew)

    db = SessionLocal()

    project_id = payload.get("project_id", 1)
    severity = payload.get("severity", 1)
    likelihood = payload.get("likelihood", 1)

    new_report = Report(
        project_id=project_id,
        content=report,
        severity=severity,
        likelihood=likelihood,
        created_at=datetime.utcnow()
    )

    db.add(new_report)
    db.commit()
    db.refresh(new_report)
    db.close()

    user = payload.get("user", "unknown")
    log_audit_action(user=user, action="Generated Safety Report", project_id=project_id)

    return JSONResponse(
        content={"report": report, "report_id": new_report.id},
        status_code=status.HTTP_200_OK
    )

# Upload Inspection
@router.post(
    "/upload-inspection",
    tags=["Inspections"],
    summary="Upload inspection file"
)
async def upload_inspection(
    project_id: int = Query(..., description="Project ID"),
    file: UploadFile = File(...)
):
    file_location = f"storage/reports/{file.filename}"

    with open(file_location, "wb") as f:
        f.write(await file.read())

    return {"filename": file.filename, "location": file_location}

# Download Report
@router.get(
    "/download-report/{report_id}",
    tags=["Reports"],
    summary="Download a safety report"
)
async def download_report(report_id: int):
    file_path = f"storage/reports/report_{report_id}.pdf"
    return {"file_path": file_path}