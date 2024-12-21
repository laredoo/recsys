import logging

from common import Model
from repository import Repository
from schemas import (
    ModelSchema,
    RepositorySchema
)

logging.basicConfig(
    level=logging.DEBUG
)

LOGGER = logging.getLogger(__name__)

class Factory:
    def __init__(self):
        LOGGER.info("Factory CREATED.")
        pass

    def create_repository(self, schema: RepositorySchema):
        return Repository(schema)

    def create_model(self, schema: ModelSchema):
        return Model(schema)