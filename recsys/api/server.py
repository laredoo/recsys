import uvicorn
import pickle

from typing import Any

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware

from .routers import router
from .config import settings

file_path = "./recsys/api/project2-pv2/fpgrowth_results.pkl"

def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.RELEASE_VERSION,
    description=settings.PROJECT_DESCRIPTION
)

def carregar_pkl():
    with open(file_path, "rb") as f:
        dados = pickle.load(f)
    return dados
    
def make_middleware():
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=settings.ALLOWED_ORIGINS,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
    ]
    return middleware

def create_app() -> FastAPI:
    app_ = FastAPI(
        title = settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.RELEASE_VERSION,
        docs_url="/docs",
        redoc_url="/redoc",
        middleware=make_middleware()
    )
    init_routers(app_=app_)
    app_.state.model_data = carregar_pkl()

    return app_
    

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

