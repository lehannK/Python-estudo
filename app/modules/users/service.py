from fastapi import Depends
from sqlmodel import Session

from app.core.database import get_session
from .repository import UserRepository


def get_user_service(session: Session = Depends(get_session)):
    repo = UserRepository(session)  # ✅ Passa a session
    return UserService(repo)


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def list_users(self):
        return self.repo.find_all()

    def get_user(self, user_id: int):
        return self.repo.find_by_id(user_id)
