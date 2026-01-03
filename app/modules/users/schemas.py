from app.modules.models import UserRole, UserStatus
from datetime import datetime
from typing import Optional
from pydantic import (
    BaseModel,
    Field,
    field_validator,
    model_validator,
)
import re  # módulo regex


class UserBaseSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
    role: UserRole
    cpf: str
    phone_number: Optional[str] = None
    status: UserStatus = UserStatus.active

    @field_validator("cpf")
    @classmethod
    def validate_cpf(cls, v: str) -> str:
        # Remove caracteres não numéricos
        cpf = re.sub(r"\D", "", v)

        # Validações básicas
        if len(cpf) != 11 or not cpf.isdigit() or cpf == cpf[0] * 11:
            raise ValueError("CPF inválido")

        # Validação dos dígitos verificadores
        for i in range(9, 11):
            soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(i))
            digito = (soma * 10 % 11) % 10

            if int(cpf[i]) != digito:
                raise ValueError("CPF inválido")

        return cpf


class CreateUserSchema(UserBaseSchema):
    password: str = Field(default="", min_length=6)

    @model_validator(mode="after")
    def generate_password(self):
        # Gera senha automaticamente após validação do CPF
        self.password = self.cpf[:6]
        return self


class UserSchema(UserBaseSchema):
    public_id: str
    created_at: datetime
    updated_at: datetime


class LoginSchema(BaseModel):
    email: str
    password: str
