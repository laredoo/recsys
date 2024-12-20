import pandas as pd
import logging

from typing import List
from schemas import RepositorySchema

logging.basicConfig(
    level=logging.DEBUG
)

LOGGER = logging.getLogger(__name__)

class Repository:
    def __init__(
        self,
        schema: RepositorySchema,
    ):
        LOGGER.info("Repository is CREATED.")

        self.playlist_1_path = schema.playlist_1_path
        self.playlist_2_path = schema.playlist_2_path
        self.songs_path = schema.songs_path

    def get_songs_df(self) -> pd.DataFrame:

        return pd.read_csv(self.songs_path)

    def get_playlists_df(self) -> pd.DataFrame:

        spotify_playlists_1 = pd.read_csv(self.playlist_1_path).dropna()
        spotify_playlists_2 = pd.read_csv(self.playlist_2_path).dropna()

        spotify_playlists = pd.concat([spotify_playlists_1, spotify_playlists_2], ignore_index=True).drop_duplicates()

        return spotify_playlists
    
    def create_model_sample(self, spotify_playlists: pd.DataFrame) -> List:

        playlist_groups_df = (
            spotify_playlists
            .groupby('pid')
            .agg(
                {
                    'track_uri': list,
                    'track_name': list
                }
            )
            .reset_index(drop=False)
        )

        sample = playlist_groups_df.to_dict('list')['track_name']

        return sample
    
    def get_sample(self):

        playlists_df = self.get_playlists_df()

        sample = self.create_model_sample(playlists_df)

        return sample

