from fastapi.testclient import TestClient
from backend.main import app
from backend.database.database import Base, engine, SessionLocal
from backend.database.models import Project

# Ensure DB tables exist for tests
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_health():
    response = client.get("/")
    assert response.status_code == 200

def test_generate_report():
    db = SessionLocal()

    # create test project
    project = Project(
        name="Test Project",
        description="Testing",
        company_id=1
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    response = client.post(
        "/api/generate-report",
        params={
            "report_type": "safety",
            "project_id": project.id
        }
    )

    assert response.status_code == 200
