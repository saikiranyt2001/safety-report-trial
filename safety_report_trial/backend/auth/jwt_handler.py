
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

def create_access_token(data: dict, expires_delta: timedelta = None):
	to_encode = data.copy()
	expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
	to_encode.update({"exp": expire})
	return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(data: dict):
	to_encode = data.copy()
	expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
	to_encode.update({"exp": expire, "type": "refresh"})
	return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_access_token(token: str):
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		return payload
	except Exception:
		return None

def verify_refresh_token(token: str):
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		if payload.get("type") == "refresh":
			return payload
		return None
	except Exception:
		return None