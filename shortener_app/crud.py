from sqlalchemy.orm import Session
from . import keygen,models,schemas

def create_db_url(url:schemas.URLBase,db:Session)->  models.URL:
    
    key = keygen.create_unique_random_key(db,5,find_db_key=get_db_url_by_key)
    secret_key = keygen.create_random_key(8)
    db_url = models.URL(
        target_url=url.target_url, key=key, secret_key=secret_key
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_db_url_by_key(url_key:str,db:Session)-> models.URL:
    return (
        db.query(models.URL)
        .filter(models.URL.key == url_key,models.URL.is_active)
        .first()
    )