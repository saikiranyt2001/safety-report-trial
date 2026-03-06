from ..agents.validation_agent import ValidationAgent
# Validate AI report quality
@router.post("/api/validate-report")
async def validate_report(payload: dict = Body(...)):
    report_text = payload.get("report_text", "")
    hazard_list = payload.get("hazard_list", [])
    regulation_list = payload.get("regulation_list", [])
    agent = ValidationAgent(hazard_list=hazard_list, regulation_list=regulation_list)
    issues = agent.validate_report(report_text)
    return JSONResponse(content={"issues": issues}, status_code=status.HTTP_200_OK)
@router.get("/api/safety-kpis")
async def get_safety_kpis():
    db = SessionLocal()
    # Example queries - replace with real logic as needed
    total_hazards = db.query(Report).count()
    high_risk_hazards = db.query(Report).filter((Report.severity * Report.likelihood) >= 3).count()
    near_misses = db.query(Report).filter(Report.content.ilike('%near miss%')).count()
    # Compliance score calculation
    audits_total = db.query(Audit).count()
    audits_completed = db.query(Audit).filter(Audit.completed == 1).count()
    checklist_total = db.query(ChecklistItem).count()
    checklist_completed = db.query(ChecklistItem).filter(ChecklistItem.completed == 1).count()
    reg_total = db.query(RegulatoryRequirement).count()
    reg_met = db.query(RegulatoryRequirement).filter(RegulatoryRequirement.met == 1).count()

    audit_score = (audits_completed / audits_total) * 100 if audits_total else 100
    checklist_score = (checklist_completed / checklist_total) * 100 if checklist_total else 100
    reg_score = (reg_met / reg_total) * 100 if reg_total else 100
    compliance_score = round((audit_score + checklist_score + reg_score) / 3)
    incident_rate = 0.8   # Placeholder, calculate from incident data
    db.close()
    return {
        "totalHazards": total_hazards,
        "highRiskHazards": high_risk_hazards,
        "nearMisses": near_misses,
        "complianceScore": compliance_score,
        "incidentRate": incident_rate
    }
from ..database.models.audit_log import AuditLog
# Admin: Get audit logs
@router.get("/admin/audit-logs")
async def admin_audit_logs():
    db = SessionLocal()
    logs = db.query(AuditLog).order_by(AuditLog.timestamp.desc()).all()
    db.close()
    return [
        {
            "user": log.user,
            "action": log.action,
            "timestamp": log.timestamp.isoformat(),
            "project_id": log.project_id
        } for log in logs
    ]
from ..services.usage_tracker import get_monthly_usage

# Admin: Get monthly usage and cost analytics
@router.get("/admin/monthly-usage")
async def admin_monthly_usage(month: str = None):
    usage = get_monthly_usage(month)
    return JSONResponse(content={"month": month or datetime.now().strftime('%Y-%m'), "usage": usage}, status_code=status.HTTP_200_OK)
# routes_reports.py
# Report API routes

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi import Body
from fastapi import File, UploadFile
from fastapi import Query
from ..services.report_service import generate_document
from ..database.models import Report
from ..database.database import SessionLocal
from ..utils.audit_logger import log_audit_action
from fastapi import Depends
from datetime import datetime
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)


router = APIRouter()


# Save generated report to DB
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
    # Audit log: record action
    user = payload.get("user", "unknown")
    log_audit_action(user=user, action="Generated Safety Report", project_id=project_id)
    return JSONResponse(content={"report": report, "report_id": new_report.id}, status_code=status.HTTP_200_OK)

@router.get(
    "/report-history/{project_id}",
    tags=["Reports"],
    summary="Get report history",
    description="Retrieve all reports for a project, ordered by creation date."
)
async def get_report_history(project_id: int):
    # Upload inspection file
    @router.post(
        "/upload-inspection",
        tags=["Inspections"],
        summary="Upload inspection file",
        description="Upload an inspection document (PDF, DOCX, etc.) for a project."
    )
    async def upload_inspection(
        project_id: int = Query(..., description="Project ID"),
        file: UploadFile = File(...)
    ):
        # Example: Save file to storage
        file_location = f"storage/reports/{file.filename}"
        with open(file_location, "wb") as f:
            f.write(await file.read())
        return {"filename": file.filename, "location": file_location}

    # Download report
    @router.get(
        "/download-report/{report_id}",
        tags=["Reports"],
        summary="Download a safety report",
        description="Download a generated safety report as a file."
    )
    async def download_report(report_id: int):
        # Example: Return file path (implement file serving as needed)
        file_path = f"storage/reports/report_{report_id}.pdf"
        return {"file_path": file_path}
    db = SessionLocal()
    reports = db.query(Report).filter(Report.project_id == project_id).order_by(Report.created_at.desc()).all()
    db.close()
    return [{"id": r.id, "content": r.content, "created_at": r.created_at.isoformat()} for r in reports]