from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemas.user import User

from utils.jwt_manager import create_token

authentication_router = APIRouter()


@authentication_router.post('/login', tags=['Authentication'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.model_dump())
        return JSONResponse(status_code=200, content=token)