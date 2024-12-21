from pydantic import BaseModel
from typing import List

from recsys.api.config import settings

class FetcherResponseModel(BaseModel):
    songs: List
    version: str = settings.PROJECT_VERSION
    model_date: str