from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from prometheus_fastapi_instrumentator import Instrumentator
import os

print("🚀 Starting AI Safety Platform...")

# Import routers
try:
    from backend.api.routes_reports import router as report_router
    from backend.api.routes_analytics import router as analytics_router
    from backend.api.routes_admin import router as admin_router
    from backend.api.routes_uploads import router as uploads_router
    from backend.api.routes_validation import router as validation_router
    from backend.api.routes_auth import router as auth_router
    print("✅ Routers imported successfully")
except Exception as e:
    print("❌ Router import error:", e)
    raise


# Check environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    print("⚠️ OPENAI_API_KEY is missing")


# Create FastAPI app
app = FastAPI(
    title="AI Safety Platform",
    version="1.0.0"
)


# Prometheus monitoring
Instrumentator().instrument(app).expose(app)


# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register routers
app.include_router(report_router, prefix="/api", tags=["Reports"])
app.include_router(analytics_router, prefix="/api", tags=["Analytics"])
app.include_router(admin_router, prefix="/api", tags=["Admin"])
app.include_router(uploads_router, prefix="/api", tags=["Uploads"])
app.include_router(validation_router, prefix="/api", tags=["Validation"])
app.include_router(auth_router, prefix="/api", tags=["Auth"])


# Static frontend
if os.path.exists("frontend"):
    app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


# Root endpoint
@app.get("/")
def home():
    return {"message": "AI Safety Platform Running"}


# Health check
@app.get("/health")
def health():
    return {"status": "ok"}