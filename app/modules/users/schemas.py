from datetime import datetime
from typing import Literal, Optional
from pydantic import BaseModel
from app.modules.models import UserRole


class UserSchema(BaseModel):
    id: int
    public_id: str
    first_name: str
    last_name: str
    email: str
    role: UserRole
    cpf: Optional[str] = None
    phone_number: Optional[str] = None
    status: Literal["active", "inactive"]
    created_at: datetime
    updated_at: datetime


class CreateUserSchema(BaseModel):
    name: str


class LoginSchema(BaseModel):
    email: str
    password: str
