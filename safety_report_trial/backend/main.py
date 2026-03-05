

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from safety_report_trial.backend.api.routes_reports import router as report_router



app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend static files
app.mount("/frontend", StaticFiles(directory="../frontend"), name="frontend")


app.include_router(report_router)

@app.get("/")
def home():
    return {"message": "AI Safety Platform Running"}