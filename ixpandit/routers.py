from fastapi import APIRouter

from ixpandit.index.routers.index import router as index_router

base_router = APIRouter()
base_router.include_router(router=index_router, prefix="")
