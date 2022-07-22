from fastapi import APIRouter, Header, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from utils.utils_jwt import write_token, validate_token
from schemas.user_schema import UserLogin
from controllers import user_controller
from utils.get_db import get_db


router = APIRouter()

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = user_controller.get_user_by_email(db, email=user.email)
    if db_user:
        return write_token(user.dict())
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=404)

@router.post("/verify/token")
def verify_token(Authorization: str = Header(None)):
    token = Authorization.split(" ")[1]
    return validate_token(token, output=True)




