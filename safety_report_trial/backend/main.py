from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import openai

from backend.api.routes_reports import router as report_router
from backend.api.routes_analytics import router as analytics_router
from backend.api.routes_admin import router as admin_router
from backend.api.routes_uploads import router as uploads_router
from backend.api.routes_validation import router as validation_router

app = FastAPI(title="AI Safety Platform")

# OpenAI key
openai.api_key = os.getenv("OPENAI_API_KEY")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routers
app.include_router(report_router)
app.include_router(analytics_router)
app.include_router(admin_router)
app.include_router(uploads_router)
app.include_router(validation_router)


@app.get("/")
def home():
    return {"message": "AI Safety Platform Running"}