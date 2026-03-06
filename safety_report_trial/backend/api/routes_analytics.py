# Safety KPI Analytics API
from fastapi import APIRouter

router = APIRouter()

@router.get("/analytics/safety-metrics")
def get_safety_metrics():
    # Dummy metrics for demo
    return {
        "total_hazards": 12,
        "high_risk": 3,
        "compliance_score": 87,
        "near_misses": 2,
        "incident_rate": 0.08
    }
