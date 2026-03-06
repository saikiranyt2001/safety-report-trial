from fastapi import APIRouter
from .inspection_service import create_inspection, get_inspections
from .inspection_schema import Inspection

router = APIRouter()

@router.post("/inspections")
def add_inspection(data: Inspection):
    return create_inspection(data.dict())

@router.get("/inspections")
def list_inspections():
    return get_inspections()
