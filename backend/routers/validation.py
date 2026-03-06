from fastapi import APIRouter

router = APIRouter()

@router.post("/validate")
def validate_report():
    return {"message": "Validation endpoint"}
