from fastapi import FastAPI
from api import api_router
from db import engine, Base
#from models.direction_user_model import DirectionUser
app = FastAPI()
app.include_router(api_router)


@app.on_event("startup")
async def startup_event():
    print("Creating database engine...")
    Base.metadata.create_all(bind=engine)
    # Base.metadata.create_all(bind=engine,  tables=[DirectionUser.__table__])
    print("start up")

@app.get("/")
async def root():
    return {"message": "Hello"}
