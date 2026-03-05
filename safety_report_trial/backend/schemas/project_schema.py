from pydantic import BaseModel


class ProjectBase(BaseModel):
	name: str
	description: Optional[str] = None
	company_id: int

class ProjectCreate(ProjectBase):
	pass

class Project(ProjectBase):
	id: int
	class Config:
		orm_mode = True