import pandas as pd

from typing import List, Dict
from collections import defaultdict

from schemas.request.fetcher import FetcherRequestModel

from schemas.response.fetcher import FetcherResponseModel
import os
import json


class FetcherController:
    def __init__(self):
        pass

    def find_recommendations(
        self, 
        input_songs: List[str], 
        rules_df: pd.DataFrame,
        n_recommendations: int = 10
    ) -> tuple[List[Dict], Dict]:

        input_songs_set = frozenset(input_songs)
        recommendations = defaultdict(lambda: {'confidence': 0.0})
        explanations = defaultdict(list)

        mask = rules_df['antecedent'].apply(lambda row: row.issubset(input_songs_set))
        masked_rules_df = rules_df[mask]

        for idx, rule in masked_rules_df.iterrows():
            antecedent = rule['antecedent']
            consequent = rule['consequent']
            consequent_item = next(iter(consequent)) # maybe think about considering all items as consequent
            
            if consequent_item not in input_songs_set:
                if rule['confidence'] > recommendations[consequent_item]['confidence']:
                    recommendations[consequent_item] = {
                        'confidence': rule['confidence'],
                        'id': idx
                    }

                explanations[consequent_item].append(
                    {
                        'id': idx,
                        'based_on': list(antecedent),
                        'confidence': rule['confidence'],
                    }
                )

        sorted_recommendations = [
            {
                'song': song, 
                **metrics
            }
            
            for song, metrics in recommendations.items()
        ]

        sorted_recommendations.sort(key=lambda x: x['confidence'], reverse=True)

        song_recommendations = [

            data['song']

            for data in sorted_recommendations

        ]
    
        return song_recommendations[:n_recommendations], explanations
    
    def get_recommendations(
            self, 
            model_data: Dict, 
            request: FetcherRequestModel
        ) -> List:

        songs_recommendation, _  = self.find_recommendations(
            input_songs=request.songs, 
            rules_df=model_data['rules']
        )

        model_date = model_data['model_date']

        return songs_recommendation, model_date
    
    def save_recommendations(self, songs: List, model_date) -> None:

        output_dir = os.environ['OUTPUT_PATH']

        recommendations = {
            'songs': songs,
            'model_version': '0.11',
            'model_date': model_date.strftime('%Y-%m-%d %H:%M:%S')
        }

        if not output_dir:
            raise ValueError("Output path environment variable is not set")

        with open(output_dir, 'w') as f:
            json.dump(recommendations, f, indent=4)

    