from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi.encoders import jsonable_encoder

class BaseDBController:

    def __init__(self, model, model_create, model_update):
        self.model = model
        self.model_create = model_create
        self.model_update = model_update


    async def get_by_id(self,db: Session, id: int):
        try:
            response = await db.query(self.model).get(id)
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=e.args)
        return response.scalar_one()



    async def get_multi(
            self, db: Session,
            page: int = 1,
            limit: int = 10):
        try:

            response = await db.execute(
                select(self.model).offset(page - 1).limit(limit)
            )

        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=e.args)
        return response.scalars().all()

    def create(
            self, db: Session, obj_in
    ):
        try:
            obj_in_data = jsonable_encoder(obj_in)
            db_obj = self.model_create(**obj_in_data)  # type: ignore
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            print("db_obj create", db_obj)
        except SQLAlchemyError as e:
            db.rollback()
            print("error", e)
            raise HTTPException(status_code=500, detail=e.args)
        return db_obj

    async def update(
            self,
            db: Session,
            db_obj,
            obj_in
    ):
        obj_data = jsonable_encoder(db_obj)
        try:
            if isinstance(obj_in, dict):
                update_data = obj_in
            else:
                update_data = obj_in.dict(exclude_unset=True)
            for field in obj_data:
                if field in update_data:
                    setattr(db_obj, field, update_data[field])
                if "altered_at" in obj_data:
                    setattr(db_obj, "altered_at", datetime.datetime.now())
            db.add(db_obj)
            await db.commit()
            await db.refresh(db_obj)
        except SQLAlchemyError as e:
            await db.rollback()
            raise HTTPException(status_code=500, detail=e.args)
        return db_obj

    async def remove(self, db: Session, id: int):
        try:
            obj = db.query(self.model).get(id)
            await db.delete(obj)
            await db.commit()
        except SQLAlchemyError as e:
            await db.rollback()
            raise HTTPException(status_code=500, detail=e.args)
        return obj


