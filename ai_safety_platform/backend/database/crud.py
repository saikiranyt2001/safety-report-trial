from .models import User, Project
from .database import SessionLocal

def create_user(email, password):
	db = SessionLocal()
	user = User(email=email, password=password)
	db.add(user)
	db.commit()
	return user

def create_project(industry, hazard, location, crew):
	db = SessionLocal()
	project = Project(industry=industry, hazard=hazard, location=location, crew=crew)
	db.add(project)
	db.commit()
	return project