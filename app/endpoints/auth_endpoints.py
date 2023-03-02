from fastapi import Depends, HTTPException, APIRouter, status
from sqlalchemy.orm import Session
from utils.get_db import get_db
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

SECRET = "571f3508915ab4504af982a36af2a2cebd85c2519da49198093476fbbe6d396c"
ALGORITHM = "HS256"

router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")
crypt = CryptContext(schemes=["bcrypt"])
ACCESS_TOKEN_DURATION = 5

users_db = {
    "cogo@cogo.com": {
        "username": "cogo@cogo.com",
        "password": "$2a$12$WEzCQTT51QYTQrxUshjfBOhfPpY9S5afkJIr4O4vAm5v1cWZrk/p."
    }

}


class User(BaseModel):
    username: str


class UserDB(User):
    password: str


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])


async def decode_jwt(token: str = Depends(oauth2)):

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas",
        headers={"WWW-Authenticate": "Bearer"})

    try:
        token_decoded = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        print(token_decoded)
        if token_decoded is None:
            raise exception

    except JWTError:
        raise exception

    return token_decoded



@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario no es correcto"
        )

    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La contrasena no es correcta"
        )
    access_token = {"sub": user.username,
                    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}

    return {
        "acces_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM),
        "token_type": "bearer"
    }

@router.post("/decode_jwt")
async def decode_jwt_route(token_jwt: str = Depends(decode_jwt)):
    return token_jwt