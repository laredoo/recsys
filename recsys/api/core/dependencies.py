from fastapi import Request, HTTPException
from typing import Any

async def get_model_data(request: Request) -> Any:
    try:
        return request.app.state.model_data
    except AttributeError:
        raise HTTPException(
            status_code=500,
            detail="Model data not found in application state"
        )
