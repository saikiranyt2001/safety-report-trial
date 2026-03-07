import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Database configuration
DATABASE_URL = "postgresql://user:password@localhost:5432/safetydb"