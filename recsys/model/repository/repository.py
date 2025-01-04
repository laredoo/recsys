import os
import pandas as pd
import logging
import pickle

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

        self.playlist_path = schema.playlist_path

    def get_songs_df(self) -> pd.DataFrame:

        return pd.read_csv(self.songs_path)

    def get_playlists_df(self) -> pd.DataFrame:

        spotify_playlists = pd.read_csv(self.playlist_path).dropna()

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
    
    def export_results(
        self,
        rules_df: pd.DataFrame,
        freq_itemset_df: pd.DataFrame,
        export_path: str
    ):
        
        data_to_save = {
            'frequent_itemsets': freq_itemset_df,
            'rules': rules_df,
        }

        with open(export_path, 'wb') as f:
            pickle.dump(data_to_save, f)



