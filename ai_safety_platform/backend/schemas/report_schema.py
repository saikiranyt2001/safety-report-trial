from pydantic import BaseModel

class ReportCreate(BaseModel):
	project_id: int
	content: str