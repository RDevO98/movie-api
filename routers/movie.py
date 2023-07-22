from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

from config.database import Session

from models.movie import Movie as MovieModel

from middlewares.jwt_bearer import JWTBearer

from services.movie import MovieService

from schemas.movie import Movie

movie_router = APIRouter()


@movie_router.get('/movies', tags=['Movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(
        status_code=200,
        content=jsonable_encoder(result)
    )


@movie_router.get('/movies/{id}', tags=['Movies'], response_model=Movie, status_code=200)
def get_movie(id: int = Path(ge=1)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie()

    if not result:
            return JSONResponse(
                status_code=404,
                content={"message":"Movie not found."}
            )
    
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.get('/movies/', tags=['Movies'], response_model=List[Movie], status_code=200)
def get_movie_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies_by_category(category)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movie_router.post('/movies', tags=['Movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"message":"Movie was inserted."})


@movie_router.put('/movies/{id}', tags=['Movies'], response_model=dict, status_code=200)
def update_movie(
    id:int,
    movie: Movie
) -> dict:
    
    db = Session()
    result = MovieService(db).get_movie(id)

    if not result:
            return JSONResponse(
                status_code=404,
                content={"message":"Movie not found."}
            )
    
    MovieService(db).update_movie(id, movie)

    return JSONResponse(status_code=200, content={"message":"Movie was updated."})


@movie_router.delete('/movies/{id}', tags=['Movies'], response_model=dict, status_code=200)
def delete_movie(id:int) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id)

    if not result:
            return JSONResponse(
                status_code=404,
                content={"message":"Movie not found."}
            )
    
    MovieService(db).delete_movie(id)
   
    return JSONResponse(status_code=200, content={"message":"Movie was deleted."})