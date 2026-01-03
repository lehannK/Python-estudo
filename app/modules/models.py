from sqlmodel import Field, SQLModel
from datetime import datetime
from enum import Enum


class UserRole(str, Enum):
    admin = "admin"
    employee = "employee"
    supervisor = "supervisor"
    finance = "finance"


class UserStatus(str, Enum):
    active = "active"
    inactive = "inactive"


class User(SQLModel, table=True):
    __tablename__ = "users"

    # Campos obrigatórios
    id: int | None = Field(default=None, primary_key=True)
    public_id: str = Field(max_length=36, unique=True)
    first_name: str = Field(max_length=255)
    last_name: str = Field(max_length=255)
    email: str = Field(max_length=255, unique=True, index=True)
    password: str = Field(max_length=255)
    role: UserRole

    # Campos opcionais
    cpf: str | None = Field(default=None, max_length=11, unique=True)
    phone_number: str | None = Field(default=None, max_length=15, unique=True)

    # Status e timestamps
    status: UserStatus = Field(default=UserStatus.active)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
