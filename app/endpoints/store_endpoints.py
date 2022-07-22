from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from schemas.store_schema import Store, StoreBase
from schemas.product_schema import Product, ProductBase, ProductCreate
from controllers import store_controller
from utils.get_db import get_db


router = APIRouter()


@router.post("/stores/", response_model=Store)
def create_store(store: StoreBase, db: Session = Depends(get_db)):
    return store_controller.create_store(db=db, store=store)


@router.get("/stores/", response_model=list[Store])
def read_stores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stores = store_controller.get_stores(db, skip=skip, limit=limit)
    return stores


@router.get("/stores/{store_id}", response_model=Store)
def read_store(store_id: int, db: Session = Depends(get_db)):
    db_store = store_controller.get_store(db, store_id=store_id)
    if db_store is None:
        raise HTTPException(status_code=404, detail="store not found")
    return db_store


@router.patch("/stores/{store_id}", response_model=Store)
def update_store(store: StoreBase, store_id: int, db: Session = Depends(get_db)):
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
