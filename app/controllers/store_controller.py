from sqlalchemy.orm import Session

from models import store_model
from schemas import store_schema


def get_store(db: Session, store_id: int):
    return db.query(store_model.Store).filter(store_model.Store.id == store_id).first()


def get_stores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(store_model.Store).offset(skip).limit(limit).all()


def create_store(db: Session, store: store_schema.Store):
    db_store = store_model.Store(
        description=store.description,
        warehouse_location=store.warehouse_location,
        store_name=store.store_name
    )
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store

def update_store(db: Session, store: store_schema.Store, store_id: int):
    db.query(store_model.Store).filter(store_model.Store.id == store_id).update(store)
    db.commit()
    db_store = db.query(store_model.Store).filter(store_model.Store.id == store_id).first()
    return db_store


def delete_store(db: Session, store_id):
    db_store = db.query(store_model.Store).get(store_id)
    if db_store:
        db.delete(db_store)
        db.commit()
        return {
            "message": "objetct deleted successfully",
            "status_code": 200
        }
    else:
        return {
            "message": "objetct not found",
            "status_code": 404
        }



