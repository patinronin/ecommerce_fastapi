from fastapi import APIRouter
from endpoints import user_endpoints, store_endpoints, auth_endpoints

api_router = APIRouter()

api_router.include_router(
    user_endpoints.router,
    tags=["User endpoints"]

)

api_router.include_router(
    store_endpoints.router,
    tags=["Store endpoints"]

)

api_router.include_router(
    auth_endpoints.router,
    tags=["Auth endpoints"]
)