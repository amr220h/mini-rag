from fastapi import FastAPI, APIRouter


basre_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)
@basre_router.get("/")
def welcome():
    return {"message": "Welcome to mini-rag!"}