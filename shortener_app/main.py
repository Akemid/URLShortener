import secrets
import validators

from fastapi import FastAPI,Depends,Request
from fastapi.responses import RedirectResponse
from typing import Annotated
from sqlalchemy.orm import Session
from .config import get_settings,Settings
from .exceptions import raise_bad_request,raise_not_found
from . import schemas,models,crud
from .database import engine,SessionLocal
from .keygen import create_random_key


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/info")
async def info(settings:Annotated[Settings, Depends(get_settings)]):
    return {"app_name": settings.app_name}

@app.get("/")
def home(settings:Annotated[Settings, Depends(get_settings)]):
    return {"message": f"Hello World from app: {settings.app_name}"}

@app.post("/url",response_model=schemas.URLInfo)
def create_url(url:schemas.URLBase,db:Session = Depends(get_db)):
    if not validators.url(url.target_url):
        raise_bad_request(message="Your provided URL is not valid")

    db_url = crud.create_db_url(url,db)
    db_url.url = db_url.key
    db_url.admin_url = db_url.secret_key
    return db_url

@app.get("/{url_key}")
def forward_to_target_url(
    url_key:str, request: Request, db:Session = Depends(get_db)
):
    url = db.query(models.URL).filter(models.URL.key == url_key,models.URL.is_active).first()
    if url is None:
        raise_not_found(message="URL not found")
    return RedirectResponse(url.target_url)