from typing import Any
from fastapi import APIRouter, Depends

from core.factory import Factory

from controller.fetcher import FetcherController

from schemas.request.fetcher import FetcherRequestModel

from schemas.response.fetcher import FetcherResponseModel

from core.dependencies import get_model_data

fetcher_router = APIRouter()

@fetcher_router.post("/songs", response_model=FetcherResponseModel)
async def read_items(
    request: FetcherRequestModel,
    model_data: Any = Depends(get_model_data),
    fetcher_controller: FetcherController = Depends(Factory().get_fetcher_controller),
):
    
    songs, model_date = fetcher_controller.get_recommendations(model_data, request)

    fetcher_controller.save_recommendations(songs, model_date)

    return FetcherResponseModel(
        **{
            'songs': songs,
            'model_date': model_date.strftime('%Y-%m-%d %H:%M:%S')
        }
    )


    