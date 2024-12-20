from pydantic import BaseModel

class RepositorySchema(BaseModel):
    playlist_1_path: str
    playlist_2_path: str
    songs_path: str