from fastapi import APIRouter, Depends, HTTPException

fetcher_router = APIRouter()

@fetcher_router.get("/items/")
def read_items():
    return {
        'Teste': 123
    }


    