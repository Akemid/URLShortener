from fastapi import FastAPI
from .config import get_settings

settings = get_settings()
app = FastAPI()

@app.get("/info")
async def info():
    return {"app_name": settings.app_name}