from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from schemas.direction_schema import DirectionUser, DirectionBase, DirectionCreate
from controllers.direction_user_controller import direction_user_controller
from utils.get_db import get_db


router = APIRouter()


@router.post("/direction_user/")
def create_direction_user(direction: DirectionCreate, db: Session = Depends(get_db)):
    print("direction", direction.json())
    print("direction type", type(direction))
    response = direction_user_controller.create(db=db, obj_in=direction.dict())
    print("response", response)
    return response
"""
@router.get("/direction_user/", response_model=list[Store])
def read_direction_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stores = store_controller.get_stores(db, skip=skip, limit=limit)
    return stores


@router.get("/direction_user/{direction_id}", response_model=Store)
def read_direction_users(store_id: int, db: Session = Depends(get_db)):
    db_store = store_controller.get_store(db, store_id=store_id)
    if db_store is None:
        raise HTTPException(status_code=404, detail="store not found")
    return db_store


@router.patch("/direction_user/{direction_id}", response_model=Store)
def update_direction_user(store: StoreBase, store_id: int, db: Session = Depends(get_db)):
    db_store = store_controller.update_store(db=db, store_id=store_id, store=store)
    if db_store is None:
        raise HTTPException(status_code=404, detail="store not found")
    return db_store


@router.delete("/stores/{store_id}")
def delete_store(store_id: int, db: Session = Depends(get_db)):
    db_response = store_controller.delete_store(db=db, store_id=store_id)
    if db_response["status_code"] == 404:
        raise HTTPException(status_code=404, detail="store not found")
    return db_response


@router.post("/stores/{store_id}/products/", response_model=Product)
def create_product_for_store(
        store_id: int,
        product: ProductCreate,
        db: Session = Depends(get_db)
):
    return store_controller.create_store_product(db=db, product=product, store_id=store_id)
"""