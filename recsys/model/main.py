import logging
import os

from core import Factory
from schemas import (
    ModelSchema,
    RepositorySchema
)

LOGGER = logging.getLogger(__name__)

# testing changes

def main():
    try:
        LOGGER.info("The Model is STARTED.")

        factory = Factory()

        LOGGER.info("Creating REPOSITORY")

        playlist_path = os.environ['PLAYLIST_PATH']
        export_path = os.environ['EXPORT_PATH']

        if not os.path.exists(playlist_path):
                LOGGER.error(f"Playlist file not found: {playlist_path}")
                raise FileNotFoundError(f"Playlist file not found: {playlist_path}")

        repository = factory.create_repository(
            RepositorySchema(
                **{
                    'playlist_path': playlist_path,
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

        LOGGER.info("Exporting results")
        rules_df, freq_itemset_df = model.get_model_df(freq_itemset_sample, rules_sample)
        repository.export_results(rules_df, freq_itemset_df, export_path)
    except Exception as e:
        LOGGER.error(f"An error occurred: {e}", exc_info=True)


if __name__ == "__main__":
    main()