from fastapi import APIRouter, Depends, HTTPException

from .fetcher import fetcher_router

router = APIRouter()

router.include_router(
    fetcher_router, prefix="/fetcher", tags=["Fetcher"]
)

__all__ = ["router"]