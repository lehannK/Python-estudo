from datetime import datetime
import uuid
from fastapi import Depends
from sqlmodel import Session
from app.core.database import get_session
from app.modules.models import User
from app.modules.users.schemas import CreateUserSchema
from app.modules.users.security import hash_password
from .repository import UserRepository


class UserService:
    def __init__(self, session: Session):
        self.repo = UserRepository(session)

    def list_users(self):
        return self.repo.find_all()

    def create_user(self, user_data: CreateUserSchema):
        if self.repo.find_by_email(user_data.email):
            raise ValueError("Este email já está em uso")

        if self.repo.find_by_cpf(user_data.cpf):
            raise ValueError("Este CPF já está em uso")

        # Converte Schema -> Model
        user = User(
            # esse ** equivale ao spread operator
            **user_data.model_dump(exclude={"password"}),
            password=hash_password(user_data.password),
            public_id=str(uuid.uuid4()),
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

        return self.repo.create(user)


def get_user_service(session: Session = Depends(get_session)) -> UserService:
    return UserService(session)
