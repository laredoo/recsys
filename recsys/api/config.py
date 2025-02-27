import os

from pydantic_settings import BaseSettings
from typing import List, ClassVar

class Settings(BaseSettings):
    PROJECT_NAME: str = "RecSys API"
    RELEASE_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = "A modern recommendation system"
    
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]

    RULES_PATH: ClassVar[str] = os.environ['RULES_PATH']
    
    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()
