from fastapi import APIRouter
from endpoints import user_endpoints

api_router = APIRouter()

api_router.include_router(
    user_endpoints.router,
    tags=["User endpoints"]

)