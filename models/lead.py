
from pydantic import BaseModel
from typing import Optional

class Lead(BaseModel):
    name: Optional[str]
    email: str
    company: Optional[str]
    message: Optional[str]
