# Core configuration for AI Safety Platform

import os

class Settings:
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./safety.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS256')

settings = Settings()
