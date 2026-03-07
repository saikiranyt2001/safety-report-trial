from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
import openai

from api.routes_reports import router as report_router
from api.routes_analytics import router as analytics_router
from api.routes_admin import router as admin_router
from api.routes_uploads import router as uploads_router
from api.routes_validation import router as validation_router
from backend.api.routes_auth import router as auth_router

app = FastAPI(title="AI Safety Platform")

# OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(report_router, prefix="/api")
app.include_router(analytics_router, prefix="/api")
app.include_router(admin_router, prefix="/api")
app.include_router(uploads_router, prefix="/api")
app.include_router(validation_router, prefix="/api")
app.include_router(auth_router, prefix="/api")

# Static files for frontend
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

@app.get("/")
def home():
    return {"message": "AI Safety Platform Running"}