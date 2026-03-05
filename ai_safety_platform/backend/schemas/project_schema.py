from pydantic import BaseModel

class ProjectCreate(BaseModel):
	industry: str
	hazard: str
	location: str
	crew: int