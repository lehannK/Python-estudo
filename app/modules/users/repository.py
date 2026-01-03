from typing import List
from sqlmodel import Session
from sqlmodel import select
from app.modules.models import Users


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def find_all(self) -> List[Users]:
        statement = select(Users)
        results = self.session.exec(statement)
        return results.all()

    def find_by_id(self, user_id: int):
        users = self.find_all()
        for user in users:
            if user["id"] == user_id:
                return user
        return None
