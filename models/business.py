from pydantic import BaseModel
from typing import Optional

class NAPData(BaseModel):
    name: str
    address: str
    phone: str
    website: Optional[str] = None
    description: Optional[str] = None
