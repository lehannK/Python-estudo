from typing import Optional
import datetime

from sqlalchemy import (
    Column,
    Enum,
    Index,
    Integer,
    PrimaryKeyConstraint,
    String,
    text,
)
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlmodel import Field, SQLModel


class Users(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint("id", name="users_pkey"),
        Index("users_cpf_key", "cpf", unique=True),
        Index("users_email_key", "email", unique=True),
        Index("users_phone_number_key", "phone_number", unique=True),
        Index("users_public_id_key", "public_id", unique=True),
    )

    id: int = Field(sa_column=Column("id", Integer, primary_key=True))
    public_id: str = Field(sa_column=Column("public_id", String(36), nullable=False))
    first_name: str = Field(sa_column=Column("first_name", String(255), nullable=False))
    last_name: str = Field(sa_column=Column("last_name", String(255), nullable=False))
    email: str = Field(sa_column=Column("email", String(255), nullable=False))
    password: str = Field(sa_column=Column("password", String(255), nullable=False))
    role: str = Field(
        sa_column=Column(
            "role",
            Enum(
                "admin",
                "employee",
                "supervisor",
                "finance",
                name="user_role",
            ),
            nullable=False,
        )
    )
    created_at: datetime.datetime = Field(
        sa_column=Column(
            "created_at",
            TIMESTAMP(precision=3),
            nullable=False,
            server_default=text("CURRENT_TIMESTAMP"),
        )
    )
    updated_at: datetime.datetime = Field(
        sa_column=Column("updated_at", TIMESTAMP(precision=3), nullable=False)
    )
    status: str = Field(
        sa_column=Column(
            "status",
            Enum("active", "inactive", name="user_status"),
            nullable=False,
            server_default=text("'active'::user_status"),
        )
    )
    cpf: Optional[str] = Field(default=None, sa_column=Column("cpf", String(11)))
    phone_number: Optional[str] = Field(
        default=None, sa_column=Column("phone_number", String(15))
    )
