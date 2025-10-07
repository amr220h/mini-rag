from fastapi import FastAPI

from dotenv import load_dotenv
load_dotenv('.env')

from routes.base import basre_router
app = FastAPI()

app.include_router(basre_router)