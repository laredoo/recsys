from typing import Any
from fastapi import APIRouter, Depends

from api.core.factory import Factory

from api.controller.fetcher import FetcherController

from api.schemas.request.fetcher import FetcherRequestModel

from api.schemas.response.fetcher import FetcherResponseModel

from recsys.api.core.dependencies import get_model_data

fetcher_router = APIRouter()

@fetcher_router.post("/songs", response_model=FetcherResponseModel)
async def read_items(
    request: FetcherRequestModel,
    model_data: Any = Depends(get_model_data),
    fetcher_controller: FetcherController = Depends(Factory().get_fetcher_controller),
):
    
    songs = fetcher_controller.get_recommendations(model_data, request)

    return FetcherResponseModel(
        **{
            'songs': songs,
            'model_date': 'now'
        }
    )


    