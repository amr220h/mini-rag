from fastapi import FastAPI
from routes import base
from routes import data
from dotenv import load_dotenv
load_dotenv('.env')

from routes.base import base_router
app = FastAPI()

app.include_router(base.base_router)
app.include_router(data.base_router)