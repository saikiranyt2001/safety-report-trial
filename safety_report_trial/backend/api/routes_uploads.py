from fastapi import APIRouter, File, UploadFile, Query
from fastapi.responses import FileResponse
import os

router = APIRouter()

UPLOAD_DIR = "storage/reports"
# Ensure folder exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post(
    "/upload-inspection",
    tags=["Inspections"],
    summary="Upload inspection file"
)
async def upload_inspection(
    project_id: int = Query(...),
    file: UploadFile = File(...)
):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())
    return {
        "filename": file.filename,
        "location": file_location
    }

@router.get(
    "/download-report/{report_id}",
    tags=["Reports"],
    summary="Download report"
)
async def download_report(report_id: int):
    file_path = os.path.join(UPLOAD_DIR, f"report_{report_id}.pdf")
    if not os.path.exists(file_path):
        return {"error": "Report not found"}
    return FileResponse(
        path=file_path,
        filename=f"report_{report_id}.pdf",
        media_type="application/pdf"
    )
