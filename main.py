from fastapi import FastAPI

from config.database import engine, Base

from middlewares.error_handler import ErrorHandler

from routers.movie import movie_router
from routers.authentication import authentication_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Movie FastAPI",
    description="API for get information about movies.",
    version="0.0.1"
)

app.add_middleware(ErrorHandler)

app.include_router(movie_router)
app.include_router(authentication_router)

@app.get('/', tags=['Index'])
def index():
    return "FastAPI it's working!"



