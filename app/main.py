from fastapi import FastAPI

from api import api_router
from db import engine, Base



app = FastAPI()
app.include_router(api_router)

@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello hewitt"}
