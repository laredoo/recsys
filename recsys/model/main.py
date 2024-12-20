import logging

from root import Factory
from schemas import (
    ModelSchema,
    RepositorySchema
)

LOGGER = logging.getLogger(__name__)

def main():
    LOGGER.info("The Model is STARTED.")

    factory = Factory()

    LOGGER.info("Creating REPOSITORY")
    repository = factory.create_repository(
        RepositorySchema(
            **{
                'playlist_1_path': './dataset/2023_spotify_ds1.csv',
                'playlist_2_path': './dataset/2023_spotify_ds2.csv',
                'songs_path': './dataset/2023_spotify_songs.csv',
            }
        )
    )

    LOGGER.info("Creating model Sample")
    sample = repository.get_sample()


    LOGGER.info("Creating MODEL")
    model = factory.create_model(
        ModelSchema(
            **{
                'sample': sample,
            }
        )
    )

    LOGGER.warning("Fitting model")
    freq_itemset_sample, rules_sample = model.run_model()
    rules_df, freq_itemset_df = model.get_model_df(freq_itemset_sample, rules_sample)
    print(rules_df)

    

if __name__ == "__main__":
    main()