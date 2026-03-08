from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./safety.db"
    SECRET_KEY: str = "your-secret-key"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 120
    STORAGE_PATH: str = "storage/reports"
    DEBUG: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
