from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from backend.database.models import User
from backend.database.database import SessionLocal
import jwt
import hashlib
from pydantic import BaseModel

SECRET_KEY = "your_secret_key"
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

class LoginData(BaseModel):
    username: str
    password: str

# Simple demo login endpoint for frontend
@router.post("/simple-login")
async def simple_login(data: LoginData):
    print(data.username, data.password)  # Debug print
    if data.username.strip().lower() == "saikiran" and data.password.strip() == "1234":
        return {"success": True}
    return {"success": False}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@router.post("/signup")
def signup(username: str, password: str, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == username).first():
        raise HTTPException(status_code=400, detail="Username already exists")
    user = User(username=username, password_hash=hash_password(password))
    db.add(user)
    db.commit()
    return {"msg": "User created"}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or user.password_hash != hash_password(form_data.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = jwt.encode({"sub": user.username, "role": user.role.value}, SECRET_KEY, algorithm="HS256")
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me")
def get_profile(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {"username": payload["sub"], "role": payload["role"]}
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
