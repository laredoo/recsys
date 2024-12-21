import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware

from .routers import router
from .config import settings

def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.RELEASE_VERSION,
    description=settings.PROJECT_DESCRIPTION
)

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    return app_

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

