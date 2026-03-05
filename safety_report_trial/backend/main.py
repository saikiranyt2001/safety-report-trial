from fastapi import FastAPI
from safety_report_trial.backend.api.routes_reports import router as report_router

app = FastAPI()

app.include_router(report_router)

@app.get("/")
def home():
    return {"message": "AI Safety Platform Running"}