from fastapi import HTTPException

def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)