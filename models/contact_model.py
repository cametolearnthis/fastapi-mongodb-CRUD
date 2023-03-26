from typing import Optional
from pydantic import BaseModel

class Contact(BaseModel):
    id: Optional[str]
    name: str
    email: str
    address: str
    phone: int
    password: str