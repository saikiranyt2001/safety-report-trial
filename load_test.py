from locust import HttpUser, task, between

class SafetyPlatformUser(HttpUser):
    host = "http://127.0.0.1:8000"   # IMPORTANT LINE
    wait_time = between(1, 3)

    @task
    def health_check(self):
        self.client.get("/")

    @task
    def generate_report(self):
        self.client.post(
            "/api/generate-report",
            params={
                "report_type": "safety",
                "project_id": 1
            }
        )
