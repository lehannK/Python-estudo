from typing import Optional
from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    name: str
    last_name: str
    birth_date: Optional[int] = None


class CreateUserSchema(BaseModel):
    name: str
