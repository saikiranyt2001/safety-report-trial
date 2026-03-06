from fastapi import APIRouter
from fastapi.responses import JSONResponse
from datetime import datetime
from ..services.usage_tracker import get_monthly_usage

router = APIRouter()

@router.get("/admin/monthly-usage")
async def admin_monthly_usage(month: str = None):
    usage = get_monthly_usage(month)
    return JSONResponse(content={"month": month or datetime.now().strftime('%Y-%m'), "usage": usage}, status_code=200)
