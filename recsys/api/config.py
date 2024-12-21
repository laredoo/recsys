from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "RecSys API"
    RELEASE_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = "A modern recommendation system"
    
    # CORS settings
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]
    
    class Config:
        env_file = ".env"

settings = Settings()
