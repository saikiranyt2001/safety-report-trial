from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers.reports import router as report_router
from backend.routers.analytics import router as analytics_router

app = FastAPI(title="AI Safety Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(report_router)
app.include_router(analytics_router)

@app.get("/")
def home():
    return {"message": "AI Safety Platform Running"}