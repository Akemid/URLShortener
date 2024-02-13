from fastapi import HTTPException

def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)


def raise_not_found(request):
    raise HTTPException(status_code=404, detail=f"URL not found: {request.url}")