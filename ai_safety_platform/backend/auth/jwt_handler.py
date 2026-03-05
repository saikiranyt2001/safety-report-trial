from jose import jwt

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

def create_access_token(data: dict):
	return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def verify_access_token(token: str):
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		return payload
	except Exception:
		return None