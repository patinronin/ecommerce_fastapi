from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from schemas.store_schema import Store
from controllers import store_controller
from utils.get_db import get_db

router = APIRouter()


@router.post("/stores/")
def create_store(store: Store, db: Session = Depends(get_db)):
    return store_controller.create_store(db=db, store=store)


@router.get("/stores/")
def read_stores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stores = store_controller.get_stores(db, skip=skip, limit=limit)
    return stores


@router.get("/stores/{store_id}")
def read_store(store_id: int, db: Session = Depends(get_db)):
    db_store = store_controller.get_store(db, store_id=store_id)
    if db_store is None:
        raise HTTPException(status_code=404, detail="store not found")
    return db_store