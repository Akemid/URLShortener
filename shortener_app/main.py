import validators
from fastapi import FastAPI,Depends
from typing import Annotated
from .config import get_settings,Settings
from .exceptions import raise_bad_request
from . import schemas

app = FastAPI()

@app.get("/info")
async def info(settings:Annotated[Settings, Depends(get_settings)]):
    return {"app_name": settings.app_name}

@app.get("/")
def home(settings:Annotated[Settings, Depends(get_settings)]):
    return {"message": f"Hello World from app: {settings.app_name}"}

@app.post("/url")
def create_url(url:schemas.URLBase):
    if not validators.url(url.target_url):
        raise_bad_request("Invalid URL")
    return {"target_url": url.target_url}