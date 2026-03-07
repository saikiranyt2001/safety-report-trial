#done
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime
from ..services.usage_tracker import get_monthly_usage

router = APIRouter(tags=["Admin"])

@router.get("/admin/monthly-usage")
async def admin_monthly_usage(month: str = None):
    try:
        usage = get_monthly_usage(month)
        return JSONResponse(
            content={
                "month": month or datetime.now().strftime('%Y-%m'),
                "usage": usage
            },
            status_code=200
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))