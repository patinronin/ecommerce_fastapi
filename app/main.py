from fastapi import FastAPI

from api import api_router
from db import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Hello hewitt"}
