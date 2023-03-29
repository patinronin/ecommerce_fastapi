from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi.encoders import jsonable_encoder

class BaseDBController:

    def __init__(self, model):
        self.model = model

    def get_by_id(self, db: Session, id: int):
        try:
            response = db.query(self.model).get(id)
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=e.args)
        return response

    def get_multi(self, db: Session, page: int = 1, limit: int = 10):
        try:
            response = db.query(self.model).offset(page - 1).limit(limit).all()
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=e.args)
        return response

    def create(self, db: Session, obj_in):
        try:
            obj_in_data = jsonable_encoder(obj_in)
            db_obj = self.model(**obj_in_data)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)

        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=e.args)
        return db_obj

    def update(self, db: Session, obj_in, id: int):
        try:
            db.query(self.model).filter(self.model.id == id).update(obj_in)
            db.commit()
            db_obj = db.query(self.model).filter(self.model.id == id).first()

        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=e.args)
        return db_obj

    def remove(self, db: Session, id: int):
        try:
            obj = db.query(self.model).get(id)
            if obj != None:
                db.delete(obj)
                db.commit()

        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=e.args)
        return obj


