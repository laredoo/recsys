from pydantic import BaseModel
from typing import List

from config import settings

class FetcherResponseModel(BaseModel):
    songs: List
    version: str = settings.RELEASE_VERSION
    model_date: str