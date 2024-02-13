import secrets
import string
from typing import Callable

from sqlalchemy.orm import Session

def create_random_key(length:int = 5) -> str:
    chars = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))

def create_unique_random_key(db:Session,length:int = 5,find_db_key:Callable[[str,Session],str]=None) -> str:
    """
    find_db_key: Must be a function that takes a key and a db session and returns a URL object
    """
    while True:
        key = create_random_key(length)
        db_url = find_db_key(key,db)
        if not db_url:
            return key