from pydantic import BaseModel

class RepositorySchema(BaseModel):
    playlist_path: str