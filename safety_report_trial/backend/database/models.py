# Audit model
class Audit(Base):
	__tablename__ = "audits"
	id = Column(Integer, primary_key=True)
	project_id = Column(Integer, ForeignKey("projects.id"))
	completed = Column(Integer, default=0)  # 1=completed, 0=not completed
	created_at = Column(DateTime)
	project = relationship("Project")

# Checklist item model
class ChecklistItem(Base):
	__tablename__ = "checklist_items"
	id = Column(Integer, primary_key=True)
	project_id = Column(Integer, ForeignKey("projects.id"))
	completed = Column(Integer, default=0)  # 1=completed, 0=not completed
	created_at = Column(DateTime)
	project = relationship("Project")

# Regulatory requirement model
class RegulatoryRequirement(Base):
	__tablename__ = "regulatory_requirements"
	id = Column(Integer, primary_key=True)
	project_id = Column(Integer, ForeignKey("projects.id"))
	met = Column(Integer, default=0)  # 1=met, 0=not met
	created_at = Column(DateTime)
	project = relationship("Project")

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from .database import Base
import enum

class RoleEnum(enum.Enum):
	admin = "admin"
	manager = "manager"
	worker = "worker"

class Company(Base):
	__tablename__ = "companies"
	id = Column(Integer, primary_key=True)
	name = Column(String, unique=True, nullable=False)
	users = relationship("User", back_populates="company")
	projects = relationship("Project", back_populates="company")

class User(Base):
	__tablename__ = "users"
	id = Column(Integer, primary_key=True)
	username = Column(String, unique=True, nullable=False)
	password = Column(String, nullable=False)
	role = Column(Enum(RoleEnum), default=RoleEnum.worker)
	company_id = Column(Integer, ForeignKey("companies.id"))
	company = relationship("Company", back_populates="users")

class Project(Base):
	__tablename__ = "projects"
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	description = Column(String)
	company_id = Column(Integer, ForeignKey("companies.id"))
	company = relationship("Company", back_populates="projects")
	created_at = Column(DateTime)
	reports = relationship("Report", back_populates="project")

	__tablename__ = "reports"
	id = Column(Integer, primary_key=True)
	project_id = Column(Integer, ForeignKey("projects.id"))
	project = relationship("Project", back_populates="reports")
	content = Column(String)
	severity = Column(Integer, default=1)      # 1=Minor, 2=Moderate, 3=Major, 4=Catastrophic
	likelihood = Column(Integer, default=1)   # 1=Rare, 2=Unlikely, 3=Possible, 4=Likely, 5=Almost Certain
	created_at = Column(DateTime)

class Usage(Base):
	__tablename__ = "usage"
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
	month = Column(String, nullable=False)  # Format: YYYY-MM
	tokens = Column(Integer, default=0)
	reports = Column(Integer, default=0)
	cost = Column(Integer, default=0)
	report_id = Column(Integer, ForeignKey("reports.id"), nullable=True)
	created_at = Column(DateTime, default=datetime.datetime.utcnow)
	user = relationship("User")
	report = relationship("Report")