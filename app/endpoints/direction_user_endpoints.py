from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from schemas.direction_schema import DirectionUser, DirectionCreate
from controllers.direction_user_controller import direction_user_controller
from utils.get_db import get_db


router = APIRouter()


@router.post("/direction_user/")
def create_direction_user(direction: DirectionCreate, db: Session = Depends(get_db)):
    response = direction_user_controller.create(db=db, obj_in=direction.dict())
    return response

@router.get("/direction_user/", response_model=list[DirectionUser])
def read_direction_users(page: int = 1, limit: int = 100, db: Session = Depends(get_db)):
    direction_user = direction_user_controller.get_multi(db, page=page, limit=limit)
    return direction_user



@router.get("/direction_user/{id}", response_model=DirectionUser)
def read_direction_user(id: int, db: Session = Depends(get_db)):
    direction_user = direction_user_controller.get_by_id(db, id=id)
    if direction_user is None:
        raise HTTPException(status_code=404, detail="not found")
    return direction_user


@router.patch("/direction_user/id", response_model=DirectionUser)
def update_direction_user(
        user: DirectionUser,
        id: int,
        db: Session = Depends(get_db)
):
    direction_user = direction_user_controller.update(
        db=db,
        obj_in=user,
        id=id
    )
    if direction_user is None:
        raise HTTPException(status_code=404, detail="not found")
    return direction_user


@router.delete("/direction_user/{id}", response_model=DirectionUser)
def delete_store(id: int, db: Session = Depends(get_db)):
    direction_user = direction_user_controller.remove(db=db, id=id)
    if direction_user is None:
        raise HTTPException(status_code=404, detail="not found")
    return direction_user


