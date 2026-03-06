from fastapi import APIRouter, File, UploadFile, Query

router = APIRouter()

@router.post("/upload-inspection", tags=["Inspections"], summary="Upload inspection file")
async def upload_inspection(project_id: int = Query(...), file: UploadFile = File(...)):
    file_location = f"storage/reports/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())
    return {"filename": file.filename, "location": file_location}

@router.get("/download-report/{report_id}", tags=["Reports"], summary="Download report")
async def download_report(report_id: int):
    file_path = f"storage/reports/report_{report_id}.pdf"
    return {"file_path": file_path}
