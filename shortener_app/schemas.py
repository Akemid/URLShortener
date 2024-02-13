from pydantic import BaseModel,ConfigDict
from pydantic.dataclasses import dataclass

class URLBase(BaseModel):
    target_url: str

@dataclass(config=ConfigDict(from_attributes=True))
class URL(URLBase):
    is_active: bool
    clicks: int
        
class URLInfo(URL):
    url: str
    admin_url: str


