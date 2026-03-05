from fastapi import FastAPI
from ai_safety_platform.backend.api.routes_reports import router as report_router

app = FastAPI()

app.include_router(report_router)

@app.get("/")
def home():
    return {"message": "AI Safety Platform Running"}