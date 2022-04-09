from fastapi import APIRouter, FastAPI

from . import combinations


def setup(app: FastAPI):
    master_router = APIRouter()
    
    for module in (combinations, ):
        master_router.include_router(module.router)
    
    app.include_router(master_router)