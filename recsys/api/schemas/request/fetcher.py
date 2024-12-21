from pydantic import BaseModel
from typing import List

class FetcherRequestModel(BaseModel):
    songs: List