from fastapi import FastAPI,Depends
from typing import Annotated
from .config import get_settings

settings = get_settings()
app = FastAPI()

@app.get("/info")
async def info(settings:Annotated[settings, Depends(get_settings)]):
    return {"app_name": settings.app_name}