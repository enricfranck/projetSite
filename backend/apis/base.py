from apis.version1 import route_general_pages
from apis.version1 import route_jobs, route_login, route_users, route_product
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(
    route_general_pages.general_pages_router, prefix="", tags=["general_pages"]
)
api_router.include_router(route_users.router, prefix="/users", tags=["users"])
api_router.include_router(route_jobs.router, prefix="/jobs", tags=["jobs"])
api_router.include_router(route_product.router, prefix="/product", tags=["product"])
api_router.include_router(route_login.router, prefix="/login", tags=["login"])
